# Frequency selective surfaces working principle

*Tags: antenna, antenna-theory, antenna-system, frequency, microwave · score 4*

## Question

I've seen that sometimes frequency selective surfaces are used to load a certain impedance to a certain antenna (for instance for input matching purposes).

These surfaces act like a filter on the equivalent transmission line that describes the radiated wave propagation in the space surrounding the antenna.

In this article an incident electromagnetic plane wave on a frequency selective surface made of a periodic sequence of square metal rings is considered.

The authors say:

When the transverse magnetic field faces the vertical strips, it induces current in the loop. This current leads to a secondary magnetic field around the strips, within which magnetic energy is stored. Thus, the vertical strips have an inductive effect.

Well, there are some things I don't understand:

1. How can a time - varying magnetic field induce current in vertical strips and so in the loops? I have always been using the Faraday law in this way: time - varying magnetic flux across a surface => Induced current along the loop that defines that surface.

In this case, the magnetic field does not enter the surfaces of the loops.

1.

Can we say that it's the Electric field of the wave that moves electrons in the vertical strips and causes current to flow?

2.

Next, the article says that the magnetic field surrounds two adjacent vertical strips, like in the following picture:

Is it the magnetic field created by induced currents in the loops?

## Accepted answer (score 1, by OH2FXN)

You had three separate questions there, I'll try to clarify some concepts:

How can a time - varying magnetic field induce current in vertical strips

Faraday's law of induction tells us how much there is electromotive force (a kind of sum of voltages that must be dissipated in the loop) along a conductive loop when a magnetic field passing through that loop changes. However, a varying magnetic field can drive a charged particle in a single wire that is orthogonal to the direction of the magnetic field. In this case, there are moving electrons that act as current. For more explanation, see:  
https://physics.stackexchange.com/questions/211293/does-a-changing-magnetic-field-impart-a-force-on-a-stationary-charged-particle

Can we say that it's the Electric field of the wave that moves electrons in the vertical strips and causes current to flow?

Yes, but that is not the whole story and is not enough to fully explain how the FSS works.

Next, the article says that the magnetic field surrounds two adjacent vertical strips, like in the following picture: -- Is it the magnetic field created by induced currents in the loops?

This graph seems to be a simplified representation of two parallel wires that carry current in the same direction (either directly in or out of your monitor). A single current-carrying wire has a magnetic field that loops around the wire. If you place two wires next to each other, then exactly between these two wires one wire creates a magnetic field pointing up and the other pointing down, causing them to cancel each other out. The authors of the paper use this to illustrate how they calculate the combined inductance of the two parallel wires from adjacent unit cells.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18070/frequency-selective-surfaces-working-principle, by Kinka-Byo, OH2FXN. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
