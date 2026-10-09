# Can I build a radio telescope out of a parabolic TV satellite dish?

*Tags: antenna, antenna-construction, satellites · score 22*

## Question

I have the possibility to buy a very inexpensive 2.4m parabolic satellite dish and I would like to build a radio telescope from it. Originally this dish was designed to be a satellite TV antenna.

Can I replace the TV LNB with radio receiver tuned for 1420MHz (hydrogen lines) and use the dish as radio telescope? Does the focal length of such an antenna depend on the frequency for which it was designed?

## Accepted answer (score 16, by Glenn W9IQ)

The primary factor to consider is the directivity of the parabolic antenna. It is given as:

$$d=\frac{(\pi D)^2}{\lambda^2} \tag 1$$

where D is the diameter of the dish and $\lambda$ is the wavelength of operation, both in the same units.

To convert frequency to wavelength in meters, we use:

$$\lambda=\frac{300}{f} \tag 2$$

where f is the frequency in megahertz.

Since your frequency of interest is 1420 MHz, we apply formula 2 to convert this to a wavelength of 0.211 meters. With a dish diameter of 2.5 meters, formula 1 give us a directivity of:

$$d=\frac{(\pi D)^2}{\lambda^2}=\frac{(\pi 2.5)^2}{0.211^2}=1386$$

We now need to convert this directivity to linear gain. Here the standard antenna formula applies:

$$G=d*e \tag 3$$

where d is the directivity from formula 1 and e is unitless efficiency with a value of 1 indicating 100% efficiency.

Most parabolic antennas have efficiencies in the 60% to 70% range. For a conservative estimate, if we assume a 50% efficiency, the linear gain of your parabolic antenna is 693. We can convert this to dBi gain using:

$$G_{dBi}=10\log_{10}(G) \tag 4$$

which nets ~28 dBi in this case.

With diligence, you may be able to obtain a 70% efficiency which will raise the gain to ~30 dBi.

The beamwidth of the parabolic antenna is given as:

$$\theta\approx\frac{70\lambda}{D} \tag 5$$

The 3 dB beamwidth of your parabolic antenna will therefore be ~6°.

The focal point of a parabolic antenna is given as:

$$f=\frac{D^2}{16c} \tag 6$$

where c is the depth of the parabolic reflector.

You can see from this formula, that it is not a function of wavelength. So the focal point of the dish remains largely the same regardless of frequency.

You now must consider the sensitivity and noise of your receive system and the expected field strength of a 1420 MHz hydrogen marker to determine if this is sufficient gain for your radio telescope operation. There is hope for success as several university students have used a similar configuration for their projects.

## Answer (score 5, by Hobbes)

It's been done before. The University of Groningen astronomy department runs (ran?) a couple of 2.5 m dishes for radio astronomy exercises. IIRC they mainly observe our Sun (strongest radio source).  
So I'd say yes, that dish could be a good starting point.

## Answer (score 2, by Phil Frost - W8II)

Yes, although not a very big one.

The wavelength at 1420 MHz is 21.11 cm. Thus the aperture of this telescope is roughly:

$$ { 240\:\mathrm{cm} \over 21.11\:\mathrm{cm} } = 11.4\ \text{wavelengths} $$

(Probably somewhat less, considering inefficiencies.)

For comparison, the wavelength of green light is around 500 nm. So in terms of the ability to resolve features, this 2.4 meter radio telescope is roughly equivalent to an optical telescope with an objective of a miniscule:

$$ 0.00005\:\mathrm{cm} \cdot 11.4 = 0.00057 \:\mathrm{cm} $$

Alternately, the -3 dB beamwidth of a 2.4 meter dish at 1420 MHz is approximately 6 degrees. Meaning, 3 degrees any direction away from the axis of maximum gain, the sensitivity of the antenna has diminished by half. With such a wide beam, you will be limited to observing only very large astronomical features.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11668/can-i-build-a-radio-telescope-out-of-a-parabolic-tv-satellite-dish, by SP5RFD, Glenn W9IQ, Hobbes, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
