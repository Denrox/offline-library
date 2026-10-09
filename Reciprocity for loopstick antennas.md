# Reciprocity for loopstick antennas?

*Tags: antenna · score 3*

## Question

What is the reason a small loop-stick antenna ( typically used for AM reception) does not have reciprocal characteristics for both reception and transmission. ( AM reception works great on those little loopsticks, but you don't get desirable results, when trying to transmit back through such a device)

## Accepted answer (score 6, by Phil Frost - W8II)

At reasonable transmission powers, the ferrite core saturates. Also, it would probably overheat, and produce a horribly distorted transmission.

The ferrite core is made of movable magnetic domains. Each of these are small bits of the material that have magnetic poles like a tiny bar magnet. Normally they are all pointing in random directions, and their individual fields cancel so the ferrite bar doesn't seem to be a magnet. A lot of matter is like this.

Ferrite is special in that the magnetic domains are easily moved. When an external magnetic field is applied, they all move to align with that external field. Then their fields add to the external field, and you end up with a magnetic field which is stronger than the external field would have been if the ferrite were replaced with air.

This property is called magnetic permeability. It's this magnetic "amplification" that makes the loopstick antenna so effective. The ferrite stick increases the antenna aperture by concentrating the magnetic flux from far away transmitter through the center of the windings where it will induce a current that is detected by the receiver.

The trouble is the magnetic domains can become only so much aligned. At some field strength they are as aligned as they can be, and the permeability drops to zero.

The ferrite doesn't care if the external magnetic field is coming from a distant transmitter, or the coil around it. Because the field from the transmitting coil is many orders of magnitude stronger, saturation of the core is likely unless the transmit power is very small, maybe microwatts.

This saturation of the core means the antenna is highly nonlinear, and would thus introduce unacceptable distortion into the transmission.

Furthermore, the magnetic domains are "sticky": it takes some amount of energy that's wasted as heat to move them. This is called hysteresis loss. When receiving this loss reduces the efficiency of the antenna, but since the field is so weak there's no significant heating. When transmitting the energy lost is higher, and without adequate cooling heat may accumulate to reach the ferrite's Curie temperature, and the ferrite's magnetic properties will be lost.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7525/reciprocity-for-loopstick-antennas, by Skyler 440, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
