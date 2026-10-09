# antenna in the rain

*Tags: antenna-theory, antenna-construction, hf, mobile · score 6*

## Question

What kind of changes can be expected in the behavior (resonance, SWR, etc.) of a mobile vertical HF antenna between dry conditions and wet rainy weather? (assume a coax feed-line and low SWR in dry conditions)

Is some form of weatherproofing required/recommended? (beyond that required to keep the upholstery or trunk dry)

Added:

The hollow core of a hamstick vertical, inside the loading windings, ended up filled with water after a couple days in heavy rain. I unstopped the ends, drained and dried it in the sun, and the SWR inside 20M went from over 5 to under 1.5. Could water inside the windings during the rainstorm have been part or all of the issue?

## Answer (score 10, by Phil Frost - W8II)

The antenna itself won't be significantly affected by the water.

However, waterproofing the coax connection is essential. If this is not done, water will creep inside the coax by capillary action and ruin the coax.

There are several products that can be used, for some examples see 3M's application guide. However all have three elements:

1. An underlying insulating layer which covers exposed conductors and/or facilitates removal of the outer layers of tape later.
2. A sealing layer of rubber or mastic tape.
3. An abrasion and UV protective top layer.

#### Step 0: clean the connection

Remove any dirt or oil with a cloth and alcohol. You'll notice I skipped this step in my photos :)

#### Step 1: Courtesy Wrap

This makes the waterproofing much easier to remove in the future. If this isn't done, over time the sealing tape will creep into the connector, making it nearly impossible to unscrew.

I used Scotch Super 88 because it's what's on hand. Some people like to wrap with the adhesive side up so it doesn't leave goo on the connector. There are also tapes designed for specifically this application which remove cleanly. Stretch the tape to get it to conform to the connector. You'll find cheap electrical tape does not conform nearly as well.

#### Step 2: Sealing Layer

For this I used 3M 2228 rubber mastic tape: it's a sticky mastic with a UV protective layer on one side. The nonsticky side goes out. I prefer mastic tapes in permanent installations since it flows better into tiny cracks, though it can be quite difficult to remove.

An alternative to mastic tape is rubber tape. It's not sticky but still fuses to itself over time. I use it if I know I'll need to dismantle the connection in less than a year.

Proper application is important:

- Stretch the tape as you wrap it such that its width is 75% or less of its original width.
- Be sure to get the tape really well into the exposed threads of the female connector.
- Each wrap should overlap the previous wrap by half the tape width.
- Extend the wrap past the connector, and if your connector has any kind of shrink wrap on it, past that as well.
- If this connection is going to be vertical with the coax coming from the bottom when installed, consider wrapping in the other direction such that water would have to travel upwards to get in.

#### Step 3: Protective Layer

3M 2228 has a UV protective layer built-in. It's the non-sticky side of the tape, so ensure that side is facing out.

Had another kind of tape been used, or if extra protection is desired, a final wrap or two with some vinyl electrical tape would be appropriate. Don't use cheap electrical tape! It will turn brittle and peel off when exposed to the elements.

As before, stretch the tape to get good conformance, though a reduction in tension on the final wrap helps prevent the tape from peeling itself off. For the same reason, it's good practice to cut the tape, rather than to pull it until it breaks.

#### Use N Connectors if Possible

The PL-259 / SO-259 or "UHF" connector common on ham equipment provides no waterproofing whatsoever, which is why it's so important to get the sealing tape into the threads.

On the other hand, male N connectors have a gasket inside which seals against the face of the female connector. It's the red thing inside:

This prevents moisture ingress through the threads.

N connectors are often installed with what looks like heatshrink over the barrel that crimps over the shield. This should be not just ordinary heatshrink but one with a waterproofing adhesive. If done properly, this combined with the gasket should make an N connector waterproof with no taping. However I still tape them for extra protection unless it's a very temporary installation.

As a bonus, N connectors are good up to 11 GHz.

## Answer (score 7, by Marcus Müller)

Water has a drastically different relative permittivity $\varepsilon$ than air (water: ca 88, air: pretty much 1); it is, however, pretty non-conductive, just like air (being distilled and all).

In a good approximation, uniform mixtures of substances with grain sizes significantly below wave length can be represented by a metamaterial with electrical properties defined by the weighted properties of the constituents. Weights are typically just the volume proportions!

So, how much volume percent in air is "moderate to heavy rain"?

Let's define that rain to be 10 mm/hr, that is, on any given surface, in 1 hour, 10mm of water column precipitate.

A large rain drop reaches 8 m/s, and has a diameter of 5 mm, thus a cross-section area of $(2.5\,\text{mm})^2\pi\approx 20\,\text{mm}^2$. Raindrops are pretty much spherical, and not at all "drop-shaped".

On these 20 mm², in one hour, 10 mm or rain fall. Thus, 1 hr brings 200 mm³ (that's 0,20 ml) of rain if you were to put out a cyclinder where that "standard" raindrop fits exactly. Since the volume of a raindrop sphere is $\frac43\pi r^3\approx 65\,\text{mm}^3$, that's pretty much 3 raindrops an hour.

At the 8 m/s that our standard raindrop has, it takes it 0.6 ms to trave 5mm, i.e. it's own height.

That means that for any given point in the volume of the air surrounding your antenna, out of 3600 s in an hour, only 6 ten-thousandsth are occupied with rain being there. That's a concentration $C$ of about $1.7 \cdot 10^{-7}$.

Now, your relative permittivity of the rain-air medium surrounding your antenna would then be

$$ \varepsilon_\text{rainy air} = C \cdot \varepsilon_\text{water} + (1-C) \cdot \varepsilon_\text{air}$$

And, as you can see, that's going to be damn irrelevant for your antenna, unless you match six digits after the comma!

## Answer (score 2, by Scott Earle)

The SWR of the antenna should not be affected too much by rain, but you should do as much as possible to protect the connectors from water.

Water inside coaxial cable changes the characteristics of the cable, as well as corroding the copper.

Many commercial antennas with a coaxial cable running from outside to inside, have heatshrink tubing around any external joints (antenna to base, or base to coax) for this reason.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12559/antenna-in-the-rain, by hotpaw2, Phil Frost - W8II, Marcus Müller, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
