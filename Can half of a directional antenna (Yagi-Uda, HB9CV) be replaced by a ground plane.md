# Can half of a directional antenna (Yagi-Uda, HB9CV) be replaced by a ground plane?

*Tags: antenna-theory, yagi · score 5*

## Question

Consider a center-fed dipole antenna. It‘s well understood how the bottom element can be replaced by a ground plane (in practice, generally a few rods but in principle a conducting plate would work as well), creating a „groundplane antenna“.

I was wondering whether it would be possible to do the same transformation for directional antannas with either parasitic (Yagi-Uda) or active (HB9CV) directors.

Are there any publications out there discussing this idea? What consequences would this change have in terms of antenna properties, and how would antenna theory explain radiation?

## Answer (score 6, by Brian K1LI)

Yes, this is a time-honored practice, particularly at the longer wavelengths where horizontal antennas need to be mounted quite high to provide low-angle radiation for DX work. Callum, M0MCX, presents a nice gallery of information about his three-element parasitic array for 40-m:

The radiating elements are the three black verticals in the foreground behind the fence.

While a "vertical yagi" can be an effective solution for low-angle radiation, it's important to remember:

- the ground screen consumes considerable area
- you lose the reflection gain attendant upon horizontal antennas
- ground conductivity near the antenna strongly affects efficiency and feedpoint impedance
- ground conductivity out to several wavelengths from the antenna determines how low the radiation angle will be

M0MCX demonstrates the advantage he hopes to achieve:

but this comparison doesn't tell the whole story:

- the text says the feedpoint shows a very low SWR across the entire 40-m band without any matching circuitry, indicating substantial losses in the system which may reduce radiation more for a vertical than for a horizontal antenna
- the comparison puts a dipole at 20-ft, while the vertical elements are at least 50% taller

I point this out only to illustrate the complexity of an antenna system in the real world, not to criticize the efforts of M0MCX, who is obviously enjoying his fine antenna. All antennas require compromises, so carefully consider your goals and resources, then set your expectations accordingly.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16639/can-half-of-a-directional-antenna-yagi-uda-hb9cv-be-replaced-by-a-ground-plane, by jstarek, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
