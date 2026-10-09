# One dipole for multiple bands?

*Tags: antenna, dipole · score 3*

## Question

I've just get my license, and I'm reviewing some equipend my father in law had when he passed away.

I have found a dipole antenna with 15m aprox in each side, so, 60m band antenna. It feels weird to have an antenna for that band and not for 20 o 40 or 80.

My questions is: Can I use this antenna for some other band? If it's posible. Is there some rule to use dipoles in other bands.

I don't have an anntenna analyzer to watch for dips in swr.

My (naive) hypothesis is that it could be used for bands like 10m, it being 3/2λ of that band.

EDIT: I just find out that the antanna I have is this one: https://en.wikipedia.org/wiki/G5RV_antenna

Thank you

## Accepted answer (score 2, by Mike Waters)

I wrote an article about the G5RV --and variants thereof-- at http://www.w0btu.com/g5rv_antenna.html.

A popular variant is the ZS6BKW.

- Neither the G5RV nor the ZS6BKW antenna works on 30 or 60 meters.
- The G5RV does NOT work well on 17 or 10 meters. The SWR is a little better on 80 than the ZS6BKW.
- The ZS6BKW does NOT work well on 15 meters, and needs a tuner to work well on 80.

I improved on the general design, but it requires:

1. 75 ohm feedline, which many hams are somehow reluctant to use
2. A switchable (in and out) section of ladder line.

Our modification to the G5RV and ZS6BKW antennas, while also somewhat of a compromise of frequency ranges and VSWR, lets us use all HF bands between 80 and 10 except 30 and 60* meters. (Details on the website above.)

It depends on what bands you want to work. Choose your poison. ;-)

## Answer (score 2, by Phil Frost - W8II)

If this is indeed a 60m dipole, it would be resonant somewhere around 5.35 MHz. Three times that is approximately 16 MHz, which unfortunately doesn't fall on a ham band.

However it might not be a 60m dipole either. A 60m dipole has a length of about 13.25 meters on each half.

Or it might be that where the antenna was installed, proximity to the ground, other conductive structures, or common-mode currents on the feedline significantly altered the resonant frequency from the ideal free-space model.

I would suggest you acquire an antenna tuner if you don't have one. You can probably get the dipole to tune on most bands with it, and while this won't be the most efficient arrangement, with less than 100 feet of reasonable LMR-400 type coax you'll still be able to make some contacts and get your feet wet. The most important thing is to get the antenna as high as possible, at least a quarter wavelength.

The tuner will also have an SWR meter, which will allow you to adjust the length of the antenna to be a better match and thus more efficient, or build more dipoles, or multi-band designs like a fan dipole.

## Answer (score 2, by Michael Baggett)

Put ladder line on the system and feed it all the way to a balanced tuner or 1:1 current balun (or 4:1?). Put it high as a kite broadside it to the places you want to talk most on higher bands. You'll be surprised what you can do.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10348/one-dipole-for-multiple-bands, by Terrik, Mike Waters, Phil Frost - W8II, Michael Baggett. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
