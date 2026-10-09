# Is a vertical noisier than a dipole, and if so, why?

*Tags: antenna, snr, noise · score 15*

## Question

I've had people tell me, anecdotally, that a vertical is noisier than a dipole. Is this true, and if so, why?

If it is true:

Is this additional noise, such that SNR is degraded, or is the vertical just more sensitive overall, making noise and signals equally louder?

Is the noise particular to vertical monopoles? How would a vertical dipole be affected?

## Accepted answer (score 8, by WPrecht)

I have read this too. I don't have personal data to back this up, but the reasoning I have read stated that local RFI (like household appliances) tended to be vertically polarized and hence more able to induce noise onto a vertical antenna than a horizontal one. I'll edit the answer when I find the references.

Meanwhile there are a few really excellent papers on the use of ferrite to eliminate noise from all facets of your shack, I highly recommend them:

Common Modes Chokes (W1HIS)

Cost Effective Ferrite Chokes and Baluns (GM3SEK)

**EDIT:** After some perusal of the literature, including the ARRL Antenna Handbook, I see nothing scientific to back up the anecdote. Which reminds me of a quote, from whom I forget: "the plural of anecdote is not data".

That said, I found 2 addition items of interest:

1. vertical antennas are omni-directional and therefore can pick all the noise there is to hear.
2. A reference that stated that RF noise had random angles of polarization (something that sounds more credible to me) and that RFI noise below VHF travels mostly by ground wave and interaction with the earth attenuates the horizontal component leaving only the vertical component.

I don't know if item 2 is any less of an anecdote than the question at hand, but that's what I have found so far.

## Answer (score 5, by Derek HL1ZIX)

I live in Seoul, Korea, a city of 15 million, with lots of lights and electronics on late until 11pm. My vertical dipoles I have created are easily 1 to 3 s-units noisier than horizontal dipoles. Absolutely no contest. The vertically-polarized antennas transmit DX very well, however. I actually run two antennas -- horizontal for listening, and transmit. The vertical for transmit (great on longpath), and less for listening, because they are so noisy here (often s5-s8 noise daytime) they are almost useless on receive. Switching between the two is best of both worlds.

That said, I built a 2-el wire 15m yagi, and the noise reduction is yet another 2 to 2.5 s-units under the horizontal dipole! Huge difference. Even though a 2-el yagi only has just under an s-unit gain, at same height as a dipole, the noise reduction is what really takes the cake!

## Answer (score 3, by on4aa)

Vertical antennas are noisier on HF and below for three main reasons:

1. At HF and below, vertical antennas have **more ohmic losses** than horizontal antennas (mainly ground losses). Any ohmic resistance produces white, thermal Johnson–Nyquist noise (QRN) which power is proportional to the square root of the resistance $\sqrt{R}$.
2. Vertical antennas are **often not DC-grounded to earth.** This may allow for static electricity to build up under the influence of wind and precipitation. Eventually, a high static voltage will arc over and cause noise at that moment.$^{[1]}$ This may happen at a relatively high frequency. Furthermore, arcing is a non-linear event, causing strong higher frequency harmonics.
3. **Lightning** discharges in thunderstorms are mainly vertically polarised. The emissions of lightning peak at around 5 kHz and drop off as a function of $\frac{1}{f}$.$^{[2]}$ Again, a lightning discharge is a non-linear event, causing strong harmonics. At 500 kHz, the signal of all kinds of lightning (earth-cloud, cloud-cloud,...) is still strong. Hence, most lightning detectors listen on 500 kHz because antennas are easier to build than on 5 kHz.

I see little valid argument in that human-made noise (QRM) were predominantly vertically polarised. Wiring in buildings is both vertical and horizontal.

However, overhead power lines are horizontal and do have a vertical electrical field component to earth. Low-voltage overhead power lines are also more prevalent in the US than in Europe, where mainly underground cabling is used for low-voltage domestic power. In absence of any good study data, I would call the debate still open on this point.

### References

1. http://www.repeater-builder.com/antenna/static.html
2. Le Vine D. M., "Review of Measurements of the RF Spectrum of Radiation from Lightning,” *Meteorology and Atmospheric Physics*, Vol. 37, No. 3, 1987

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/849/is-a-vertical-noisier-than-a-dipole-and-if-so-why, by Phil Frost - W8II, WPrecht, Derek HL1ZIX, on4aa. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
