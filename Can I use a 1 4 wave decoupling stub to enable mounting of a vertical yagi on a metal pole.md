# Can I use a 1/4 wave decoupling stub to enable mounting of a vertical yagi on a metal pole?

*Tags: antenna, antenna-theory, vertical-antenna · score 3*

## Question

My understanding is that the ground plane radials used on, for example, a free standing 5/8 wave 10 m vertical antenna mounted on a metal pole, are actually 1/4 wave length decoupling stubs, the function of which is to present a high impedance at the frequency being used to isolate in an RF sense the metal mounting pole from the antenna and stop the pole from becoming part of the antenna and radiating / receiving.

Whether this is true or not, can i use the decoupling stub idea to enable a 10 m vertical yagi to be mounted on a metal pole with the pole in between the elements and not have the metal pole upset the operation / radiation pattern / impedance of the yagi ?

If anyone knows about this, any chance of getting details on construction or pointing in the right direction for more information ?

## Answer (score 4, by Richard Fry)

**RE:** *...understanding...that...ground plane radials are...used to isolate...the metal mounting pole from the antenna and stop the pole from becoming part of the antenna and radiating / receiving.*

Unfortunately (for an example), even a set of 4 x 1/4WL radials of a 1/4WL v-pol "Ground Plane" antenna does not prevent r-f current from flowing along the outer diameter of the outer conductor/shield of coaxial transmission line connecting it to the source (the transmitter), even though the coax shield outer conductor is connected to and at the surface of the Earth.

R-F current flowing along the coax shield OD (and/or the OD of a metallic tower/pole etc used to support the antenna) produces e-m radiation into space just as it does when flowing along the vertical conductor of the ground plane antenna, itself.

The following NEC4.2 analysis is an illustration of this. The red lines surrounding the wire model at the right side of the graphic show the relative amplitude and phase of the r-f currents flowing along those conductors.

## Answer (score 3, by Brian K1LI)

I modeled a $\frac{\lambda}{2}$ vertical dipole located $\frac{\lambda}{10}$ from the top of a grounded $\lambda$ conductive pole. Numerous NEC2 simulations with four (4) $\frac{\lambda}{4}$ and $\frac{\lambda}{2}$ radials at locations up and down the conductive support did meaningfully reduce currents in the support.

Reducing currents in the conductive pole requires breaking it up into lengths that won't support current at the operating frequency. Shown below is the first example that showed meaningful current reduction, requiring the pole to be broken into three sections.

Each of the upper sections is $\frac{\lambda}{5}$ long and they are separated by $\frac{\lambda}{20}$, but the separation was just for convenience in simulation. This can be accomplished with insulators, of course, but also using de-tuning "loops" a la W8JI and others:

Maximizing the current through the capacitor-tuned loop sections A and B minimizes the currents in the adjacent sections C and D.

## Answer (score 3, by Phil Frost - W8II)

The radials are there to present a low impedance, not a high one. The idea is to make the radials the lowest impedance thing around, though whether that's true or not depends on the mast, feedline, and other environmental factors beyond the antenna designer's control.

Mounting a vertical Yagi on a vertical mast is necessarily going to alter the antenna's behavior since the mast is essentially an additional element. You will want to minimize the interaction between the antenna and the mast since the contribution of the mast to the radiation pattern will probably not be a desirable one.

The other answers have demonstrated some models which show potential scenarios. It's tempting to overgeneralize these results, but keep in mind the way the antenna interacts with the mast is highly dependent on the geometry between the two. You'll have to model or empirically evaluate your specific situation to know what can work.

Unfortunately the only sure way to minimize interaction between the antenna and the boom is to get them apart, either through a horizontal member or a non-conductive one.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16515/can-i-use-a-1-4-wave-decoupling-stub-to-enable-mounting-of-a-vertical-yagi-on-, by Andrew, Richard Fry, Brian K1LI, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
