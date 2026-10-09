# What exactly is impedance?

*Tags: impedance, antenna-system · score 7*

## Question

I see "impedance" used everywhere.

Equipment has an input and output impedance.  
Antennas and feedlines all have this 'impedance' thing.

For someone that understands DC electronics, Ohm's law and a little bit of complex numbers, what *is* impedance?

## Accepted answer (score 8, by Kevin Reid AG6YO)

**As resistance is to DC circuit analysis, impedance is to AC (or RF) circuit analysis.** Now let's take a closer look at what that means, from several angles. I'm going to not include any of the math, and just state without proof the various concepts' relationships.

1.

In simple, idealized circuit analysis of DC or digital circuits, we often assume that lots of elements are ideal and *have no resistance*, except for things we think of as *loads.* But in reality they do — if you short-circuit a battery, then the universe does not end, both because it only contains a finite amount of energy, and because it and the wire both have some internal, usually undesired, resistance. (Whereas in simulation, if you short-circuit a voltage source the simulator will stop with an error.) Resistance is everywhere.

2.

The big nifty idea in AC analysis is that you can, to a point, use the same formulas you do in DC analysis even though the voltages and currents are changing all the time, as long as they are all sinusoids. But, physically, there is a novel phenomenon which just happens to line up to let the math work.

In a true DC analysis (nothing is changing at all, there is no time), the only way — to speak loosely — the flow of electricity can be affected is to add a resistance, which *converts electrical power into heat.*

In an AC system, because we have voltages and currents that are varying, we have the possibility of inductances and capacitances — collectively, *reactances* — which are both elements which *store energy and release it later*. It works out that this is precisely the same as having a *phase shift* of the sinusoidal waveform. (If we didn't have any reactances in the circuit, then all of the voltages and currents in the circuit would be exactly in phase, and a DC analysis of any given instant would give you the right answer.)

3.

It happens that the math of complex numbers is exactly the right tool to understand reactances; if you generalize resistance (real) to impedance (complex) then an imaginary impedance is a reactance.

This ties into the fact that reactances do not dissipate power as heat — go around in a circle on the complex plane and you have the same magnitude.

4.

As resistance is everywhere, so is reactance.


Deliberately: A second way in which reactance is unlike resistance is that it is *frequency-dependent:* the reactance of a component depends on the applied frequency as well as on its inductance or capacitance. This effect is used to create filters and oscillators — circuits that treat different frequencies differently.


Accidentally: Electrical signals have a propagation time. Therefore, there are delays. Therefore, signals can meet while out of phase, and this is *exactly the same* as if there were deliberately introduced reactances.

5.

Any arrangement of two conductors which carries signals over a significant distance is a *transmission line.* Because there is distance, there is delay, which is more or less the same as inductance. Because there are two conductors, there is capacitance between them. Both of these properties scale proportionally to the length of the line. The way the math works out, if you look at the input (or output) side of the line as if it were a two-terminal circuit element, it turns out to have an impedance which is a positive real number — which, yet, is not a resistance in that it is not dissipative.

 - An inductor stores energy in the magnetic field and releases it later.
 - A capacitor stores energy in the electric field and releases it later.
 - A transmission line *transports* energy and releases it *elsewhere* later.
6.

Now, since an (ideal) transmission line is not dissipating power, we can ask the question: What happens if the circuit on the far end in some way does not itself absorb/dissipate the power? For example, an open circuit, with a resistance of infinity, clearly dissipates no power, and a short circuit, with a resistance of zero, does not either.

What you actually get is a wave reflection — the power comes back out of the input side of the line after a delay. This is generally undesirable because it is not useful, and can also cause damage.

We can imagine that there would also be reflections of lesser magnitude if the properties of the far end are “too much like a short” or “too much like an open”. It turns out that these properties are exactly characterized and summarized by an impedance value. The “sweet spot” of such impedance depends on the design of the transmission line, and is known as the **characteristic impedance** of the line.

If there is no reflection of the signal, then we can conclude that the near side cannot tell when the signal has reached the far side. Therefore the length of the line does not matter. Therefore, the line could be of zero length or infinite length. We conclude that a transmission line of *any length* looks like an impedance whose value is the characteristic impedance — provided that the circuit on the other end has that impedance also.

If the far end is not matched, then the near end will have an impedance which is not the characteristic impedance — but it can be different in any direction on the complex plane, depending on the exact magnitude and phase of the reflection. (This is what a Smith chart illustrates.)

7.

Reflections in an antenna system are undesirable, so outside of specific applications (filtering, dividing/combining, antenna tuners), every component of an antenna system is generally designed to have the same impedance at every *port* (place where a circuit or transmission line meets another — physically, a coaxial or balanced connector).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7456/what-exactly-is-impedance, by Xunie, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
