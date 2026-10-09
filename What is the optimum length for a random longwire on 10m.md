# What is the optimum length for a random longwire on 10m?

*Tags: antenna, wire-antenna, end-fed-antenna · score 3*

## Question

I have all the space in the world and wish to errect a single random longwire **to use on the 10 meter band only**.

I understand that once such a wire is very long, losses associated with the wire itself (a wire of suitable gauge) mean that after a certain length, there is little more to gain.

- So at what point would it become impractical based on performance?
- Also, is there some way of calculating the optimum length where space is not a real limitation?

I used the term 'random longwire' because a longwire is defined as a length of wire at least two or more multiples of a wavelength (and I made it clear that it is for single band use), and random is in reference to the fact that it doesn't have a relationship to the wavelength within.

The height is rather varied, as it will be strung over a deep gorge. Minimum height will start at a quarter wavelength, then travel for some length averaging three quarters of a wavelength. The maximum height above ground will be between 100 and 200 metres depending on droop.

## Answer (score 8, by Phil Frost - W8II)

A *random* longwire is just that, a random length. There is no optimum length, by definition. Usually people use random longwires for multi-band operation. Since the design frequency is "a lot of them", the strategy of a random longwire is more or less to give up on making the wire suit any particular frequency, and just deal with the mismatch with a tuner.

If you are wondering what the optimal length is for "some single-wire antenna for use on one band", the answer is probably "about 0.47 wavelengths". Without defining "optimal" I'm making some assumptions, but I would very much recommend you install a half-wave dipole because:

- No tuner is required, minimizing losses
- Making the wire longer does not improve performance
- Unlike and end-fed antenna, it is quite easy to [address feedline common-mode current with a balun](Using%20a%20balun%20with%20a%20resonant%20dipole.md)

For height, "as high as possible" is generally a good answer, since this minimizes ground losses. But if you have the time and space, you can squeeze out a few more decibels by being more precise. This analysis by by Jari Perkiömäki OH6BG/OG6G suggests a multiple of 0.5 wavelengths, plus 0.1 wavelengths (0.6, 1.1, 1.6, 2.1, ...)

If you wish to further improve your antenna performance, you'll want to consider antennas which can improve your gain and/or directivity. Some of the more popular choices on HF being Yagi, 4-square, and Beverage antennas.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17540/what-is-the-optimum-length-for-a-random-longwire-on-10m, by Francis Archibald, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
