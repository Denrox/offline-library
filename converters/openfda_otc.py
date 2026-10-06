"""Over-the-counter drug labels from openFDA (FDA "Drug Facts", public domain).

All human OTC labels are paged from the openFDA API. Homeopathic products and
labels without uses, directions and warnings are left out. Labels are grouped by active ingredients and route (hundreds of store
brands share one ingredient); each group becomes one page built from its most
complete current adult label, listing the brand names it is sold under.
Categories come from the label's "Purpose".
"""

import collections
import re
import time

from .lib.openfda import Group, body, form_key, fetch_all, group_key, has, join_names, label_date, table_md, text
HOMEOPATHIC = re.compile(r"\bHPUS\b|homo?eopath|\b\d+\s?(X|C|CH|CK|LM|DH)\b", re.I)
WARNING_FIELDS = ("warnings", "do_not_use", "ask_doctor", "stop_use", "keep_out_of_reach_of_children")

# Drug Facts order: (label field, heading, leading words the field repeats).
SECTIONS = [
    ("active_ingredient", "Active ingredients", r"active ingredients?( \(in each [^)]*\))?"),
    ("purpose", "Purpose", r"purposes?"),
    ("indications_and_usage", "Uses", r"uses?|indications?( and usage)?"),
    ("warnings", "Warnings", r"warnings?"),
    ("do_not_use", "Do not use", r"do not use"),
    ("ask_doctor", "Ask a doctor before use if", r"ask a doctor before use( if)?"),
    ("ask_doctor_or_pharmacist", "Ask a doctor or pharmacist before use if",
     r"ask a doctor or pharmacist before use( if)?"),
    ("when_using", "When using this product", r"when using this product"),
    ("stop_use", "Stop use and ask a doctor if", r"stop use and ask a doctor( if)?"),
    ("pregnancy_or_breast_feeding", "Pregnancy or breast-feeding", r""),
    ("keep_out_of_reach_of_children", "Keep out of reach of children", r""),
    ("dosage_and_administration", "Directions", r"directions?|dosage and administration"),
    ("storage_and_handling", "Other information", r"other information|storage and handling"),
    ("inactive_ingredient", "Inactive ingredients", r"inactive ingredients?"),
]
KEEP = {f for f, _, _ in SECTIONS} | {f"{f}_table" for f, _, _ in SECTIONS} | {"openfda", "effective_time", "set_id"}

# Purpose wording -> everyday category; first match wins, a label can match several.
CATEGORIES = [
    ("Sunscreens", r"sunscreen|sun protect"),
    ("Smoking cessation", r"stop smoking|smoking cessation|nicotine"),
    ("Sleep aids", r"sleep|nighttime"),
    ("Cold, cough and allergy", r"antihistamine|decongestant|cough|expectorant|cold|allerg|sore throat|oral anesthetic"),
    ("Pain and fever", r"pain reliever|fever|analgesic(?! .*(topical|external))|headache"),
    ("Topical pain relief", r"topical analgesic|external analgesic|topical anesthetic|counterirritant|local anesthetic"),
    ("Digestive health", r"antacid|acid reducer|laxative|stool soften|antidiarr|anti-diarr|antiemetic|nausea|gas|antiflatulent|hemorrhoid"),
    ("Antiseptics and hand sanitizers", r"antiseptic|antibacterial|antimicrobial|hand sanit|first aid"),
    ("Antifungals", r"antifungal|athlete|ringworm|jock itch|yeast"),
    ("Acne", r"acne"),
    ("Dandruff and scalp", r"dandruff|seborrheic|psoriasis"),
    ("Skin protectants", r"skin protectant|diaper|anti-itch|itch|poison ivy|insect bite|astringent"),
    ("Warts, corns and calluses", r"wart|corn|callus"),
    ("Oral care", r"anticavity|cavity|gingivitis|antiplaque|plaque|sensitivity|tooth|fluoride"),
    ("Eye care", r"eye|ophthalmic|lubricant drops"),
    ("Antiperspirants", r"antiperspirant"),
    ("Lice", r"lice|pediculicide"),
    ("Hair loss", r"hair regrowth|hair growth|hair loss|minoxidil"),
    ("Ear care", r"earwax|ear wax|\bear\b"),
    ("Insect repellents", r"repellent|mosquito"),
    ("Asthma", r"bronchodilator|asthma"),
]

