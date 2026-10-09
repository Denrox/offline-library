# How does inductive base loading cause low feedpoint impedance in verticals?

*Tags: impedance, vertical-antenna · score 3*

## Question

As an extreme example, take mobile HF antennas. These can have very low feedpoint impedances, maybe as low as $6\Omega$. The ideal impedance of a quarter/wave vertical is $36\Omega$, but electrically lengthening it makes the impedance go down. How's that work?

## Accepted answer (score 2, by jcoppens)

The ideal $36\Omega$ comes from the fact that a vertical is 1/2 dipole (so 1/2 of $72\Omega$).

If you shorten a dipole (shorter than 1/2$\lambda$, the resistive part of the antenna will lessen, and the antenna will get more capacitive. You could see this on a Smith chart, or from the impedance formulas.

Then, if you eliminate the capacitive part, by adding an inductor in series you get only the resistive part. Remember, a capacitor + inductor in series, at resonance are a short-circuit.

There's a catch though: if the resistive part is so low, the resistance of the inductor (copper!) will start heating up because of the high currents, and you'll loose part of your power through heat, unless you use really thick wire. The same, high, current must also be managed by the ground-plane.

That's also why AM stations, which can only afford a fraction of the tower they'd need, have to use a really effective ground-plane to handle such large currents. ELF stations are build near large - preferably salty - water surfaces to have a reflector able to handle 1000's of A.

This reasoning is slightly simplified to make it clear enough to make it understandable, I hope.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1852/how-does-inductive-base-loading-cause-low-feedpoint-impedance-in-verticals, by Phil Frost - W8II, jcoppens. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
