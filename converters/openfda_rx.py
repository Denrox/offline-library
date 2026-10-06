"""Prescription drug labels from openFDA (FDA prescribing information, public domain).

Labels are grouped by active ingredients and route like the OTC converter; each
group becomes one page from its most complete current label. Pages keep what a
reader needs (uses, dosage, contraindications, boxed warning, warnings,
interactions, specific populations, overdose, the patient leaflet) and leave
out pharmacology, clinical studies and packaging. Categories come from the
FDA drug class.
"""

import collections
import re
import time

from .lib.openfda import Group, body, fetch_all, group_key, has, join_names, label_date, table_md, text

N = r"(?:\d+(?:\.\d+)?\s+)?"  # PLR section numbers ("5 WARNINGS AND PRECAUTIONS")

# (label field, heading, leading words the field repeats, max characters)
SECTIONS = [
    ("boxed_warning", "Boxed warning", r"boxed warning", 4000),
    ("indications_and_usage", "Uses", N + r"indications?( (and|&) usage)?", 6000),
    ("dosage_and_administration", "Dosage", N + r"dosage (and|&) administration", 8000),
    ("dosage_forms_and_strengths", "Forms and strengths", N + r"dosage forms (and|&) strengths", 3000),
    ("contraindications", "Contraindications", N + r"contraindications?", 4000),
    ("warnings_and_cautions", "Warnings and precautions", N + r"warnings (and|&) precautions", 10000),
    ("warnings", "Warnings", N + r"warnings?", 8000),
    ("precautions", "Precautions", N + r"precautions?", 8000),
    ("adverse_reactions", "Side effects", N + r"adverse reactions?", 6000),
    ("drug_interactions", "Drug interactions", N + r"drug interactions?", 6000),
    ("use_in_specific_populations", "Pregnancy, breastfeeding, children and older adults",
     N + r"use in specific populations", 8000),
    ("pregnancy", "Pregnancy", N + r"pregnancy", 3000),
    ("nursing_mothers", "Breastfeeding", N + r"(nursing mothers|lactation)", 2000),
    ("pediatric_use", "Children", N + r"pediatric use", 2000),
    ("geriatric_use", "Older adults", N + r"geriatric use", 2000),
    ("controlled_substance", "Controlled substance", N + r"controlled substance", 1000),
    ("drug_abuse_and_dependence", "Abuse and dependence", N + r"drug abuse (and|&) dependence", 4000),
    ("overdosage", "Overdose", N + r"overdosage", 4000),
]
# Older labels split these out; newer ones repeat them inside use_in_specific_populations.
POPULATION_FIELDS = {"pregnancy", "nursing_mothers", "pediatric_use", "geriatric_use"}
# Best patient-facing text first.
PATIENT = [
    ("spl_medguide", "Medication Guide (for patients)", r"medication guide", 12000),
    ("spl_patient_package_insert", "Patient information", r"patient information", 12000),
    ("information_for_patients", "Patient counseling information",
     N + r"(patient counseling information|information for patients)", 6000),
]
TABLES = {"dosage_and_administration", "dosage_forms_and_strengths"}
KEEP = ({f for f, *_ in SECTIONS + PATIENT} | {f"{f}_table" for f in TABLES}
        | {"openfda", "effective_time", "set_id"})

