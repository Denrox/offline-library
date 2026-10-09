# Does Kirchhoff's current law (KCL) apply to antennas?

*Tags: antenna · score 5*

## Question

I think I'm having a hard time understanding HF antennas because they go against everything I've been taught about analyzing circuits.

If we look at a dipole antenna, there is the highest current in the middle and zero current at the ends. So if we consider any point along the dipole to be a Kirchhoff's current law (KCL) node, then there is less current going out of the node than flowing in. Does KCL not work with RF circuits?

## Answer (score 5, by Phil Frost - W8II)

Wikipedia states the KCL as:

The algebraic sum of currents in a network of conductors meeting at a point is zero.

The key word here is *point*. If you pick a single geometric point on the antenna, then yes, this law holds. It's fairly easy to see why intuitively from the law of charge conservation: since charge can't be created or destroyed, if an electron enters the point it will create a net negative charge at that point, which is associated with an electromotive force that will push some other electron out.

But KCL is often applied to nodal analysis problems. For example consider these two equivalent circuits:

In this schematic it doesn't really matter if we pick node A or B, because the circuit can be redrawn as show to have all three current sources and the LED meet at one point. We can do this because a line in a schematic isn't a real conductor, but rather an idealized connection. Everything connected by a line in the schematic has the same electric potential, and any changes propagate instantly throughout the entire net.

This is such a useful and ubiquitous simplification we tend to apply it without even thinking. Here's the trap: an antenna, although it may be just a conductor, is not a line on a schematic.

Neither are the wires in the circuit above, for that matter. Even just a wire is an inductor, albeit a small one. And two wires separated by a dielectric (like air, silicone, PTFE, or PVC) are a capacitor. So if we really wanted to draw an LED driven by three current sources, it might look more like this:

Of course we haven't put any discrete inductors or capacitors in the circuit: we are simply including in the schematic (some of the) non-ideal behavior of actual wires. Normally we omit them because the capacitance and inductance is too small to be relevant to the operation of the circuit. For example if we just want to blink an LED at 1 Hz, all this parasitic capacitance and inductance doesn't matter at all.

But in antennas it absolutely does matter. Imagine a dipole as a bunch of short sections of wire, each having a little inductance, and some capacitance to ground, at least. You might draw that as:

If you continue dividing the antenna into smaller and smaller segments forever, until each segment is infinitesimal and you have infinitely many of these inductors and capacitors, you're getting close to the theoretical model of a transmission line. You just need to add some resistance to account for energy lost to radiation, finite conductivity of the metal making the antenna, and dielectric losses.

While in the LED circuit this level of detail wasn't necessary because it was insignificant, in an antenna it is not so. Remember above when we assumed changes in electric potential propagate instantly across schematic lines? An antenna is explicitly designed for this to be untrue. Real changes only propagate at the speed of light, and antennas are big enough and the frequency high enough that this propagation delay is significant. Consider a half-wave dipole: being a half-wavelength long means any change at one end of the antenna takes a full half cycle before its propagated to the other end. So, the conductors in an antenna are very much not simply lines on a schematic.

## Answer (score 2, by hotpaw2)

You are not considering distance, time, frequency, and the speed of light (or EM propagation) being finite.

If the current flowing into on end (point A) of a segment of wire changes, that change won't occur at the other end of the wire segment (point B) until later in time, due to the finite speed of light between the two points. If it's AC current, then the current will change again at point A before the first change in current reaches point B. So the current flowing in and out of end of each inch/foot/meter of wire in an antenna can be almost always non-equal for any non-zero frequency signal.

Thus KCL won't apply unless the antenna is infinitely small (or close enough given your calculation error bounds), or the frequency is zero (or low enough given your error bounds or measurement resolution, etc.).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17782/does-kirchhoff-s-current-law-kcl-apply-to-antennas, by Kenth Mirta, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
