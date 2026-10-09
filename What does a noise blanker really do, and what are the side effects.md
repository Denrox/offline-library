# What does a noise blanker really do, and what are the side effects?

*Tags: hf, noise-blanker · score 18*

## Question

Most HF rigs have a **noise blanker** (NB) feature. It does reduce some types of noise (car ignition noise and such). How does it really work?

I've read it has negative side-effects with strong signals, which is why it is not enabled all the time.

## Accepted answer (score 16, by Phil Frost - W8II)

Some types of noise are very short bursts of energy. Car ignition noise is one example. Power-line noise caused by switching triacs in light dimmers is another. For example, see the top image here:

(source: *A Line-Synchronous Noise Blanker* by KA7OEI)

This image also illustrates the effect of band-pass filtering on these pulses. The middle image shows the effect of filtering the pulses through a SSB filter, and the bottom image through a narrower CW filter. Though the filters remove the higher harmonics of the pulses, they do this at the expense of introducing ringing and "smearing" the pulse over a longer time.

This is why noise blankers are desirable for this kind of noise: if you can chop out the noise in the time domain, just for those very brief pulses, without introducing the ringing that a bandpass filter would introduce. A noise blanker detects when these noise pulses occur, and then attenuates the receiver for the duration of the pulse.

The downside is that this has the potential to introduce more noise and distortion than it removes. Attenuating the signal for these brief periods is equivalent to multiplying the signal by a square wave which is usually 1 but is 0 for the brief periods where the attenuation is happening.

This can be viewed as a kind of amplitude modulation or mixing, and what you get at the output are frequency components that are the sum and the difference of the frequency components of the original signal, and the square wave from the noise blanker. The square wave, being very rich in harmonics, creates frequency components over a wide band. An analogous and more familiar phenomenon happens in CW: if the carrier is switched on or off too quickly we get "key clicks" or "splatter". In a noise blanker we aren't switching on and off a carrier, but rather whatever signal we might be receiving, but the mechanism by which noise is introduced is the same.

Thus, practical noise blankers filter the square wave, such as by limiting the slew rate of the attenuation or such. This reduces the harmonic content of that square wave, thus reducing the distortion introduced by the blanker. There's a trade-off to be made here: more filtering of the blanking square wave means it can't cut out the pulses with the same precision because it can't respond as quickly, so the trick is to adjust the response to remove as much as the pulse as possible, as little of everything else as possible, while introducing a minimum of distortion.

The main problem with strong signals is that it makes it more difficult to find the noise pulses. Recall from the image that if the signal is filtered, the pulses get smeared and the noise blanker becomes ineffective. Thus, the noise blanker is most effective where receive bandwidth is greatest: right at the antenna, and not behind any receive filters. However, if there are strong signals present anywhere, even not necessarily at the tuned frequency, then these signals contain peaks which can look, to the noise blanker, like noise.

Different kinds of noise blankers have different ways of deciding what peaks are "noise" and what are not, and may be more or less susceptible to being confused in a particular situation. There are many kinds of noise, and many kinds of band conditions, so there is no one noise blanker design that works in all situations. Thus, one will always want the ability to enable or disable the noise blanker.

## Answer (score 4, by sm5bsz)

The traditional noise blanker that Phil, W8II describes is useless when there are strong signals within the passband of the blanker. Strong in relation to the interference pulses that is. Blanking the strong signals causes keying clicks that become stronger than the original interference...

There are two traditional ways, reduce the blanker bandwidth to place strong signals outside the blanker path or increase the bandwidth (very much.) At 100 times larger bandwidth the pulses contain 100 times more energy and are also 100 times shorter (if you are lucky) If the wider bandwidth does not give many more strong signals the 100 times larger bandwidth is a 40 dB advantage. In the seventies I was using a blanker on 144 MHz with a 5 MHz bandwidth with excellent results in Stockholm where many strong stations were present on the band: http://www.sm5bsz.com/blanker.htm

I was made aware of selective blankers a couple of years later: https://ieeexplore.ieee.org/document/1447305

My attempts to attenuate strong signals by use of NMR failed, but with the Pentium MMX enough CPU power had become available to do selective limiting in software. http://www.sm5bsz.com/pcdsp/sellim.htm (this is part of a description of my first SDR in a PC: http://www.sm5bsz.com/pcdsp/pcdroot.htm

Today anyone can use Linrad which has a feature to route strong signals outside the blanker. Here is a demo: https://www.youtube.com/watch?v=qMd5y036HtA http://www.sm5bsz.com/linuxdsp/blanker/leon2001/leon2001.htm

Operating the blankers in Linrad is non-trivial, but it can be very rewarding.

The Perseus v5 has a "vectorial blanker" which sometimes can be very useful. I do not know how it works but you can see some of it here: https://www.youtube.com/watch?v=sA36EzcS684

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1124/what-does-a-noise-blanker-really-do-and-what-are-the-side-effects, by oh7lzb, Phil Frost - W8II, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
