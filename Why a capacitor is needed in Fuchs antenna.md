# Why a capacitor is needed in Fuchs antenna?

*Tags: antenna, wire-antenna, end-fed-antenna, transformer, inductor · score 5*

## Question

I tried to understand the physics of Fuchs antenna and there is one thing that I don't quite understand. This is probably a very silly question, but I spent a lot of time looking for an answer (books, online) and didn't manage to find it.

Modern Fuchs antenna looks like this:

The L1,L2 is a transformer, typically 64:1 or 49:1. It is required because the end fed half wave wire has an impedance about 2500..3200 Ohm, assuming a counterpoise wire is about 0.05 lambda. OK, this is clear.

Also the L2,Cv circuit has to resonate on the frequency of interest (e.g. 7.1 Mhz for 40m band). This is the part I don't quite understand. Why using only a transformer is not enough to convert 2500..3200 Ohm to 50 Ohm of the feed line and feed the antenna as a regular dipole? Why we also need a capacitor to form a resonant circuit? Or, in other words, what happens if we remove Cv?

I'm not an expert in antennas or physics. I would appreciate very much if you could explain it like I'm 10 years old.

## Answer (score 3, by Brian K1LI)

It may be simpler to think of the matching network this way:

The high-impedance antenna (in the example, R1 = $3500\Omega$) is connected to a parallel-resonant network consisting of an inductor (L1+L2: note the coupling indicated by the "k1" statement) in parallel with a capacitor (C1). L1 is, in reality, a "tap" on a single inductor comprising (L1+L2). As the "tap" approaches ground - that is, as L1 becomes a smaller part of the total L1+L2 - the impedance presented to the generator (V1) becomes smaller.

This is the impedance presented to the generator vs. frequency:

Judicious selection of components produces the desired match at the operating frequency. Air-spaced and vacuum-variable capacitors are often used to accommodate: the difficulty of knowing the antenna impedance at a particular frequency; the narrow operating bandwidth; the high voltages that come with high-impedance levels. This method, commonly referred to as "voltage feed," is often used with end-fed antennas such as half-squares, etc.

The coupling link, L1, shown in your question is another way to "tap" down on the impedance across L2.

## Answer (score 2, by Ryuji AB1WX)

In the world of an ideal transformer, you wouldn't want that Cv. In fact, that cap would be worse than useless because it’d only get in the way if the antenna wire were perfectly tuned to be a pure resistive load.

But here’s the rub: real-world transformers aren’t ideal. Far from it. Those neat textbook theories? Forget them. A real transformer is plagued with chronic diseases and brain fog, with invisible forces lurking in both its electric and magnetic circuits. If you knew what is concealed behind the neat schematic symbols, you would be afraid to use them.

First off, conventional transformers are notoriously lossy and leaky. A good chunk of the magnetic flux just wanders off, never coupling with the secondary winding. That’s leakage flux, and it makes both ends of the circuit behave inductively.

See 6.1.4: https://www.uni-ruse.bg/disciplines/TE/Lecture%20notes/Lectures%20notes%20Mutually%20coupled%20inductors.pdf

Another good stuff: https://owenduffy.net/blog/?p=22904

You questioned the idea about L2 and Cv needing to resonate at the frequency of interest. That's totally hogwash. What’s really happening is that the transformer’s leakage inductance and Cv are forming an L-match to the antenna wire. Notice that the inductance in action is the leakage inductance, not drawn in the schematic. Not L2.

And yet, you’ll see people nodding along to the wildest explanations—bizarre equivalent circuits and tortured logic that don’t hold up in the real world or in some idealized fantasy. But hey, amateur radio is neither of them.

And this antenna design? Don’t bother. It’s a bad engineering dressed up as simplicity, fooling people into thinking it’s clever. It’s lossy, inefficient, and one of the worst ways to match 50Ω to a high-impedance wire antenna. There are better ways to do this. Use one of those and save yourself the headache.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15020/why-a-capacitor-is-needed-in-fuchs-antenna, by Aleksander Alekseev - R2AUK, Brian K1LI, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
