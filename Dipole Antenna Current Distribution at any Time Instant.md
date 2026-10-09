# Dipole Antenna Current Distribution at any Time Instant

*Tags: antenna-theory, antenna-construction, dipole · score 7*

## Question

Above is a connection of half-wave dipole antenna. The book states that the current profile is same at any given time instant on both the radiators, each of quarter wavelength length.

Now my confusion is clearly the coaxial cable is connected to both radiators. Say I am sending the signal through centre wire and the braid of the coaxial cable is always at ground. Now at any given time instant, only left end of the cable is going to have non zero potential, while the right end is always at $0V$. Then how come both radiators would have same current profile at any given time when the excitation is different for left and right radiators!

To be very specific, say at any given time instant the voltage at the left end is 2.3V, so standing wave is generated in the left radiator, but on the right radiator the voltage is zero (braid is at ground), so how any excitation would happen on the right radiator.

Support will be greatly appreciated. I am a total newbie in antenna systems.

## Accepted answer (score 10, by Phil Frost - W8II)

You have aptly discovered why a [balun is necessary when feeding a dipole with coax](Using%20a%20balun%20with%20a%20resonant%20dipole.md). You are right to think the book is wrong, because it is. With a coax feed and no balun, the current distributions on the dipole are not equal because some share of the current that should be on the right half (connected to the shield) of the dipole is instead flowing on the feedline common mode.

The book would be accurate had it used a balanced feedline instead, or included a balun.

The coax shield is in fact not at 0V relative to ground, because without a balun there will be common-mode currents on it. The shield being at 0V is not a law but rather an assumption. That assumption is based on an antenna design with a properly designed feed and an absence of common-mode currents, which this design has not.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7108/dipole-antenna-current-distribution-at-any-time-instant, by user3001408, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
