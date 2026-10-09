# How do dual band J poles work?

*Tags: antenna-theory, j-pole · score 4*

## Question

My understanding is a J pole is a $\frac{1}{2} \lambda$ dipole attached to a $\frac{1}{4} \lambda$ impedance matching element.

How does this dual band work? What acts as the impedance matching element and what is the radiating element? Does the smaller rod act as the impedance match for 2 m and the larger one for 440 MHz with the longest rod acting as the radiating element?

How is a feedline connected to this?

From http://ve3elb.ham-radio.ch/2m-70cm%20antennas.html#:~:text=ARROW%20ANTENNAS%20DUAL%20BAND%20J%2DPOLE

## Answer (score 2, by hobbs - KC2G)

In the J146/440 antenna, on the right:

For 2m, the leftmost and rightmost element form the J-pole, and the center element is too short to matter very much. (It probably adds some inductance, which could explain why the left element seems a little shorter than it should be for 2m).

For 70cm, the center and leftmost element form the J-pole, and the rightmost element, being a little over 2WL long, isn't resonant and doesn't have much of an effect.

It's not super important whether a J-pole is fed at the "long" or the "short" element; since the leftmost (medium length) one is the one that both bands have in common, that's the one that gets fed. The coax center goes to the left rod (which is insulated from the aluminum angle). The coax shield goes to the aluminum angle itself, which the center and right rods are in electrical contact with.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17207/how-do-dual-band-j-poles-work, by rsn, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
