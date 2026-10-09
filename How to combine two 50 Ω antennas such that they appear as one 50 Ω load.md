# How to combine two 50 Ω antennas such that they appear as one 50 Ω load?

*Tags: antenna-construction, impedance-matching · score 11*

## Question

I'm looking for a simple way to impedance match an array of two 50 Ω antennas so that when they are combined they appear as one 50 Ω load.

Assume that both antennas are identically constructed, are in phase with one another, and have the same VSWR very close to 1. The frequency the antennas are tuned to is 2.4 GHz.

Is there a simple “rule of thumb” method that I could use that requires little equipment?

## Accepted answer (score 10, by Phil Frost - W8II)

The canonical solution to this problem is a Wilkinson power divider. There are of course other power dividers, but the Wilkinson is easy to fabricate, provides good isolation between the output ports, and is lossless when the output ports are equal and in phase, which is true for an ideal antenna array.

If you were to make one of these yourself, you'd probably do it with coax. However, it's easier to illustrate with microstrip:

P1 would be connected to your transmitter, and P2 and P3 to your antennas.

Between P1 and P2, and also between P1 and P3, are quarter-wavelength transmission lines having an impedance of $\sqrt 2 \cdot Z_0$. For your case that works out to $\sqrt 2 \cdot 50 \Omega = 70.7\Omega $. 75 ohm coax is close enough and easier to find.

Between P2 and P3 is a resistor that's twice the characteristic impedance. For your case, that's $100\Omega$.

Made with coax, it looks something like this (click for bigger version):

Although it's not impossible to fabricate this sort of thing yourself, doing so at 2.4 GHz is a bit of a trick, especially if you don't have test equipment. 2.4 GHz is a very popular band, and this is a very common device, so you won't have any difficulty finding a pre-made solution for purchase.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1764/how-to-combine-two-50-o-antennas-such-that-they-appear-as-one-50-o-load, by Ben, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
