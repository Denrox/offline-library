# What is IQ in the context of SDRs?

*Tags: software-defined-radio, jargon · score 5*

## Question

What is IQ, in the context of software-defined radios (SDRs)?

## Accepted answer (score 7, by Phil Frost - W8II)

"IQ" refers to the practice of having two mixers with their oscillator phase 90 degrees apart, and then the digitization and processing of those two streams of data.

One practical problem is in a superheterodyne receiver, the LO must be selected and the filters designed for the best image response.

The problem can be understood intuitively like this: say there is a spinning disk, with a mark on its diameter. The disk is spinning so quickly it's a blur, but you can use a strobeoscope to observe it. You know approximately how fast the disk is spinning, and you set the strobeoscope to this frequency. It will then appear the disk is spinning slowly, with the speed corresponding to the difference in speed between the strobeoscope and the disk. Depending on the direction of spin, you can tell if the disk is spinning faster or slower than the strobescope.

If you separate the horizontal and vertical positions of the mark into functions, you will find they are the trigonometric functions $\sin()$ and $\cos()$, which are the same function but 90 degrees apart:

The problem is a single RF mixer operates like a stroboscope that only gives you the position of the mark in one dimension. With just one dimension you can tell the difference in speed, but you can't tell if that difference is positive or negative.

The mathematics of how this works is elegantly expressed in Euler's formula:

$$ e^{ix} = \cos x + i \sin x $$

It turns out this is really useful. The reason a frequency mixer has sum and difference frequency products is because

$$ \cos(x) = \cos(-x) $$

But if we allow the calculations to have complex values we can write signals not like this:

$$ s(t) = \cos(\omega t) $$

but instead like this:

$$ s(t) = e^{i \omega t} $$

and because

$$ e^{ix} \ne e^{-ix} $$

we no longer have that pesky issue of dealing with images at every mixing stage.

In analog hardware this is implemented by having two mixers. They each get the same RF signal, but their local oscillators are 90 degrees out of phase. This means one mixer (call it $I$) produces the $\cos$ component in Euler's formula, and the other mixer ($Q$) produces the $\sin$ component. After these signals have been digitized we can treat each pair of samples and the real and imaginary part of a complex number, and then go on processing them as if it's a single, complex-valued signal.

It turns out complex numbers show up in all kinds of DSP math. For example, the discrete Fourier transform (DFT) can be thought of as calculating the correlation of the input with a $\sin$ and a $\cos$ function at each bin. That means with Euler's formula we can consider the DFT to operate on complex numbers.

Also, many demodulation algorithms will involve shifting things up and down in frequency, and in the digital domain, just like the analog domain, if we do this only with real numbers then we have to be concerned with rejecting image frequencies at every step.

These are just a few examples. The point is generally IQ processing simplifies both the analog and digital implementations of an SDR.

## Answer (score 5, by Marcus Müller)

To just answer the literal question:

**I** stands for *Inphase* and **Q** stands for quadrature.

These are the two baseband signals you get when you mix the RF signal with a cosine of the carrier frequency, and with a 90° shifted version of that cosine, respectively (and properly low-pass filter afterwards).

We call the first the inphase component, because it is literally what you get *in phase* with the cosine.

Mathematically, mixing-and-filtering is an *inner product* on the vector space of *$L^2$ signals* (it's effectively the integral of the point-wise multiplication of two functions – the RF signal and the local oscillator). That is: it's a projection, very much in the geometric sense! That explains the name of the quadrature component, as it's *orthogonal* to the inphase component.

Being orthogonal also means, just like in geometry: no matter which length you have orthogonal to the other vector, the projection on that vector is going to be 0.

That is very important – it means that I and Q, respectively, are two signals that are, together, equivalent to the RF signal in what they contain in signal "content", but they are independent; no matter what you do to the I part, it doesn't change the Q part.

That gives us a way of understanding *any* RF signal around *any* carrier frequency by describing the *equivalent baseband* signal in terms of I and Q signals, which individually have half the bandwidth of the RF signal.

That is the strength of it – no matter to which carrier frequency your transmitter mixes its signal, the equivalent IQ baseband doesn't change (only the LO frequency).

And the same applies to all the nice linear channel models we have: You could describe what happens to your signal between your transmitter and your receiver by describing what happens at the carrier frequency – or you could do the same directly in baseband, and *ignore* the fact that you have a mixer to go up from baseband to RF, then some amplifier, an antenna, the air, another antenna, an LNA, a mixer in between and just describe all this as a channel on the baseband, mathematically (and SDR, being software, is very good at math).

Now, to do things mathematically with the baseband, it has proven elegant to associate complex numbers with the I and Q components: The complex baseband signal at any time $t$ is just $I(t) + jQ(t)$, with $j=\sqrt{-1}$, the imaginary unit.

## Answer (score 3, by natevw - AF7TB)

If you're looking for just a basic definition, I/Q data is the result of a special form of sampling. Unlike "normal" sampling which takes a single measurement of a signal at each division of the sample rate, I/Q sampling gathers *two* measurements for each sample: both an "In phase" **and** a "Quadrature" component — thus the acronym.

The "quadrature" part only makes sense in a context where you are mixing the signals before sampling them. Although the ultimate signal of interest may be chosen selectively via software only, a typical SDR still gets "tuned" to a particular range of frequencies to start with. This is done by multiplying the incoming RF with an "LO" signal, similar to the first stage of an analog heterodyning receiver. The center frequency of the tuned-in range is determined by the frequency of that "LO" signal.

Now you can think of the in-phase component as the "normal" sample, and the quadrature component is equivalent to a second sample taken "90º later" **in terms of the tuning frequency** (i.e. delayed in time by 1/4 of the LO's period). In practice, both the I and Q "ADC inputs" would be provided simultaneously as separate signals from the mixer circuit, and the two components are taken together as a single "vector" sample at each point in time.

Capturing a two-component I/Q sample is more useful than just doubling the acquisition rate of "normal" [scalar] sampling. The vector I/Q samples are better for DSP processing because they avoid some ambiguity issues that come about in the mixer/heterodyning process. See Phil's comments below in response to an earlier version of this answer.

I found Whiteboard Web's I/Q Data for Dummies to be a great intro to the concept personally, as it works through questions like "why isn't normal sampling good enough?" at least from a processing perspective. (Especially now that other posters here have provided greater clarity on what it is trying to say… ;-)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16457/what-is-iq-in-the-context-of-sdrs, by Geremia, Phil Frost - W8II, Marcus Müller, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
