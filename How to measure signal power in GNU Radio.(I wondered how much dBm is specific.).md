# How to measure signal power in GNU Radio.(I wondered how much dBm is specific.)

*Tags: gnuradio · score 4*

## Question

I used the "QT GUI frequency sink" and "WX GUI FFT sink" to measure the signal.

But I got different value. I would like to know what dB stands for in them. Whether it is dBm or just a ratio.

## Accepted answer (score 6, by Marcus Müller)

They don't "measure", they just *display*.

And yes, as you noticed, this is digital signal processing, so there's no physical units involved – the display axes are correctly labeled with "dB", as in "dB relative to an arbitrary reference vector", typically a energy=1 time signal (e.g. $(0,\ldots,0,1,0,\ldots,0)$), or a power=1 signal (e.g. $(1,\ldots,1)$).

So the value displayed by WX and QT only differs by a fixed dB offset; the difference, if I remember correctly, is only the length of the DFT being used as normalizing factor for one, but not the other sink. (By the way, there's historically been a long discussion about what's "right" to use as references. Turns out that's hard to say.)

So, all is relative. If you need physical units, you'll need to calibrate your SDR device with a measurement device that gives you "real world powers" in Watt, dBm, eV/s or whatever.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9260/how-to-measure-signal-power-in-gnu-radio-i-wondered-how-much-dbm-is-specific, by H.Dog, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
