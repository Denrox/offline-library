# Does a receiving antenna need radials?

*Tags: antenna, antenna-theory, antenna-construction · score 5*

## Question

I am very new to radio and am using two 433MHz 1/4 wavelength monopole antennas to send and receive data. On the transmitting antenna I'm going to add radials (as it is the standard in my application). However I wonder, would it help adding radials to the receiver too? On the one hand it makes sense, but on the other I wonder, why would a receiver need a ground plane? I hope you can help me and that my question is not too dumb.

## Accepted answer (score 14, by Kevin Reid AG6YO)

Most antennas are reciprocal — they have the same properties when receiving as when transmitting. This means that in many ways, a good antenna design makes both a good receiving antenna and a good transmitting antenna.

(The biggest exception to this is active antennas which have an internal amplifier that only works for receiving.)

However, the properties that you *want* for a receiving antenna are not necessarily the same as a transmit antenna. For example, when transmitting, you care about how efficiently the antenna radiates, so that you're getting the best output for power input, and whether it can handle the power without failing (e.g. arcing, heating). Receiving does not care about this a bit, because the power is miniscule.

And if you are receiving, it is often the case that you care more about the *signal-to-noise ratio*, not the absolute amount of signal you receive.

Now let's talk about radials (or a ground plane) in particular. Every antenna *always* has two halves, no matter what; if you try to leave one out then either something else will replace it or your antenna won't work at all. If you leave off the radials in an antenna designed to have them, then what happens is the shield of your coax will start acting as the other half — you have instead a vertical dipole with a lower element of no particularly well-designed length or positioning.

This means that your antenna's radiation pattern will not be what you expect — it will receive less well in some directions than it was designed to. Being a too-long antenna, it will have an extra-spiky pattern, so if the other station is moving you'll see lots of nulls (directions with very low signal strength) which is bad for reliable communication.

Additionally, since the coax shield is acting as an antenna element, any noise from your equipment will come into the receiver, more than it would otherwise (that is, a decreased signal-to-noise ratio).

So, to summarize: put on the radials. You will get more predictable performance.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7639/does-a-receiving-antenna-need-radials, by user5227744, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
