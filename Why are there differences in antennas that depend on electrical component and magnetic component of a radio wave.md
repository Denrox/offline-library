# Why are there differences in antennas that depend on electrical component and magnetic component of a radio wave?

*Tags: antenna, antenna-construction, loop-antenna, magnetic-loop · score 9*

## Question

I understand the idea that when we are targeting the electrical component of the radio waves we need to have some form of a linear conductor that receives the electrical component, this creates a current in the circuit and thus induces a signal. But in antennas that are designed to capture the magnetic component we use loop antennas.

From the understanding of how radio waves are propagated, the electrical and the magnetic component are orthogonal to each other and are in phase, and therefore the wavelength must be the same as well (assumption). So I would expect the antenna that focuses on the magnetic component to be similar in design to the antennas that capture the electrical component.

But then, why do these two antennas look remarkably different?

## Accepted answer (score 10, by Phil Frost - W8II)

In free space, the electric and magnetic fields are always in a fixed ratio, a physical constant called the impedance of free space, about 377 volts per ampere. The two are always in phase (and thus have identical wavelength) but in orthogonal angles. In fact, the magnetic field is explained by relativity to be the effect of length contraction of moving electric charges. Viewed in this light, the magnetic field doesn't really exist: there are just electric fields, and relativistic distortions of electric fields in moving reference frames. The "magnetic field" is an abstraction that accounts for relativistic effects as they apply to electric charges.

Point being, the two are quite inseparable: it's not possible to build an antenna which receives just the "magnetic component" of a radiated wave, because the magnetic and electric fields are the *same thing*. So I think your intuition is on the right track.

Theoretically, an antenna could be described only in terms of Maxwell's equations, or even more modern science if you prefer. But this wouldn't be very practical. To be able to reason more intuitively about antennas, or any electrical device, we apply fundamental laws to derive abstractions which are less general but more practical.

For example, a small loop can be described by Faraday's law of induction. But if the loop becomes longer that abstraction stops working, because we must account for differences in phase of the waves propagating around the loop. If the loop's perimeter grows to a full wavelength, it's easier to explain it as a folded dipole. A typical explanation of folded dipoles involves transmission lines and quarter-wave stubs, abstractions that have no particular association with magnetic or electric fields.

So to answer your question, I'd say maybe you're thinking about it backwards. An antenna can't "target" the electric or magnetic field specifically: after all, for electromagnetic radiation the two are the same thing. But there are many possible ways to design an antenna, and there are many abstractions we may choose to use to explain how those antennas work, and some of those abstractions (like Faraday's law) are most conveniently phrased in terms of the magnetic field. It's not that loop antennas receive a different "kind" of radiation, just that the magnetic field happens to be the most accessible abstraction for conveying an intuitive sense of the approximate operation of the antenna.

## Answer (score 3, by Cecil - W5DXP)

Whether an antenna is called an "electrical" or "magnetic" antenna, the generated and captured far-field electromagnetic photons of the same wavelength are identical. The difference in the two antennas occurs in the near-field where the electric field is dominant for electrical antennas and the magnetic field is dominant for magnetic antennas. The difference is most noticeable during receive in noisy environments.

## Answer (score 2, by Richard Fry)

RE: *It's an oversimplification to say that antennas respond to E or H fields. Antennas respond to the electromagnetic wave. Loop antennas are just as "electric" as dipoles.*

Following is some background on this topic from Johnson & Jasik's "ANTENNA ENGINEERING HANDBOOK, 2nd Edition, Section 5-4:

"RECEIVING LOOP When the electrically small loop is used as a receiving antenna, the voltage developed at its open-circuited terminals is proportional to the component of the **incident magnetic flux density normal to the plane of the loop**, where the incident field is assumed to be uniform over the area of the loop. This simple relation makes the small loop useful as a probe for measuring the magnetic flux density."

Note (1) that magnetic flux density is related to the r-f current component of a radiated e-m wave, and (2) that such a receive loop is insensitive to the E-field that accompanies that H-field.

Edit of 30 May 2019

Quoted from:

Proceedings of the Institute of Radio Engineers

Volume 23, Number 4; April, 1935

GENERAL CONSIDERATIONS OF TOWER ANTENNAS FOR BROADCAST USE

by H. E. GIHRING AND G. H. BROWN

(RCA Victor Company, Inc., Camden, New Jersey)

*APPENDIX B MAGNETIC FLUX DENSITY MEASUREMENTS WITH A LOOP ANTENNA

*The ordinary field intensity measuring set makes use of a loop antenna. This device inherently measures the magnetic flux density of a radiated field, and really yields the electric intensity by virtue of the fact that at remote points from the source of radiation the magnitudes of the electric vector and the magnetic flux density vector are related in a constant ratio.*

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12670/why-are-there-differences-in-antennas-that-depend-on-electrical-component-and-, by Bartha, Phil Frost - W8II, Cecil - W5DXP, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
