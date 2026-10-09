# How do antennas over 1/2 wavelength work?

*Tags: antenna, vhf · score 5*

## Question

I've been told countless times that an antenna should be 1/4, or 1/2 wavelength. That increasing this size to a higher multiple of 1/4 will *work*, but it will distort the radiation pattern to include several high gain lobes shooting energy off in useless directions (like straight upwards).

But I also see stuff like this for sale https://www.dxengineering.com/parts/dmn-x300a. How does this antenna work when it's around 1.5x the wavelength for 2m, and about 4.25x the wavelength for 70cm? Is it just some tech I'm not familiar with, or are these just giant useless poles?

## Answer (score 8, by hobbs - KC2G)

It's not a single long element, it's a collinear antenna, which is an array of several dipole elements stacked "end to end", connected in such a way that the current on each element has a well-defined phase relationship to each other element. This gives a single strong lobe (with higher gain than a dipole) instead of multiple "useless" lobes. The more elements you stack, the greater the gain gets, within practical limits.

In the case of most antennas that look like that Diamond, the phasing is done by inserting coils in between the elements that delay the signal on its way up, creating a phase jump between the top of one element and the bottom of the next — but there are several different ways of building collinears, including coils between elements, transmission line stubs between elements, elements separately fed with coax "phasing lines" of particular lengths, and the lazy but effective coax collinear which swaps the inner and outer conductors of each element to get a 180° phase shift.

In the simplest case a collinear has maximum gain at 0° elevation, but one interesting aspect is that you can slightly adjust the phase of the higher or lower elements to get an "up-tilt" or "down-tilt" of the pattern. So if you have a repeater on a mountain high above the area it's servicing, you can "aim the pattern down" and get more gain down on the ground. Unlike physically tilting the antenna, this is an omnidirectional effect — the peak gain is below the horizon in *every* direction.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21101/how-do-antennas-over-1-2-wavelength-work, by Dportology, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
