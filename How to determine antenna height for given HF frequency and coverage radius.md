# How to determine antenna height for given HF frequency and coverage radius?

*Tags: antenna, hf, propagation, range, nvis · score 6*

## Question

I'm planning on setting up a low-HF antenna for near to mid-range contacts.

In my particular case, *ideally* I would like to be able to cover a radius of approximately 1000-1200 km with good reliability, operating on 3.5 MHz and possibly supplanted by 7 MHz. (Using a combination of the two bands to achieve full coverage is perfectly acceptable.) At a minimum, I want to be able to cover something like a 600-700 km radius. I'm at approximately 58°N, locator JO68; this of course means that I need to take into consideration large seasonal variations in ionosphere illumination.

Now, such coverage seems to me to be a nearly ideal fit for NVIS.


Given an antenna height above ground and operating frequency, how do I determine an approximate resultant coverage radius in the case of NVIS?


Or alternatively, given an operating frequency and desired coverage radius, how do I determine how high above ground the antenna needs to be?

I'm preferably looking for a (mathematical) answer that does not involve using antenna modeling software.

For simplicity's sake, let's just assume a straight half-wave dipole at an even height above perfect ground.

## Accepted answer (score 6, by Adam Davis)

Near Vertical Incidence Skywave (NVIS) is already pretty well defined in both radius and antenna height by definition. The antenna achieves best performance no more than 1/4 wavelength above the ground, and typically reaches receivers 50km-650km (30-400 miles) away. It isn't going to help you out much with receivers 1000-2000km away.

Unfortunately there isn't a single, simple, good calculation for antenna height vs transmission distance, which is why so many antenna modeling packages exist.

You'll get line of sight at close distances, which uses one equation.

You can get groundwave propagation distances further out with another equation.

Skywave and NVIS propagation distances will get you even further which each have their own calculations.

An antenna modeling package takes into account all these various radiation modes, and can account for many other factors to bring you to a reasonable decision. You might not want to use one, but they were actually created to make this problem simpler to solve. Doing it by hand is more difficult, but can be rewarding if you want to learn more about propagation.

The simplest answer is that the "ideal" height for an antenna at these frequencies is 1/2 wavelength - but even there "ideal" depends on whether you want optimum ground reflection. If you can't get your 3.5MHz antenna 140 feet in the air, though, then "as high as you can" is the ideal height. Technically this is actually shifted up a little bit - the ideal height is 0.6 wavelengths above the ground, and every additional half wavelength thereafter (1.1wl, 1.6wl, etc).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/746/how-to-determine-antenna-height-for-given-hf-frequency-and-coverage-radius, by user, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
