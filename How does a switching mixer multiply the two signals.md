# How does a switching mixer multiply the two signals?

*Tags: theory, electronics, mixer · score 10*

## Question

I understand what a mixer does, and when I see it in a block diagram it's obvious what purpose it serves and how it fits in the overall design of the radio.

However, when I look at the schematics and see how it's created, I don't understand how it works.

For the purposes of this question, I'm referring to only a switching mixer:

How does switching between the RF and the inverted RF at the LO frequency accomplish $RF \cdot LO$?

## Accepted answer (score 8, by Phil Frost - W8II)

Switching to the inverted signal is equivalent to multiplying by -1. While in an ideal mixer, the RF input can be multiplied by a sinusoidal LO, the switching mixer multiplies by a square LO.

It still works as any mixer would. That is, for each frequency component in the first input $f_1$, and each frequency component in the second input $f_2$, it produces at the output frequency components $f_1 + f_2$ and $f_1 - f_2$.

However, because the LO input must be a square wave (if it's not, the gain of the switching mixer's LO input will make it so), the frequency components of that input are the LO frequency, plus all its odd harmonics. These must be removed with filtering somewhere up or down the line to avoid undesired mixing products. The advantage is that frequently it's easier to make a good switching mixer with a good filter than it is to make an ideal mixer that produces exactly $RF\cdot LO$ for arbitrary inputs.

Here's a related question on Electrical Engineering.SE: Can I input a square wave LO into a mixer?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1363/how-does-a-switching-mixer-multiply-the-two-signals, by Adam Davis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
