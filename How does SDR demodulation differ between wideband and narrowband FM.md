# How does SDR demodulation differ between wideband and narrowband FM?

*Tags: modes, software-defined-radio, fm · score 9*

## Question

What is the difference between software demodulation of an IQ signal between wideband FM and narrowband FM? Both seem to look at the 2nd difference in unwrapped phase angles of IQ samples.

## Accepted answer (score 8, by Kevin Reid AG6YO)

There are actually three different distinctions one could mean by referring to “narrowband” FM.

Wideband FM in this context generally refers to the type of FM used for broadcast stations — those picked up by consumer FM receivers — as opposed to that used by two-way communications, including amateur transceivers.

You are right that there is no fundamental difference between them in how the *frequency modulation* is demodulated via DSP. In both, the difference between the instantaneous frequency of the signal from some nominal carrier frequency is proportional to the modulating (audio) signal. The distinction is in the *maximum deviation*, which is closely related to the occupied bandwidth.

That is, if you modulated either type of FM transmitter with a signal at, say, 50% of maximum input level, the wideband FM signal would have a much larger deviation for the same signal. The advantage of this is that wideband FM has higher fidelity and picks up less noise, because the larger instantaneous frequency changes are less easily affected by noise.

You could in principle demodulate either type of FM with the exact same demodulator with the same settings; however, the wideband FM would come out louder because of the larger deviation. In practice, you also need a *filter* before the demodulator which removes all the noise or other signals which would interferes with the instantaneous-frequency demodulation; this is what actually makes the biggest difference. To a narrowband receiver, a wideband signal is extremely over-deviating; the frequency repeatedly moves entirely out of the filter passband, so that all but the zero-crossings of the signal are replaced by noise. To a wideband receiver, a narrowband signal is extremely quiet.

An additional difference in practice, not inherently related to the deviation and bandwidth, is that wideband FM signals may include stereo or other additional information. Stereo is actually added *to the modulating signal* — that is, the FM modulation is unchanged. The “pilot tone” and stereo difference signal are added to the mono audio but shifted to a frequency high enough that they do not conflict with the audio frequencies and a typical mono receiver will not reproduce them. Wikipedia has a nice plot of what you might find in a broadcast FM signal — this is an “audio” spectrum, so you will not see these things laid out on a waterfall display.

Another “wide vs. narrow” distinction you might hear about: there are two different maximum deviations (5 kHz and 2.5 kHz) that have been used for two-way radios — in the US, the FCC required a shift to the narrower bandwidth to enable using more channels in the same spectrum; this event was called “narrowbanding”. Amateur equipment is under no such requirement and to my knowledge still typically uses the wider (5 kHz) deviation.

In radio software I have seen these distinct modes being cryptically labeled "NFM1" vs. "NFM2", or "FM" vs. "NFM", whereas broadcast FM is usually "WFM".

Finally, in the theory of modulation, FM is called wideband if the maximum deviation significantly exceeds the highest modulating frequency, and narrowband if the highest modulating frequency significantly exceeds the maximum deviation. By “modulating frequency” we mean the frequencies present in the modulating signal (the audio signal). This relationship affects the effective occupied bandwidth of the signal, and therefore the choice of low-pass filter used to select the channel before demodulating it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1515/how-does-sdr-demodulation-differ-between-wideband-and-narrowband-fm, by hotpaw2, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
