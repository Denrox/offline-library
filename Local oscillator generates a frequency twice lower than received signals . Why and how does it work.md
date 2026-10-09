# "Local oscillator generates a frequency twice lower than received signals". Why and how does it work?

*Tags: receiver, oscillator · score 3*

## Question

I would like to construct the following receiver:

I have a fair knowledge about a receiver building blocks. I have previously build small receivers.  
In the description it say:

The local oscillator ... generates an oscillations with a frequency twice lower than the frequency of received signals.

**How can that be possible and why it is needed?**

## Answer (score 3, by Josef)

The oscillator may really be running at half of the received frequency. Search for Poliakov mixer on the web for an example of this.

## Answer (score 2, by user2943160)

This appears to be a design that uses a harmonic mixer (or a subharmonic mixer, both names are used on the Wikipedia page). While these are more commonly used at microwave or millimeter wave frequencies in contemporary equipment, they were probably reasonable, low-cost solutions for these single-conversion receivers. As described in the text, VD1 and VD2 form the mixer for this radio receiver.

As a consequence of being a harmonic mixer, the mixer uses a harmonic of the local oscillator, making the local oscillator a subharmonic of the radio frequency being received.

A diagram for a microwave-type mixer using this concept shows the anti-parallel diodes seen in the HF mixer in the question's design. This is currently advantageous because generating high-power oscillations >10GHz is difficult and there are applications targeting 60 and 70 GHz with test equipment up to 110 GHz.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4980/local-oscillator-generates-a-frequency-twice-lower-than-received-signals-why-a, by machineaddict, Josef, user2943160. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
