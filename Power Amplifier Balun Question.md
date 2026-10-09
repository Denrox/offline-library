# Power Amplifier Balun Question

*Tags: balun, amplifier · score 3*

## Question

Second (and last hopefully) question on the classic *Solid State Design for the Radio Amateurs* (SSDRA) book by Hayward et al. Again it's a power amplifier circuit (Chapter 4, pg. 66), and again it's related to baluns. Is it just me or are baluns complicated to understand (at times)? Here's the circuit, with the balun in question identified as T2 at the output.

Here's my spice interpretation of the balun and it's no coincidence that it has a similar layout to that found in the balun analysis paper by G3TXQ (http://www.karinya.net/g3txq/baluns/baluns.pdf). On the right-hand side is the balanced load (pins 1 and 2 in the original SSDRA circuit) and on the left side is the unbalanced input, with pins 4 and 5 going to ground (these pins are AC grounded in the original).

In fact, it's very similar to the 1:1 voltage balun described in this document, except that the polarity (dot) of the tertiary winding is reversed.

Without doing any analysis on the SSDRA balun, I figured it was going to be a voltage balun and I was expecting the voltages across the balanced load to be equal, as with the conventional voltage balun given in the G3TXQ document. I was wrong. In fact the winding directions of the SSDRA balun seem to generate a short in the unbalanced source. That sortof makes sense, since the voltage across L1 and L2 cancel leaving a short to ground. See the spice current across R4 below:

So, my question is: what exactly is this balun doing?

## Accepted answer (score 5, by Phil Frost - W8II)

I believe it's a misprint. Comparing the drawing showing the construction of the balun with its schematic representation, it does appear the dot on the lowermost winding (terminals 2 and 5) is backwards.

If we build it like the schematic suggests, consider the application of a differential mode input on the balanced side:

V1 drives current in L3 and L1, but the polarity of these windings are opposite, resulting in zero net magnetic flux. Thus it's as if the inductors aren't even there, and V1 sees a short. Not a useful property in this application.

However if we flip L3 the other way:

Now L1 and L3 are working together rather than cancelling each other.

Vcc is attached to the center tap (with a little filtering), and half of the primary winding is the load for each of the transistors. So at a basic level, each half of the amplifier is just a common-emitter amplifier:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11949/power-amplifier-balun-question, by Buck8pe, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
