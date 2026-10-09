# Partially Collapse Telescoping Antenna to Change Effective Length

*Tags: antenna, dipole · score 4*

## Question

I recently purchased a cheap RTL-SDR kit to experiment with SDRs and different frequency bands. This kit came with 23cm and 100cm telescoping antennas. I now wish to use the 100cm antenna to pick up NOAA APT signals at 137 MHz. Many sites with instructions for a V-Dipole antenna for this purpose indicate that a 53cm half-wave antenna works well.

Is there something special about telescoping antennas such that they only work when fully extended, or can I partially retract the 100cm antennas to 53cm to get the proper length?

## Answer (score 2, by gbarry)

Telescoping antennas work at any length you set them. They are always connected internally.

Speaking from experience, being able to move the antenna around to find the best signal makes a much bigger difference than fine tuning its length.

## Answer (score 2, by Kevin Reid AG6YO)

Yes, you can partially collapse a telescoping antenna. There are no special considerations versus other types of antenna elements / monopoles.

There is a slight effect from the thickness of the antenna — thicker conductors, such as the telescoping elements closer to the base, exhibit more bandwidth (less selectivity). This is usually not very significant at all for receiving purposes, but if you're trying to pick out a single signal then you can theoretically get a **small** reduction of out-of-band interference by extending the thinner sections of the antenna rather than the thicker ones, provided that you also get the length exactly right (adjusting to maximize the power of the received signal).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12470/partially-collapse-telescoping-antenna-to-change-effective-length, by Alex Wulff, gbarry, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
