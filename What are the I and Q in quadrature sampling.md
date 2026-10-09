# What are the I and Q in quadrature sampling?

*Tags: direct-conversion · score 9*

## Question

For some reason I've long believed that given I and Q, one corresponds to amplitude, and one to phase, so I thought that I could hold one steady and create AM, or hold the other steady and create FM.

Now that I'm delving more into it, though, it appears I'm completely wrong. Or not. I'm not really sure, and the articles I'm reading aren't helping the situation.

Can AM and FM be demodulated from quadrature signals relatively easily? I feel that if I understand this, I might be able to wrap my head around it.

## Accepted answer (score 8, by Phil Frost - W8II)

Your understanding is almost correct. I/Q data represents phase and amplitude, but in Cartesian coordinates. Conversion between the two is elementary trigonometry:

$$ r = \sqrt{I^2+Q^2} \\ \theta = \text{atan2}(Q, I) $$

To demodulate AM, you just need $r$, and to demodulate FM, you just need $\theta$.

Usually, an I/Q pair is represented as a complex number, with $I$ being the real part, and $Q$ being the imaginary part. This makes possible some interesting mathematical manipulations like multiplying a signal by a complex exponential to make a mixer. However, unlike a usual ("non-complex") mixer, this mixer does not make *two* new signals (sum and difference), but rather *just one*. This ability to shift a spectrum of frequencies without creating an additional sideband (which must then be filtered out, typically) is a big win in DSP.

## Answer (score 4, by Kevin Reid AG6YO)

Quadrature samples are essentially *complex numbers*. Complex numbers can be represented as two real numbers in two equivalent ways:

1. Cartesian form: real (here called I or *in-phase*) and imaginary (here called Q or *quadrature*).
2. Polar form: magnitude (or absolute value) and phase (or angle, or argument).

When you have I and Q signals or samples, those are in Cartesian form. However, when you want to *demodulate*, or even describe mathematically, a complex signal, the magnitude/phase form is more relevant; this is because **the received phase is arbitrary** (unless the transmitter and receiver have perfectly synchronized clocks and mixers and the path length never changes), which means that the signal has an arbitrary phase shift and therefore has no specific relationship with your I and Q "axes".

To help understand this, visualize an *unmodulated* complex (analytic) signal as a helix in 3D space: the axes are I, Q, and time. Unlike a real-valued signal, **there are no zero crossings**; the sample values follow a circle about the origin over time, and never meet it except when the amplitude is 0.

Furthermore, if the signal is *baseband* (after a receiver's mixer or before a transmitter's), then the rotation rate is 0 by definition: your samples have a constant value, except for the effects of the modulation. And this is the condition under which modulation and demodulation are typically done!

You ask for analog demodulation examples:


Demodulating AM from complex samples consists of taking the *magnitude* of the samples (and then subtracting the carrier amplitude from that, or equivalently using a high-pass filter), because that is exactly the amplitude of the original signal.


Demodulating FM from complex samples consists of taking the *difference* between the *phase* of successive samples, because that difference is the instantaneous frequency; if the signal is at baseband, then the instantaneous frequency is exactly the modulating signal!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1038/what-are-the-i-and-q-in-quadrature-sampling, by Adam Davis, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