# When the purpose names no category, the route can.
ROUTE_CATEGORIES = {"OPHTHALMIC": "Eye care", "DENTAL": "Oral care", "NASAL": "Cold, cough and allergy",
                    "RESPIRATORY (INHALATION)": "Asthma", "AURICULAR (OTIC)": "Ear care"}
NO_INFO = re.compile(r"see the (enclosed )?leaflet|read the enclosed|see (the )?package insert", re.I)


def for_children(rec):
    brands = " ".join(rec.get("openfda", {}).get("brand_name", [])).lower()
    directions = text(rec, "dosage_and_administration").lower()
    return bool(re.search(r"child|infant|junior|kid|pediatric|baby", brands)
                or re.search(r"weight \(lb\)|right dose on (the )?chart|dosing (cup|syringe)", directions))


def score(rec):
    """Complete adult labels first."""
    s = sum(1 for f, _, _ in SECTIONS if has(rec, f))
    if "adult" in text(rec, "dosage_and_administration").lower():
        s += 3
    if for_children(rec):
        s -= 5
    return s


def categories_for(rec, routes):
    purpose = (text(rec, "purpose") or text(rec, "indications_and_usage")[:300]).lower()
    found = [name for name, pattern in CATEGORIES if re.search(pattern, purpose)]
    found = found or [ROUTE_CATEGORIES[r] for r in routes if r in ROUTE_CATEGORIES]
    return found or ["Other"]


def build(out, source):
    p = source.get("params", {})
    groups = {}
    meta = {}
    for rec, meta in fetch_all(p.get("product_type", "HUMAN OTC DRUG"), KEEP):
        subs, routes = group_key(rec)
        probe = " ".join(text(rec, f) for f in ("active_ingredient", "purpose")) + text(rec, "indications_and_usage")[:300]
        if not subs or HOMEOPATHIC.search(probe):
            continue
        # Only real Drug Facts labels: uses, directions and warnings.
        if not (has(rec, "indications_and_usage") and has(rec, "dosage_and_administration")
                and any(has(rec, f) for f in WARNING_FIELDS)):
            continue
        if NO_INFO.search(text(rec, "indications_and_usage")[:200] + " " + text(rec, "purpose")[:200]):
            continue
        group = groups.setdefault((subs, routes), Group(join_names(subs)))
        group.add(rec, score(rec), form_key(rec), preferred=not for_children(rec))

    routes_per_combo = collections.Counter(subs for subs, _ in groups)
    notice = f"> **Note:** {p['notice']}\n\n" if p.get("notice") else ""

    for (subs, routes), group in groups.items():
        rep = group.representative()
        title = group.name
        if routes_per_combo[subs] > 1:
            title += f" ({', '.join(r.lower() for r in routes)})"
        o = rep.get("openfda", {})

        parts = [f"# {title}\n", notice.rstrip("\n") + "\n" if notice else ""]
        facts = [f"**Route:** {', '.join(r.lower() for r in routes)}"]
        forms = [f for f, _ in group.substances.most_common(6) if f.lower() not in title.lower()]
        if forms:
            facts.append(f"**Ingredient forms:** {', '.join(forms)}")
        if o.get("pharm_class_epc"):
            classes = [re.sub(r"\s*\[EPC\]$", "", c) for c in o["pharm_class_epc"]]
            facts.append(f"**Drug class:** {', '.join(classes)}")
        facts.append(f"**Labels on file:** {group.count}")
        parts.append("  \n".join(facts) + "\n")
        top, more = group.brand_names(subs)
        if top:
            parts.append("**Also sold as:** " + ", ".join(top) + (f" and {more} more" if more > 0 else "") + "\n")

        for field, heading, lead in SECTIONS:
            content = text(rep, field)
            if not has(rep, field):
                continue
            level = "###" if field in ("do_not_use", "ask_doctor", "ask_doctor_or_pharmacist", "when_using",
                                       "stop_use", "pregnancy_or_breast_feeding",
                                       "keep_out_of_reach_of_children") else "##"
            section = body(content, lead)
            table = rep.get(f"{field}_table")
            if table:
                section += "\n\n" + "\n\n".join(table_md(t) for t in table)
            parts.append(f"{level} {heading}\n\n{section}\n")

        parts.append(
            f"---\n\n*Source: FDA drug label via openFDA, label effective {label_date(rep)}, "
            f"DailyMed set ID {rep.get('set_id', 'unknown')}. Public domain.*\n"
        )
        out.page(title, "\n".join(x for x in parts if x), categories_for(rep, routes))

    return meta.get("last_updated", time.strftime("%Y-%m-%d"))