# FDA drug class (or route) -> everyday area; a drug can fall in several.
CATEGORIES = [
    ("Antibiotics", r"antibacterial|antimicrobial|penicillin|cephalosporin|macrolide|tetracycline|quinolone|"
                    r"sulfonamide|aminoglycoside|carbapenem|lincosamide|glycopeptide|nitroimidazole|nitrofuran|"
                    r"oxazolidinone|monobactam|polymyxin|rifamycin|antimycobacterial|antituberculosis"),
    ("Antivirals", r"antiviral|nucleoside|nucleotide|reverse transcriptase|protease inhibitor|neuraminidase|"
                   r"integrase|polymerase inhibitor|hepatitis c|hiv"),
    ("Antifungals", r"antifungal|azole|polyene|echinocandin|allylamine"),
    ("Antiparasitics", r"anthelmintic|antimalarial|antiprotozoal|pediculicide|scabicide|antiparasitic"),
    ("Heart and blood pressure", r"angiotensin|beta-adrenergic blocker|calcium channel blocker|diuretic|"
                                 r"nitrate vasodilator|antiarrhythmic|cardiac glycoside|vasodilator|"
                                 r"alpha-adrenergic blocker|aldosterone|renin|alpha-2 adrenergic agonist|"
                                 r"neprilysin|vasopressor|catecholamine|alpha-adrenergic agonist|"
                                 r"endothelin receptor|soluble guanylate"),
    ("Cholesterol", r"hmg-coa|fibrate|peroxisome proliferator|bile acid sequestrant|cholesterol absorption|"
                    r"pcsk9|lipid"),
    ("Blood and clotting", r"anti-?coagulant|vitamin k antagonist|factor xa|thrombin inhibitor|platelet aggregation|"
                           r"p2y12|heparin|antifibrinolytic|erythropoie|thrombopoietin|coagulation factor"),
    ("Diabetes", r"sulfonylurea|biguanide|insulin|dipeptidyl peptidase|glp-1|sglt2|sodium-glucose|"
                 r"thiazolidinedione|meglitinide|alpha-glucosidase|amylin|antihypoglycemic"),
    ("Pain and inflammation", r"nonsteroidal anti-inflammatory|opioid|analgesic|cyclooxygenase|"
                              r"local anesthetic|amide local anesthetic|ester local anesthetic"),
    ("Corticosteroids", r"corticosteroid"),
    ("Mental health", r"antidepressant|serotonin reuptake|serotonin and norepinephrine|tricyclic|monoamine oxidase|"
                      r"antipsychotic|mood stabilizer|lithium|central nervous system stimulant|"
                      r"amphetamine|anxiolytic|phenothiazine|butyrophenone"),
    ("Sleep and anxiety", r"benzodiazepine|gamma-aminobutyric|hypnotic|sedative|orexin|melatonin"),
    ("Epilepsy and neurology", r"anti-epileptic|anticonvulsant|dopamine agonist|parkinson|"
                               r"cholinesterase inhibitor|triptan|serotonin-1b|migraine|nmda|potassium channel|"
                               r"decarboxylase inhibitor|catechol-o-methyltransferase"),
    ("Muscle relaxants", r"muscle relaxant|neuromuscular blocker"),
    ("Stomach and digestion", r"proton pump|histamine-2|antiemetic|laxative|antidiarrheal|serotonin-3|serotonin-4|"
                              r"prokinetic|antispasmodic|aminosalicylate|bile acid"),
    ("Hormones and contraception", r"estrogen|progestin|androgen|thyroid|contracepti|gonadotropin|"
                                   r"testosterone|vasopressin|somatostatin|growth hormone|bisphosphonate|"
                                   r"selective estrogen|aromatase"),
    ("Allergy and asthma", r"histamine-1|antihistamine|leukotriene|bronchodilator|beta2-adrenergic agonist|"
                           r"beta-adrenergic agonist|mast cell|methylxanthine|antitussive|anticholinergic|"
                           r"allergenic extract"),
    ("Cancer", r"antineoplastic|kinase inhibitor|alkylating|antimetabolite|antiandrogen|topoisomerase|"
               r"programmed death|microtubule|anthracycline|platinum|proteasome|histone deacetylase|"
               r"cd20|cd19|cd38|her2|folate analog|leukocyte growth factor|asparagine|vascular endothelial growth"),
    ("Immune system", r"immunosuppress|calcineurin|tumor necrosis|interleukin|janus kinase|"
                      r"disease-modifying|monoclonal antibody|interferon|complement inhibitor|"
                      r"sphingosine|integrin"),
    ("Urology and sexual health", r"phosphodiesterase 5|5-alpha reductase|antimuscarinic|"
                                  r"beta3-adrenergic"),
    ("Gout", r"xanthine oxidase|uricosuric|uric acid"),
    ("Skin", r"retinoid|keratolytic|psoralen"),
    ("Vitamins, minerals and fluids", r"vitamin|electrolyte|mineral|^calcium$|iron replacement|iron chelator|"
                                      r"potassium binder|phosphate binder|parenteral nutrition|osmotic|isotonic|"
                                      r"amino acid|lysosomal|enzyme replacement"),
    ("Diagnostic agents", r"diagnostic agent|contrast agent|radiographic|radioactive|imaging agent"),
    ("Antidotes", r"antidote|chelator|opioid antagonist|cholinesterase reactivator|digoxin immune"),
    ("Anesthesia", r"general anesthetic"),
]
# Fallback for drugs without an FDA class (most labels): what the "Uses" section treats.
USE_CATEGORIES = [
    # Specific uses first: only the first two matches count.
    ("Anesthesia", r"anesthesia|nerve block"),
    ("Diagnostic agents", r"diagnostic|imaging|contrast|scintigraph"),
    ("Antidotes", r"(treatment|management|emergency treatment) of (known or suspected )?(an )?\w* ?overdos|"
                  r"poisoning|reversal of|antidote"),
    ("Antivirals", r"\bhiv\b|hepatitis [bc]\b|herpes|influenza|cytomegalovirus|covid|sars-cov"),
    ("Antibiotics", r"bacteri|infections caused by|pneumonia|urinary tract infection|tuberculosis|gonorrh|syphilis"),
    ("Antifungals", r"fungal|candid|aspergill"),
    ("Antiparasitics", r"malaria|parasit|helminth|worm infection|scabies|\blice\b"),
    ("Cancer", r"cancer|carcinoma|lymphoma|leukemia|myeloma|tumou?r|melanoma|sarcoma|neoplas"),
    ("Heart and blood pressure", r"hypertension|heart failure|angina|arrhythmi|atrial fibrillation|"
                                 r"myocardial infarction|hypotension|\bshock\b"),
    ("Cholesterol", r"hyperlipid|cholesterol|triglycerid|dyslipid"),
    ("Blood and clotting", r"thrombo|embolism|anemia|anaemia|hemophilia|bleeding"),
    ("Diabetes", r"diabetes|glycemic control|hypoglycemia"),
    ("Mental health", r"depress|schizophreni|bipolar|attention deficit|\badhd\b|psychos|alcohol dependence|"
                      r"opioid (use disorder|dependence)"),
    ("Sleep and anxiety", r"insomnia|anxiety|sedation"),
    ("Epilepsy and neurology", r"seizure|epilep|parkinson|alzheimer|migraine|multiple sclerosis|dementia|"
                               r"neuropath"),
    ("Pain and inflammation", r"\bpain\b|analgesi|osteoarthritis|inflammat"),
    ("Allergy and asthma", r"asthma|allerg|\bcopd\b|bronchospasm|rhinitis|urticaria"),
    ("Stomach and digestion", r"ulcer|gastroesophageal|reflux|nausea|vomiting|constipation|diarrh|bowel|"
                              r"crohn|colitis"),
    ("Hormones and contraception", r"contracept|menopaus|hypothyroid|hypogonadism|osteoporosis|infertility|"
                                   r"endometriosis"),
    ("Immune system", r"transplant|rheumatoid|psoriasis|lupus|immunodeficien(?!cy virus)"),
    ("Urology and sexual health", r"overactive bladder|erectile|prostat|urinary incontinence"),
    ("Skin", r"\bacne\b|dermatitis|eczema|rosacea|dermatos"),
    ("Eye care", r"glaucoma|ocular|conjunctivitis|intraocular"),
    ("Vitamins, minerals and fluids", r"(?<!immuno)deficiency|electrolyte|fluid (and|or) |replenish|parenteral nutrition|"
                                      r"hypokalemia|dehydration|hypocalcemia"),
    ("Gout", r"\bgout\b|hyperuricemia"),
    ("Muscle relaxants", r"muscle spasm|spasticity"),
]
ROUTE_CATEGORIES = {"OPHTHALMIC": "Eye care", "DENTAL": "Oral care", "TOPICAL": "Skin",
                    "RESPIRATORY (INHALATION)": "Allergy and asthma", "VAGINAL": "Hormones and contraception"}


