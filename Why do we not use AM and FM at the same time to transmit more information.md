# Why do we not use AM and FM at the same time to transmit more information?

*Tags: fm, am · score 17*

## Question

Amplitude modulation uses the modulation of the amplitude of a carrier wave to transmit data while leaving the carrier frequency constant, and in the case of FM it's just the other way round.

Why is a modulation of the frequency in an AM signal not used to transmit additional information, e.g. two audio channels or RDS information?

## Accepted answer (score 16, by Mike Playle)

QAM modulates both the phase (= frequency) and amplitude of the signal.

## Answer (score 14, by Brian K1LI)

It turns out that we *DO* simultaneously use frequency and amplitude modulation: our everyday term for this is "single sideband." As described on Wikipedia, single-sideband is a special case of quadrature modulation in which the quadrature component (Q) is derived directly from the in-phase component (I) of the modulating signal.

This effect becomes evident upon examination of the waveform of an SSB signal produced by modulating tones of 700Hz and 1900Hz:

Note that the period of the envelope is 833$\mu$s, a frequency of 1200Hz, which is the difference between the frequencies of the two modulating tones. At the "cusp" of the waveform, it experiences a 180-degree phase reversal, whose accurate reproduction is essential to a clean output. The mathematical combination of these amplitude and phase modulation components produces the two tones that are offset from the frequency of the carrier wave.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12113/why-do-we-not-use-am-and-fm-at-the-same-time-to-transmit-more-information, by DK2AX, Mike Playle, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
