# What is the aperture efficiency of an antenna?

*Tags: antenna, antenna-theory, antenna-reflector · score 5*

## Question

For reflector antennas, I see a number called aperture efficiency. What does it mean?

## Answer (score 4, by K7PEH)

The aperture efficiency of a horn or reflector antenna is the ratio of the effective aperture to the physical aperture. The formula usually looks like: $$ \epsilon_{ap} = \frac{A_e}{A_p} $$ The aperture efficiency is a dimensionless number usually reported as a percentage and $A_e$ is the effective aperture and $A_p$ is the physical aperture.

For horn and reflector antennas, the aperture efficiency is typically in the range of 50 to 80 percent.

I assume the OP understands antenna aperture. The effective aperture is usually less than the physical aperture because the $E$-field is not uniform across the physical aperture. The effective aperture and physical aperture are specific to each kind (with size dimensions) of horn and reflector antennas.

## Answer (score 2, by Phil Frost - W8II)

The aperture efficiency tells you what percentage of the power incident upon the antenna is available at the feedpoint.

The concept of "power incident upon the antenna" is a bit weird. So let's take a step back, and consider something more visible, like a sheet of paper. At any time there's some amount of light hitting this sheet of paper. We can increase the light hitting the paper by making the paper bigger, or by shining brighter lights at it. More specifically, all the light hitting the sheet of paper is called luminous intensity measured in candelas. The brightness of the light at the paper is called luminance, which is luminous intensity per unit area, measured in candelas per square meter.

The candela is a photometric unit: it takes into account only *visible* (by humans) electromagnetic radiation. The analogous unit which takes into account *all* electromagnetic radiation is familiar: it's the watt.

So now consider a receiving reflector or horn antenna. Depending on the transmitter's power, gain, and distance, there will be some irradiance at the receiving antenna, measured in watts per square meter. This irradiance, multiplied by the area of the reflector (assuming it's pointed in the right direction) gives you a power in watts, the theoretical power intercepted by the antenna. The ratio of the actual power at the feedpoint to this theoretical power is the aperture efficiency.

There is another number, the "effective aperture", which is the area we come up with if we run this calculation in reverse: start with the actual power at the feedpoint, and then calculate the area required to intercept that much power from the transmitter. The effective aperture is another way of expressing gain:

$$ A_\text{eff} = {G \lambda^2 \over 4\pi} \tag{1} $$

Where:

- $A_\text{eff}$ is the effective aperture,
- $G$ is the gain (as a unitless ratio, not in dB), and
- $\lambda$ is the wavelength.

If $A_\text{phys}$ is the physical aperture, for example the area of the reflector, then aperture efficiency is simply the ratio:

$$ e_a = {A_\text{eff} \over A_\text{phys}} \tag{2} $$

Which we can combine with equation 1 to be expressed in terms of gain rather than effective aperture:

$$ e_a = {G \lambda^2 \over 4 \pi A_\text{phys}} \tag{3} $$

Or if your gain is expressed in decibels and you have frequency, not wavelength:

$$ e_a = {10^{G_\text{dB}/10}\: c^2 \over 4 \pi \: A_\text{phys} \: f^2} \tag{4} $$

As an example, let's find an arbitrary antenna on the internet with specifications:

- 2.4 GHz
- 24 inch diameter (0.2235 square meters area)
- 21 dBi

Thus by equation 4, the aperture efficiency of this antenna is:

$$ e_a = { 10^{21\mathrm{dBi}/10}\: c^2 \over 4 \pi \: 0.2235\:\mathrm{m}^2 \: (2.4\:\mathrm{GHz})^2 } = 70\% $$

That is, 70% of the power hitting that 24 inch reflector is available at the feedpoint, while the other 30% is lost. The losses could be due to:

- the feedhorn and its support structure shadowing the dish
- diffraction around the edges of the dish
- less than perfect focus and reflectivity of the dish
- inefficiencies of the feedhorn itself

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3643/what-is-the-aperture-efficiency-of-an-antenna, by Communicationantennas.com, K7PEH, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
