# Is copper-clad steel a good material for wire antennas?

*Tags: wire-antenna, antenna-construction · score 6*

## Question

There are some people selling steel wire plated with copper for making wire antennas.

Perhaps the most well-known brand of this product, Copperweld, makes at least two kinds of copper-clad wire, copper-clad steel (CCS), and copper-clad aluminum (CCA). On Copperweld's applications page, they write:

CCA is a natural for antennas in a variety of applications such as large ground-based arrays or even ham radios or mobile phones. CCA is applicable to most localized RF transmitters and is being used near radio towers to shield other structures from creating interference.

(note: CCA, the A for *aluminum*)

Wikipedia on copper-clad aluminum lists applications:

The primary applications of this conductor revolve around weight reduction requirements. These applications include high-quality coils, such as the voice coils in headphones, portable loudspeakers or mobile coils; high frequency coaxial applications; such as RF antennas; CATV distribution cables; and power cables.

The article on copper-clad steel lists nothing about RF applications:

Grounding, union of ground rods to metallic structures, meshes, substations, power installations and lightning arrestors.

To be fair, most of the amateur radio sites I've seen selling anything similar call it simply "copper-clad wire", and don't specify if the core is steel, aluminum, or gold.

It seems to be understood that [steel is not a good antenna wire](Effect%20of%20different%20metals%20for%20antenna%20elements.md). So, is copper-clad steel a good antenna wire, or no? Why?

## Answer (score 7, by hotpaw2)

Depending on the RF frequency and wire diameter, skin effect may dominate the effective resistance at that frequency. If so, since copper has a lower resistance, any resistive losses of a copper skin might be lower. Silver or gold plating would be even better, but a little too expensive except in exotic applications.

However, pure copper also has a lower tensile strength that steel, so would be more likely to fail under load (wind, etc.) without a stronger core. Copper is usually more expensive than steel as well. Steel is cheaper and stronger. And AL is lighter, if weight is an important issue.

If corrosion or oxidation is likely to affect reliability, than gold plating might increase contact reliability, or wire lifetime in unusual chemical environments.

Thus, a blend may be the best trade-off, depending on all the constraints and requirements.

## Answer (score 4, by Adam Davis)

Copper clad steel is a good antenna wire. It's not the best for every application, but it's good for most applications.

The advantages it has are:

- Doesn't stretch as much as copper and other good conductors (which changes the resonant frequency)
- Stronger than other wires, so when you don't need a large gauge for electrical reasons, you can save on weight and size and still have sufficient strength for self support
- Less expensive than copper wire of a similar gauge, strength, and electrical capacity at RF frequencies
- More conductive than steel

It does have a few disadvantages:

- More expensive than steel wire of a similar gauge and strength
- Have to correctly seal the ends to avoid oxidation of the center steel conductor

Keep in mind that at frequencies between 3.5MHz and 30MHz the conductor's skin depth, the depth at which 63% of the electrical current flows, is between 35uM and 12uM for copper wire. The link you gave has 30% or more copper, which provides a total copper skin depth much greater than 35uM, so the majority of the current will be carried in the copper cladding at the frequencies we are interested in for HF and higher frequency antennas.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1391/is-copper-clad-steel-a-good-material-for-wire-antennas, by Phil Frost - W8II, hotpaw2, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
