# Dual Polarization Yagi Antenna for 10 m

*Tags: antenna, antenna-theory, polarization · score 3*

## Question

Imagine that someone has built a 4 element horizontal yagi antenna for 28 MHz with elements insulated from the boom, and with the driven element not split in the middle and using a gamma match to set the feed point impedance to 50 ohms.

Then, assuming a non-metallic mounting pole, if vertical elements were added which are identical in length and spacing and then joined exactly in the middle to the middles of the horizontal elements so the result is an antenna that looks like 4 plus s (+s) in a row, and keeping just the one gamma match on the horizontal driven element, is the following true ?

1.

The feed point impedance of the antenna will now be about 25 ohms.

2.

The same gamma match can be used to adjust the impedance back up to 50 ohms.

3.

The antenna will now be both horizontally and vertically polarized.

4.

For transmit, half the applied power will be radiated by each of the two driven elements.

5.

The radiation pattern will be the same in the plane of each set of elements.

Will this antenna give any advantages over a standard yagi with one set of elements ?

## Accepted answer (score 5)

From your description:

1. the vertical polarized antenna has no feed point. Since the antennas are orthogonal and on-axis there is almost no mutual effect, no coupling: the feed impedance of the horizontal antenna does not change. (2) No need for re-adjustment of the gamma match. (3) Not any effect from the vertical antenna parts. (4) No coupling, no power from that vertical part. (5) no change in polarization or radiation pattern.

When both antenna's are connected to the feeder line (and indeed: two gamma matches that need realignment) and there is no phase difference you end up with a 45 degrees polarization; in-between H and V.

When there is 90 degrees (or -90 degrees) phase difference between the H and V antenna then you have a circular polarization antenna. Effective in reduction of fading in skywave transmissions (DX).

## Answer (score 3, by Phil Frost - W8II)

From what you describe, it doesn't seem the vertical elements would be fed at all. Since they pass directly through the plane of symmetry of the horizontal elements they experience no electric field along the vertical axis, and so, aren't driven at all. It's as if they aren't there.

Furthermore, there's a simpler way for the antenna to be "both horizontally and vertically polarized": mount it such that the elements are at a 45 degree angle relative to the horizon.

Alternatively, you could build elements like you describe, and feed them both with a 90 degree phase offset to obtain circular polarization.

In either case, if the receiving antenna is either horizontally or vertically polarized, it will incur an additional 3 dB loss since half the power is in whichever polarization the receiving antenna isn't.

More generally, any possible polarization can be visualized on the Poincaré_sphere. Your radiation in any one direction can occupy only one point on this sphere at a time. If the receiving antenna's polarization is the opposite point on that sphere, polarization loss is infinite. If the polarization of receiving and transmitting antennas are 90 degrees apart, the loss is 3 dB. If they're the same, 0 dB.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18028/dual-polarization-yagi-antenna-for-10-m, by Andrew, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
