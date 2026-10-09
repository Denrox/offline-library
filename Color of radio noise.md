# Color of radio noise?

*Tags: noise · score 4*

## Question

Is typical background RF plus radio receiver electronics noise (wide-band audio) closer to white noise or pink (1/f) noise?

Does it depend on the demodulation scheme (AM/FS/SSB/etc.), if any, currently configured or the band being tuned?

## Answer (score 3, by Phil Frost - W8II)

There is no single answer to your question.

Atmospheric noise varies over the RF spectrum. It's generally true that the natural RF noise power is higher at lower frequencies, but to call it something like "pink noise" would be inaccurate. For example, lightning is a significant contributor to noise on HF, and it comes in "crashes" as you might expect. There are also regions of higher or lower noise due to the varying absorptive capability of the atmosphere at some frequencies, or due to astronomical noise sources (like the sun) which emit more strongly at some frequencies than others. Of course man-made noise enters into it too: for example the 2.4 GHz ISM band is *very* noisy due to the proliferation of microwave ovens, Wi-Fi access points, etc.

So, noise over the RF spectrum as a whole doesn't fit any simple mathematical model. However, many communications are band-limited, and within the passband of a typical communications channel the variations from one end to the other are not much, so it's a good approximation to call it white noise.

Now concerning receiver noise, there are several kinds.

Every component in the receiver generates thermal noise, which is like white noise. This is noise due to the thermal movement of charge carriers in the receiver, and the only way to avoid it is to cool the radio to absolute zero. Radio astronomers have radios that are cooled to reduce thermal noise, but the radios most mortals use are not.

Additionally, there is flicker noise, also called 1/f noise or pink noise. There are many physical mechanisms that generate this kind of noise, but it's ubiquitous.

Below some frequency, the flicker noise is stronger than the thermal noise, and the converse is true above that frequency. So whether the noise at some point in the receiver is closer to pink or white, or some combination thereof, depends on the relevant frequency at that point. For example, after demodulation, the signal has been mixed down to baseband and so the frequencies are much lower, so the pink noise becomes more relevant.

Additionally, there's "other" noise in the receiver: noise from digital components, power line hum, and so on.

How do all of these noise sources combine together into the signal you hear from the receiver? It depends on many factors. In a simple demodulation scheme like SSB, the RF spectrum is just shifted down into audio range, ideally through a filter with a flat passband. Thus, white noise in the RF input becomes white noise at the audio output.

FM is not so simple. FM leads to a different demodulated noise spectral density function, and you have pre-emphasis further coloring things. The pre-emphasis is designed to approximately cancel the noise distribution introduced by the demodulation, so you end up with approximately white-ish noise in the end, but this is only approximately true, and it varies by the particular pre-emphasis standard you are using.

Digital modulations can use even more exotic filters which are more concerned about time-domain behavior, so they can color the noise in complex ways.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3616/color-of-radio-noise, by hotpaw2, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
