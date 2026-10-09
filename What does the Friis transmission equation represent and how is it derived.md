# What does the Friis transmission equation represent and how is it derived?

*Tags: math, path-loss · score 7*

## Question

I've read that the Friis transmission equation can be [applied to calculate path loss in ideal space](What%20is%20the%20average%20fade%20margin%20required%20for%20proper%20operation%20at%202.4%20GHz.md). However, I'd like to better understand the factors that define it and what it represents, and *why* it is the equation it is.

## Accepted answer (score 7, by Phil Frost - W8II)

Let's imagine that there are two antennas, entirely in free space. There is no Earth or any other object near enough to affect propagation. Let's also assume that these antennas are far enough apart that the antennas interact only by their far fields.

To start, let's assume that both antennas are isotropic, meaning that they radiate equally in each direction. If we supply a pulse of energy to such an antenna, this energy will spread out as a sphere, to infinity, at the speed of light. It also means that if we supply a constant power to such an antenna, then for any sized sphere centered on that antenna, the power passing through that sphere is equal to the power being fed to the antenna.

If we are interested in the power received by an antenna at distance $r$ from the transmitting antenna, then all the transmitted power will be spread across a sphere of radius $r$ by the time it reaches the receiving antenna. The area of that sphere is $ 4 \pi r^2 $. The transmit power $P_t$ divided by that area gives us:

$$ P_t \over 4 \pi r^2 \tag{1} $$

This number has units $\mathrm W/\mathrm m^2$ and is a *power flux density* or irradiance. A watt is one joule per second, so a power flux density of $1\mathrm W/\mathrm m^2$ means that every second, one joule of energy passes through an area of one square meter.

Isotropic antennas can't exist, and even a dipole has some gain. Assuming the receiving antenna is in the direction of maximum gain, this multiplies the power flux density, so if the transmitting antenna's gain is $G_t$, the equation becomes

$$ {P_t \over 4 \pi r^2} G_t \tag{2} $$

This gives us the power flux density at the receiving antenna, but how much of this power is received? The antenna aperture answers that question. Let's call the aperture of the receiving antenna $A_r$. The power received ($P_r$) is then

$$ P_r = {P_t \over 4 \pi r^2} G_t A_r \tag{3} $$

Effective aperture $A$ and gain $G$ are related by

$$ A = {\lambda^2 \over 4 \pi} G \tag{4} $$

Substituting this into equation 3 gives us

$$ P_r = {P_t \over 4 \pi r^2} G_t {\lambda^2 \over 4 \pi} G_r $$

Simplified:

$$ P_r = P_t G_t G_r \left({\lambda \over 4 \pi r}\right)^2 $$

Or rewritten to use decibels:

$$ P_{r(\mathrm{dB})} = P_{t(\mathrm{dB})} + G_{t(\mathrm{dB})} + G_{r(\mathrm{dB})} + 20 \log_{10} \left({\lambda \over 4 \pi r}\right) $$

Since wavelength is a function of frequency and the speed of light ($\lambda = c/f$), the equation can also be written:

$$ P_{r(\mathrm{dB})} = P_{t(\mathrm{dB})} + G_{t(\mathrm{dB})} + G_{r(\mathrm{dB})} + 20 \log_{10} \left({c \over 4 \pi r f}\right) $$

Finally, we can factor out the constant ${c \over 4 \pi}$ and write that as:

$$ P_{r(\mathrm{dB})} = P_{t(\mathrm{dB})} + G_{t(\mathrm{dB})} + G_{r(\mathrm{dB})} + 147.6 - 20 \log_{10} (rf) $$

Where:

- $r$ is the distance between antennas in meters, and
- $f$ is the frequency in Hz.

This formula is essential to the calculation of [link budgets](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md), and gives the best case path loss. It's then easier to consider other sources of loss as separate factors.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1539/what-does-the-friis-transmission-equation-represent-and-how-is-it-derived, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
