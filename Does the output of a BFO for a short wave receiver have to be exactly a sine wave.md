# Does the output of a BFO for a short wave receiver have to be exactly a sine wave?

*Tags: receiver, ssb · score 4*

## Question

I want to build an external beat frequency oscillator (BFO) for an old valve Eddystone receiver I have.

There are many circuits for BFOs on the internet, they are mostly similar, the idea seems simple enough, the two most important criteria it seems being frequency stability and output level.

I found a couple of circuits designed by W1FB DeMaw and built these, the first one didn't work at all and the second one has an output that looks nothing like a sine wave.

Is it important for a BFO to have a pure sine wave output if you want to use it to resolve SSB signals giving decent audio quality? What happens to SSB demodulation if the BFO output is a triangle or square wave, for instance?

For the moment there is a HP signal generator connected to the radio and that works very well.

## Accepted answer (score 5, by Phil Frost - W8II)

The BFO is one input to the mixer, the other being the RF signal you're wanting to receive. An ideal mixer simply multiplies its inputs: if at one instant one input is 2V, and the other input is 3V, the output will be 6V.

This is useful because multiplication like this can accomplish a frequency shift. The objective in receiving USB is simply to take all the frequencies at RF, say 10,000,000 Hz to 10,004,000 Hz for example, and shift them down to something you can hear like 0 to 4000 Hz. LSB is similar except you're aiming for 0 to -4000 Hz, which has the effect of "flipping" the spectrum.

The ideal mixer products output frequency components that are the sum and difference of its inputs. So if one input to the mixer is a sinusoid at 10 MHz, and the other is a sinusoid at 9 MHz, then the output will be sinusoids at 1 MHz and 19 MHz.

What if one or both of the inputs is not a simple sinusoid? By superposition the input(s) can be decomposed into sinusoids, so the above still holds.

For example, a square wave consists of a sinusoid at the fundamental frequency, and then every odd multiple thereof. So if the BFO is a square wave at 10 MHz, this is equivalent to having a series of separate mixers, one with a sine wave BFO at 10 MHz, another at 30 MHz, another at 50 MHz, and so on, and then summing all the outputs of these mixers together.

What this means is if the BFO is a square wave, additional frequencies in the RF input can also be mixed to baseband where they will add and interfere with your desired signal. For example if the desired USB signal is at 10 MHz the BFO will be set to 10 MHz to mix that signal down to baseband. But if there's also a signal (or any noise) at 30 MHz you'll hear that too, added to the desired signal.

There's a simple solution: filter the RF input to the mixer such that there is nothing at 30, 50, 70, ... MHz. A lot of times, such a filter is already present in the receiver anyway, since it's generally desirable to minimize the power at all points in the circuit since this minimizes nonlinear distortion.

In fact, many receiver architectures use a mixer that is deliberately far from ideal. For example, the Elecraft receivers use an FST3253 as the mixer. This is an analog multiplexer IC which is functionally similar to a switch, with the position of the switch controlled by a digital input. The BFO provides this digital input, and the analog inputs and outputs are arranged so when the "switch" is flipped, the polarity of the analog signal is inverted.

As such, this is far from an ideal mixer. Effectively, it can only multiply by 1 or -1, so even if the BFO was a sine wave, it would become a square wave by nature of the digital input.

## Answer (score 7, by Marcus Müller)

So, the job of a BFO is essentially "faking" the carrier oscillation of the AM transmission that was suppressed, together with the other sideband, so that the rest of the receiver can demodulate the SSB signal.

As such, it's the input to a specific nonlinear device: the mixer (sometimes combined with a power detector, then called "product detector", as far as I know).

Now, an ideal mixer does a very simple thing: It multiplies two signals. That's all.

The trick why multiplication is frequency mixing is pretty intuitive:

1. Trigonometric identities say that $$\cos(x)\cdot\cos(y)=\frac12 (\cos(x+y)+\cos(x-y))\text;\tag1\label{trig}$$ similar things for $\sin\cdot\sin$ and $\cos\cdot\sin$.
2. Every signal can be decomposed into a sum of cosines and sines.

## Mixing = Multiplication + Filtering

When you look at $\eqref{trig}$, you can imagine what happens when you multiply say, a cosine of 1.2 MHz with one of 1 MHz frequency:

\begin{align} x &= 2\pi\;1\,200\,000\;t &= 2\pi f_1t\\ y &= 2\pi\;1\,000\,000\;t&=2\pi f_2t\\ &\text{insert into \eqref{trig}:}\\ \cos(x)\cos(y) &= \cos(2\pi f_1t)\cos(2\pi f_2t)\\ &=\frac12\left[\cos(2\pi f_1t + 2\pi f_2t)+\cos(2\pi f_1 t -2\pi f_2 t)\right]\\ &=\frac12\left[\cos(2\pi (f_1+f_2)t)+\cos(2\pi(f_1-f_2) t)\right]\label{prods}\tag2 \end{align}

