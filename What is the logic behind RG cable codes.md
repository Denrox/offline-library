# What is the logic behind RG cable codes

*Tags: coaxial-cable · score 8*

## Question

What is the logic behind the names of different RG cables? The Wikipedia's Coaxial cable page has a list of different coaxial cable standards but I cannot find the internal logic of the naming. I would assume that coding pretty much anything would be easier if you give meaning to the number, such as outer diameter or insulator material. Now the numbers seem totally random.

## Accepted answer (score 11, by Adam Davis)

"RG" stems from old, obsolete military specifications, standing for "radio guide", and the number is actually arbitrary. Part of the reason they are obsolete is that they weren't specific enough - RG-6 can reasonably be assumed to have an 18 gauge solid center conductor, but beyond that the dielectric, velocity factor, or completeness of the shielding conductor aren't always specified. Some amount of standardization exists, as shown in the wikipedia article, with additional characters after the "RG-6" type code.

Whenever you see generalizations like "RG-6 has better performance than RG-59 for application X" you must ask for manufacturer and part number for the two cables, because the performance advantage might not exist with two other "RG-6" and "RG-59" cables.

While we don't necessarily need to shy away from using the generic name, be sure to specify important cable parameters whenever they matter if you are ordering or sharing project information. Otherwise you may end up with a cable that doesn't meet your needs, or someone attempting to replicate your project or solve your problem will be unsuccessful at duplicating your setup.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1135/what-is-the-logic-behind-rg-cable-codes, by OH2FXN, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
