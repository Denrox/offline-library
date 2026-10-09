# Does the waveform of the VFO necessarily have to be sinusoidal?

*Tags: equipment-design, oscillator, vfo · score 6*

## Question

Looking around for a VFO online, I see most kits/manufacturers make it a point to mention the waveform. Sinusoidal is a fundamental shape, whereas others (sawtooth, square) are a composite.

I recall reading online (can't remember where it was) that a VFO with a composite waveform is actually better than one with a pure sinusoid.

- Does the VFO signal necessarily have to be a sinusoid?
- Does the remark about a VFO with a composite signal ring true?

## Accepted answer (score 2, by Phil Frost - W8II)

Does the VFO signal necessarily have to be a sinusoid?

Absolutely not. For each frequency component on a mixer's inputs, it produces at the output the sum and difference of those frequency components. Of course, if one of the inputs is sinusoidal, then it has just one frequency component. However, if there are more frequency components it still works.

Does the remark about a VFO with a composite signal ring true?

Sure. Joseph Fourier proved that any periodic function can be decomposed into a (possibly infinite) number of sinusoidal components, each with some amplitude and phase.

For example, a square wave consists of some fundamental frequency, plus all its odd harmonics. A sawtooth wave has even and odd harmonics. Each of these harmonics will generate mixing products, just as if you fed in a sine wave at that harmonic frequency. This can be used to an advantage in some designs, as long as the filtering is such that the mixing products from the other harmonics don't cause issues.

## Answer (score 2, by jcoppens)

A small extra bit of information... Even though many VFO circuit descriptions, as you say, make it a point mentioning the 'cleanliness', by far most mixer circuits then proceed to convert the sine wave into something horrible :)

Mixers, in order to function as such, must be non-linear. Ideally, they should multiply both input signals, and produce neat sum and difference frequencies. In practice however, most mixers only approximate that behavior. An extreme example, is the digital mixer which just inverts the input signal (using analog switches) at the pace of a digital signal (the VFO).

As Phil told you, many harmonics are present, so it's up to the designer to include the necessary tricks to avoid those extra frequencies having a bad effect.

More important than the harmonic content of the VFO, is something more difficult to measure. As most analog sine oscillators use amplifiers (transistors or integrated circuits) to oscillate, thermal effects in those semiconductors introduce modulation onto the carrier frequency. This makes the VFO not generate one clear sine, but rather an AM and FM modulated one. Depending on many factors, the Q factor of the resonator being probably the most important one, this noise can cause much more problems than harmonics.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1887/does-the-waveform-of-the-vfo-necessarily-have-to-be-sinusoidal, by VU2NHW, Phil Frost - W8II, jcoppens. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
