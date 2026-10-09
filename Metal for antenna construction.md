# Metal for antenna construction?

*Tags: antenna, antenna-construction, bandwidth · score 3*

## Question

What do I need to consider when choosing metal for an antenna? How do I determine what thickness to use?

## Accepted answer (score 3, by Ron J. KD2EQS)

My non-technical over-simplified answer; **yes, the type of metal used for an antenna will present different characteristics**. The most obvious is the conductivity. Greater conductivity will yield higher radiation patterns, however, the size and dimension of the conductor also affects its performance. Cost, weight, and ease of manipulation of the material is often MORE of an issue than a slight percentage of increased performance due to the metal type.

Aluminum for example, is a prime choice for beams as it is easy to cut and bend, provides great conductivity, and is lightweight. A copper beam would provide greater conductivity, but as a soft metal it would bend out of shape easily and become unusable. Likewise, a dipole is usually copper wire as its flexibility provides better ease of mounting and wind resistance, and low cost for a long wavelength antenna.

## Answer (score 5, by Glenn W9IQ)

The type and thickness (up to a point) of the metal plays a key role in the efficiency of the antenna. Efficiency is important because it is efficiency times directivity that determines the gain of the antenna. Thus the greater the efficiency, the greater the gain.

Efficiency is the ratio of radiation resistance divided by radiation resistance plus resistive losses. The RF resistance of the metals of the antenna are one of the causes of resistive losses.

As the radiation resistance becomes lower, the resistive losses become more critical. So for a 70 ohm, 1/2 wavelength dipole, reasonable resistive losses do not change much. A vertical, 1/4 wave antenna has about 22 ohms of radiation resistance so resistive losses become more significant. For a small diameter, 40 meter loop antenna with a radiation resistance less than 1/10 ohm, the resistive losses become critical.

The resistive losses of the metal are determined by the type of metal, the surface area and thickness of the metal, and the frequencies involved. The two most common metals for antennas are copper and aluminum. While copper has lower resistive losses, aluminum is lighter and less expensive. However, since copper is more conductive, less material is required to achieve the same RF resistance as aluminum.

By way of comparison, 100 feet of common 14 gauge, copper wire has a resistive loss of ~7.1 ohms on 15 meters while the same wire in aluminum has a resistive loss of ~8.9 ohms. For a 1/2 wave dipole, this difference ratio would be negligible in terms of comparative gains.

5 feet of 1/2 inch copper has a radiation resistance of ~0.02 ohms compared to aluminum with ~0.03 ohms. This difference in a small loop antenna has a substantial influence on the gain of the antenna.

For standard antenna work, five times the skin depth is the maximum thickness of the conducting material that is required. Beyond this maximum, the material is essentially unused from an RF perspective although it may contribute to other physical properties such as strength. This is why a properly copper coated steel wire can be used to make a wire antenna. As long as the copper has sufficient thickness, the RF current will never reach the much higher loss inner core of steel. On 160 meters, a 5 times skin depth in copper is ~240 micrometers. As the frequency rises, the skin depth decreases. At 10 meters, the 5 times copper skin depth is only ~ 60 micrometers. This also highlights why hollow copper or aluminum tubing can be used to save costs and weight in many cases.

RF resistance and skin depth calculators abound on the Internet, making quick comparative analyses possible.

## Answer (score 2, by Dan KD2EE)

Yes, but unless you get really carried away it doesn't matter. The amount of metal being used, whether it be a bar, pipe, or sheet, is enough to make any concerns about resistive losses meaningless.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/133/metal-for-antenna-construction, by Timtech, Ron J. KD2EQS, Glenn W9IQ, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
