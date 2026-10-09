# What is the antenna design and gain for the WA1 U/V band antenna on the ISS?

*Tags: antenna, antenna-theory, antenna-construction, rf-power, path-loss · score 3*

## Question

My son KJ7NLL is working to contact the ISS using an antenna we built together, and we were wondering the approximate minimum transmission power to reach the ISS. If I understand correctly (and correct me if I'm wrong), roughly speaking, we need to solve for tx_power from the following equation (in dB) to estimate the minimum tx_power:

- tx_power - feedline_loss + tx_antenna_gain - path_loss + rx_antenna_gain + (-rx_sensitivity) = 0

The Kenwood TM-D710GA onboard the ISS has a sensitivity of 0.16uV (which we think is -122dBm if we did the math right). Our 2m helical antenna gain is ~13dB and path loss to the ISS when directly overhead is ~127dB (of course, we need more than that when near the horizon, but not sure what that distance would be).

The ISS has a series of "WA" antennas, but we have not found the gain specs.

- What are the gain specs (and patterns?) for the ISS U/V antennas?
- Is our math right?

These are the ISS U/V Amateur Radio antennae pictured from this PDF:

## Accepted answer (score 5, by hobbs - KC2G)

I did a reverse image search for the image in your question and found an article by VK3FS which says:

The ISS actually features four different vertical antennas on the spacecraft. They are made of flexible metal tape that is coated in Kapton, a polyimide film that can withstand extreme temperatures.

Three of the four antennas are identical and measure 0.5-meter (1.5 feet) in length and each can support both transmit and receive operations on 2 meters, 70 cm, L-band, and S-band.

In other words, they're quarter-wave "vertical" whips for 2m, which also serve as 3/4 wave whips for 70cm. So you can take the gain as being equivalent to a dipole (2.1dBi max) for 2m, and a bit higher (about 3.5dBi), with pointier lobes, for 70cm.

Is our math right?

Your helical antenna is circularly polarized, and the ISS's antennas are linearly polarized, so you should subtract an additional 3dB for polarization loss. There's also going to be some feedline loss there, which you probably have no way of knowing.

ath loss to the ISS when directly overhead is ~127dB (of course, we need more than that when near the horizon, but not sure what that distance would be).

At the ISS's ~420km orbit, its radio "footprint" is a circle 4500km in diameter, and the slant range to the ISS when it's just on the horizon is approximately 2300km. So about 143dB path loss in that case (ignoring atmospheric effects).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22308/what-is-the-antenna-design-and-gain-for-the-wa1-u-v-band-antenna-on-the-iss, by KJ7LNW, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
