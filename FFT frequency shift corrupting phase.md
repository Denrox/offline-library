# FFT frequency shift corrupting phase

*Tags: receiver · score 3*

## Question

I have written a Software Defined Radio. I take I/Q audio into the computer at a 192K sample rate and perform a 4096 sample Complex FFT. I display the spectrum (PSD) to the user so they can pick the signal they want to listen to, and capture the given frequency bin. So far so good.

I copy a set of frequency bins around the selected bin (based on the bandwidth I want) to baseband, following the approach in the QEX article "SDR For the Masses" by Youngblood. I multiply the copied bins with a blackman window whoes width is the same as the bandwidth. I then run an inverse FFT, and FM demodulate using a fast Arctan algorithm.

Everything works well, except with some frequency bins I get terrible phase distortion and at some bins it sounds perfect. I can literally nudge the center bin a few to the right or left and clean up the audio completely.

I read that this is an issue associated with copying the bins to baseband and that only certain bins avoid the issue. Specifically the paper says:

The mixing precision is limited further by the fact that we don't use complete buffer of output in fast convolution. We use only L samples. We must restrict the mixing to the subset of frequencies whose periods complete in those L samples. Otherwise, phase discontinuities occur. That is, one can only shift in multiples of V bins

So my question is how do I determine which bins are good? I have tried many calculations to get "V", which is the Overlap Factor but can't seem to find an algorithm that sorts the good bins from the bad. I think it's because V is defined in terms of the filter length and I do not know my filter length

I can also comment on the alternative approach, which is mixing in the time domain. I have written a Numerically Controlled Oscillator (NCO) to generate a Complex "carrier" and multiplied it by the I/Q signals thus: $$ i = i \sin(p) + q \cos (p) \\ q = q \cos(p) - i \sin (p) $$ (where $p$ is the phase accumulator).

This also works well and you get nice clear audio after FM demodulation. But it needs to be low pass filtered, otherwise you FM demodulate the entire IF. When I low pass filter it, again it sounds terrible. Much worse than copying the bins.

My understanding is that a complex signal can be filtered with a linear filter by just filtering the I and Q individually. I have lots of digital filters working for other audio purposes, but in this case they do not work. I tried IIR filters (because of linear phase response) as well as FIR, but no difference.

## Answer (score 2, by Kevin Reid AG6YO)

I don't have a complete understanding of the implications here, but here's a vague gesture in the direction of the answer which might be helpful.

What you are doing **is filtering**. And you've defined your filter as a brick-wall in the frequency domain (by copying some bins and ignoring the rest), without regard for the phase or time-domain characteristics. Therefore it's garbage in those ways.

I'll guess that you should be able to fix the phase response by applying the appropriate phase offsets to each bin, but I don't know what those offsets would look like (likely linear).

FFT-modify-IFFT is a valid implementation strategy for a filter, and it can be more efficient than a straightforward FIR filter while getting the same answer, but you need to actually design a sensible filter (not a rectangular-in-the-frequency-domain one) to use it with.

Here's a question over on Signal Processing Stack Exchange that I think is essentially the same question. The answers aren't all that illuminating for me, though, so I don't know if it'll help you: What are the problems with designing an FIR filter using FFT? The answers suggest that part of the problem with this approach is that it's defining the filter to be perfect at each frequency bin but disregarding its characteristics at the frequencies between the bins.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4991/fft-frequency-shift-corrupting-phase, by Chris AC2CZ, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
