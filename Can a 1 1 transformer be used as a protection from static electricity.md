# Can a 1:1 transformer be used as a protection from static electricity?

*Tags: dipole, vertical-antenna, transformer · score 10*

## Question

It's well-known that under certain conditions verticals and dipoles can gather static charge, which is a common reason of transceiver damage. There are several ways to solve this issue. Some hams suggest to place a 100 kΩ high-power resistor to the feed point (not an ideal solution, because the charge dissipates slowly). Others suggest to use a coil with inductance about 200 µH instead of the resistor. The inductance works as a short circuit for DC and has little effect (high resistance) on HF.

Here is what surprises me. I don't believe I ever encountered an advice to use a regular 1:1 transformer, nor could I find such an advice online. It isolates the feed line from the antenna and works as a short circuit for DC. This is probably the simplest solution I can think of.

Assuming that power losses in the transformer are acceptable, and that it's placed after 1:1 current balun (which eliminates common-mode current), is there any reason why it might be a poor solution?

## Accepted answer (score 4, by Phil Frost - W8II)

Assuming that power losses in the transformer are acceptable, and that it's placed after 1:1 current balun (which eliminates common-mode current), is there any reason why it might be a poor solution?

Well, the assumption about loss may not be a great assumption to make. It takes a substantial core to avoid saturation and overheating even at modest transmit powers, and then you've necessarily introduced some amount of loss.

Of course designing a suitable transformer isn't impossible, some might not even consider it difficult. It's just costly compared to other solutions, which I suspect is why it's not often recommended.

## Answer (score 11, by tomnexus)

A transformer can help and could also make things worse. I have some bad experience with this.

The way that a radio is damaged by *static* is simple:  
**Something charges up to a high voltage, and then there's a sudden breakdown resulting in a high voltage on the first transistor of the receiver.**

This can happen in a few ways:

1.

A long-wire or monopole type antenna is not grounded, and the radio has a decoupling capacitor before the front-end amplifier. When the antenna charges up to a few hundred volts, the capacitor breaks down and the charge surges into the transistor.

2.

A dipole type antenna is connected with a transformer, where the antenna side of the transformer, and the antenna itself, are not grounded.

3.

Someone already charged, walks up to the antenna and touches it.

In both cases, even if the receiver has an inductor or resistor for DC grounding, it will be damaged because the impulse caused by the breakdown or spark is so fast.

It isolates the feed line from the antenna...

**You can see that there are cases that adding a transformer could actually make things worse**, by isolating a the antenna and allowing it to charge up. Eventually it will jump across the transformer insulation...

... and works as a short circuit for DC.

If there is something isolated that can be charged up, then the DC short on the radio side will mean nothing. The breakdown is an impulse and its initial peak will go right past the DC short.

The solution in cases 1 and 2 is to *prevent anything in or near the antenna from becoming charged up*. This could be done with a resistor or inductor to ground, or by shorting the centre tap of the transformer. Transmission-line transformers are generally DC short throughout, so that solves it completely.

In case 3, someone touching the antenna, the grounding is of limited use. You can add fast limiter diodes to the input - these are widely available, have low capacitance (0.2 pF maybe) and can handle the full current of a human body discharge. They clamp at just a few volts though, so aren't appropriate for transmitting antennas. A bandpass or highpass filter will also help to reduce the energy that reaches the receiver.

None of this is advice about *lightning* protection, though some of it may help a bit in the case of distant lightning.

## Answer (score 4, by vu2nan)

The answer is no.

The best way to protect against static build-up would be to have both antenna elements DC-connected to ground.

This would be automatically ensured with a 1:1 voltage balun.

With a 1:1 current balun, only one element would be DC-connected to ground. Hence a resistor would be required to be connected between the two elements.

With the 1:1 transformer suggested, both the elements would not be DC-connected to ground.

Hence it would offer no protection.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16137/can-a-1-1-transformer-be-used-as-a-protection-from-static-electricity, by Aleksander Alekseev - R2AUK, Phil Frost - W8II, tomnexus, vu2nan. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
