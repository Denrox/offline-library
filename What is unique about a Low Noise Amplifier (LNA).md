# What is unique about a Low Noise Amplifier (LNA)?

*Tags: electronics, amplifier, lna · score 4*

## Question

What is so special about a low noise amplifier? If I were to design an amplifier, I would always design an amplifier with low noise anyway.

1. Why is it emphasised as being “Low Noise”?
2. What are the design features that makes an amplifier “low noise”?

## Answer (score 5, by Marcus Müller)

If I were to design an amplifier, I would always design an amplifier with low noise anyway.

Nope! For a power amplifier, you'd do a different tradeoff; the noise figure of that amplifier nearly doesn't matter at all, whereas the capability to produce a high output power does very much.

Same goes for other aspects of amplifiers, things like linearity/fidelity, power-efficiency (*immensely* important both in the portable radio as well as in the higher-power regime, since cooling is a hard technical problem)…

Why is it emphasised as being “Low Noise”?

Because, as explained above, the design tradeoffs made for that amplifier led to it being low in noise, rather than power-efficient, powerful-output, low in cost, small, …

What are the design features that makes an amplifier “low noise”?

Good question! That's actually a hard one and it involves more than just the way you connect the components of an amplifier:

Achieving a low noise figure requires your amplifier to be operated in a manner that its input impedance can be *low* (which is unusual for amplifiers, if you think about it), because that means that thermal noise doesn't induce high voltages on the input. This can be achieved via various means – appropriate input resistors, biasing of transistors, feedback mechanisms, carefully matched transistor pairs...

Also, you'll want to have few transistor stages doing the majority of the gain; more transistors will just increase the noise figure, and this being a low-noise amplifier, that's undesirable.

Obviously, that single transistor can't have incredibly high gain – and its gain needs to be especially stable, since there's no supporting circuitry to compensate anything. Also, you'd want the transistor gain to be as high as possible, because the gain of the LNA defines, together with its noise figure, the whole signal chain's noise figure (Friis' Noise Formula; you definitely want to read up on that!)

So, that requires your semiconductor manufacturer to very carefully select the wafer dies that make it into LNAs. As you can imagine, that leads to discarded parts and thus cost – and thus, another reason why not every amplifier is an LNA.

You'll want to design your amplifier circuit so that the central transistor is very robustly biased in a high-gain region of its IO curve; that wastes power, since it implies that

- more than a minimal current is always flowing to keep up that bias
- you're not operating the amplifier close to its maximum output, where it's most effective

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15859/what-is-unique-about-a-low-noise-amplifier-lna, by user5349, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
