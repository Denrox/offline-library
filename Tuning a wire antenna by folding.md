# Tuning a wire antenna by folding

*Tags: wire-antenna · score 11*

## Question

Last weekend we tuned a quad loop for 80 m and 40 m. Instead of cropping, we folded the isolated wire using cable ties as shown in the picture below.

After folding several quite large sections of the wire, we got the SWR under 1.2, so this approach seems to work. However, I do not understand the theoretical background, because the wire itself has still the same length and because it is isolated there is no electrical contact and the current has to flow over the same distance. Of course, this approach has an influence on the radiation pattern, but I do not see the direct influence on the resonance.

- Why does this have an influence on the standing wave?
- Is the result equivalent to cropping a section of the same length? Can we now just remove the excessive part and solder the wire directly and get the same result?
- Are there any disadvantages of folding instead of cropping, e.g. a lower radiation efficiency?

## Accepted answer (score 11, by Phil Frost - W8II)

Why does this have an influence on the standing wave?

Although there is no electrical connection between the folded sections at DC, that analysis neglects effects that are relevant at RF. Imagine a voltage step initiated at the feedpoint. It's important to consider not just the voltage at some point on the wire, but the fields *around* the wire.

Let's assume this is a dipole: as a positive voltage step is propagating down one half, a negative voltage step is propagating down the other half. *Between* these halves is a changing electrical field.

Furthermore, this voltage step will be accompanied with some change to current as well, and associated with this current is a magnetic field around the wire.

When the wavefront in the field reaches the folded section, the folded back section of the antenna isn't really "isolated" from the rest of the antenna. Indeed, the insulation provides no DC connectivity between the sections, but each wire in the folded section is within these electric and magnetic fields. Through laws like Faraday's law of induction, and more generally Maxwell's equations, these fields mean the components of the folded section interact.

For a simpler case, consider a capacitor. A capacitor is two plates, separated by an insulator. At DC they are isolated, but in any circuit where current or voltage is changing, the interaction of the plates through the electric field becomes relevant.

Is the result equivalent to cropping a section of the same length? Can we now just remove the excessive part and solder the wire directly and get the same result?

Not exactly. Because the wires in the folded section are near each other and thus tightly coupled through their mutual electric and magnetic fields, the wavefront can just propagate over the folded section at the speed of light.

However, that folded section has a different impedance than a plain wire. You might consider each pair of wires a transmission line, which might be open on one end, or shorted. In other words, a stub. The impedance of these stubs might be negligible, depending on the particular folding. But in no case is it strictly correct to say simply cropping the antenna is equivalent.

Are there any disadvantages of folding instead of cropping, e.g. a lower radiation efficiency?

It's very difficult to say. You might look at loading coils and electrically shortened antennas for a more common case where this is a concern. As a very blunt guess, I'd say if the amount of folding is small relative to the overall size of the antenna, losses will be negligible.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7828/tuning-a-wire-antenna-by-folding, by koalo, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
