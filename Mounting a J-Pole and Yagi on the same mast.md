# Mounting a J-Pole and Yagi on the same mast

*Tags: antenna, antenna-construction, vhf, j-pole · score 3*

## Question

I have two 2-meter antennas, a copper J-Pole and a Hy-Gain VB-25FM. The J-Pole is my all-around antenna, what I use for general 2 meter stuff like connecting to my local repeaters using my main 2-meter radio. The VB-25FM will be used to establish a connection to a specific ham that lives across town from me to play around with digital modes on a different radio.

My thinking was it would be great if I could mount the VB-25FM mid-way up the mast, and then mount the J-Pole on the very top. Would this work, or is it a bad idea?

Thanks.

## Answer (score 2, by Glenn W9IQ)

**Near and Far Fields**

To mount the two antennas in close proximity to one another, you should minimally ensure that neither reactive (near) field interferes with the reactive field of the other in order to avoid disturbing the pattern or gain of either antenna.

The reactive near field is generally defined as:

$$R\approx0.62\sqrt{\frac{D^3}{\lambda}} \tag 1$$

where R is the radius (separation distance), D is the longest linear dimension of the antenna in meters and $\lambda$ is the wavelength.

In the case of two antennas, calculate R for each one and add the results together. For example, if one D is 1 meter, the other D is 2 meters and the band is 2 meters:

$$R_1\approx0.62\sqrt{\frac{1^3}{2}}$$ $$R_1\approx0.88 \text{ meters}$$

$$R_2\approx0.62\sqrt{\frac{2^3}{2}}$$ $$R_2\approx1.24\text{ meters}$$ So the minimum separation would be ~2.1 meters.

If you wish to play it safer and have each antenna in the other's Fraunhofer zone (far field) then use the formula:

$$R=\frac{2D^2}{\lambda} \tag 2$$

where D is the maximum linear dimension of the two antennas.

For the same example as above, the maximum linear dimension is 2 meters which would yield a distance of 4 meters. But since you are dealing with stacked vertical antennas, the radiating near field in the direction of the other antenna is greatly suppressed. Therefore this is an excessive distance in your application. A compromise between the results of the two formulas should prove sufficient.

**Common Mode Current**

The J pole antenna is notorious for the development of common mode current on the coax. This results in the coax becoming part of the radiating / receiving antenna. Since this coax will likely pass adjacent to your yagi, the above near and far field calculation efforts will be nullified without a proper current balun on the J pole feedpoint to mitigate the common mode currents.

**Receiver Overload**

If you plan on operating both radios at the same time, take into account that while transmitting on one antenna, a good deal of this power arrives at the other antenna. This can overload the receivers front end or, in a worst case, damage the receiver even if they are not on the same frequency.You may wish to use the Friis equation to help estimate the amount of power impressed upon the receiver. Use the gain of the each antenna in the direction of the other (which will be far less than their stated maximum gain). You may find this thread on ["How to find or derive the maximum safe input power to a receiver?"](How%20to%20find%20or%20derive%20the%20maximum%20safe%20input%20power%20to%20a%20receiver.md) to also be helpful.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11664/mounting-a-j-pole-and-yagi-on-the-same-mast, by user16442, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
