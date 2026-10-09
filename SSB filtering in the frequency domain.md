# SSB filtering in the frequency domain?

*Tags: software-defined-radio, filter, ssb · score 5*

## Question

I'm not sure whether it's more appropriate to ask this question here, or in the dsp.stackexchange. But I'll try here first.

There seems to be a lot of information available on the filtering and demodulation of SSB signals in the analog or time-domain. But my iOS RTL-SDR radio app is doing all of it's fine tuning and filtering in the frequency domain (via overlap-add FFT fast convolution). So I'm wondering what would be the cleanest method of filtering in the frequency domain, without just emulating the chain of processes needed in the time domain or with an analog SSB demodulator. For instance, a Hilbert transformer isn't needed, since the input to the complex FFT filter already has the imaginary component of the complex or IQ signal provided by an RTL-SDR (or other similar SDR front-end). And asymmetric filtering can be accomplished in the complex IQ frequency domain without shifting the signal’s spectrum.

Here's one possible idea: Shift my FFT lowpass filter from being magnitude symmetric around DC to either only the positive or negative frequency side of DC (equivalent to using a complex FIR filter impulse response of the same length or order). Mirror/flip the retained side (positive or negative frequencies for USB or LSB) to the other side of DC and complex conjugate it, resulting in a strictly real time-domain signal after the fast-convolution IFFT. Feed that result to a simple AM demodulator. Would that work?

Is there another canonical and clean SSB demodulation method?

## Answer (score 5, by Kevin Reid AG6YO)

For DSP with complex samples, whether you are working in the time domain or the frequency domain, you *don't need* an AM demodulator, or complex conjugation, or a Hilbert filter.

You say you have available a shifted low-pass filter — in other words a band-pass filter suitable for SSB. From the output of that filter, **discard the imaginary part.That's it. You're done. You have a real audio signal.**

The fundamental elements of SSB demodulation are

- the downconversion (a.k.a. mixing or frequency shift) from RF to audio baseband, and
- the band-pass filtering to the standard 3-ish-kHz passband.

Everything else you might hear about (intermediate frequencies, BFOs, decimation, or the FFT and inverse FFT you're doing) is an implementation detail of a particular approach.

(Possibly interesting tangent: you could even implement it with only low-pass; you would shift the input signal to put the desired SSB passband centered around 0 Hz, low-pass filter, then shift back up to only positive audio frequencies.)

## Answer (score 5, by sm5bsz)

If you want to do SSB in the frequency domain:

1) Compute the complex FFT.

2) Pick the frequency band of interest.

3) Perform a backwards FFT on the bins that contain the signal of interest.

Typically the sampling rate would be 192kHz I and Q and one would want 3 kHz for SSB. That means that the inverse FFT would have to be 64 times smaller. (VERY small CPU load) The time domain signal would be 64 times slower.

There are many interesting complications, but the above is the method used in Linrad to do frequency shift, filtering and decimation. It is very CPU efficient. http://www.sm5bsz.com/linuxdsp/linrad.htm With appropriate windows and overlapping FFTs one can get extremely good dynamic range (freedom of resampling spurs.)

Receiving SSB is a linear process. One has to do two things:

1) Apply a filter to remove everything outside the frequency band of interest.

2) Do a frequency translation to place the frequency of the suppressed carrier at DC (zero frequency.)

It does not matter in which order we do those things (it is a linear process) and it does not matter if we do it in many steps. In analog radios we use multiple conversions and in DSP we typically filter and decimate in several steps. It is just a matter of convenience. When Linrad uses the 2 MHz wide FFT from a Perseus, the hardware has applied filtering and decimation from the original raw data at 80 MHz.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10228/ssb-filtering-in-the-frequency-domain, by hotpaw2, Kevin Reid AG6YO, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
