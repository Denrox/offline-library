# Can I use a “bunny ears” TV antenna for RTL-SDR?

*Tags: antenna, software-defined-radio, rtl-sdr · score 3*

## Question

I'm trying to get into SDR and was planning on buying an RTL-SDR. For an antenna, I was thinking of using an old set of bunny ears I have lying around. However, I first want to make sure that they'll work with the dongle.

I'm only planning on receiving in the 10's to 100's of MHz which is in the listed range of the RTL. In addition, it looks like TV stations broadcast in similar ranges so the antenna should be built for receiving them.

Is my logic correct or is there something I have overlooked that would make the antenna not work with the dongle?

## Accepted answer (score 3, by Kevin Reid AG6YO)

First of all, the properties of an antenna are far less important for *receiving* than *transmitting*. To receive anything at all, just about any piece of metal will do.

That said, the lower the frequency (longer wavelength) you want to receive, the larger the antenna should be for it to work well. Once you get into the “HF” range (below 30 MHz, formally, but that's an arbitrary division not a physics-based one), you want the sort of antenna that, practically implemented, is often less like a stiff metal rod sticking up and more like a wire strung out between supports. This is both because the wavelengths are larger, and because the signals people are often interested in (e.g. shortwave radio stations) are weaker.

To be precise, the length of an antenna “element” (the distance from the receiver or coax to the end of the rod or wire), should be one-quarter of the wavelength, or

$$\frac{1}{4}\times\frac{c}{f}$$

where $f$ is the frequency and $c$ is the speed of light (the idealized conversion factor between wavelength and frequency for radio waves). For making these calculations it can be handy to use Wolfram Alpha (example) or any other calculator that understands physical units and knows what $c$ is. There are also various web pages with dedicated calculators for specific antenna designs.

In the example I linked above, we see that 100 MHz corresponds to 0.75 meters or 2'6"; so assuming your “rabbit ears” are telescoping, then for good reception at 100 MHz, you should extend each of the two elements to that length. **This is a simplification,** because all sorts of secondary effects and details of the antenna construction; use this number as a rough guide, and then adjust the antenna to see what gets you good reception.

If for some frequency you find your antenna can't be that size, that's a sign that you might want a different antenna. But it's still worth trying, because as I said to start with, receiving antennas can work well enough despite being “totally wrong” for the application.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15770/can-i-use-a-bunny-ears-tv-antenna-for-rtl-sdr, by genghiskhan, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
