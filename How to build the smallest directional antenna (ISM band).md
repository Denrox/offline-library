# How to build the smallest directional antenna (ISM band)?

*Tags: antenna, antenna-construction, microwave · score 3*

## Question

What kinds of configurations should I try when trying to make the physically smallest 2.4 GHz (ISM band) antenna that is significantly directional front-to-back. "Smallest" meaning in in cm maximum dimension. "Significant" meaning quickly measurable as above above typical ISM band noise floors when turning the antenna around.

## Answer (score 5, by tomnexus)

(Sorry about the long delay)

An antenna that might meet your requirements is called the HB9CV. It's an array with two dipoles about 1/4 wave apart, driven with the correct current that they add in-phase in the forward direction, and completely out of phase in the backward direction.

Getting the currents to do this isn't trivial, because they interact with each other, but Mr Baumgartner, HB9CV, designed this neat way of doing it.

I built mine for the 2 m amateur band, 15 years ago, after some optimisation in NEC. It worked well, had a sharp null which produced a nice "Crunch" of static in the receiver as I rotated the null past the direction of the source. Searching now on the net, I can find instructions but no simulated patterns, so here they are.

A 3D pattern, which looks cute but doesn't really tell you anything:  
And a 2D cut at Theta=90, on the horizon, which looks great:  
A compact antenna can't really have high gain, or a narrow beam in the front, but it can have this deep null. The one above is over 30 dB deep, in simulation, in practice you won't achieve this.

This is the layout of the antenna, I made it with soldered copper water pipe:  
  
Dimensions are in m, for 145 MHz, so you could scale these down by about 16.8 times for 2450 MHz. But it will get very fiddly making the antenna out of piping, so I proposed you make it on a PCB, like this:  
The two colours represent the copper on the two sides of the PCB.

This is obviously an incomplete design, I can't simulate it on PCB for you, so there will be some more research, design and trial and error required to get it working.

The final size is reduced slightly by the PCB, if I remember correctly, to about 80% for the dipole lengths, and say 90% for the spacings. So the final PCB will be about 50 x 50 mm.

Hope that is small enough for you!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3727/how-to-build-the-smallest-directional-antenna-ism-band, by hotpaw2, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
