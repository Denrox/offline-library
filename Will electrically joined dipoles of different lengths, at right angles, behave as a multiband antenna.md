# Will electrically joined dipoles of different lengths, at right angles, behave as a multiband antenna?

*Tags: antenna-theory, hf, diy · score 11*

## Question

I haven't seen this done, (which, after more than a century of amateur and professional radio development, is probably a bad sign), but I had an idea the other day for simplifying the setup and feed to cover more than one band without the compexity of traps or multiple feeds and RF switching.

If I were to build a pair of dipoles at right angles, on the same feed line, one sized for, say, 40m, the other for, in this case, 20m, would they act as one very poorly tuned antenna, or would they act like a wave trapped dipole (except with two different radiation patterns)? I can think of arguments for either case, and I'm pretty fuzzy on antenna theory.

## Accepted answer (score 9, by Brian K1LI)

The results depend on the two bands you choose. Frequency ratios of 2:1 are a good choice because the longer dipole, which is a full wavelength at the higher frequency band, will show high impedance on that band, while the shorter dipole, which is only a quarter wavelength at the lower frequency band, will show a high (capacitive) impedance on that band.

Let's use your example of crossed dipoles that are a half wavelength on 40m and 20m, respectively. In EZNEC, this is accomplished by connecting identical very short transmission lines from the center of each dipole to a virtual segment that hosts the single driving current source.

As shown below, the current at the center of the 20m dipole is about 8% of the current at the center of the 40m dipole when operated on 40m:

The situation is reversed when operating on 20m, where the current at the center of the 40m dipole is about 1.4% of the current at the center of the 20m dipole:

One might suspect that interactions between the the currents in the two antennas could adversely affect the SWR on each band, but these plots show that this is not the case:

These SWR curves are virtually identical to the curves obtained when each dipole is swept after the other dipole is completely removed from the model.

One reason this is not frequently done could be that more supports are needed and that the patterns of the two dipoles are orthogonal to each other, which might not serve the desired communicating directions.

Rotating one dipole to be parallel to the other requires the 20m dipole to be lengthened slightly to achieve resonance, but dramatically reduces the 20m SWR bandwidth. This design begins to look like a so-called open-sleeve dipole, in which the longer element is fed directly and excites the shorter dipole through close coupling, restoring much of the useful SWR bandwidth while preserving the directivity on both bands:

Beginning on page 21 of Choosing Your First HF Antenna, the ARRL's Joel Hallas, W1ZR, describes Unfolded and Folded Skeleton Sleeve Dipoles for many band pairs. I have used these antennas at home, for DXpeditions and Field Days and can attest to their simple construction and reliable performance. A matching unit may be required to obtain the SWR required by your transmitter across an entire amateur band. A folded skeleton-sleeve dipole for the 40m and 20m bands would look like this:

## Answer (score 7, by Phil Frost - W8II)

What you describe is not far off from a common *fan dipole*. This is a multiband antenna consisting of several dipoles in parallel, each cut to a different length. Only instead of orienting each dipole at right angles, they are simply spread apart with spacers.

The idea is that the resonant dipole for the band will have a low impedance, while the non-resonant dipoles will have a higher impedance. By the basics of parallel impedances, most of the current ends up on the resonant dipole, and the addition of the higher-impedance non-resonant dipoles don't have a significant effect on the overall feedpoint impedance.

The spacers reduce the interaction between the dipoles which makes the arrangement much easier to tune. Rotating the dipoles to be 90 degrees apart would reduce interaction even more, at the expense of doubling the number of supports required.

## Answer (score 4, by Cecil - W5DXP)

The feedpoint current will take the path of least resistance (or least impedance) so it will always flow mainly into the center-fed resonant 1/2WL dipole rather than into any other higher impedance path.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14818/will-electrically-joined-dipoles-of-different-lengths-at-right-angles-behave-a, by Zeiss Ikon, Brian K1LI, Phil Frost - W8II, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
