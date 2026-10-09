# How can Ground Penetrating Radar work?

*Tags: propagation, equipment-design, earth · score 5*

## Question

I was reading about GPR devices recently.

Considering the operation frequency of these devices, how they can go that deep (up to 50 feet)? Normally you would only expect a Hz to KHz range signal to go that deep into the ground.

## Accepted answer (score 9, by Glenn W9IQ)

There is a special adaptation of the Friis equation, called the Radar Equation, that describes the range of a radar system. Here is a *basic* version that calculates the maximum range of a radar system:

$$R_{max}=\sqrt[4] {\frac {P_tG^2\lambda^2\sigma}{P{_{r(min)}}*(4\pi)^3*L}} \tag 1$$

where $R_{max}$ is the maximum range in meters, $P_t$ is the transmit power in watts, $G$ is the linear gain the combined transmit and receive antenna, $\lambda$ is the wavelength in meters of the frequency, $\sigma$ is the effective radar target cross section in square meters, $P_{r(min)}$ is the minimum receiver power required in watts, and $L$ is a linear loss factor to consolidate all losses other than free space effects encountered in the radar path.

So if we take a 2 GHz radar (0.15 meters) with 10 watts of transmit power, a receiver with 0.25 $\mu$V of sensitivity (1.25e watts for a 50 ohm system), an antenna with a linear gain of 31.6 (15 dBi), a 1 square meter metal target and no other path losses, we calculate a maximum effective distance of 3,085 meters (10,121 feet).

We would now need to account for the losses of earth (rock, soils, sands and water) to apply this to a ground penetrating radar. This can be factored into $L$ in equation 1. I do not have data at hand to suggest what the possible attenuation factors would be for various forms of earth so instead, it may be instructive to rework equation 1 to solve for the maximum attenuation that can be accommodated over a specified distance:

$$L={\frac {P_tG^2\lambda^2\sigma}{P{_{r(min)}}*(4\pi)^3*R_{max}^4}} \tag 2$$

If we set $R_{max}$ to 15.24 meters (50 feet) as questioned by the OP and leave all other parameters the same, we find that an additional path loss ($L$) of ~92 dB (~1.68e linear attenuation) could be accommodated before the radar would not be able to detect a signal from a 1 meter square metal target 15.24 meters below the surface.

So armed with these basic formulas, one can run various "what if" scenarios to get a sense of what is possible. Do keep in mind that this is a very simplified form of the radar equation that does not 'reflect' (pun intended) all of the factors involved.

Edit:

I did find some very basic soil attenuation data at https://archive.epa.gov/esd/archive-geophysics/web/html/ground-penetrating_radar.html. Here is an extract of attenuation in the 40 to 1,500 MHz range:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9706/how-can-ground-penetrating-radar-work, by Samk80, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
