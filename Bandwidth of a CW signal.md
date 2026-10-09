# Bandwidth of a CW signal?

*Tags: cw · score 13*

## Question

What is the RF bandwidth of a typical CW signal? How is the signal bandwidth affected by WPM and/or transmitter rise-time?

What is the narrowest bandwidth that can still be copied by a human? Or what is the narrowest receiver audio filter that operators find useful for Morse Code?

## Answer (score 15, by Phil Frost - W8II)

In the simplest form, CW consists of a pure sine wave multiplied with a square wave that's either 0 or 1, corresponding to the keying of the carrier.

As with a mixer, or amplitude modulation, multiplying two signals generates frequency components that are the sum and difference of each frequency component of the multiplicands. In our simple form above, where the switching waveform is a square, the bandwidth can be very large, because a square wave consists of an infinite series of odd harmonics.

Real transmitters filter this square wave to some extent, and perfect square waves can't exist in practice anyway. The slower the transition from "on" to "off" is made, the less bandwidth is required.

If you send faster, then there are more transmissions per second. Since each transition requires a certain amount of energy away from the carrier frequency, faster speed means more sideband power, that is, more bandwidth.

Because every transmitter is different, it's difficult to say what the bandwidth is, exactly. We'd have to define more precisely what we mean by "bandwidth" anyhow. Because CW consists of brief periods of high bandwidth (the transitions) mixed with relatively long periods of zero bandwidth (everything but the transitions), the measured bandwidth depends greatly on how it's measured, anyhow. Are we looking at the average spectral density function over the entire transmission, or just some brief period around an on-off transition?

CW receive filters with a passband around 500 Hz are typical. It's certainly possible to make them narrower, but remember, it takes more bandwidth to make a sharp transition from "on" to "off". It doesn't matter if that bandwidth was never transmitted, or it was transmitted but we removed it with a filter. If the receive filter is too narrow, you won't hear a "dit dit" with clear starts and stops to the tone, you will hear a smeared "waahwaah". If we think about this problem in the time domain, it's called ringing, if we think about the filter as a resonant system, we say it has a high Q factor. This is actually a case of the uncertainty principle: the more sharply we localize a thing in frequency, the less sharply we can localize it in time.

I think the type, width, and nature of filters for CW is a matter of preference and circumstance. Between each pair of human ears is a wetware filter which is already very good at selecting tones by frequency, without help. Moreover, wetware filters can include context that simple linear filters can not: CW has a particular rhythm, QSOs follow a particular format, etc. However, a wetware filter can't remove a nearby strong signal causing desensitization.

## Answer (score 4, by hotpaw2)

Answering my own question:

First, the question was ambiguous, as it does not differentiate between (1) the bandwidth required to transmit the information, (2) the bandwidth required for the typical operator to copy the signal in realistic RF conditions, and (3) the bandwidth actually used by the transmitter, which are really 3 different bandwidths.

The second (bandwidth required for human copy) is actually called out in an old CCIR/ITU recommendation, where the bandwidth specified is to pass the 3rd or 5th harmonic of the baseband dot modulation rate for human copying, or a bandwidth in Hz of about 4 times the character WPM. (See: http://life.itu.int/radioclub/rr/ap01.htm)

The last bandwidth is often falsely calculated. Every sharp transient of an RF carrier produces local wide-band noise in the frequency domain. If the transients are exactly periodic, this wide-band signal will actually cancel out except at exact harmonics of the transition rate. However, real Morse Code (especially Farnsworth timed) is not exactly periodic. So this analysis is inaccurate. The actual spectrum generated is thus mostly created from the envelope (roughly the rise/fall time) of the carrier produced by the transmitter, and nearly completely independent of the WPM (except perhaps when sending repeated 555 RST's at extremely high WPM's). 2 to 5 mS rise times seem to be common, taking up around roughly 125 to 350 Hz in bandwidth between the 40 dB rolloff points. (See: http://www.eham.net/articles/16649), with the code WPM only varying this bandwidth used by a few percent. A typical 500 Hz CW audio filter would allow for this plus some drift in carrier and receiver LO frequency as well as manual tuning error.

The first bandwidth is related to the theoretical bandwidth required using optimally modulated (e.g. likely Gaussian pulse shaped) dots/dashes, where the minimum bandwidth in Hz required to transmit the information content can be as low as 1.2 times the synchronized dot WPM (there is a slight variability given that Morse Code is a variable length encoding). But without the signal harmonics (3rd or 5th as per CCIT/ITU), a human can't hear the signal redundancy provided by hearing the onset and end of each dot or dash, so few operators might be able to do this in actual practice. So this narrow bandwidth is only useful with computer(DSP)-mediated Synchronous Morse Code modulation/demodulation.

## Answer (score 3, by sm5bsz)

Have a look in some issues of QST. They provide spectra for keyed signals from tested transceivers. That is "the RF bandwidth of a typical CW signal." The minimum bandwidth is often assumed to be something like 25 Hz, but with appropriate frequency stability one would get the best copy at a bandwidth around 18 Hz for normal hand keyed CW. 20 years ago I was very active on CW EME (moonbounce) and I always optimized bandwidth for weak stations. It is enough to let through the first side-bands that would be present when transmitting a series of dots. The slowest keying station was OK1MS and his signal was best received at a bandwidth of 12 Hz. I was receiving with about 5 seconds of delay using a time span of 15 seconds (10 in the past and 5 into the future) to lock to the carrier of the CW signal by means of a power weighted least squares fitting. This way the filter was always kept symmetric around the signal. Mistuning by a single Hz would destroy performance since that would cause loss of one or the other side-band.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1412/bandwidth-of-a-cw-signal, by hotpaw2, Phil Frost - W8II, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
