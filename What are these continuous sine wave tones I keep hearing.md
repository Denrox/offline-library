# What are these continuous sine wave tones I keep hearing?

*Tags: hf, frequency, noise · score 9*

## Question

I'm messing around on WebSDR and by just scanning through I sometimes come across these continuous tones in USB. One in particular was 28.800 MHz USB.

I've picked them up on nearly every WebSDR unit I've used. This one in particular was the most recent.

It seems weird that an entire frequency would be occupied by a single tone. Is this a coded tone of some kind? It doesn't sound like it modulates at all. Maybe its for testing the tuning of your gear?

## Accepted answer (score 17, by Kevin Reid AG6YO)

A pure tone is an unmodulated signal — it carries no data. Almost nobody intentionally transmits a pure tone — it would be wasteful. The exceptions are the time-and-frequency reference signals like WWV, but they have modulated time information in addition to the carrier which serves as a frequency reference signal.

What you are receiving is almost certainly *unintentional* transmission. Any oscillator, or clock in the digital-electronics sense, usually ends up radiating some of its output through the attached circuitry. Particularly when the oscillator is inside the receiving equipment, it is known as a “spur” or “birdie”.

The popular RTL-SDR has a 28.8 MHz oscillator inside, so you will see a signal there (and at harmonics (multiples) of that frequency) if the WebSDR you were using is based on that hardware.

Other unintentional transmissions may be more complex than pure tones, either because they are intentionally modulated signals intended to pass through cables (e.g. USB) or because they are controlled or perturbed in some fashion (e.g. switching power supplies under varying load).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9771/what-are-these-continuous-sine-wave-tones-i-keep-hearing, by Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
