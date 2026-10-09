# How do PL tones make it through so much noise?

*Tags: fm, tone-squelch · score 3*

## Question

So sometimes I hear people trying to get into a repeater with pure noise, and no audible audio on their transmission.

With the repeaters that require a PL tone, how can the PL tones get through all of that noise if I can barely get DTMF through with a bit of white noise?

## Accepted answer (score 5, by WPrecht)

As Michael noted, a repeater's CTCSS system is looking for a very specific frequency with a very low deviation (typically 10% or less) as low as about 40 dB down. What you are hearing is of course the whole audio range.

The decoder in a CTCSS system is based on a very narrow bandpass filter which passes the desired CTCSS tone. There is a balance between a tone that can be quickly recognized and one that can intrude on the audio. The higher the frequency of the tone, the faster the hardware can recognize it and open the transmit, but the more likely you'll notice it. On the other hand a very low tone consequently takes longer to be recognized and you risk missing a syllable or two off the beginning of a transmission.

These days most amateur radio repeater controller manufacturers offer an audio delay option - this delays the repeated speech audio for a selectable number of milliseconds before it is retransmitted. During this delay period, the CTCSS decoder has enough time to recognize the right tone. This also keeps two transceivers in close proximity to each other (say two people with HTs) from creating an annoying impromptu oscillator.

References:

- Wikipedia - Continuous Tone-Coded Squelch System
- WA6ILQ - A Historical and Technical Overview of Tone Squelch Systems

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1598/how-do-pl-tones-make-it-through-so-much-noise, by Skyler 440, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
