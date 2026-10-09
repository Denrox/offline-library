# Calculating the signal-to-noise ratio for CW (Morse Code) signals?

*Tags: cw, dsp · score 9*

## Question

How is the signal-to-noise ratio for received CW and QRSS CW (and/or other ultra narrow-band DSP digital modes) typically computed? e.g. What noise bandwidth should be used to measure the spectrum power against the narrow CW "on" signal power?

Should one use the DSP detection bandwidth (roughly 1X the WPM), the human decode bandwidth (approximately 3X to 5X the WPM according to an ISO or ITU document), the actual bandwidth used by the transmitter rise time, or some other standard radio bandwidth (SSB LSB filter width?)?

How should the CW S/N be computed to compare its data rate (at a given WPM) against the theoretical Shannon limit for that S/N?

Is the same S/N number meaningful depending on whether the noise is mostly Gaussian noise, white noise, or 1/f RF noise?

## Accepted answer (score 4, by Aleksander Alekseev - R2AUK)

The answer can be fond in The ARRL Handbook 2019, Vol 3, although it's spreaded across different chapters. In short, SNR is typically calculated for the noise floor of 2500 Hz SSB signal. Particularly this is how WSJT-X calculates negative SNRs for FT8 and other modes.

Now the trick is that by deviding the bandwidth in half you decrease the noise floor by 3 dB assuming the noise is distributed evenly. When I use 500 Hz wide DSP filter in my Yaesu FT-891 I typically see S2-S3 noise floor on 20m, and S4 when 2500 Hz bandwidth is used. Now keeping in mind that one S-unit is approximately 6 dB we get:

```
>>> from math import log2
>>> 3*log2(3000/500)/6
1.292481250360578

```

And we really see 1-2 less S-units, as expected.

Now back to CW. The ARRL Handbook claims with the reference to "The ITU Classification of Emission Standards" that the bandwidth of CW signal can be estimated as:

```
BW = WPM * 0.8 * 5

```

For instance, a 17WPM signal has a bandwidth about 68Hz. This means that the signal can be received:

```
>>> 3*log2(2500/68)
15.600748614897329

```

... 15.6 dB "under the noise floor".

Please note,

1) This assumes that there is a 68 Hz bandpass filter on the receiver side. This in fact is a reasonable assumption in the era of DSP filters. For instance, FT-891 has a very narrow-band audio peak filter (APF).

2) When you compare the decoding threshold of different modes (e.g. FT8 and CW) there are many other factors to consider. In case of FT8: 1) it's not a "chat mode" as CW 2) FT8 frequencies are often crowded (read - QRM) thus the decoding threshold doesn't matter *that* match 3) sadly many people who use digital modes don't [check the IMD of their sound card and transceiver combo](How%20to%20fix%20SignaLink%20non-linearity%20problem.md) which gives even more QRM, etc.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15886/calculating-the-signal-to-noise-ratio-for-cw-morse-code-signals, by hotpaw2, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
