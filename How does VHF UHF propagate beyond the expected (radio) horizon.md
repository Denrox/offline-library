# How does VHF/UHF propagate beyond the expected (radio) horizon?

*Tags: propagation, vhf, uhf · score 11*

## Question

I am not asking about the fairly well-known effect of the earth "appearing less curved to radio waves" that are otherwise still essentially line-of-sight, but a deeper arcanum:

In the ARRL Antenna Book, 17th edition (1994) there is a discussion of "Reliable VHF coverage" in starting on page 23-7 in the Radio Wave Propagation chapter. The claim is made,

Because of age-old ideas, misconceptions about the coverage obtainable in our VHF bands persist. This reflects the thoughts that VHF waves travel only in straight lines, […] However, let us survey the picture in the light of modern wave-propagation knowledge and see what the bands above 50 MHz are good fro on a day-to-day basis, ignoring the anomalies [presumably referring to the tropospheric ducting of previous section] that may result in extensions of normal coverage.

It goes on, after mentioning an article by D.W. Bray, K2LMG in the November 1961 QST magazine, to present two graphs that plot "tropospheric path loss" against distance. The curves therein rise steeply from 120 dB of loss at a distance of 0 miles [?!] to around 180 dB near 50 miles, then level off slightly so that at 500 miles there is a path loss around 240 dB. (That's reading the 50% reliability chart roughly, there's actually 4 lines plotted for 144/50, 220, 432, and 1296 MHz, as well as a second separate chart showing 99% reliability; the 99% reliability chart is very approximately 10–20 dB worse than the 50% one at any given point.)

**UPDATE**: thanks to W0BTU Mike, here's the actual charts scanned from an earlier edition:

What "modern wave-propagation knowledge" is this referring to? What mechanism(s) would allow VHF signals to be 99% **reliably** received 500 miles away, albeit with more than 250 dB of path loss, or 50%-of-the-time reliability with a little less loss? (These path-loss charts do NOT assume any antenna-height gain.)

## Accepted answer (score 4, by natevw - AF7TB)

Turns out that, after turning to discussion of HF propagation for a number of intervening pages, this Antenna Book ends up getting back around to its own answer for this question!

From the "Scatter Modes" section on page 23-30 of the same 17th edition:

The wave energy of VHF stations is not gone after it reaches the radio horizon, described early in this chapter. It is scattered, but it can be heard to some degree for hundreds of miles. Everything on Earth, and in the regions of space up to at least 100 miles, is a potential scattering agent.

*Tropospheric scatter* is always with us […] **this is what produces that nearly flat portion of the curves given in an earlier section** on reliable VHF coverage. … As long ago as the early 1950s, VHF enthusiasts found that VHF contests could be won with high power, big antennas and a good ear for signals deep in the noise. … *Ionospheric scatter* works much the same as the tropo version, [… and] can fill in the skip zone with marginally readable signals scattered from ionized trails of meteors, small areas of random ionization, cosmic dust, satellites and whatever may come into the antenna patterns at 50 to 150 miles or so above the Earth. […]

[bold added for emphasis]

It goes on similarly to discuss "backscatter" and "transequatorial scatter" before going on to a different section on "auroral propagation" (which can also affect VHF but is probably *not* related to the reliable propagation graphs).

So in short, "scatter" (in many forms) is claimed as the mechanism that allows VHF signals to be heard hundreds of miles beyond the primary "radio horizon".

I also believe the ARRL editors consider the experimental discoveries of the various scatter modes to be the "modern wave-propagation knowledge" referred to earlier — in this "Scatter Modes" section there are a couple historical references around the same dates as the QST article, including the "early 1950s" one quoted above as well as Transequitorial scatter as "an amateur 50-MHz discovery in the years 1946–1947".

## Answer (score 2, by Richard Fry)

Terrestrial, point-point propagation paths can exist due to diffraction of the radiated e-m fields over terrain peaks and man-made structures, with each diffraction adding loss at the receive antenna to the normal inverse-distance field loss for an LOS path of that total length.

The graphic below illustrates this for an FM broadcast station, where the line-of-sight path is severely obstructed, but the signal can be received well beyond those obstructions.

The real propagation path would consist of several straight-line segments over terrain peaks, joined together to connect the transmit and receive antennas.

In this example, the additional loss due to diffractions compared to an LOS path of that total length is shown to be 76.59 dB.

The received field will vary over time depending on atmospheric K-factor and other conditions.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7265/how-does-vhf-uhf-propagate-beyond-the-expected-radio-horizon, by natevw - AF7TB, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
