# Twisting copper wire for a less-flexible DIY antenna

*Tags: antenna, antenna-theory, antenna-construction, wire-antenna · score 5*

## Question

I am making DIY antenna for a home project. The antenna is going to be "V-dipole" with leg length about 53cm.

Unfortunately, I didn't find a thick copper wire, but I have a lot of thin core from tv antenna cable.  
I am attending to twist a few thin wires together (without isolation, of course) in order to get a less-bendy leg. Something like this:

So, does the twist make any changes in physical antenna characteristic? Skin effect? I guess it is the same conductor, which probably will have less resistance than a single thin wire.

Thank you.

## Accepted answer (score 5, by Glenn W9IQ)

Your thought processes are on track - the primary electrical impact is on the RF resistance of the wire.

Twisting the wires effectively creates a larger wire diameter with more surface area. The additional surface area reduces the RF resistance attributable to skin effect. Depending on the frequencies involved, this may be of minimal benefit. Based on the geometry of your antenna, it appears that you are in the 130 MHz range. If so, the radiation resistance of the antenna is around 70 ohms which means it would take at least of couple of ohms to have a significant effect on efficiency. The formula for antenna efficiency is:

$$Efficiency=\frac{R_r}{R_r+R_l} \tag 1$$

where Rr is the radiation resistance of the antenna and Rl is the resistive losses in the antenna.

Efficiency is multiplied times directivity to specify the gain of the antenna.

One thing to consider is that corrosion between the individual strands can offset the increased surface area. We often see this when a coaxial cable gets water inside the jacket. The braided outer conductor becomes corroded and it no longer makes an effective shield. But since mechanical strength is your primary reason for twisting the wires, this will probably have negligible impact on the performance of your antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11786/twisting-copper-wire-for-a-less-flexible-diy-antenna, by Deliaz, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
