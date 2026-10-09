# How should two loopstick antennas be placed w.r.t each other to maximize transmission?

*Tags: mf · score 5*

## Question

An engineer working in the RF industry told me something which left me very confused: He said that a pair of emitter-receiver beacons get the clearest signal when loopstick antennas in the receiver and the emitter are parallel. That is, when both loopstick ferrite rods point at each other. (We are talking low MF band, with distances of 50-100 meters between antennas)

This left me confused for the following reasons:  
- I had been taught from multiple sources that a loopstick antenna has a null in the loop axis.  
- According to my limited knowledge of the Maxwell equations, near and far field, and antennas, the opposite should be true.

First off, a visualization of the EM field around a dipole antenna field is easy to find:

As I understand, the field around a loopstick antenna would look something like this:

If this is correct, I would assume that placing the loopstick antennas parallel but side by side would maximize the signal strength, and not placing them parallel on an axis.

( like this || || VS like this = = )

So what is the right answer?

(An extra question: this engineer mentioned that at distances 50+ meters away, it should still be considered as near-field. Wouldn't the near-field for a ~600m wavelength, loopstick antenna be much, much smaller?)

Thanks!

## Accepted answer (score 9, by tomnexus)

When they're very close together, aligning them end to end will give better coupling - think of them as coupled inductors or a transformer. You want the strongest magnetic field from one magnet, to pass through the other.

When they're very far apart, you're right, side to side, broad side, is best. Remember that you're free to think of an antenna as a magnetic or an electric device. A loop or coil is just a lot of little dipoles in series, and its far fields reflect this. From the end of a small loop, the (far) electric fields of all the little dipoles clearly cancel out, so there's a null.

In the cross-over region it might be complicated.  
Near fields (the reactive fields that decay as $1\over{r^2}$ ) and far fields (travelling wave components that decay as $1\over{r}$) are equal at approximately $\lambda\over{2\pi}$ or 90 metres in your case, so the transformer type coupling might dominate over the antenna-type coupling.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14889/how-should-two-loopstick-antennas-be-placed-w-r-t-each-other-to-maximize-trans, by Dugas, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
