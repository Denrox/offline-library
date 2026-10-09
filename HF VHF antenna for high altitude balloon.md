# HF/VHF antenna for high altitude balloon

*Tags: antenna, wire-antenna, 2m-band, wspr · score 5*

## Question

I'm working on the design of a dual band transmitter for use on a high altitude balloon. I'll be transmitting on 2 meters and 20 meters (APRS and WSPR) with about 50 mW. To keep the weight to an absolute minimum, I'm designing it to use a single antenna for both bands. Using 4nec2 modeling I came up with an off center fed (20M 1/2 wave) dipole having a feedpoint positioned where the impedance is about 200 ohms on both bands (using 38 AWG wire.) A diplexer circuit will merge the outputs of the 2M and 20M RF paths and match the impedance to the antenna. I estimate this antenna configuration should weigh less than 1 gram. Any advice from experienced wire antenna/ high altitude balloon experimenters before I commit too much to hardware?

## Accepted answer (score 4, by Glenn W9IQ)

It is equally important to consider the pattern of the antenna. If you hang a 1/2 wave antenna vertically, there will be minimal radiation in the earth facing direction. This will be most problematic for HF NVIS contacts.

You may also wish to check the RF resistance of 38 AWG wire on 2 meters. I roughly calculate it to be > 100 ohms at 146 MHz for 10 meters in length. This will have significant effect on the efficiency, and thus the gain, of the antenna on 2 meters. At 20 meters, it is > 40 ohms, which can also be a significant factor in the performance of the antenna.

Have you modeled the directivity and efficiency of the antenna to ensure it meets your path budget?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9799/hf-vhf-antenna-for-high-altitude-balloon, by whalphen K8VFO, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
