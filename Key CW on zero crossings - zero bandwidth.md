# Key CW on zero crossings - zero bandwidth?

*Tags: cw, theory, bandwidth · score 11*

## Question

I remember being surprised to learn that a CW signal has a bandwidth (albeit small), but when I thought it over, it made sense. Essentially, we are modulating the carrier with a low frequency square wave. This would explain key clicks: a perfect square wave has infinite bandwidth, but if you smooth the rising and falling edges, the bandwidth goes down.

This got me thinking. If, theoretically, we could key up and key down precisely on the zero-crossings of the carrier, it seems to me that there would not be any distinct rising or falling edge. Then, would the signal have zero bandwidth?

(I haven't the slightest idea whether this would be practical in practice. I have to assume either a) it's not or b) I'm wrong about this theory, because otherwise I'm sure transmitters would already do this.)

## Accepted answer (score 7, by Glenn W9IQ)

You raise an excellent question and your thought processes are indeed on the right track.

First some background. An ideal, uninterrupted sinusoidal carrier has zero bandwidth. Real world factors such as phase noise, amplifier distortion, etc. produce a measurable bandwidth of the carrier. When the carrier is keyed on and off as it is with Morse code, this is a special form of ASK (Amplitude Shift Keying) called OOK (On Off Keying) as it is discussed in professional literature. Normally, the bandwidth of the modulated OOK signal is minimized when the keying waveform rise and fall times take on a Gaussian or raised cosine form. Most amateur radio transceivers are using simpler RC filtering to shape the keying waveform, resulting in less than ideal bandwidth but at least avoiding the key clicks from the otherwise sharp raise and fall time of the modulating signal. In any case, it is the rise and fall shape of the keying waveform that determines the bandwidth of the modulated signal.

When the transition of the modulating signal is synchronized with the zero crossing of the carrier signal, this is known as *coherent OOK modulation*. This is, of course, much more difficult to implement than a simple, non-coherent RC filtering scheme so it is not commonly seen in amateur radio applications. However, when implemented properly coherent OOK does reduce, but does not eliminate, the signal bandwidth. The "residual" bandwidth is largely due to a variety of real world factors including non-instantaneous keying time which introduces a distortion of the carrier waveform. Any distortion, no matter how small, of the sinusoidal carrier will result in a non-zero bandwidth.

[EDIT] Even with ideal zero crossing switching and ideal amplification, there will be minor sidebands but these will roll off as a function of frequency at a significantly greater rate than switching at non-zero points. With zero crossing switching, however, non-linear amplification present in most CW transmitters will likely introduce greater side band components than those caused by zero crossing switching. [/EDIT]

So you could win over some of the CW aficionados with a coherent OOK transmitter but in a hobby market the commercial viability of such a transmitter would be a question of price elasticity. Perhaps in this new era of DSP based radios, the lowered cost of implementation will make this commercially viable. But given that few, such as the Elecraft K3, amateur radio transceivers implement Gaussian keying, we still have a ways to go to optimize the bandwidth of our CW signals.

## Answer (score 4, by Phil Frost - W8II)

There is no way to transmit information in a signal with zero bandwidth. Switching the carrier at the zero crossings would reduce bandwidth but not take it to zero.

There's a mathematical explanation on DSP StackExchange: Does “keying on” a sine wave at a zero-crossing reduce its bandwidth? Summary: in the worst case of switching on/off at the peak instantaneous amplitude, the sidebands fall off in proportion to 1/f. In the best case of switching at zero crossings, the proportion is 1/f. A significant improvement, but still far from zero bandwidth!

Without delving into math, the simple explanation is that a band-limited signal must not only be continuous itself, but so too must be its derivatives. A hard switch at a zero crossing has a discontinuity in the first derivative at the switching point.

For having smooth derivatives, the Gaussian function is a limiting case because the derivative of a Gaussian function is another Gaussian. The Gaussian function comes up in the central limit theorem for similar reasons.

It's generally true that resolving something precisely in the time domain requires a wide bandwidth and vice-versa, and the Gaussian function is a "middle ground" which maximizes the rise and fall times while minimizing sidebands to the extent mathematically possible. This is because the Fourier transform of a Gaussian is a Gaussian. So in this sense, the minimal bandwidth keying envelope for CW would be a Gaussian function.

## Answer (score 2, by Bill)

The "Coherent CW" folks use something similar.

Very slow CW is keyed at zero crossings with Raised Cosine envelope to give minimal bandwidth.

But yeah, it's the rise and fall times which gives key-clicks, not whether it's keyed at zero crossings or not

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9436/key-cw-on-zero-crossings-zero-bandwidth, by Dominick Pastore, Glenn W9IQ, Phil Frost - W8II, Bill. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
