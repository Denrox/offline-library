# Can antennas have reverse harmonics

*Tags: antenna · score 5*

## Question

I know antennas can have 1/4 wavelength, 1/8th etc. but if you are operating from UHF bands, can the antenna be lets say twice as long?

## Answer (score 7, by Phil Frost - W8II)

can the antenna be lets say twice as long?

Yes. 1/2 wave dipoles are the common choice, because it's the minimum length for a resonant dipole without using tricks like a loading coil or capacitive hat to make the antenna appear longer electrically than it is physically. Verticals are 1/4 wave for the same reason, but the image antenna formed by the reflection of the vertical through the ground makes it appear as a 1/2 wave dipole.

With a 1/2 wave dipole, a standing wave forms on the wire, with voltage and current distributed like so:

If you increase that to 3/2 wave, you still get a standing wave, like this:

These images from an article on radio-electronics.com.

Notice that the feedpoint is still at a node where voltage is at 0, and current is at a maximum. This works for any odd harmonic, 1/2, 3/2, 5/2, ...

Off-center fed dipoles exploit this: by getting the feedpoint at just the right spot, the feedpoint can end up on a similar impedance point on the antenna for a number of bands, even when those bands aren't odd harmonics of each other. For example, 40 meters (7 MHz) and 20 meters (14 MHz).

## Answer (score 7, by Dan KD2EE)

The answer is yes (sort of), but it isn't because of "reverse harmonics". That doesn't actually mean anything.

Quarter-wave antennas work for the same reasons as dipoles do - due to the physics of the situation, the feed point impedance works out to be just right - about 50 ohms - and most of the power is radiated instead of reflected. Other lengths may require matching or may not work at all.

For example, 5/8 wave is common for vehicle antennas because you get slightly better gain at a slightly different angle. But any 5/8 wave antenna will have a little "bulge" at the bottom that contains a coil (or some other type of matching circuit) which adjusts the feed point impedance to that magic 50 ohms to prevent the signal from being reflected right back into the radio.

This is what we measure with SWR, by the way - if the impedances all match out, the standing wave ratio will be 1:1. If there's an impedance mismatch, the SWR will vary and you lose power.

While the exact "good" and "bad" points will vary due to other conditions, typically, any radiator that is close to an odd number of quarter wavelengths will be good, and close to an even number will be bad. Anything in between may not be good, but can probably be impedance matched (like 5/8ths), whereas anything too close to 1/2 or a multiple of 1/2 will have a feedpoint impedance that is so extreme that it cannot be practically matched.

In HF, we have this sort of question come up in relation to long wire (or random-wire) antennas. Here, we choose an antenna that is an odd multiple of a quarter wavelength on many different bands to get a simple multi-band setup - one good length is around 85 feet, which is close enough to tune on most of the HF bands. In UHF we probably only care about one band at a time, but the idea is the same. A plain 1/2, full, or double wavelength vertical won't tune up very well (unless it's secretly a dipole), but 3/4, 5/4, and so on will, and 5/8, 7/8, and so on can be tuned.

So how do we choose? Well we usually just use a quarter wave, it's smaller and cheaper and never a bad choice. Other antennas come into play when we need either a different radiation pattern or some such. For example, yes a 5/8 wave has "better" gain, but it also has a higher radiation angle, which may or may not work out depending on what you're trying to do. To determine this sort of thing, we use computer modeling programs like EZNEC to calculate an antenna's radiation pattern and can then use other software like Radio Mobile to generate coverage maps based on that pattern.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/678/can-antennas-have-reverse-harmonics, by Skyler 440, Phil Frost - W8II, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
