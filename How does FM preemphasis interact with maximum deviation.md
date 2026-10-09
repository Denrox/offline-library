# How does FM preemphasis interact with maximum deviation?

*Tags: gnuradio, fm, filter · score 4*

## Question

I'm trying to design a broadcast stereo FM transmitter in GNU Radio and I'm running against an issue. After preemphasis is applied using the built-in "FM Preemphasis" block, the amplitude of higher frequencies (> 4 kHz) can get boosted beyond 1 when the input amplitude is 1, which after FM, yields frequencies greater than the maximum deviation. Even if the input amplitude is significantly less than 1, the maximum deviation is still exceeded, just at higher frequencies. To avoid that, the only solution seems to be to reduce the gain of the input, but the necessary reduction is so great, that the audio at the receiver (using the built-in WBFM Receive PLL block) is unreasonably quiet compared to the loudness of audio in actual broadcasts that I capture with an SDR.

- How do stations transmit so "loudly"?
- Is the maximum deviation not a strict limit, and the boosted high frequencies are actually allowed to cross it?
- Is it expected that the audio is pre-filtered with a low-pass filter that starts dropping off way sooner than 15 kHz?
- Is the GNU Radio preemphasis block broken?
- Or am I missing some other important step in the process of modulation?

To clarify, the built-in demodulator block works fine with broadcasts received with an SDR. It also works fine with my own modulator, yielding a linear frequency response all the way up to about 4 kHz, at which point distortion is introduced inside the demodulator.

## Accepted answer (score 4, by Marcus Müller)

How do stations transmit so "loudly"?

Ryuji mentioned this: Audio gets compressed so that it sounds "loud" and "voluminous" under less-than-perfect reconstruction conditions.

What happens there is both an emphasis on psychoacoustically important features while de-emphasing things you, as a human, aren't likely to hear anyway. (This is also done in *audio codecs*, but the term "compression" there means "reduction of data volume", that's got nothing to do with compression here). In essence, you tend to have louder sections more often.

In a bad, method-of-times-gone / guitar distortion pedal way, you'd do that by simply amplifying your audio until it regularly crosses a loudness maximum – then just clip it there, i.e., cut off what's above that allowable maximum; you get heavy, "unclean" harmonics and snaring. You can be a bit more subtle, and instead of sharply cutting off just weighting the instantaneous amplitude such that the closer your signal gets to maximum, the less quickly the output rises. That allows you to make most of your song louder without the crests sounding like hell instantly. You get harmonics, but they are more benign.  
And then there's much more advanced methods that actually incorporate the frequency-dependent sensitivity of the human observer, and do compression with models that optimize for some perceptional quality.

It's trading *fidelity* for *loudness*.

I'd have a lot kinder words for the work of sound engineers than Ryuli found there: Not everything on radio is an US-American advertisement. What sound engineers often do is to take a song and making a trade-off between reproducing the crisper parts of highs and perceived volume. It's a necessity; especially if you think about who still listens to FM radio, and on which devices. A kitchen radio or an alarm clock are not appropriately equipped with speakers to give you hifi, so making the most of it is what you do.

Is the GNU Radio preemphasis block broken?

GNU Radio does none of the above: takes the audio in as you, the sound engineer (from the point of the radio station) meant it to be, and applies a standardized filter to it. No big choice there: from the hayday of FM radio, there was a standard passive filter that larger stations used, and receivers used, and nowadays everyone has to emulate these filters. For more infos on that, https://wiki.gnuradio.org/index.php/FM_Preemphasis . (The reason they did that is because noise does not affect all frequency in the message signal equally in FM reception, so you use a preemphasis at the transmitter and a deemphasis at the receiver, to shape the noise spectrally such that it sounds nicer.)

It's not the job of the FM modulator to define what audio the human at the receiver is supposed to hear – it's up to the audio engineer to define what they want to do: reduce volume to allow for critical high-frequency components to be reproduced accurately, or to cut loud high-frequency content and keep the overall volume high. The FM modulator can't do that for you; it's a "sound design choice", if you will.

Is it expected that the audio is pre-filtered with a low-pass filter that starts dropping off way sooner than 15 kHz?

Well, yes. While 15 kHz is the nominal bandwidth of the audio, you'll find that at 12 to 13 kHz you're typically a solid 30 dB below the amplitudes you see between 200 Hz and 3000 Hz; there's simply not much information that high in audio, and again, consider that FM broadcasting is a 1940's technology, aimed at 1940's receivers. You tell me how high your Grandma's living room tube radio goes in audio frequency! It's not likely to go higher than 9 kHz at all! There's a reason why the US was very slow to adopt FM in breadth – up to 1978, there was more AM receivers than FM receivers – and that was that the advantage to the budget-bound listener was just not that great (among other things. Americans had no wars on their soil, so no necessity to replace aging infrastructure, either. And a lot of distance to cover. And a lot of lonesome outlandish stations. And lobbying to keep AM stations funded. I mean, crazy AM talk radio is still a thing in the US, would these transmitters have to pay proportionally for their spectrum usage, that would not be the case.)

