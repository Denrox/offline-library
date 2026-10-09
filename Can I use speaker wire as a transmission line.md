# Can I use speaker wire as a transmission line?

*Tags: transmission-line · score 4*

## Question

Speaker wire is really cheap and available everywhere, and it doesn't seem that different to 300 ohm twin lead. It seems to me it would make an excellent balanced transmission line.

What would the approximate impedance and loss be? Can I use a balun / matching transformer at the radio end and then tune the antenna to the speaker wire impedance?

## Accepted answer (score 17, by Kevin Reid AG6YO)

I can think of a reason expect this not to work very well. The impedance of twin-lead transmission line is dependent on the *ratio between*

- the diameter of the conductors, and
- the distance between their centers.

In twin-lead or any parallel-conductor transmission line, the insulation is designed to keep that distance stable. On the other hand, in speaker wire, the insulation is usually quite soft, and a small amount (<1 mm) of incidental squishing of the cable will quite significantly change the distance between the conductors, and thus the impedance.

But, that's a *theoretical* answer, on why we don't in general use cheap speaker wire or lamp-cord for transmission lines. What about in practice?

Well, I've got a piece of speaker wire handy (30 ft or so, 16 AWG). I unplugged it from my speaker and plugged it into a resistance decade box and my antenna analyzer, and made some measurements. Impedance, 0-30 MHz:

So, an adequate piece of transmission line around 110 Ω.

Does it have obvious impedance discontinuities measured in my analyzer's "TDR" mode?

Not very much! (The spike on the left end is the connection to the analyzer, and the wiggle on the right is the connection to the termination.)

I'd guess that the practical reasons not to use speaker wire are:

- It's not a standard impedance, so you'd need matching on both ends
- Any *particular* product might have a different impedance
- It's not coax, so you have to treat it like any twin-lead and keep it away from other things, but people generally prefer coax unless they're building a high-performance HF station, at which point why use the cheap stuff?

## Answer (score 8, by hobbs - KC2G)

It depends substantially on the particular speaker wire — available gauges range from 14-2 to 22-2, insulation materials and spacing vary, and the impedance is probably somewhere between 80 and 150 ohms, depending. The loss will be worse than 300-ohm ladder line because of the lower impedance (meaning higher current for a given power), because speaker wire has a higher "fill factor" (percentage of the space between conductors occupied by insulator rather than air), and because the insulator is usually PVC (which is much lossier than PE or PTFE), and will probably be on a par with very cheap coax.

But since there's no standardization for this stuff in terms of its RF properties, you can't really tell what you'll get from a particular roll without buying it and measuring it. It's probably fine for a "whatever dipole" but not for any design that requires careful impedance matching.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20939/can-i-use-speaker-wire-as-a-transmission-line, by Andrew, Kevin Reid AG6YO, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
