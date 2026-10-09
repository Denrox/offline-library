# How to choose the right sampling rate and bandwidth for RTL-SDR dongle?

*Tags: software-defined-radio, rtl-sdr, gnuradio · score 8*

## Question

Receiving the frequency of 97.9 MHz

I have a Terratec SDR dongle and I am trying to capture a radio frequency. The FFT window shows the frequency range from -500 to 500 KHz. Is there a way to increase this or it depends on the dongle and is fixed? Does it depend on the sampling rate?

## Accepted answer (score 9, by Marcus Müller)

What the FFT sink shows as frequency axis actually has no basis in "real world signal" – it just takes the sample rate you set (here, you set 1 MHz), and scales the full nyquist bandwidth to that. If you used a different number in the sample rate field of the FFT sink, the spectrum would look absolutely the same, just the frequency axis would have different labels!

It's important to understand that in DSP (and in GNU Radio especially), things are always only handled with respect to samples – e.g. a sine with a period of three samples would have frequency $\frac13$, no unit. The spike on the FFT plot would be at $2 \cdot \frac 13= \frac23$ of the axis (factor of two: your Nyquist zone is from $-\frac{f_\text{sample}}{2}$ to $+\frac{f_\text{sample}}{2}$).

Here's an example to illustrate:

How that $\frac 13$ relates to real world frequencies is defined by the sampling rate of the analog-to-digital (or digital-to-analog, in TX) converter.

So if you need to increase the observed bandwidth, you need to increase the sampling rate at the dongle! They are identical for complex sampling, like the direct-conversion receiver that the RTL dongle is does. For real-valued sampling, your bandwidth is half the sampling rate.

The RTL dongles support multiple sampling rates. You should simply try – for example, 2 MS/s should work with most dongles.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6530/how-to-choose-the-right-sampling-rate-and-bandwidth-for-rtl-sdr-dongle, by Jack, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
