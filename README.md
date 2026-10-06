# Offline library

Reference manuals on many topics, converted to markdown for offline use with
the cheatsheets in [ui-apt-mirror](https://github.com/Denrox/ui-apt-mirror).

This `main` branch holds the converters. Each source is generated into a branch
of its own, named `<topic>-<source>`, which contains only that source's pages,
its `categories.json` and its license. A branch is a self-contained download, so
adding one source never pulls in the others.

## Catalog

<!-- catalog:start -->
| Topic | Source | Pages from | License | Add to ui-apt-mirror |
|---|---|---|---|---|
| Medicine | **Army First Aid (ATP 4-02.11, 2026)** — U.S. Army manual for non-medical personnel: bleeding control and tourniquets, airway, breathing, shock, head and eye injuries, burns, fractures and splinting, bites and stings, heat and cold injuries, evacuation. | https://armypubs.army.mil/epubs/DR_pubs/DR_a/ARN46159-ATP_4-02.11-000-WEB-1.pdf | Public domain (U.S. Government work); approved for public release, distribution unlimited. | `https://github.com/Denrox/offline-library/tree/medicine-first-aid-army` |
| Medicine | **MedlinePlus health topics** — About 1,000 plain-language health topics (conditions, symptoms, tests, wellness) from the U.S. National Library of Medicine. | https://medlineplus.gov/ | Public domain (U.S. Government work). | `https://github.com/Denrox/offline-library/tree/medicine-medlineplus` |
| Medicine | **Over-the-counter drugs (FDA labels)** — About 2,300 non-prescription medicines and products (pain relievers, cold and allergy, digestive, skin, eye and oral care, sunscreens, antiseptics) from official U.S. "Drug Facts" labels, one page per active ingredient with the brand names it is sold under. Homeopathic products are excluded. | https://open.fda.gov/apis/drug/label/ | Public domain (CC0, openFDA). | `https://github.com/Denrox/offline-library/tree/medicine-drugs-otc` |
| Medicine | **Prescription drugs (FDA labels)** — About 2,900 prescription medicines from official U.S. prescribing information: uses, dosage, contraindications, boxed warnings, side effects, interactions, pregnancy and children, overdose, and the Medication Guide for patients where there is one. One page per active ingredient with its brand names. | https://open.fda.gov/apis/drug/label/ | Public domain (CC0, openFDA). | `https://github.com/Denrox/offline-library/tree/medicine-drugs-rx` |
<!-- catalog:end -->

To use a source, open **Cheatsheets → Sources** in the ui-apt-mirror admin
panel and add its URL from the last column.

Content is general reference information. Medical sources are not medical
advice; in an emergency call your local emergency number.

## Adding a source

1. Reuse a converter in `converters/` (for example `wikibook` for any Wikibooks
   book) or write a new one: a module with `build(out, source)` that calls
   `out.page(title, markdown, categories)` for every page and returns a
   snapshot label (a date or version).
2. Add an entry to `sources.json`: `id` (the branch name: lowercase,
   `<topic>-<source>`, no `/`), `topic`, `title`, `description`, `converter`,
   `source_url`, `license`, `attribution`, and `params` if the converter takes any.
3. Check it locally: `pip install -r requirements.txt` (add any package a new
   converter needs there), `python3 build.py <id> /tmp/out`, then `python3 build.py --readme`.
4. Push to `main`. The **Update sources** workflow builds every source daily and
   commits to its branch only when the content changed; run it by hand from the
   Actions tab to publish a new source straight away.

Each page is a markdown file whose first `# Heading` is its title.
`categories.json` maps a category to the pages in it:
`{"Category": ["Page.md", ...]}`.

Only add content whose license allows redistribution, and record the license
and attribution in `sources.json`.
