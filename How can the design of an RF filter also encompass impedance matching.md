# How can the design of an RF filter also encompass impedance matching?

*Tags: equipment-design, filter, impedance-matching · score 6*

## Question

I'm installing an antenna which will require a matching network. (A fixed network: the load will not change.)

I'm also building some low-pass filters to reduce transmitted harmonics.

It would be a simple exercise to design an ordinary 50Ω filter through normalized tables (which assume equal input and output impedances), and follow that with a matching network. Maybe a pair of inductors or capacitors can be combined, but not much is saved. Furthermore the characteristic of the filter is perturbed, as the reactance of the matching network will change over frequency in a way which was not considered in the filter design.

But I wonder: is there a more intelligent way to design a filter for unequal input and output impedances? Perhaps a way which involves fewer components, or affords additional design flexibility, for example to steer component values to standard values, or minimize loss? How?

## Answer (score 2, by Marcus Müller)

So, to answer your: "Is it possible?" question: yes.

Yes, and in fact, it's more inevitable than possible!

As you know, one of the major challenges in RF design is that not only do you need to match components and transmission lines at a single frequency (or wavelength, depending on how you look at it), but usually across a whole bandwidth! Generally, the larger that bandwidth becomes, the harder it is to sustain a good match.

Now, what happens outside that bandwidth where you've successfully matched? Right, signal energy gets reflected at the impedance discontinuity, and hence, doesn't "move forward" through the signal chain.

That's *exactly* what a filter is!

In fact, any passive filter can be understood as frequency-selective matching network. Consider the simple RC low-pass: at low frequencies, its complex impedance is very much dominated by the real-valued resistance, but as soon as you get close to the the cutoff frequency, you see the phase of transmission increase – which reflects the fact that the imaginary part of the impedance now reaches the magnitude of the real part. From the (hopefully) purely real-valued wave impedance of the transmission line, you now see a complex impedance, not even with the same absolute value. You get reflections (which basically means you get higher SWR).

So what one can do here: Read about the problems of making high-bandwidth matching circuits, and just do *the opposite* to get a filter.

Or really, just design a filter whose impedance at passband works to match in- to output :) The RC example actually works pretty nicely here: you actually have two degrees of freedom when designing an RC filter, one is the resistance, and the second the capacitance; as the we assume that $f_c = \frac1{2\pi RC}$ is fixed, you'll find that actually, you can't just pick any capacitance – the ratio of $R$ to $C$ is fixed by that requirement!

Thus, pick your $R$ so that at the frequencies you want to pass, your complex impedance is usable as matcher.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9893/how-can-the-design-of-an-rf-filter-also-encompass-impedance-matching, by Phil Frost - W8II, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