I'd say, you go, run Audacity (or any other digital audio workshop software you like, but that one is free), and you take a song you know relatively well, and you filter it to 12 kHz (say, *Journey – Don't stop believing*). Listen to the original, then listen to the filtering. Then find the worst speakers you have – maybe you have an old computer screen with built-in speakers? – and play the same. Does it make any difference? Will it make a difference to someone who owns an FM radio alarm clock?

Repeat experiment with 8 kHz and 10 kHz cut-off. The older you are, the less of a difference does it make.

Is the maximum deviation not a strict limit, and the boosted high frequencies are actually allowed to cross it?

You have a spectral mask to keep. That's the full answer here – a spectral mask gives you "how much power is my emitter allowed to transmit in which small bandwidth". Now, naively, at any given arbitrarily short instant, an FM emitter transmits a carrier at one frequency, at a constant power, but that's not how that works - the power densities tell you how much power was emitted in a given bandwidth, and that means it "integrates" for how long the carrier "remained" in that small bandwidth during the observation.

So if your spectral mask says, and it does for the US FM broadcast bands and you're a US government-sanctioned FM broadcast station (i.e., legal)

on any frequency removed from the assigned frequency by more than 75 percent, up to and including 150 percent, of the authorized bandwidth, and the image, at least 25 decibels attenuation;¹

that means that if you have a 75 kHz wide channel, then that's +- 37.5 kHz from the center frequency. So, from +37.5 kHz to +1.5·37.5 kHz, you need to have 25 dB less of power. As long as you exceed your 75 kHz max attenuation less than -25 dB of time (and that's some 0.3 % of time, not very much), you're fine!

If you can't guarantee that, well, maybe just attenuate the carrier when it ventures outside of your 75 kHz band – it's FM, the receiver doesn't "care" about carrier amplitude anyways; you become more susceptible to noise, but again, this only affects high frequencies, so, not that much lost.

¹ National Telecommunications and Information Administration, Manual of Regulations for Federal Radiofrequency Spectrum Management, Chapter 5 "Spectrum Standards", Section 5.2.2.2 "General Standards", Subsection "29.7 MHz and above", sentence "a."

## Answer (score 7, by Ryuji AB1WX)

The maximum frequency deviation for FM broadcasting in the US and Europe is ±75 kHz. It is a number born of regulation and necessity, designed to ensure order in a world that thrives on chaos. Deviate beyond this, and the signal spills over into someone else’s frequency, disrupting their broadcast, their message, their truth. The spectrum is 200 kHz wide—a slice of air reserved for each station, nothing more, nothing less.

Transmitters, like the ever-watchful eyes of authority, employ limiters to enforce this boundary. They do not allow for deviation beyond the prescribed limits. It is not a matter of artistry or expression but compliance and control. A signal that exceeds the bounds is not just an interference; it is a violation of order, an offense against the collective system.

Pre-emphasis is used to reduce annoying hiss, just like those used in analog tape recording and records. In the US, the time constant is set at 75 microseconds, boost beginning at 2.1 kHz and reaching its peak at 15 kHz. In Europe, the number is 50 microseconds, starting at 3.2 kHz. The differences between them expose the arbitrary nature of national boundaries. European FM radio receivers in North America will sound harsh, overbright; an American radio set in Europe will sound muddy, subdued. Even in the universal medium of sound, the borders of nations assert themselves.

The system was designed with the natural world in mind. Speech and music carry their power in the lower frequencies, leaving the higher ones free for manipulation. Pre-emphasis, like so much in human systems, exploits this gap. But test the system with white noise or sinusoids, and it fails—emphasis cracks it apart, revealing its fragility. The system was built for speech and music, for the voices and songs of humanity, not for inhumane synthetic noises.

And then there is compression. Once a gentle hand, it is now a fist. In the early days, compression was a simple matter, akin to the automatic gain control of a cheap tape recorder, lifting up the soft sounds. Now it is a multiband beast, dividing the signal into parts and pushing them into forceful loudness. Advertisers, ever hungry for attention, can't be happy without it. The result is loudness that drowns out subtlety, aggression that overwhelms nuance. The listener is bombarded, not invited.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23308/how-does-fm-preemphasis-interact-with-maximum-deviation, by Cosinux, Marcus Müller, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
