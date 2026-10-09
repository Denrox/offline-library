# What is the radiation pattern and feedpoint resistance of a raised feed point vertical?

*Tags: vertical-antenna · score 4*

## Question

If you put a vertical 1/4 wavelength antenna on a pole of about 15 feet and tie the base of the pole to a massive grid of radials and the ground itself how does it affect the radiation pattern and the feed point resistance? It is like an infinitely wide ground plane but the current in the lower pipe element supplements the field of the upper.

## Answer (score 2, by hobbs - KC2G)

The pattern of a 1/4 wave vertical monopole above perfect ground is the same as that of a 1/2 wave vertical dipole, so the pattern of a 1/4 wave+15' vertical monopole above perfect ground is the same as that of a 1/2 wave+30' vertical dipole — for 20 meters this will be about 0.93 wavelengths long, which is theoretically beneficial, since the gain of the main lobe (the one towards the horizon, for a vertical dipole) increases with length between 0.5 and 1.25 wavelengths. It's not *much* of an increase, though, and see below for a caveat. For bands shorter than 15m, the 15' of extra length makes the equivalent dipole more than 1.25 lambda, and so you start to get additional high-angle lobes that are probably unwanted.

The feedpoint location doesn't matter to the pattern, but it does matter to the impedance. Modeling with NEC2 above perfect ground, the impedance comes out to a rather unfriendly 1100-j2200 ohms, varying a bit across the band. Replacing perfect ground with NEC fast ground and adding a field of 8 1/4 wave radials does little to change that. The best result, matching-wise, comes from using real ground and having *no radial field*, in which case we have a vertical OCFD touching (or almost touching) the ground. If we allow the antenna to connect to ground (using ground rods, say) we get an impedance of about 360±j20 ohms, which could be matched to 50 ohms fairly easily (and in fact has a pretty nice SWR wrt 450 ohm ladder line), but has a calculated efficiency of only about 10%. If we elevate the whole thing by 10cm and disconnect it from the ground, we get an impedance of about 50-j475 ohms and the efficiency increases to 25%. But that still falls short of the performance of a quarter-wave vert fed at the ground.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21216/what-is-the-radiation-pattern-and-feedpoint-resistance-of-a-raised-feed-point-, by david, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
