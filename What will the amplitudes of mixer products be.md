# What will the *amplitudes* of mixer products be?

*Tags: electronics, theory, mixer · score 8*

## Question

The key fact about mixers, which iirc is even part of the FCC amateur radio exam(s) in the USA, is that they output **"the sum and difference"** of the input frequencies. And iiuc in practice it's usually assumed that besides those products the mixer output will also include both of the original two frequencies as well.

But how is the **power** distributed between all these different outputs? Are the mixer "sum and difference" products quite subtle compared to the original frequencies? Or are the original frequencies basically just leaked a little, while most of the output power being in the sum/difference?

Basically if I put an RF signal of -10 dBm and an LO of 1 dBm, what ballpark should I expect each of the RF, LO, |RF - LO|, and RF + LO frequencies to be in the mixer's output?

While I'm interested in a more generic/conceptual explanation, the context here that finally made me think about amplitude levels rather than just the frequencies was the "offset attenuator" idea used in fox hunting.

Basically if you want to weaken a very strong/close RF signal you can mix it with a 2 or 4 MHz e.g. signal and tune to one of the new frequencies. So instead of listening directly on the actual frequency (say 146.565 MHz) you'd listen up or down by that offset (so 142.565 or 150.565 MHz).

The big benefit of that is explained by http://kc9on.com/ham-radio/fox-hunting/:

The attenuator has a potentiometer to raise or lower the amount of drive going from the oscillator into the diode. This in turn raises or lowers the offset frequency signal level, in cases to almost zero!

Or in a bit more detail at http://homingin.com/joek0ov/offatten.html:

An offset attenuator consists of a local oscillator (LO) connected to a diode mixer through the attenuation control. The higher the LO level, the higher the amplitude of the offset signal applied to the receiver. To increase attenuation, decrease the LO signal into the mixer with the control.

That is, the amplitude of the LO definitely matters since it effects the amplitude of the mixer output frequencies. I'm just wondering what the usual mathematic relationship is between the inputs and outputs **amplitude**-wise, and perhaps how much the type of mixer might play into those ratios too.

## Accepted answer (score 3, by Marcus Müller)

This actually depends on your actual mixer! I go into the math in this answer.

In short: Any amplifier is a mixer, it's just that highly linear amplifiers are bad mixers, and excellent mixers are very non-linear amplifiers. Things get easier when you start to represent the output $f$ of some amplifier, giving it input $x$, as a power series:

$$f(x) = a_0 + a_1 \cdot x^1 + a_2 \cdot x^2 \cdot \, \cdots \, \cdot a_N x^N$$

Your $a_0$ is just the output DC bias. $a_1$ is your linear amplification ($x^1$ being $x$). The relation of that to the other $a_\times$ is what defines the amplitudes of the different intermodulation products.

So, how does one know these? Really depends. Many mixers are meant to just to the first-order intermodulation products of two input tones, so the things at the sum or difference of the input frequencies. They are designed to suppress any $a_{n>2}$, in order to keep the higher order harmonics/intermodulation products out. In that case, the datasheet will tell you things like the third-order intercept point (IIP3) and you can match your power series model to that, and then make a prediction on the amplitudes based on that – works reasonably well for well-behaved mixers, usually.

But some other mixers are working on higher-order intermodulation products. In that case: sometimes the manufacturer supplies measurement curves, or digital models. You will need to torture these a bit to get answers. Also note that two-tone testing/modeling is not always good enough, for broad-band signals. Sometimes, really, measuring with your specific type of signal and LO will be inevitable.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21275/what-will-the-amplitudes-of-mixer-products-be, by natevw - AF7TB, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
