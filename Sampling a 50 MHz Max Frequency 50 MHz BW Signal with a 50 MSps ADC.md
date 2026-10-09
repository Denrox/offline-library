# Sampling a 50 MHz Max Frequency 50 MHz BW Signal with a 50 MSps ADC

*Tags: software-defined-radio · score 5*

## Question

I paste below a superhetorodyne based Software Defined Radio Architecture for an Rx channel below.

Suppose the IF signal has a max frequency of 50 MHz and 50 MHz IF BW. In that case, is it possible to just use an ADC of only 50 MSps for sampling process?

According to Nyquist, an ADC should sample at 2X the max frequency of IF. But here, the DDC produces 2× samples once the IQ conversion is completed. So I feel like it fulfills Nyquist criteria before sending IQ samples to the PC/DSP. I.e. After the IQ conversion, the number of samples produced is equal if an ADC of twice the speed were used.

This concept is very clearly proposed in this video (timed to the precise point) https://youtu.be/BK9QkHxeYQI?t=430

I see that this may not be a way of getting around Nyquist but can get away with purchasing a slower ADC by using this method for software defined radio?

I also understand that this way of Super Heterodyne design of a Software Defined Radio hardware can be more difficult and expensive and perhaps also outdated and never used compared to Direct Sampling Method architecture. But I am merely interested in the technicality of this concept.

## Accepted answer (score 3, by Phil Frost - W8II)

In the diagram above, the A/D converter must have a sample rate which is strictly more than twice the maximum frequency output by the RF tuner. So for a 50 MSPS A/D converter, that's a maximum analog frequency up to but not including 25 MHz. In practice it will be less, subject to the limitations of the antialiasing filter implementation.

What follows is irrelevant. Once the signal has been converted to digital real signals the aliasing has already happened and nothing can undo that.

If the mixer was analog, it would then be possible to have two 50 MSPS A/D converters, one for the I channel and one for the Q channel. This would allow an analog input bandwidth of up to but not including 50 MHz, from -25 MHz to 25 MHz. This works because the quadrature shift was accomplished in the analog domain.

## Answer (score 2, by Marcus Müller)

In that case, is it possible to just use an ADC of only 50MSPS for sampling process?

No, for 50 MHz of bandwidth, you'll need 100 MS/s, if we're doing this in real-valued sampling.

This is (one of the, but the dominating) technical reason why for high-bandwidth applications, the superheterodyne receiver architecture like the one you show in your picture is not generally chosen.

Instead, many (not all) SDRs use *direct conversion*, or *quadrature mixing* to *complex baseband*. Equivalent complex baseband is a topic covered in all digital communications textbooks, so I'm not going to elaborate on it much here, but it just shifts the signal instead of to an IF to baseband, i.e. so that it's around 0 Hz, but for that you require then mixing with one cosine and one sine, essentially, and after that, a dual-channel ADC. Advantage is now that it's sufficient to sample at 2× 50 MS/s instead of 1× 100 MS/s.

But here, the DDC produces 2X samples once the IQ conversion is completed.

No, not necessarily. You mix down to complex baseband, and on the way, you can decimate by a factor of 2 without any loss in information.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10263/sampling-a-50-mhz-max-frequency-50-mhz-bw-signal-with-a-50-msps-adc, by Denis, Phil Frost - W8II, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
