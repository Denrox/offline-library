# Radial length for vertical antennas?

*Tags: vertical-antenna, radial · score 5*

## Question

I plan on installing a vertical antenna soon. I expect it to cover from 80 meters to 10 (or perhaps 6). I plan on putting down 32 radials.

I am wondering if 16 66' and 16 33' radials will be just as efficient for the higher bands as would having fewer radials separately cut for each band of interest. (Eg. 8 radials each for 80, 40, 20 & 10.)

The same question differently: If I cut all the radials for 80 meters, would it negatively affect the signals of 40, 20, 10, etc.?

Does anyone know the answer to this or where I can find it?

## Answer (score 6, by Phil Frost - W8II)

Rule of thumb: if the radials are elevated, at least two resonant radials for each band.

If the radials are buried or lying on the surface, at least 16 radials, each at least a 1/4 wavelength at the lowest operating frequency, and don't worry about resonance: just get as much wire in the ground as you can. More and/or longer is better.

The objective of any radial system is to avoid current in the soil by presenting a lower impedance alternative. Current in soil is undesirable since it dissipates power in ohmic losses, reducing antenna efficiency.

In an elevated radial system, the separation between the radials and the soil surface provides isolation, meaning the current in each is largely independent. The soil and radials could be considered two parallel current paths, as such the one with the lowest impedance will take most of the current. Thus, it's important to minimize the radial impedance by ensuring some radials are resonant on any band used.

In a buried radial system, soil and radials are tightly coupled due to their proximity. Low ground losses are achieved not by providing a low impedance alternative but rather by effectively increasing soil conductivity by stuffing it full of copper. Thus, attempting to reduce radial impedance by cutting some of the radials to be shorter to be resonant on higher frequencies is futile or even counterproductive.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11940/radial-length-for-vertical-antennas, by MarqTwine, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
