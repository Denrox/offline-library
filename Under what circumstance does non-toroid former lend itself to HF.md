# Under what circumstance does non-toroid former lend itself to HF?

*Tags: diy, inductor · score 4*

## Question

Many HF circuits posted in my copy of the ARRL manual (1972 edn - Yes, it's a vintage) appear to use a toroidal former with a coil. The same applies to HF circuits posted on the internet.

From what I recall - a toroidal former is to be preferred over a linear former when

- space is at a premium
- coil emi is to be avoided

Apart from these above -

Under what circumstance would a non-toroidal former lend itself to HF?

## Answer (score 3, by Phil Frost - W8II)

HF or not, toroidal transformers are pretty great. They'd be the only kind anyone would use were it not for:

- Fabrication cost. They are hard to wind with automated machines, since you have to somehow pass the end through the middle multiple times. Try winding one without ever letting go of the wire to see the problem.
- They have a lossy core.

 - Ferrite materials become lossier with increasing frequency and at some point become totally useless.
 - Even at HF, ferrite materials have some loss, which can be problematic for power components.

While you could wind a toroidal transformer on a very low-loss material (like air, or something magnetically like it), then there wouldn't be a high-permeability core completing a magnetic circuit. Leakage inductance would thus be higher, so there's reduced justification for the increased cost.

You pretty much summarized the advantages of a toroid core. So, you might use something other than a toroid core when those advantages don't outweigh these disadvantages. Examples:

- loading coils for antennas. Here you don't care much about leakage inductance, since "leakage" is a desirable property in antennas.
- UHF inductors. Ferrite materials are poor performers at high frequencies. Fortunately, higher frequencies require less inductance to achieve the same reactance, so higher frequencies need ferrite cores less.
- high-power inductors for baluns or matching networks. A ferrite core of sufficient size to keep losses acceptably low might be prohibitively expensive.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1772/under-what-circumstance-does-non-toroid-former-lend-itself-to-hf, by VU2NHW, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
