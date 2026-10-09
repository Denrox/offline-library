# How is the FM-signal demodulated in my receiver?

*Tags: receiver · score 8*

## Question

I've built a radio receiver and I'm wondering how the demodulation works here. I think it's done by T1 and T2 (I've used BC547 instead of BF494, they're quite similar), but I'd like to know more about it. Source: http://www.electroschematics.com/5150/tiny-fm-radio/

## Accepted answer (score 9, by Phil Frost - W8II)

Essentially, it is an FM to AM converter, followed by an AM detector, followed by an audio amplifier.

The heart of this circuit is C1 and L. Together, these make a parallel LC circuit. At resonance, this looks like a very high (for ideal components, infinite) impedance. Away from resonance, the impedance decreases and becomes more inductive or capacitive.

Our circuit will mostly be operating at or very near resonance, so the reactive part of the impedance is negligible. Instead, we can think of the parallel LC circuit as a variable resistor, the resistance of which varies with frequency.

You might see where this is going: if we can design an amplifier and use this LC circuit to set the gain, then changes in frequency change the gain, and thus, the amplitude. Then we'd have an FM to AM converter.

T1 and T2 form that amplifier. Specifically, they are a regenerative circuit. Regenerative circuits use positive feedback to increase gain beyond what would be possible with a single active device. They are very much like oscillators. Like oscillators, they require feedback with a 360° (or equivalently, 0°) phase shift. Unlike an oscillator, we want the gain to be less than 1 (but very close). If it's more than 1, then we have an oscillator and we've actually made a transmitter.

Let's consider what the AC signal from the antenna does to this circuit. When the antenna voltage rises, T2 turns on more, lowering its collector voltage (that's an inversion, or a 180° phase shift). This in turn decreases the base current of T1, increasing T1's collector voltage (another 180°). Thus, these two transistors form a positive-feedback amplifier.

The gain depends on LC. Near resonance, LC is a very high impedance and gain is at a maximum. Away from resonance, LC is a lower impedance and the gain decreases.

This forms an FM -> AM converter: at resonance (tuned to the center frequency of the station) amplitude is at a maximum, and as the carrier deviates away from this center, the amplitude decreases. Other stations are far enough away from resonance that the gain is very low, and they have very little effect on the circuit.

From here on out it works just like an AM radio. The output of the oscillator (taken off the base of T2) can only sink current and not source it: this provides the rectification. That rectification in combination with C2 and R1 forms an envelope detector. IC1 is just an audio amplifier.

And there you have it. A dead-simple, direct-conversion, regenerative FM receiver.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2434/how-is-the-fm-signal-demodulated-in-my-receiver, by Superlimonade, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
