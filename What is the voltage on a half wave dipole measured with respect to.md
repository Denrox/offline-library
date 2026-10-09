# What is the voltage on a half wave dipole measured with respect to?

*Tags: antenna-theory · score 4*

## Question

As I understand, voltage is a measure of the potential difference between two points, and voltage causes current to flow.

I see lots of descriptions on how dipoles work with lots of references to the voltages on the dipole and to the ratio of the voltage of the standing waves on a dipole and along the transmission line etc etc.

Can someone tell what these voltages are measured with respect to ...

... because i'm all confused.

## Accepted answer (score 2, by Phil Frost - W8II)

"Voltage" is anything measured in volts. *Electric potential difference* requires a reference voltage because it's a *difference*.

On the other hand, *electric potential*, which is also measured in volts, is defined at a single point. 1 volt is one joule per coulomb. Increasing the potential of a charged object by 1 volt requires 1 joule of work per coulomb of charge.

The choice of "zero potential" is arbitrary, but for antenna analysis it's usually assumed to be potential at infinity. Assuming the system being analyzed has zero net charge, this is equivalent to defining zero potential as the mean potential of every point in the system.

When discussing antennas, it's usually assumed the quantities discussed are RMS values of a sinusoidal oscillation. So to say "electric potential is zero at the center of a dipole" also means "electric potential at the center of a dipole is unchanging". Which makes sense, because as one side of the dipole is increasing in potential, the other side is decreasing by a similar amount. The center has a potential in the middle of these two extremes, and since each half is changing by equal in magnitude but opposite in sign amounts, the net change is zero at the middle.

It is not electric potential, but electric potential *difference* that relates to current. So that the potential is zero in the middle of the dipole does not mean the charges there don't want to move. At some instant in the antenna's operation, one end of the antenna will be at a positive potential, and the other at a negative potential. All the positive charges in the middle (protons) will try to move towards the negative potential side, while the electrons do the opposite. The electrons are mobile and thus "fall down" the difference in potential like rocks falling down a ramp, and this gives rise to the current in the antenna.

## Answer (score 5, by Kevin Reid AG6YO)

Any voltage can be measured with respect to any reference point you like, because the electric field has a value everywhere. **Some reference points are more useful than others.**

For example, if you put your one of your DC voltmeter probes in some arbitrary point in empty air, the electric charges making up the meter probe, and the impedance of the meter, disturb the measurement so much it looks like there is no effect. But if you held up your probes some distance apart while standing inside an oversized high-voltage capacitor, you'd get a reading — if you didn't cause it to arc over by being there.

(Another example, less relevant but to emphasize the point: there *is* some potential difference between two electric circuits that aren't wired together in any way. However, you can't readily measure it because as soon as you place a voltmeter between them, it discharges through the meter. We call these phenomena “electrostatic”, and in order to detect them you need special ultra-high-impedance electrostatic instruments — or for the difference to be large enough that you touch something and notice the shock of the sudden flow of current that equalizes the charge and potential.)

What reference point to use, in the specific cases you mentioned:

the voltages on the dipole

An ideal dipole is completely symmetric, so a good reference point, and probably the one that any analysis you've seen uses, is the center of the dipole.

the voltage … along the transmission line

Common transmission lines have two conductors; the voltage of interest is the voltage between those two conductors at some position along the line. (Other transmission lines are *waveguides*, which carry electromagnetic waves inside or outside a single conductor. In this case, there is still a potential difference but it is in the propagating electric field that is guided by the waveguide.)

If you want to relate the potential at a point on an antenna to a point on its feed line, then you have to take into account how the antenna is connected to the feed line — what matching devices are used at that interconnection — and also how the feed line is physically located (it is, after all, metal in the presence of an electromagnetic wave); there is no simple single answer.

## Answer (score 4, by Brian K1LI)

For ease of analysis, the voltages impressed on the feedpoint terminals of a dipole by a two-conductor transmission line are referred to a theoretical plane at the midpoint of the terminals, that plane representing a virtual ground. That is, rather than using one terminal as the "common" point against which the other terminal varies sinusoidally from 0 to V, the two terminals vary from +V/2 to -V/2 in opposite polarity when referred to the mid-plane.

This symmetry is obvious for a balanced feedline and a "T" match, the symmetrical version of the gamma match. The gamma match, about which you asked in an earlier post, is an asymmetric (or, in antenna parlance, "unbalanced") matching technique that exploits the asymmetric nature of a coaxial feedline by connecting the shield of the coax to the midplane.

The solutions to Maxwell's equations for the electromagnetic fields around the dipole require that equal and opposite currents flow on both sides of the dipole, restoring the "balanced" behavior we observe.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12131/what-is-the-voltage-on-a-half-wave-dipole-measured-with-respect-to, by Andrew, Phil Frost - W8II, Kevin Reid AG6YO, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
