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
| Mathematics | **Linear Algebra (Wikibooks)** — Complete proof-based linear algebra textbook (after Jim Hefferon's book): linear systems and Gauss' method, vector spaces, linear maps and matrices, determinants, eigenvalues and Jordan form, inner product spaces and the spectral theorem, with applied topics such as Markov chains, networks and line of best fit. Formulas are in TeX. | https://en.wikibooks.org/wiki/Linear_Algebra | CC BY-SA 4.0 (Wikibooks). | `https://github.com/Denrox/offline-library/tree/math-linear-algebra` |
| Medicine | **Army First Aid (ATP 4-02.11, 2026)** — U.S. Army manual for non-medical personnel: bleeding control and tourniquets, airway, breathing, shock, head and eye injuries, burns, fractures and splinting, bites and stings, heat and cold injuries, evacuation. | https://armypubs.army.mil/epubs/DR_pubs/DR_a/ARN46159-ATP_4-02.11-000-WEB-1.pdf | Public domain (U.S. Government work); approved for public release, distribution unlimited. | `https://github.com/Denrox/offline-library/tree/medicine-first-aid-army` |
| Medicine | **MedlinePlus health topics** — About 1,000 plain-language health topics (conditions, symptoms, tests, wellness) from the U.S. National Library of Medicine. | https://medlineplus.gov/ | Public domain (U.S. Government work). | `https://github.com/Denrox/offline-library/tree/medicine-medlineplus` |
| Medicine | **Over-the-counter drugs (FDA labels)** — About 2,300 non-prescription medicines and products (pain relievers, cold and allergy, digestive, skin, eye and oral care, sunscreens, antiseptics) from official U.S. "Drug Facts" labels, one page per active ingredient with the brand names it is sold under. Homeopathic products are excluded. | https://open.fda.gov/apis/drug/label/ | Public domain (CC0, openFDA). | `https://github.com/Denrox/offline-library/tree/medicine-drugs-otc` |
| Medicine | **Prescription drugs (FDA labels)** — About 2,900 prescription medicines from official U.S. prescribing information: uses, dosage, contraindications, boxed warnings, side effects, interactions, pregnancy and children, overdose, and the Medication Guide for patients where there is one. One page per active ingredient with its brand names. | https://open.fda.gov/apis/drug/label/ | Public domain (CC0, openFDA). | `https://github.com/Denrox/offline-library/tree/medicine-drugs-rx` |
| Navigation | **Land navigation (Wikipedia)** — Map and compass navigation from hand-picked Wikipedia articles: topographic maps and contour lines, map scale, coordinates (latitude and longitude, UTM, MGRS, WGS 84), compass use and magnetic declination, bearings, finding your position by resection, dead reckoning and pace counting, the stars, and how satellite navigation works and fails (jamming, spoofing). | https://en.wikipedia.org/ | CC BY-SA 4.0 (Wikipedia). | `https://github.com/Denrox/offline-library/tree/navigation-wikipedia` |
| Radio | **Amateur Radio Q&A (Stack Exchange)** — About 2,300 well-received questions from Amateur Radio Stack Exchange with their best answers: antennas you can build, coax, baluns and SWR, programming handhelds (Baofeng UV-5R, Yaesu, Icom, Kenwood) and tone squelch, licences and operating procedure, HF propagation, VHF/UHF and repeaters, digital modes, CW and APRS, receivers and SDR, interference, power, batteries and lightning safety, emergency and field operation, and satellites. | https://ham.stackexchange.com/ | CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange. | `https://github.com/Denrox/offline-library/tree/radio-ham-qa` |
| Radio | **Meshtastic documentation** — Off-grid text messaging and position sharing over LoRa radios without phone networks: what Meshtastic is and how the mesh works, getting started and flashing firmware, every radio and module setting (region, presets, channels, encryption, position, telemetry, store and forward, range test), the Android and iPhone apps, the Python command line, Linux nodes (meshtasticd), antennas, and the supported devices (LILYGO T-Beam, T-Echo, T-Deck, Heltec, RAK WisBlock, Seeed SenseCAP and more) with their specifications. | https://meshtastic.org/docs/ | GPL-3.0 (Meshtastic documentation). | `https://github.com/Denrox/offline-library/tree/radio-meshtastic` |
| Radio | **Radio communication (Wikipedia)** — Two-way radio from hand-picked Wikipedia articles: how radios, squelch and repeaters work, licence-free services (PMR446, FRS, GMRS, CB, LPD433, marine VHF), amateur radio and its bands, radio procedure, phonetic alphabet, Morse and Q codes, distress and emergency communication, antennas, feed lines and connectors, propagation, analog and digital modes (DMR, D-STAR, P25, TETRA, APRS, Winlink, FT8), mesh messaging (Meshtastic, LoRa), receivers and SDR, jamming and communications security, satellite phones and Starlink, and specific radios: Baofeng, Yaesu, Icom, Elecraft, Motorola, military AN/PRC and Soviet/Russian R-series sets. | https://en.wikipedia.org/ | CC BY-SA 4.0 (Wikipedia). | `https://github.com/Denrox/offline-library/tree/radio-wikipedia` |
| Survival | **Army Survival (ATP 3-50.21, 2018)** — U.S. Army survival manual: survival mindset, survival medicine and medicinal plants, finding and purifying water, wild food (edible and poisonous plants, trapping, fishing), fire, shelter and clothing, navigation and river crossing, survival kits, and knots and rope. | https://armypubs.army.mil/epubs/DR_pubs/DR_a/pdf/web/ARN12086_ATP%203-50x21%20FINAL%20WEB%202.pdf | Public domain (U.S. Government work); approved for public release, distribution unlimited. | `https://github.com/Denrox/offline-library/tree/survival-army` |
<!-- catalog:end -->

To use a source, open **Cheatsheets → Sources** in the ui-apt-mirror admin
panel and add its URL from the last column.

Content is general reference information. Medical sources are not medical
advice; in an emergency call your local emergency number.

## Adding a source

1. Reuse a converter in `converters/` (for example `wikibook` for any Wikibooks
   book, `wikipedia` for a hand-picked set of Wikipedia articles grouped into
   categories, `docusaurus` for a documentation site built with Docusaurus,
   `stackexchange` for a Stack Exchange site from its Kiwix ZIM) or write a new
   one: a module with `build(out, source)` that calls
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
`manifest.json` describes the branch for clients that check for updates:
`{"format": 1, "id", "pages", "categories", "bytes", "content_hash", "snapshot"}`,
where `bytes` is the total size of the pages and `content_hash` (SHA-256 over the
pages and `categories.json`) changes only when the content does.

Only add content whose license allows redistribution, and record the license
and attribution in `sources.json`.
