# Can a Digital Down Converter, at the same time, generate I,Q streams & Downconvert?

*Tags: software-defined-radio, direct-conversion, superheterodyne · score 4*

## Question

A Digital Down Converter (DDC) is usually used to convert Real Digital Signals at a high frequency to baseband (centered around 0Hz). DDC does this so by producing negative and positive frequencies.

However, **at the same time**, perhaps using an approach as follows, is it possible to **downconvert** a real digital signal present at the DDC as well as **generate the corresponding I,Q** from it? How can we prove that it can be done? (mathematically or by other means)

## Accepted answer (score 4, by Phil Frost - W8II)

One way to convert a real-valued signal into a complex-valued one is to set the complex part to zero. This has the effect of "mirroring" the spectrum: all the negative frequencies are the mirror of the positive frequencies. This can be seen by the Fourier transform property for any real $f(x)$:

$$ \hat f(-\omega) = \overline{ \hat f(\omega) } \tag 1 $$

Here the overline indicates the complex conjugate.

A DDC is usually implemented by multiplying the input by a complex sinusoid to shift the desired signal to 0 Hz, which works due to this Fourier transform pair:

$$ f(x)e^{iax} = \hat f(\omega - a) \tag 2 $$

After shifting the desired signal to 0 Hz, a filter removes out-of-channel interference. Since the negative frequencies that appeared as a consequence of setting the complex part of the real input to zero are removed by a filter, a DDC implemented in this way need not do anything in particular to generate the complex-valued output.

The alternative is for the DDC to operate entirely with real numbers. So rather than calculating $f(x)e^{iax}$ as in equation 2, it calculates $f(x) \cos(ax)$. As with a simple analog mixer the result is output frequencies at the sum and difference frequencies of the input and the LO. One of these image frequencies must then be removed by filtering.

Maintaining precise and stable phase and amplitude relationships between the real and imaginary parts in an analog circuit is difficult. However in digital implementation this is a non-issue, so it's common to see digital processing done almost entirely in the complex domain. As such, in some sense it's *more* work to implement a DDC which does not output complex samples.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10276/can-a-digital-down-converter-at-the-same-time-generate-i-q-streams-downconvert, by Denis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
