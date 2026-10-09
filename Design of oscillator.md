# Design of oscillator

*Tags: electronics, oscillator · score 5*

## Question

I'm looking for a good tutorial about oscillator design (electronically) for transmitter. The problems with current tutorials are almost all provide only schematics, some explain how it works. But noone show how we determine the transistor (select beta, or frequency range), determine resistor values (bias voltage and output modulation voltage), or capacitor values, etc. It is so hard to experiment and learn by myself about transmitter.

Not to mention about next stage amplifier, how sound added to the signal, and how filter works (I heard for x'tall filter, we should select x'talls with the closest frequency as possible. But why, I don't know. No need to answer this.). Basically, not practical thus cannot learn in depth.

## Answer (score 6, by Aleksander Alekseev - R2AUK)

I would like to applaud your interest not only for homemade transmitters but also a theory! I started to build my own receivers and transmitters not a long time ago and completely understand how frustrating it can be at the beginning.

However this is a broad and complicated topic. If we consider only oscillators for transmitters, there are LC oscillators - Clapp, Colpits, Hartley, and several other, crystal oscillators, various types of VFOs, also PLLs, DDSs, you name it. People write not a single tutorial but **books** on this subject.

OK I can give you a simple VXO schematic that I used in a CW transmitter not a long time ago:

This is a so-called Super VXO. Q2 is a buffer, Q1 and all the left part is an oscillator. How does it work? OK basically it's a Clapp crystal oscillator, but a crystal is de-Q'ed with a second crystal and also L1 and VC1. What brings a question like "what is Q", "what I need a buffer for", "what are R5 and C3 for", also about oscillator stability, amplification (it's output is only 4 dBm, now what is dBm and how much of it do I need...), filtering, keying, and Barkhausen criterion. If you are interested in this particular schematic here is a tutorial. It's in Russian, but Google Translate should help.

However the goal was to show how a simple schematic creates more and more questions, which create even more questions, and this is why it's impossible just to write a simple tutorial on oscillators.

Here are several books that helped me a lot:

1. **ARRL Handbook**. Consider it a starting point with a list of your future projects and references to further reading.
2. **Hands-On Radio Experiments**, vol 1, 2 and 3. Ditto. Vol 1 is especially worth reading.
3. **Practical Electronics for Inventors, 4th Edition**. Good source of information on various topics, not excluding oscillators and filters. Especially filters.
4. **Amateur Radio Transceiver Performance Testing**. This one explains in great detail what are IMD, MDS, etc and how to measure them. You will need this.
5. **Solid State Design for the Radio Amateur**. It's not new, circa 1977. But it explains many things well, mixers especially. The good thing about SSD is that it's available for free.
6. **Experimental Methods in RF Design**. The newer book by the authors of SSD. It's great but I wouldn't recommend to start from it. Some context is required for better understanding.

My advice would be to read at least (1), (5) and (6), but better - all of them. Start with simple projects. Build an attenuator or a 50 Ohm dummy load. Measure them. You will need both to test your transmitter. Then build a simple LC oscillator. Measure it. Is it stable? Why not? Build a crystal oscillator. Is it better? Is it possible to make the frequency adjustable? How clean is an output signal? Is it possible to clean it up? Build a filter. Is it any good? Did it help?

In other words proceed one little step after another. And soon you will be on the air with your first QRP rig. 73s de R2AUK

## Answer (score 2, by Brian K1LI)

I find these *Electronics Tutorials* on Oscillators to be very instructive. *LTSpice*, the free electronic simulator from Analog Devices, includes example circuits for Clapp, Colpitts and Hartley oscillators. Perturbing the values of the example circuits' elements can help you develop a fuller understanding of how each affects the oscillators' performance parameters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17253/design-of-oscillator, by RainerJ, Aleksander Alekseev - R2AUK, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
