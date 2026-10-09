# What is Spectral Subtraction for noise reduction?

*Tags: noise, dsp · score 3*

## Question

I previously asked a [general question about noise reduction](What%20does%20a%20receiver%27s%20noise%20reduction%20function%20do.md), but none of the answers mentioned this specific method or algorithm. (the noise reduction button on some radios and DSP software seems to enable spectral subtraction, rather than just blanking, etc.)

How does Spectral Subtraction reduce noise in receiver audio? Why does this method or algorithm of noise **reduction** possibly create the problem of (reportedly) **adding** musical noise?

## Answer (score 5, by Mike Waters)

From https://link.springer.com/chapter/10.1007/978-3-322-92773-6_9 :

*Spectral subtraction* is a method for restoration of the power or the magnitude spectrum of a signal observed in additive noise, through subtraction of an estimate of the average noise spectrum from the noisy signal spectrum. The noise spectrum is estimated, and updated, from the periods when the signal is absent and only the noise is present.

The assumption is that the noise is a stationary or a slowly varying process, and that the noise spectrum does not change significantly in-between the update periods. For restoration of time-domain signals, an estimate of the instantaneous magnitude spectrum is combined with the phase of the noisy signal, and then transformed via an inverse discrete Fourier transform to the time domain. In terms of computational complexity spectral subtraction is relatively inexpensive.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15190/what-is-spectral-subtraction-for-noise-reduction, by hotpaw2, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
