# Measurement of antenna with VNA does not match its specs

*Tags: antenna, antenna-analyzer, nanovna · score 5*

## Question

I have a NanoVNA V2 Plus (50kHz - 3GHz) and decided to test my LoRa antennas:

1. an unknown antenna delivered with a LoRaWAN gateway (RAK831)
2. a 868Mhz antenna from Linx Technologies (ANT-868-OC-LG-RPS)

As the range was poor between my gateway and my devices using the first antenna (1), I thought that maybe this was an antenna for US LoRa frequencies (915MHz) so I bought the second antenna (2) that works in the 868Mhz band. The datasheet of (2) contains the following figures:

However, when I measured the antenna response with the NanoVNA I got very different results:

In my results, the VSWR is ~2.7 at 868Mhz and never go under 2.5. It also seems from the smith chart that the antenna has too much inductance. As a comparison, the response from the unknown antenna (1) looks much better:

I configured the sweep from 840Mhz to 940Mhz with 0.25Mhz steps. I calibrated the VNA with the included calibration kit. The antenna is connected directly to the NanoVNA SMA connector. Since the antennas use SMA-RP, I used an adapter and compensated for it in the calibration by adding 57ps in the port length extension configuration. This is the first time I use a VNA and mostly followed the Andreas Spiess NanoVNA V2 tutorial.

Could such a large discrepancy between the datasheet and my result come from the lack of precision of my cheap VNA? The fact that the SWR is much better for the unknown antenna (1) makes me think that the Linx antenna (2) is crap. However, it does not match the analysis from the datasheet.

I am misusing the VNA? What could explain this behavior?

**Edit**: I made some new measurement, this time with a 30cm SS405 cable between the antenna and the NanoVNA.

unknown antenna (1) without touching the coax (antenna end):  unknown antenna (1) touching the coax (antenna end):  Linx antenna (1) without touching the coax (antenna end):  Linx antenna (1) touching the coax (antenna end):

## Accepted answer (score 7, by Phil Frost - W8II)

The NanoVNA isn't exactly precision equipment, and the Linx datasheet specifies a maximum VSWR of 2.3, so it's possible the antenna is within spec (barely).

You could double-check your calibration by attaching a 50 ohm load and running a sweep: you should see a 1:1 VSWR at every frequency. Of course, if you use the same 50 ohm load you used in the calibration, this doesn't rule out a bad calibration reference as the issue.

Note that the figures in the datasheet were measured with the antenna straight up above a ground plane:

Were your measurements taken under similar conditions? If not, the results may not be the same.

The antenna is claimed to be ground-plane independent, but it may still rely on some kind of choking at the feedpoint to isolate the feedline. One thing you can do is put your hand over the feedline or significantly change the geometry of the feedline (for example, twist it into a loop) while running a sweep: if you see this significantly affecting the measurements then it's an indication there are common-mode currents on the feedline, and you are measuring the impedance of not just the antenna but also the feedline. In actual use, things may be different especially if the antenna is mounted on a metal box.

Finally, keep in mind VSWR doesn't need to be 1:1. A higher VSWR doesn't mean worse performance per se: it just means the radio will see an impedance other than 50 ohms. Often, radios specify an acceptable range for VSWR although I could not find one for the RAK831. I would hope the VSWR would at least be below the maximum specified in the antenna's datasheet, but without a calibrated reference it's hard to say if there are problems with your antenna or your measurements.

## Answer (score 6)

Most probably the discrepancy is caused by lack of ground: surface or radials. The coax and/or the VNA are no good ground and the impedance of this counterpoise adds up to the total antenna impedance.

## Answer (score 5, by Dieter Vansteenwegen)

In addition to Phil's excellent answer, these specifications are in an "ideal" free space. Having your NanoVNA in close proximity to the antenna (even having the antenna lying on a wooden desk) will influence your measurements. Try just moving it around, closer or farther from other objects, you'll see your results changing.

These measurements are not that simple to do "right" (I found out the hard way).

Additionally, I wonder... If these antennae function as a dipole, should they not (ideally) have some kind of current choke at the feed point? If so I would like to see if/how they do this.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18558/measurement-of-antenna-with-vna-does-not-match-its-specs, by DurandA, Phil Frost - W8II, Dieter Vansteenwegen. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
