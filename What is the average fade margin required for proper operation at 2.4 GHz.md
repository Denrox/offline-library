# What is the average fade margin required for proper operation at 2.4 GHz?

*Tags: antenna, amplifier, wifi · score 4*

## Question

I have two radios. Sensitivity is -84 dBm and transmitting EIRP is +30 dBm. How much distance should I expect?

I want it to be somewhere near about 2-3 km. Is it possible?

## Accepted answer (score 4, by Phil Frost - W8II)

Your question can be answered by the Friis transmission equation. One way to write it is:

$$ P_r=P_t+20\log _{10}\left({\frac {\lambda }{4\pi R}}\right) $$

Where:

- $P_r$ is the received power (in dBm)
- $P_t$ is the transmitted power
- $\lambda$ is the wavelength
- $R$ is the distance between the antennas, in the same units as wavelength

Wavelength at 2.4GHz is about 0.125m. With your numbers of 30dBm, and a maximum distance of 3km, the equation becomes:

$$ \begin{align} P_r&=30 \:\mathrm {dBm}+20\log _{10}\left({\frac {0.125\:\mathrm m}{4\pi \cdot 3000 \:\mathrm m}}\right) \\ &= 30 \:\mathrm{dBm}-109.6 \:\mathrm{dBm} \\ &= -79.59 \:\mathrm{dBm} \end{align} $$

This is about 4dB above your specified minimum of -84dBm, so it's theoretically possible, but only barely. The Friis equation calculates received power for ideal propagation in free space between isotropic antennas.

Your receive antenna probably has some gain which gives you some additional margin. A resonant dipole has theoretically a 1.76 dBi gain, which adds to the number calculated above. Of course if you have a more directional antenna you get even better improvements.

However, you also aren't propagating through free space. You can approach this with a very good path: antennas on towers, clear line of sight, and so on. You must also consider the Frensel zone around the path also. If all of these conditions are very good, your losses compared to free space will be small or negligible. If not, you will need additional antenna gain or transmit power to make your link work.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1486/what-is-the-average-fade-margin-required-for-proper-operation-at-2-4-ghz, by user40713, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
