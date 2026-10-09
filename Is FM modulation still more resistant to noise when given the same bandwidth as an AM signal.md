# Is FM modulation still more resistant to noise when given the same bandwidth as an AM signal?

*Tags: modes, fm, noise, am · score 11*

## Question

FM modulated radio is much more resistant to noise and can deliver better sound quality than AM radio. But FM signals also use more bandwidth than AM signals. In general a wider bandwidth signal is more resistant to noise / can send more data than a narrower bandwidth signal. The bandwidth of an FM signal can in fact be chosen, and one can create wideband or narrowband FM signals, with the wideband ones giving better sound quality.

Is FM's better noise resistance only a function of its larger bandwidth, or is this noise resistance also an inherent property of FM? In other words, does a narrowband FM signal that uses the same bandwidth as an AM signal still produce better sound quality?

## Accepted answer (score 6, by Marcus Müller)

FM modulated radio is much more resistant to noise and can deliver better sound quality than AM radio.

Under certain conditions, that is! Namely, additive noise, and a fading channel.

or is this noise resistance also an inherent property of FM?

Huh, that surprisingly can be a pretty philosophical question about what bandwidth actually is, but let's break it down.

Let's first assume our noise is white. That means, we have a constant noise power spectral density. That's very handy arithmetically, because that means that the noise power is simply proportional to the observed bandwidth.

With AM, this simply means that audio SNR == RF SNR, if you use a filter that is as wide as the audio you want to hear.

With FM, ok, we first need to figure out what you mean with "the same bandwidth". Because that's pretty hard – the bandwidth occupied by an FM signal is actually hard to define, as its spectrum has a specific Bessel shape. Don't get me started.

Luckily, we have the Carson Bandwidth Rule, which gives us the amount of bandwidth needed to transport an FM signal to include at least 98% of energy.

That rule is

$$CBW = 2(\Delta f + f_m) $$

With $f_m$ being the highest audio frequency we need to transport, and $\Delta f$ being the frequency deviation, ie. the largest deviation from the nominal center frequency that the carrier will be moved to.

So, yes, the difference between AM and FM is that FM can actually make use of the higher bandwidth it uses to transport information. AM is damned to transport all info within the audio bandwidth.

On the other hand, that means that purely from a bandwidth in, bandwidth out perspective, you can never build an FM system that is more efficient than an AM system.

Then: let's look at the information side of things. What you want to do when communicating is getting info from A to B. Noise might be in the way, but really, what we care about is how much of the info from A reaches B.

So, let's say we pick an FM modulation that has a bandwidth $b$, and we define $\alpha$ as the ratio between the occupied bandwidth and the audio bandwidth.

$$b=2(\Delta f + f_m)=\alpha f_m$$

so, compared to the same audio signal transmitted using AM, we need to first reduce the bandwidth by a factor of $\frac 1{\alpha}$. Which means that only $\frac 1{\alpha}$ of the original info² reaches the FM receiver, *at all*¹.

The advantage of FM really is that it only is sensitive to apparent changes in frequency, not in amplitude. That brings us to the channel model:

Most channels exhibit fading of some sorts. That not only changes the amplitude of your receive signal over time (slowly, typically), but also over frequency. Which means that with AM, you might have bad luck, and just the let's say frequency 400 Hz of the carrier frequency is dampened very much, and you can't understand what the other end is saying.

With FM, certainly, you'll "hit" that frequency, too, but only for a short duration, and also, it doesn't really matter – as long as the noise power on other frequencies isn't higher, that does not impede the audio quality!

So, there's your inherent advantage of FM.

Technically, this is especially nice and easy to motivate: you're using an PLL to receive, that is, you don't look for phase changes that are faster than your audio signal's change rate (and that is, basically, the audio bandwidth) allows them to be. So, whilst your noise is certainly present on the whole CBW, what matters happens only within $2f_m$ around the current carrier position. Thus, FM makes use of the autocorrelation of the signal.

**Takeaway:**

- FM is *always* broader than AM for the same audio bandwidth
- FM isn't sensitive to noise in its whole bandwidth, but only to a specific part of it
- The channel is nicer to FM than it is to AM

¹: This presumes that the information is spread evenly through the audio bandwidth. It's not, but taking that into consideration quickly brings us to speech modelling, and discretized speech, and voice codecs. And why analog is a dead-end, and why we know that since the 80s. But that's simply out of scope.

²: I realize this is really hand-waving. We need to define *information* in the context of a continuous signal — that would lead us to differential entropy and whatnot.

Anyway, we can take a shortcut, by knowing the sampling theorem (which actually is more of a result of that consideration than something that leads to it, but nevertheless): Any analog signal of finite bandwidth $f_m$ can be digitized with a sampling rate of $2f_m$. Conversely, an analog signal of bandwidth $f_m$ can carry as much info as twice that bandwidth in digital numbers, given a fixed SNR (which defines how many bits can be in each digital number). Corollary, the discrete info transportable is proportional to the bandwidth, and that directly translates to an analog info content, with finite-resolution observers.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9096/is-fm-modulation-still-more-resistant-to-noise-when-given-the-same-bandwidth-a, by JanKanis, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
