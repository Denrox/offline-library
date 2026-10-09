# Understanding "ground" in ham radio

*Tags: grounding · score 3*

## Question

What is a good explanation of the different "ground" types that hams deal with? Specifically:

- grounding an antenna mast/tower (outside, lightning prevention)
- grounding transceiver/equipment (inside shack, RF leakage prevention)
- antenna ground plane (on/under antenna)

## Accepted answer (score 6, by Ron J. KD2EQS)

grounding an antenna mast/tower (outside, lightning prevention)

A tower or mast must be grounded to "earth", usually through an 8' conductive (copper) rod driven into the ground as close to the antenna setup as humanly possible. Should the worst happen and lightning strike on or about the mast/tower, you offer the electricity a shorter path to "earth" and reduce the possibility of it entering the shack through your feed line.

grounding transceiver/equipment (inside shack, RF leakage prevention)

Radio equipment may leak RF or high currents. Grounding the case (usually with a ground screw conveniently provided thereupon) will reduce the risk of operator injury and equipment damage.

antenna ground plane (on/under antenna)

The antenna system requires a "ground plane" for the radio wave to form. With dipoles, one half of the antenna is your ground. In verticals, something below must provide ground to complete the RF wave. This is usually achieved with radials, either attached to the base of the vertical, or buried below a ground mounted antenna. The presence of a metal mast/tower (which is lightning grounded) may contribute/interfere with the ground plane but it is not considered the antenna ground.

While all three of these "ground systems" may end up connected directly or indirectly to "earth" (grounding rod, water pipe, etc) — they are actually all different.

## Answer (score 2, by Dan KD2EE)

There are two traditional meanings of an electrical "ground". In DC systems, we often refer to the return conductor (the negative lead) as "ground". You won't encounter that meaning very often in amateur radio, but when dealing with vehicles you need to ensure that you have a good "ground" connection from the battery to the negative lead at the radio, not for RF or safety reasons, but to prevent any voltage loss along the power supply.

The more well known use of a ground is a safety ground in an AC system. The purpose here is to have a conductor that has no voltage and ideally no current on it which is connected to the chassis of a device. That way, if there is a fault which puts a voltage on the chassis, it will trip a fuse or breaker, preventing injury to the user.

The other advantage of a conductive chassis is RF shielding. In this case we don't actually rely on the fact that the chassis is grounded, as long as it encloses all the circuitry with a minimum size of holes (for connectors or buttons), it will significantly dampen any RF going in or out.

Finally, when we're talking about antennas, the ground acts in a completely different manner, "reflecting" signals and enabling certain modes of propagation. Vertical antennas can often be modeled as if there is a "mirror image" underground, creating a dipole antenna with certain ideal characteristics. If the ground is missing or not ideal (such as a metal vehicle or roof instead of a true ground) then the properties of that antenna will be less than the perfect dipole model. Once again, the ground is acting as the "return" - current flows one way in the antenna and opposite through the ground, keeping the currents equal at every instant. Sometimes, especially in the case of HF verticals, we will "help" the ground by using radials - wires just slightly underground, cut to be a quarter wavelength on the desired frequency. This is all about making the actual ground more like the ideal model.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/402/understanding-ground-in-ham-radio, by Ron J. KD2EQS, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
