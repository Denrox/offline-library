# Why are some electrical contacts gold plated?

*Tags: connectors · score 5*

## Question

Gold is really expensive. Why then would anyone bother to plate connectors with it? Does it have some unique electrical characteristics that make it useful?

## Accepted answer (score 8, by PearsonArtPhoto)

Gold has several really unique properties that allow for it's frequent use:

1. Gold is the least likely metal to oxidize. From this table, it can be shown that Gold's electro-potential value is -1.1, meaning it should not oxidize at all, even in water. Wikipedia states this is the primary reason that some electrical contacts are gold plated.
2. It is an extremely conductive material, one of the best known.
3. Gold is very malleable, it is very easy to get a thin sheet of it.

Bottom line, it might be a bit overkill, but there are some advantages to gold plated materials.

## Answer (score 5, by Phil Frost - W8II)

Gold makes good contacts because it is very nonreactive, and thus won't corrode or tarnish over time.

Copper is a better conductor than gold, but copper will form a layer of oxide or other tarnish through normal exposure to the elements that will eventually increase the contact resistance of two mating copper contacts, rendering the connection faulty. See for example, architectural copper roofs:

Where this corrosion isn't desired in architectural applications, a protective coating is applied. This isn't feasible in electronic applications since such coatings are generally non-conductive.

Gold does not corrode. Check out this shiny roof:

Although gold is expensive, its physical properties also make it easy to deposit a very thin layer. The plating can be extremely thin while still being effective. Consequently, gold plated contacts aren't as expensive as one might think. Normally the determining concern in the thickness of the plating is wear resistance.

In applications where extremely low cost is more important than maintaining a good connection over time, tin plating is frequently used. Tin is not as good as gold in the corrosion resistance department, but it is better than copper, and cheaper than gold.

## Answer (score 5, by AlmostDone)

Gold plated contacts provide reliable switching when the wetting current is low, because there is no oxide to breach for electrical contact to occur. Ex: a pushbutton switch used to signal a microcontroller digital input has a pullup resistor sized to flow 50 uA when the switch is closed. A switch without gold plating might not be reliable.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1394/why-are-some-electrical-contacts-gold-plated, by Phil Frost - W8II, PearsonArtPhoto, AlmostDone. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
