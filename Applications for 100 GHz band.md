# Applications for 100 GHz band?

*Tags: antenna, frequency, microwave · score 3*

## Question

I was reading this paper and I found it very interesting and the following question came up,

What are the main applications (what is used for) 100 GHz band?

I couldn't find any reference on what is used nowadays.

## Answer (score 4, by Marcus Müller)

Aside from what Zeiss Ikon wrote, these high frequencies are indeed also interesting for communications technology, for very high-rate and typically narrow-range links.

For example, in cellular mobile communications ("phones"), 5G specifies the "New Radio", which includes using several mmWave bands, the highest among them spanning 37 – 40 GHz.

The motivation is actually a bit complex, but mostly

- The higher your band, the easier it is to get a large bandwidth (you can't get 50 MHz of bandwidth around 144 MHz; it's easy to get 500 MHz in mmWave bands, simply because there's "more spectrum there")
- The higher your frequency, the shorter the wavelength, the smaller your antenna, the more antennas you can integrate in a device of a fixed size. This results in the feasibility of *massive MIMO* techniques that basically use very many antennas per device, mathematically arguing that when you combine enough of the signals of these antennas, it's almost certain you get a few good usable transmissions.
- At mmWave frequencies, antennas are so small that they can actually be integrated into IC packages – and that's very important, because for the higher microwave frequencies, building boards that carry these reliably is already very complicated and expensive.

Also, for long range links in space, especially inter-satellite links, going as high as 100 GHz does make sense for exactly Zeiss' reasons: The smaller the wavelength, the narrower the beam an antenna (array/dish) of fixed size can achieve. The math works out that this effect is exactly the same in magnitude as the increase of free space path loss (if you keep antenna system size constant and just change wavelength). If you have a dynamic constellation of satellites, you'll need digitally steerable antennas – and then, going for higher frequencies simply gives you the freedom to do exactly that.

## Answer (score 2, by Zeiss Ikon)

A frequency of 100 GHz is equivalent to a 3 mm wavelength; these "millimeter waves" have been used for decades in airborne radars. The short wavelength allows a narrow beam and excellent gain from a dish that can fit inside the nose of a fighter aircraft, allowing a forward-looking radar with mechanical sweep to be used without disturbing the aerodynamics of a potentially supersonic airplane.

More modern radars use phased arrays (eliminating the need to physically move a dish, replacing it with an array of small flat panels and beam focusing and steering done by precisely delaying the signal to various portions of the array), but the same size limitations apply; shorter wavelengths allow smaller arrays to give required gain and beam spread for the application.

## Answer (score 2, by Phil Frost - W8II)

Emissions around this wavelength are used by millimeter wave scanners, of the sort you may have encountered in airport security.

Radiation in this band is useful because it penetrates clothing quite well, but skin not so much. This means the scanner can see contraband hidden under clothing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14746/applications-for-100-ghz-band, by SNR, Marcus Müller, Zeiss Ikon, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
