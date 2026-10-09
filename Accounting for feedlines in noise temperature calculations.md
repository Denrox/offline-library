# Accounting for feedlines in noise temperature calculations

*Tags: noise, math · score 3*

## Question

In writing an answer to "Use noise figure and gain to calculate weakest signal radio can receive?" I've managed to confuse myself.

I believe this much is true:

$$ T_\text{eq} =T_1 +{T_2 \over G_1} +{T_3 \over G_1 G_2} +\cdots \tag 1$$

So let's say the 2nd component is a 3 dB resistive attenuator at room temperature. Then:

$$ T_\text{eq} =T_1 +{290\:\mathrm K \over G_1} +{T_3 \over G_1\cdot 0.5} +{T_4 \over G_1 \cdot 0.5 \cdot G_3} +\cdots \tag 2$$

OK maybe it wasn't a resistive attenuator exactly, but a feedline with 3 dB loss. So let's make that feedline shorter, so much so that it's lossless:

$$ T_\text{eq} =T_1 +{290\:\mathrm K \over G_1} +{T_3 \over G_1 1} +{T_4 \over G_1\: 1\: G_3} +\cdots \tag 3$$

Couldn't we consider a section of lossless feedline as three cascaded shorter sections of lossless feedline?

$$ T_\text{eq} =T_1 +{290\:\mathrm K \over G_1} +{290\:\mathrm K \over G_1\cdot 1} +{290\:\mathrm K \over G_1\cdot 1 \cdot 1} +{T_5 \over G_1\cdot 1 \cdot 1 \cdot 1} +\cdots \tag 4$$

Wait a minute, as we further divide the feedline, noise approaches infinity!

This can't be right. Where's the error in my reasoning?

## Accepted answer (score 2, by Glenn W9IQ)

The equivalent noise temperature of a passive device, is approximately given as:

$$T_\text{e}=(A-1)T \tag 5$$

where A is the linear attenuation (1/Linear Gain) and T is the physical temperature of the device in Kelvin.

Thus the equivalent noise temperature of a passive device with 3 dB of attenuation at room temperature is: G=0.5, A=2, Te=290 K. This is correctly reflected as the T2 term in equation 2 of the question.

The equivalent noise temperature of a lossless device (G=1, A=1) at any ambient temperature, using equation 5, is 0 K (noiseless). So for the examples in formula 3 of the question, the T3 value should be 0 K, not 290 K as shown. Similarly in formula 4 of the question, T3, T4 and T5 should all be 0 K. The associated terms then drop away.

## Answer (score 2, by Phil Frost - W8II)

The noise temperature for a feedline should be:

$$ T = 290\:\mathrm K\: (A-1) $$

Where $A$ is the ratio of input power to output and will be greater than 1 for any real feedline. For example, a feedline with 2 dB loss has:

$$ A = 10^{2/10} = 1.585 $$

The 290 K term can be replaced with the physical temperature of the line if it is not at room temperature.

This is because only the loss part of the transmission line contributes its thermal noise. Think of it this way:

An attenuator is not typically built as a single series resistor, but from a noise equivalence perspective we can consider it so, with Rattenuator being some value required to achieve the necessary attenuation, which will also depend on the source and load impedances. As the transmission line becomes lossless, Rattenuator approaches zero, and thus so too does the noise.

Rigorous mathematical proofs are given elsewhere (maybe I'll include one here when I get my head around them):

- http://www.reeve.com/Documents/Noise/Reeve_Noise_3_AttenAmpNoise.pdf
- http://www.dtic.mil/dtic/tr/fulltext/u2/265414.pdf (page 33)
- http://www.arcetri.astro.it/~mosca/radioastronomy/corso/node28.html

As an example, consider a transmission line (or any attenuator) at room temperature (290 k) with a loss of 10 dB:

$$ T = 290\:\mathrm K (10^{10/10} - 1) = 2610 \:\mathrm K $$

This seems odd for a passive device to have a noise temperature greater than it's physical temperature, as if it had infinite loss it would be simply a resistor and we'd expect thermal noise to be the only contribution.

But consider, if the receiver sees a noise power equivalent to a resistor at some temperature, but it's actually seeing that through an attenuator, then the original source must have been even noiser. As the attenuation approaches infinity the effective noise temperature must also approach infinity to account for the fact that the source has been attenuated.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9818/accounting-for-feedlines-in-noise-temperature-calculations, by Phil Frost - W8II, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
