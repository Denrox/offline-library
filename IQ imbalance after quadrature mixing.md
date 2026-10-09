# IQ imbalance after quadrature mixing

*Tags: software-defined-radio, receiver, transverter · score 9*

## Question

What is IQ imbalance in the output of complex or quadrature downconverter/demodulator/mixer? What are the causes and effects of IQ imbalance? (A spike in the spectrum display of RF noise?) Are there any SDR algorithms for reducing the negative effects (if any) of IQ imbalance in a digitized complex or IQ signal before further signal detection or demodulation?

## Answer (score 6, by Phil Frost - W8II)

A quadrature mixer contains two signal paths, I and Q. For a sinusoidal input into the mixer, the outputs will be in quadrature. It's this property that allows a quadrature mixer to distinguish between frequencies above and below the LO.

Discarding one of the I or Q components still works as a mixer, but input frequencies above and below the LO become indistinguishable. For example if the LO is set to 10 MHz, and the output of the mixer shows a signal at 100 kHz, it's unknown if the original signal is at 10.1 MHz or 9.9 MHz.

For the isolation between negative and positive frequencies to be complete, the I and Q components must have equal gain and quadrature phase. When this is not the case, images of the input signal appear at the mixer output.

Imbalance between the I and Q components comes from component variation, a result of manufacturing processes, temperature, and aging. For example, variance in resistance may result in one component having higher gain than the other. Variations in capacitance or inductance may result in unequal, frequency dependent phase delay.

Correction involves finding the best phase and magnitude coefficients to minimize images. If a test input of a single tone can be applied this is pretty easy. If a test input signal is not possible, then the positive frequencies can be compared with the reversed negative frequencies and the coefficient adjusted to minimize their correlation. See https://github.com/osmocom/gr-iqbal for an example.

## Answer (score 4, by sm5bsz)

IQ imbalance causes a spur at the mirror image frequency:-( If your LO is at 7.050 MHz a signal at 7.040 MHz will show up as an image spur at 7.060 MHz and a signal at 7.060 MHz will show up as a spur at 7.040 MHz.

IQ imbalance is caused by various imperfections in the hardware. I and Q are obtained from mixing the input RF signal with two versions of a LO signal that are 90 degrees out of phase. There are two problems. The mixers and subsequent amplifiers differ in gain. Typically something like 0.5%. Depending on hardware the phase might differ. For two reasons. The 90 degree phase shift between I and Q might have a (small) time shift and also there might be an anti-alias filter in the channels that could give a slightly different phase shift at the high end of the frequency range.

In modern hardware, like the Airspy HF+, the main problem is the amplitude imbalance. This means that the I/Q imbalance can be eliminated just by computing the correlation between the signal at a frequency F and the signal at its mirror image. The correlation gives a complex coefficient that can be applied to the signal to eliminate the mirror image. This is implemented in the HF+ drive routine. It works well just because the I/Q imbalance is not much depending on the frequency. (In the HF+ the evaluation of correlation puts an extra weight on the frequency one is currently tuned to.)

Linrad uses a very different strategy. That is because it was originally developed for the WSE converters that have VERY sharp anti-alias filters and an IQ imbalance that changes rapidly with frequency. The user is required to run a calibration procedure.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10246/iq-imbalance-after-quadrature-mixing, by hotpaw2, Phil Frost - W8II, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
