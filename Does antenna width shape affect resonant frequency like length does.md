# Does antenna width/shape affect resonant frequency like length does?

*Tags: antenna, vertical-antenna, polarization · score 4*

## Question

I was wondering if I made an antenna from a Rohn 25G tower, would it have the same resonant frequency as a pole of the same height (assuming guys are insulated)? Also with the Rohn antenna, the waves would be both vertically and horizontally polarized, right?

## Answer (score 2, by Phil Frost - W8II)

Yes, width and shape are relevant. It's mathematically simpler to assume that antennas are infinitesimally thin, however, and usually this is close enough to true that it makes a reasonable simplifying assumption.

Antenna-theory.com has a good article on "thick" dipoles, summarized by this graph:

Here, "A" is the thickness of the dipole, and the length of each dipole is 1.5m. As you can see, as the dipole gets thicker, the resonant frequency goes down and the bandwidth goes up.

However, this is only but one of many variables in actual antenna construction that might change the resonant frequency. The effect of thickness is minor enough for reasonable thicknesses that it's best to initially make the antenna bit long, and then trim or otherwise tune it by actual measurement.

Because the support structure of your tower is probably very small relative to the wavelength at which you intend to operate it, it will behave almost identically to a solid bar of metal of similar outside dimensions. It will not make your signal horizontally polarized.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2372/does-antenna-width-shape-affect-resonant-frequency-like-length-does, by Synaps3, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
