# How to make a "you're getting warm/cold"/"fox hunting" game based on RF signals

*Tags: receiver, antenna-construction, direction-finding, fox-hunt · score 3*

## Question

I would like to build a system in which the emitter emits omnidirectional RF signals, and the receiver gets a stronger signal (it does not have to be accurate) with a) closer distance from the emitter b) better pointing with the emitter (directional receiver).

Kind of like a "you're getting warm/cold" game.

What's the simplest technology and type of circuit that would allow me to do this?

I have thought of a signal strength circuit with a directional antenna, is that the simplest way? i.e. If I wire "data in" of a 315MHz transmitter such as this one https://www.sparkfun.com/products/10535 to Vcc, and if I build a tuned (adjustable) tank circuit + OA81 diode + ADC at the receiver, could it work?

## Answer (score 2, by SDsolar)

First the answer: When I worked for the forest service I built single-transistor transmitters where one of the leads of the transistor was the antenna. It doesn't get any more simple than that.

They used hearing aid batteries. Then we could enclose them in beeswax so we could stuff them down the throats of animals, even snakes. The batteries would last about three days. EPA said we were supposed to recover the batteries, but some of them apparently got lost on the way back. The receivers were about the size of a canteen, using D cells and hung around the neck so one operator could handle it. We used 3-element Yagi antennas to follow the animals.

Now a story:

We played 2-meter "rabbit hunting" every Saturday for years in Fairbanks.

The receiver wasn't the key to success. It was the antenna and the skill to use it.

It turned out that instead of using Yagi antennas to find the source, the best way to get a fix was to use a tuned loop antenna and utilize the nulls in the donut-shaped pattern of the antenna.

Nulls are much sharper than the broader beamwidth of a Yagi or a quad.

Newer DF systems, (like the 4 antennas on police cars to find transmitter packs inserted in stolen money), use time-of-arrival, and are best used when they are close to the source. Plus they generally can only give you 8 LEDs to indicate the first antenna (and in between two) where the signal arrives.

We didn't use computers like that. About the only portable computer we had back then was the KIM-1, anyway.

Our loops could go for miles.

For the record, one of our rules was to never work in teams other than having two people in the vehicle. It was up to each pair of us to establish our own bearings. The second rule was that the rabbit couldn't move. But there was no rule as to how often the rabbit must transmit.

Then as we got closer, we would detune the loops (with a capacitor at the top of the loop) to avoid desense in the receiver.

We had very modest prizes, like first plates of food at the inevitable BBQ.

Those were really fun days.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6818/how-to-make-a-you-re-getting-warm-cold-fox-hunting-game-based-on-rf-signals, by user42875, SDsolar. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