def categories_for(classes, routes, uses):
    classes = [c.lower() for c in classes]
    found = [name for name, pattern in CATEGORIES if any(re.search(pattern, c) for c in classes)]
    if not found:
        uses = uses[:700].lower()
        found = [name for name, pattern in USE_CATEGORIES if re.search(pattern, uses)][:2]
    found += [ROUTE_CATEGORIES[r] for r in routes if r in ROUTE_CATEGORIES and ROUTE_CATEGORIES[r] not in found]
    return found or ["Other"]


def subsections(t):
    """Break PLR subsection numbers ("5.1 Serotonin Syndrome") onto their own lines;
    drop the empty "( )" left where cross-references ("5.1") were removed."""
    t = re.sub(r"\s*\(\s*(,\s*)*\)", "", t)
    return re.sub(r"(?<=[.:)\]])\s+(\d{1,2}\.\d{1,2})\s+(?=[A-Z][a-z])", r"\n\n**\1** ", t)


def shorten(t, limit, set_id):
    if len(t) <= limit:
        return t
    cut = t.rfind(". ", 0, limit)
    t = t[: cut + 1 if cut > limit // 2 else limit]
    return (f"{t} …\n\n*(Shortened. The full text is in the official label: DailyMed set ID {set_id}.)*")


def score(rec):
    """Complete, current-format labels with a patient leaflet first."""
    s = sum(1 for f, *_ in SECTIONS if has(rec, f))
    if has(rec, "warnings_and_cautions"):
        s += 2
    if has(rec, "spl_medguide") or has(rec, "spl_patient_package_insert"):
        s += 2
    return s


def form_key(rec):
    return re.sub(r"[^a-z0-9]", "", text(rec, "dosage_forms_and_strengths").lower())[:80]


def section(rep, field, heading, lead, limit, level="##"):
    content = shorten(subsections(body(text(rep, field), lead)), limit, rep.get("set_id", "unknown"))
    tables = rep.get(f"{field}_table") if field in TABLES else None
    if tables:
        content += "\n\n" + "\n\n".join(table_md(t) for t in tables[:3])
    return f"{level} {heading}\n\n{content}\n"


def build(out, source):
    p = source.get("params", {})
    groups = {}
    meta = {}
    for rec, meta in fetch_all(p.get("product_type", "HUMAN PRESCRIPTION DRUG"), KEEP):
        subs, routes = group_key(rec)
        if not subs or not (has(rec, "indications_and_usage") and has(rec, "dosage_and_administration")):
            continue
        group = groups.setdefault((subs, routes), Group(join_names(subs)))
        group.add(rec, score(rec), form_key(rec))

    routes_per_combo = collections.Counter(subs for subs, _ in groups)
    notice = f"> **Note:** {p['notice']}\n" if p.get("notice") else ""

    for (subs, routes), group in groups.items():
        rep = group.representative()
        title = group.name
        if routes_per_combo[subs] > 1:
            title += f" ({', '.join(r.lower() for r in routes)})"
        o = rep.get("openfda", {})

        parts = [f"# {title}\n", notice]
        facts = [f"**Route:** {', '.join(r.lower() for r in routes)}"]
        forms = [f for f, _ in group.substances.most_common(6) if f.lower() not in title.lower()]
        if forms:
            facts.append(f"**Ingredient forms:** {', '.join(forms)}")
        classes = [c for c, _ in group.classes.most_common(3)]
        if classes:
            facts.append(f"**Drug class:** {', '.join(classes)}")
        facts.append(f"**Labels on file:** {group.count}")
        parts.append("  \n".join(facts) + "\n")
        top, more = group.brand_names(subs)
        if top:
            parts.append("**Brand and product names:** " + ", ".join(top) + (f" and {more} more" if more > 0 else "") + "\n")

        populations = has(rep, "use_in_specific_populations")
        for field, heading, lead, limit in SECTIONS:
            if not has(rep, field) or (populations and field in POPULATION_FIELDS):
                continue
            if field == "boxed_warning":
                parts.append(section(rep, field, "⚠ Boxed warning", lead, limit))
            else:
                parts.append(section(rep, field, heading, lead, limit))
        patient = next((s for s in PATIENT if has(rep, s[0])), None)
        if patient:
            parts.append(section(rep, *patient))

        parts.append(
            f"---\n\n*Source: FDA prescribing information via openFDA, label effective {label_date(rep)}, "
            f"DailyMed set ID {rep.get('set_id', 'unknown')}. Public domain.*\n"
        )
        out.page(title, "\n".join(x for x in parts if x),
                 categories_for(classes, routes, text(rep, "indications_and_usage")))

    return meta.get("last_updated", time.strftime("%Y-%m-%d"))
