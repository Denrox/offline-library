# Is "coil loading" a type of impedance match?

*Tags: antenna, impedance-matching · score 5*

## Question

If I have a too short dipole, or vertical, I can add a coil to lenghten in electrically. But it's my understanding that I could also do this with any other kind of match: given the complex impedance at the frequency of interest, I could calculate, for example, a LC network that will match my radiator to present 50 ohms.

So what's the difference between doing it one or the other way? Is a "loading coil" a type of match or does it behave differently?

## Accepted answer (score 3, by Brian K1LI)

The short answer to your question is, "Yes."

Every change made to an antenna is likely to change the feedpoint impedance: lengths, diameters and configurations of driven and parasitic conductors; positions, values and parasitic characteristics of "loading" circuits; distance from ground and "nearby" conductive structures, including near-resonant feedlines; etc., etc., etc.

The approach used to maximize power transfer from the transmitter to the antenna may or may not include impedance matching circuitry at the feedpoint or as part of the antenna structure, depending on the losses incurred in the feedline as a result of any mismatch. In typical ham antenna applications, resources of time and treasure are relatively limited, so the need for and implementation of impedance matching means are driven by higher-order design constraints.

## Answer (score 3, by Phil Frost - W8II)

Anything done to get the antenna impedance closer to 50 ohms (or whatever the design might call for) can be called an impedance match, loading coils included.

However I would note: many loading coils aren't exactly equivalent to an inductor at the feedpoint.

Quite often, the loading coil is not at the base of the antenna but rather somewhere in the middle. This requires the inductance to be larger, but it also increases the current in the section of the antenna below the coil. Getting more current over a longer length increases radiation efficiency.

There's an optimal place to put it: too high and the inductance required is so high that the resistance of the additional wire required offsets the other gains.

It's also possible to "stretch out" the coil which distributes the inductance over the entire length. For example consider the rubber ducky antenna, ubiquitous on handheld radios.

Or consider the MFJ hamstick which has a lower section of loosely wound coil like a rubber ducky, a tightly wound loading coil in the middle, and a simple whip at the top.

So yes, loading coils are a matching technique. And it's true it's possible, with ideal lossless components, to make a matching network from inductors, capacitors, and transmission line stubs that will match any load.

But when you start to consider real components with loss that can impact performance, the reasons for one matching technique over another become more apparent. For example, an air-core loading coil in the middle of an antenna performs differently than an inductor wound on a lossy ferrite core at the feedpoint.

## Answer (score 2, by Richard Fry)

A "loading coil" in series with its feedpoint terminals can offset the capacitive reactance of an electrically short set of radiating wires (where the *jX* term of the feedpoint impedance *R -jX* is zero ohms at the operating frequency).

However the loading coil value and its physical location in the antenna system have much less affect on matching the R term of the feedpoint impedance to the Zo of the transmission line connecting it back to the source (transmitter).

An electrically short antenna system still can have **very** low radiation resistance, even though a loading coil has reduced the j term to zero ohms.

Radiation resistance is the only dissipative resistance that produces useful e-m radiation into space. With very short radiators using only a loading coil, the radiation resistance can be only a few tenths of an ohm, even though the feedpoint Z has zero reactance (i.e., it is "resonant").

A more complex matching network can match both the R and jX terms of the feedpoint Z of a short antenna to the Zo of a transmission line connected to its input terminals. However the radiation efficiency of that antenna system will be relatively poor.

Radiation efficiency = Radiation Resistance / Total Dissipative Resistance of the Antenna System.

So for example, if a very short, center-fed dipole antenna has a radiation resistance of 1 Ω, and the ESR of the matching network used to produce a 50 Ω feedpoint impedance to it is 9 Ω, then the radiation efficiency of that system is 1/10 = 0.1, or 10%.

**Not** matching both the R term and the j term to the source impedance reduces the radiation efficiency of that antenna system even further.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16444/is-coil-loading-a-type-of-impedance-match, by hjf, Brian K1LI, Phil Frost - W8II, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
