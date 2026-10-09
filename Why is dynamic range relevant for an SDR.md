# Why is dynamic range relevant for an SDR?

*Tags: software-defined-radio, equipment-design, dynamic-range · score 10*

## Question

Sometimes I see dynamic range mentioned as a figure of merit for an SDR. For example, I know that the [bits per sample](SDR%20sampling%20bandwidth%20-%20do%20the%20bits%20per%20sample%20matter.md) used by the analog to digital converter can affect the dynamic range.

Why do I care about dynamic range? What happens when I don't have enough of it? Can I have too much of it? Does dynamic range have special significance or importance for an SDR compared to a traditional analog receiver?

## Accepted answer (score 10, by Kevin Reid AG6YO)

#### Signal strength and dynamic range

Generally speaking, dynamic range is the ratio between the strongest and weakest signal that can be received. In a digital signal, the dynamic range is determined by the number of bits per sample: the strongest signal is one which uses the full range of the sample values, and the weakest signal is one which uses only two adjacent values (one bit change).

In a software-defined radio, the *analog* signal level fed into the analog-to-digital converter must be adjusted (either manually or by an AGC) to make best use of the available dynamic range:


If the analog signal is too strong, then the logically corresponding digital values are not representable in the numeric range of the samples, and the ADC will substitute the maximum or minimum possible output; this is known as **clipping**, which from a signal processing perspective is an extreme form of nonlinearity.

If you have clipping, it can be observed as the appearance of spurious signals which are copies of actual signals in the received band at different frequencies.


If the analog signal is too weak, then its presence will not manage to make even one bit of difference in the digital output. More practically, well before the one-bit point you will be losing information due to the digital sample values being too coarse-grained to accurately represent the signal. This can be thought of as a source of noise, called **quantization noise**.

The above image shows a sampled (50 samples) and quantized (5 bits) sine wave with different amplitudes, showing each of the above effects. Note in particular how even the relatively nice-looking sine on the left has slightly irregular points (because the sine function's real-number values get rounded to the closest representable value): this is an example of quantization noise.

#### Why dynamic range matters for SDRs

Given the above, it might sound like you can have an AGC that keeps the input signal at just the right level, and not need very much dynamic range.

This would be true, except that in a software-defined radio of the kind we're interested in, **the signal into the ADC is much wider bandwidth than the individual signals we want to demodulate!** This additional bandwidth is what allows you to get the “waterfall” or “panadapter” display characteristic of SDRs (because you're actually digitizing a wide band of RF), but it means that the analog signal coming into our ADC contains lots of RF power which is not any one signal we want to demodulate — it includes a large amount of noise, and possibly many intentional signals, some of which may be very strong compared to the desired signal.

The best analog gain setting is determined by the *total RF power* coming into the ADC (from the tuner and analog filter, if present). This fixes the “strong” end of the scale of possible digital signal levels, leaving the “weak” end determined by dynamic range. Therefore, the more dynamic range we have, the less quantization noise is present in narrow-band signals (which are more or less weak compared to the overall signal), allowing them to be received more clearly.

You can also improve reception with the same dynamic range by using a narrower analog filter, thus reducing the input power and allowing more gain to be applied to it without clipping — if your SDR hardware has a usefully adjustable filter.

The extreme case of using a narrower filter is using one just as wide as a single signal you want to receive. The disadvantage is you don't have any spectrum view while you're doing that — you can only receive that one signal.

#### Direct answers

Why do I care about dynamic range? What happens when I don't have enough of it?

Signals you want to receive disappear into the (quantization) noise floor.

Can I have too much of it?

As a user of a SDR, no, except as it affects the price tag. As a designer, additional sample bits:

- require additional computation (significant for embedded systems; probably moot if you're using a general-purpose machine for your DSP since the samples will likely be expanded into 32-bit integers or floats for computation),
- require a higher-performance (expensive) ADC, and
- may be worthless due to noise received by the antenna (if the electromagnetic noise floor is higher than the quantization noise floor when the gain is set optimally) or noise getting into the system between the gain-control stage and the ADC (the low bits are always noise).

Does dynamic range have special significance or importance for an SDR compared to a traditional analog receiver?

Strictly speaking, no — it is not being software-defined that makes dynamic range matter, but the wide bandwidth. However, if by SDR you mean something with a waterfall display, then yes, it does (as described above).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2475/why-is-dynamic-range-relevant-for-an-sdr, by Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
