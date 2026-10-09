# What is antenna reactance?

*Tags: impedance-matching · score 4*

## Question

I have a V5000 antenna and I’m tuning it but can’t get the Reactance (X) on my MFJ 259B down. Resistance is at 50 ohms, SWR reading 1.2 to 1.3 (I don’t give that much credence) but the Reactance (X) is around 15. Any ideas how to get that down? LMR 400 coax if it matters.

That's what I'm still trying to get a grip on! From what I've been told it has to do with the capacitance of the antenna which is affected by the proximity of the driven element to ground plane radials or whatever your ground plane is. I'm still figuring that one out!

## Answer (score 8, by Phil Frost - W8II)

Reactance is the imaginary part of impedance. Together with the real part, resistance, impedance describes how a given load will respond to an AC voltage or current source. While for DC analysis resistance alone is sufficient for this purpose, for AC analysis we need to know not only the magnitude of the voltage or current, but the phase angle between them, which is given by:

$$ \theta = \tan^{-1}\left( X \over R \right) $$

Inductors and capacitors are examples of discrete components that have reactance but no resistance. In an antenna, the reactance comes from the timing of the wave reflected from the ends of the antenna. At some length, the reflections align such that voltage and current are in phase at the feedpoint terminals, which means reactance is zero, and the antenna is said to be resonant.

I should note there's no particular reason reactance needs to be zero. An SWR of 1.3 is perfectly acceptable, and there's likely no practical performance gain to be realized by reducing it further. Furthermore, reactance will be zero only at one particular frequency (and likely harmonics thereof) but it is impossible for the SWR to be 1:1 or for the reactance to be zero across the entire band.

However if you want to get reactance to zero you can do that by adjusting the length of the antenna or whatever other mechanisms your antenna has for tuning it. If you have an antenna analyzer then measure the reactance over a range of frequencies:

- A little below the resonant frequency, the antenna is "too short" and reactance will be negative.
- A little above the resonant frequency, the antenna is "too long" and reactance will be positive.
- Precisely at the resonant frequency, reactance will be zero.

If you get very far away from the resonant frequency these rules will not hold, but you would not ordinarily operate an antenna this far away from resonance.

Make the necessary adjustments to your antenna and repeat your measurements until you have the resonant frequency where you want it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17752/what-is-antenna-reactance, by booksbenji, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
