# Not-too-distant saltwater ground

*Tags: antenna, hf, grounding, earth · score 3*

## Question

### Problem

I'm planning on mounting a vertical HF multiband antenna on the edge of my roof.

Due to the presence of a paved walkway and some other similar property constraints, I have no room for radials anywhere near the mounting area.

However, I do have a saltwater canal behind my yard.

This is a rough and not-to-scale rendering of the situation. The red tapered cylinder represents the vertical antenna. The green part is the yard. Then there is the seawall and the canal itself. The yellow cylinder would be a floating foil-lined tube to maximize surface area and maintain water surface contact as the tides rise and fall.

The base of the antenna will be about 10ft above the surrounding grade and the canal is about 60ft away from the antenna mounting point.

### Questions:

1. Can this idea work to provide a good ground for transmission?
2. How should I connect the antenna to this somewhat distant ground?

### Thoughts:

If I were just to try this without seeking advice, I'd run coax with the center conductor attached to the antenna base ground out to the floating tube, probably in some PVC pipe to protect the cable itself from the soil. Is that a reasonable plan?

I've tried modeling this in CocoaNEC, but the transmission line interface is broken and the project hasn't seen active development for a while.

I've considered mounting the antenna on the sea wall itself, but the surrounding area makes that tricky.

## Accepted answer (score 7, by Phil Frost - W8II)

With the canal 60 feet away it's not of much help.

The objective with a monopole antenna is not just to have any ground connection, but to have a low-loss ground *plane* under the base of the antenna. The ground plane provides the return current and creates an image antenna. The return current density is highest where it converges at the base of the antenna.

As a rule of thumb, a radius of a quarter-wavelength around the base is where the ground is most important. Small improvements can be realized by extending the ground out as far as two wavelengths. Beyond that, the ground is insignificant.

The canal is so far away, and only on one side of the antenna, so it will have negligible effect on the antenna. The antenna's operation will be dominated by things closer to the base, like the feedline, or the wire you run from the antenna to the canal. You'll essentially have a vertical with one radial.

If at all possible, I'd suggest considering alternate antenna designs. Verticals can be made to work well with as few as two radials, but this involves tuning them to be resonant, and raising them several feet off the ground. This minimizes the current in the soil, thus minimizing losses.

Without deliberately installing radials you will make some contacts, and if that's all you're able to install then by all means go for it. But it's far from ideal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9867/not-too-distant-saltwater-ground, by Eric, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
