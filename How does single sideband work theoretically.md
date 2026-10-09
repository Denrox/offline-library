# How does single sideband work theoretically?

*Tags: modes, ssb, theory · score 5*

## Question

How does single-sideband (SSB) work theoretically? If a theoretical SSB transceiver is a "black box" and only its inputs and outputs can be analyzed, not the way it works internally, what is happening?

## Accepted answer (score 1, by Marcus Müller)

It's quite simple, really. If we're describing a black box, we will have to describe the blackbox in terms of the things going in and out. So, we start by giving them names:

- Signal  Description
- $m(t)$  Message signal in time domain – the audio to be transmitted
- $M(f)$  Message signal in frequency domain – spectrum of the audio
- $s(t)$  Transmitted (passband) RF signal in time domain
- $S(f)$  Transmitted (passband) RF signal in frequency domain

Note that $s$ and $S$ are the **same** signal – just that the first describes the signal as how it is over time, and the other how it is over frequency. Both representations contain the exact same information – you can convert between them back and forth as you want, using the Fourier transform. The same is true for $m$ and $M$.

What every mixer does is simply shift a signal in spectrum. What that means is that it takes some signal (like our message signal $m(t)$ / $M(f)$, for example) and moves it to a different frequency (same example: it simply makes a different signal $Q(f) := M(f+f_{\text{mixer}})$). That's it. If we do that to our message signal (audio) with an RF frequency, we end up with AM with a "suppressed carrier" (there's no carrier, but it's the name hams tend to give the mode). But that's a *double-sideband AM*:

Because the message signal $m(t)$ is a real-valued signal (i.e., the pressure at the microphone, and consequently the voltage in your mic amp, are real numbers at any point in time), the spectrum is (hermitian) symmetrical to the $f=0$ line – that's a direct consequence of how the Fourier transform defines what the spectrum is. By shifting it up to some $f_{\text{mixer}}$, we shifted both the positive frequencies to $f_{\text{mixer}} + \text{something}$ and the negative frequencies to $f_{\text{mixer}} - \text{something}$.

So, all we need to do is get rid of everything below $f_{\text{mixer}}$ to get the upper sideband or everything above $f_{\text{mixer}}$ to get the lower sideband modulation.

There's multiple ways to represent that in a blackbox model: we can say that after mixing, a low-pass filter with cutoff at $f_{\text{mixer}}$ is convolved with the time-domain signal for USB (high-pass for LSB); we could say the spectrum is multiplied with a mask (which is the same filtering operation).  
The way "modern" (read: after 1940) communications technology would write that is probably that instead of "killing" half of the transmit RF signal after mixing, you just "kill" half of the message signal: A complex filter can filter out the negative (for USB) or positive (for LSB) half of the spectrum, before mixing.

So, for me, I'd write the blackbox model of SSB:

$$s(t) = \cos (2\pi f_{\text{mixer}}) \cdot \left(h_{\text{complex half-band filter}}*m(t)\right),$$ where $*$ is the convolution operation and $h$ is the above-mentioned "kills all negative (or positive) frequencies" filter's impulse response.

Technologically, that's how I'd actually implement the SSB modulator, myself. Because: Having a sharp filter at RF is harder (both if you want to build that as analog filter, and if you want to implement that as digital filter in a microcontroller, DSP, FPGA or ASIC) than at low frequencies. (Generally, "hardness" of a filter is pretty well-described by how quickly it goes from passband to stopband, relative center frequency it works at.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21576/how-does-single-sideband-work-theoretically, by kj7rrv, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