So, multiplying two cosines gives you two new cosines, one at a frequency that is at the sum of the two input frequencies, the other at the difference.

Usually, you only want either, not both new tones. We're trying to get an RF signal down to audio frequency, so we care about difference. We simply use a low-pass filter to filter out the sum frequency component.

Where do we let that low-pass filter cut off? Well, essentially, anywhere above the audible frequency range works. If $f_1$ was the frequency of the RF (or IF, depending on your receiver's architecture) signal, our job in tuning to a transmission is nothing but adjusting $f_2$ (which is our BFO frequency!) so that the difference $f_1-f_2$ is such that the resulting frequencies are exactly the audible frequencies used to excite the transmitter!

## Everything is a sum of cosines and sines

In general, what Fourier derived is that every periodic signal can be written as a discrete sum of cosines and sines. Say, we have a signal (for example, a square wave or a triangle or a chirp sequence) $s(t)$, which repeats every for every difference in $t$ of $1$, then we can write that as

$$s(t) = \sum_{n=0}^{\infty} a_n\cdot \cos (2\pi n t) + b_n\cdot\cos(2\pi n t)\text.\tag3\label{fseries}$$

Repeat that mentally: What $\eqref{fseries}$ means is that hey, if something is periodic, it can be understood as sum of cosines and sines, and the "weights" of these are in the different $a_1, a_2, \ldots$ and $b_1, b_2,\ldots$.

If it's actually a sine or cosine, then this is pretty simple. For a cosine wave, all but one $a_n$ are zero, and all $b_n$ are zero. For a sine wave, all $a_n$ are zero and only a single $b_n$ is not.

For everything that is not a pure sine or cosine, there will be more than one $a_n$ and/or $b_n$ that is not 0.

For example, the square wave with fundamental frequency $f$ has the formula

$$s_{\text{sq. wave}}(t) = \frac 4\pi\left(\frac 11 \sin(1\cdot2\pi f t)+\frac 13 \sin(3\cdot2\pi f t)+\frac15 \sin(5\cdot2\pi f t)+\frac 17 \sin(7\cdot2\pi f t)+\cdots \right)$$

## Mixing with things that aren't pure sines

When you look at that, it'll become apparent that if you mix with anything but a clean sine, or cosine, you end up with more products.

For example, multiplying with a square wave BFO with fundamental frequency $f_2$ will not only mix what is at $f_1$ down to $f_1-f_2$, because there's not only a sine with a single frequency in there, but also harmonics. So, you get what you want, but also things that are at every odd multiple of $f_2$ apart to your "target frequency". Uff! Not good. You wanted to mix what is at 100.001 MHz to 1 kHz, so you used a 100 MHz square wave, so you actually did get what was at 100.001 MHz at 1 kHz, but also what was at 300.001 MHz, and at 500.001 MHz, and so on, mixed to 1 kHz.

## Effects of that on receivers

Often, that's undesirable. (because you don't care what is at 300.001 MHz, it only interferes with your 100 MHz signal of interest.) Sometimes, it doesn't matter, because the signal mixture you put into your mixer is already filtered sufficiently, so that there's nothing at 300.001, 500.001, … MHz to begin with. (that is typically the case for a well-filtered IF.)

So, it depends on your receiver architecture whether the BFO not being a single tone is critical or not. In general, it's advisable that it is!

#Generating a pure-sine BFO from a square wave

that's easily done:  
Say, you want to use a microcontroller to generate a square wave BFO between 10 Hz and 20 Hz (just an example). If you look at the formula of the square wave, you'll notice that the first harmonic is at three times the fundamental frequency – a low pass filter at 29 Hz converts any square wave between 10 Hz and 29 Hz to a pure sine wave, because none of the harmonics make it through.

## Other aspects of BFOs that affect your quality

If your BFO has so-called phase noise (i.e. it might be a single sine, but that sine isn't really clean and shifts a bit in frequency, i.e. is a bit faster or slower than it should be at times), then that's a problem, and this noise ends up being very detrimental to your audio quality. In general, because as shown above, filtering out harmonics is easy, but getting rid of phase noise is not, it's more important that your oscillator is very stable than that it's a perfect sine wave.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17100/does-the-output-of-a-bfo-for-a-short-wave-receiver-have-to-be-exactly-a-sine-w, by Andrew, Phil Frost - W8II, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
