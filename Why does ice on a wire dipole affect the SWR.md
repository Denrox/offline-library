# Why does ice on a wire dipole affect the SWR?

*Tags: antenna, impedance, dipole · score 13*

## Question

We just had snow and ice overnight and my wire dipole was coated in ice. Why does the ice covering negatively affect the SWR of the antenna?

## Accepted answer (score 3, by Phil Frost - W8II)

A heavy coating of ice or snow is likely to short the feedpoint of the antenna. Compare:

Even if the wires and feedpoint are protected by insulation and the ice isn't directly touching, a thick coating of ice will make a tube around the wires, and the resulting capacitive coupling is a low impedance at RF. (ANT3)

Snow or ice isn't a great conductor, but it's a much better conductor than the air or PTFE insulator that was between the halves of the antenna. Clearly the antenna impedance, and thus the SWR, will be affected.

The change in temperature, dielectric constant, and other things mentioned in other answers do affect the antenna impedance, but not to a very significant degree. I'd wager that 80% of the times you sit down in the morning after a storm to find the SWR is all messed up, it's because there's water in the feedpoint. The other 20% of the time, it's because the antenna is sagging into a tree or the ground or broken from the additional weight.

## Answer (score 2, by Communicationantennas.com)

Ice and water has very big dielectric permittivity. If the antenna is in a dielectric, so the resonance frequency changes with the square root of it. So for ice the dielectric permittivity may change due to its density. Water has dielectic permittivity of 80. So the antenna resonance frequency changes with the ratio 1/squareroot (80). It doesn't guarantee that the antenna works well at the new frequency, because 80 is very high permittivity wich can create high reflection, but it works better at this frequency. That's why the antenna doesn't work when it has ice on it. It is not about the change of antenna length or anything else because of temperature. If you want to solve this problem you must have heat resistance wires on it in order not to have ice on it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1702/why-does-ice-on-a-wire-dipole-affect-the-swr, by Ron J. KD2EQS, Phil Frost - W8II, Communicationantennas.com. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
