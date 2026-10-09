# Impedance Matching between RF Amplifier Stages

*Tags: impedance-matching, amplifier · score 7*

## Question

I'm in the process of building a RF buffer-amplifier chain for a VFO and I'm experiencing a design issue trying to impedance match between the sections.

The issue I'm having is that many (most) of the circuit designs documented are characterized with a source or load impedance of 50 ohms. Lets take the following snippet as an example:

Taken from here pg. 520. I've prototyped this buffer amp at 50 MHz and works quite nicely. It gives a gain of just over 3 and a power output of ~12dBm. But, the key point is that all of these characteristics are based on a reflected collector impedance of ~260 ohms and **assume a 50 ohm load**.

Now, I'd like to follow this pre-amplifier with a power amp and many of the examples I'd like to prototype have an impedance transformer at the input. Something like the following is very common:

And again, the amplifier is documented assuming the signal generator at the input has a 50 ohm output impedance.

In my case, I would like to combine these two amplifiers into a pre-amp and power amp chain. The obvious solution is to combine the transformers into a single transformer that presents ~260 ohms to the collector of the pre-amp and ~6 ohms at the base of each power transistor base (in the power amplifier shown T1 is a 4:1 impedance transformer => 50 ohms becomes 12.5 and each base sees half of that).

But, I've lost my fixed 50 ohm impedance. If I combine the transformers I make the collector load of the pre-amp directly dependent on the RF input impedance of the power amp transistors (which is nearly always a complex quantity and is non-trivial to measure).

**So, I'd like to know if there are any "tricks" to pin the inter-stage impedance to a particular value or is there nothing for it but to characterize the input impedance of the power amp?**

## Answer (score 6, by Glenn W9IQ)

There is no need to "pin" an interstage impedance. You may directly transform from the native output impedance of one stage to the native input impedance of the next without going through an intermediate transformation or termination.

When designing an interstage transformer, the general design rule is to ensure that the inductive reactance of each winding is at least 10 times the impedance to which it is connected. This ensures that the transformer winding impedance does not swamp out the attached impedance.

Also take care to think through the transformer topology. Take note that the first circuit uses isolated windings for the output transformer while the second circuit uses an autotransformer at its input stage. The combined impedance transformation will require isolated windings so as to restore a ground referenced output of the previous stage.

## Answer (score 3, by Brian K1LI)

T1 in the "power amp" schematic you provided is a 4:1 step down transformer. Its purpose is to match - that is, maximize power transfer between - the preceding stage and the power amp transistors, whose high impedance is "swamped" by the 10-ohm resistors.

You can match the ~260-ohm driver to the PA by replacing T1 with a 16:1 step down transformer and replacing the 10-ohm resistors with 15-ohm resistors. You might find it simplest to accomplish the higher step down ratio by adding a second "copy" of T1 between the input and T2. Simulation indicates that an inductance of 1-uH should suffice for each of the four windings on T1a and T1b:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12075/impedance-matching-between-rf-amplifier-stages, by Buck8pe, Glenn W9IQ, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
