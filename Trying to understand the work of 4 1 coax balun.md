# Trying to understand the work of 4:1 coax balun

*Tags: coaxial-cable, balun, impedance-matching · score 3*

## Question

Let's consider the following picture (source):

When current passes the half-wavelength matching section it changes the phase to the opposite, this is why we get +V and -V in the feed point, 2V difference in total. Also I understand that the current splits to 2 x I/2, this is why we get ( R = 2V/[I/2] ) 1:4 impedance matching.

What I'm not sure about is what happens to the current in the shield of the half-wavelength coax. The current in the shield of the feed line should flow somewhere.

Does it flow to the half-wavelength coax and cancels itself because of the phase shift? What prevents it from jumping over the beginning of the half-wavelength section and flowing from the end to the beginning of this section? Could you please explain this part in a little more details.

**Update:** Or there is no current in the shield at all? After all it has no connection to the center part of the cable.

## Accepted answer (score 7, by Phil Frost - W8II)

Think of it first without the feedline:

The half-wavelength of transmission line provides a 180 degree phase shift, and the (short) connection between the shield ends is "ground". That means it's at 0V relative to the environment, and also the voltage at the open ends of the coax center conductor will be equal in magnitude but opposite in sign relative to this ground point.

Assume now this is somehow magically fed: there must indeed be an induced current on the shield, equal but opposite to the current on the center conductor. This shield current is also subject to the phase inversion, so if it's going in the coax on one end it's not coming out the other end because it's been inverted: it's also going in. Equal but opposite currents cancel. Which is good, since we said this was ground.

Now if you've read about coax you may know this is exactly the kind of place we want to attach the shield end of a feedline: we want to attach it at a place where the voltage is unchanging relative to the environment, otherwise we get common-mode current that causes the feedline to radiate. And examining the original diagram, this is indeed where the coax is attached.

But still, where does the shield current go? If you like, you can imagine that it splits equally into each half of the 1/2 wave loop:

Each half then independently travels around the loop where it's inverted then cancels itself.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15597/trying-to-understand-the-work-of-4-1-coax-balun, by Aleksander Alekseev - R2AUK, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
