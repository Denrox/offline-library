# How does a folded balun work?

*Tags: antenna, theory, balun · score 6*

## Question

A folded balun is made from two quarter-wavelength, parallel conductors. A picture is worth a thousand words:

Here are some pictures of an actual construction from Gisela & Joe Noci on diydrones.com:  
  
Sometimes they are [printed on a PCB](Connect%20Printed%20Yagi-Uda%20Dipole%20Array%20with%20Balun%20to%20coaxial%20cable%20correctly.md), so the quarter-wave sections are not coax but PCB traces.

How does this balun work?

## Accepted answer (score 9, by Phil Frost - W8II)

It's easier to see what's going on with a bit of rearrangement. Imagine this built of tubing:

The feedpoint is still where it would be on a dipole without the balun. The feedpoint sees the dipole as usual (blue).

In parallel with that is a twin-lead transmission line formed by the two parallel sections of the balun (red). This is a quarter-wave section with a short at the end, so it looks like an infinite impedance. An infinite impedance in parallel with the dipole at the feedpoint doesn't change the impedance the feedpoint sees. The red section might as well not be there at all.

Then, there's this green stub on the bottom. It's insignificant to the operation of the antenna because there can be no currents on it. Although there may be currents of the balun (red section), they are equal and opposite, and so at the point where the green stub is, they cancel. So you can't drive a current on the green stub via the feedpoint. Furthermore, because the green stub is symmetrical with respect to the dipole, it will have equal capacitance to either half of the dipole, and so you can't drive a current on the green stub capacitively, either.

So there's no way to drive a current on the green stub via the feedpoint. That sounds like exactly what we want in a balun, if the green stub is the coax shield. Trouble is, the feedpoint is up there at the top. How can the shield be connected at the bottom while the feedpoint is at the top? Easy, if it's made from tubing. Just cut a little hole near the feedpoint, and run the feedline inside the tubing. The shield is connected to one half of the dipole at the hole, and the center conductor goes through the hole to feed the other side:

This is equivalent to the more usual construction:

This uses the coax as the tubing, and since the spacing between the balun halves is usually very small (assuming coax diameters far smaller than the wavelength), not exiting exactly in the center has a negligible impact on performance.

By running the feedline "inside" the antenna and balun, we have the option of connecting the shield in a location where there can be no common mode current, while connecting the feedpoint somewhere else. A similar trick is used by the [shielded loop antenna](What%20does%20the%20addition%20of%20a%20shield%20to%20a%20small%20loop%20accomplish.md).

## Answer (score 2, by tomnexus)

It's possible to make a folded balun on a double-sided PCB, with a track on top of a double-sided PCB. This makes the whole yagi (or dipole or vivaldi) quite easy to fabricate.

It looks something like this (terribly not to scale)

The short-circuited 1/4 wave stub already helps a lot with matching, it broadens the bandwidth of a dipole nicely. For more difficult matching problems, you can

1. design the yagi for a reasonable feedpoint impedance, of course
2. adjust the length of the driven element
3. adjust the depth of the balun short, by filling it in, or extending it back, which allows you to add some parallel inductance or capacitance
4. use a 1/4 wave open stub to excite the other half of the dipole, which allows you to add some series inductance or capacitance. The feed will then look like this:  
Bear in mind that normal fibreglass PCB is quite lossy, so at GHz frequencies this is not a very efficient antenna. It helps to make only the feed area out of PCB, and the rest out of solid metal, wire, etc., but there's still the transmission line loss, which is much much worse than coax. Going to a Rogers or other low-loss dielectric also helps.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3591/how-does-a-folded-balun-work, by Phil Frost - W8II, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
