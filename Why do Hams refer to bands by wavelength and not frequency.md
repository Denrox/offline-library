# Why do Hams refer to bands by wavelength and not frequency?

*Tags: frequency · score 9*

## Question

I've noticed while reading literature and websites geared towards and written by amateurs and ham radio enthiuasts that frequency bands are commonly referred to by wavelength.

In professional environments I have been a part of, we always used frequency (170 MHz) or band name (ie VHF, UHF) to describe the signal.

Why do hams prefer wavelength? Is this tradion or convention? Is it more accurate?

I have seen VHF frequencies referred to by wavelength and UHF frequencies referred to by frequency in the same sentence, thereby lacking consistency.

## Accepted answer (score 3, by Edwin van Mierlo)

Just to add to the answers already given; there used to be a practice to call "CQ 40m" indicating you are indeed on the 40m band, avoiding stations to comeback to your call if your transmitter would have harmonics... say in the 15m band...

This was obviously a long time ago, when filtering harmonics was more difficult, and more difficult to measure/tune when building/operating equipment... and probably license conditions were different then today's.

Still this practice can be heard on the bands today, although modern transmitters would not have harmonics (or should not have harmonics) outside the band. I guess old habits die hard, especially in Amateur Radio.

I guess the practice referring to the bands is also a matter of "least effort to indicate". Which is already discussed in previous answers. Far more practical to say "I had some contacts on the 20m band" is stead of "I had some contacts between 14.000 MHz and 14.350 MHz"

or band name (ie VHF, UHF) to describe the signal.

To answer that part of the OP question: the indication of VHF/UHF, and respecively HF would be a too broad indication to be accurately describing the operating band.

If you would take HF alone, it would be 9 (or 10, or 11 bands) which are included, namely: 80m, 60m, 40m, 30m, 20m, 17m, 15m, 12m, 10m. Some will count the 6m band as HF and some will count the 160m as HF. Although I believe 6m is actually inside VHF and 160m is actually MF.

VHF would have 3, or 4 bands; 6m, 4m, 2m, and some regions will have an allocation at 220MHz.

And so on so forth; so the indicators "VLF, LF, MF, VHF, UHV, and higher" are not suitable for use for Amateur radio to indicate where you are operating, they do have their uses, and are used if a "broad term" is sufficient in the context of what is communicated...

## Answer (score 6, by Marcus Müller)

I'd agree with @user3486184's answer, that this is primarily an effect of tradition. However, what @DaveTweed answered hit the spot how that tradition came to be:

In early radios, you really had not much of a notion of electrical fields doing something periodic at a fixed frequency; these were simple crystal radios, doing nothing but taking the envelope of the (rectified) signal they were fed. They weren't radio frequency selective at all – the channel selection happened by *tuning the antenna* (ie. matching its resonant frequency to the channel you want to receive), not the receiver circuit, like in (most) modern radios!

So antenna designers were the people that actually executed the concept of channel selectivity first, hence they got some normative powers :)

Now, if you look at this, you'll notice that for someone who builds frame or long wire antennas, *wavelength* is an excellent description of what they'd be designing the antenna for. You can, within boundaries of material effects, usually scale any antenna design to a different frequency/wavelength by just multiplying its dimensions – and hence, someone who was able to build 200m antenna, was instantly also able to build one for 20m. They were the kind of people that build radio receivers that made it to the "living room customer market", and hence, they decided what as on the frequency selection scale. That was meters.

## Answer (score 5, by Dave Tweed N3AOA)

I think that one reason is that talking about the wavelength gives an immediate sense of the scale of the antenna required.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6255/why-do-hams-refer-to-bands-by-wavelength-and-not-frequency, by YetAnotherRandomUser, Edwin van Mierlo, Marcus Müller, Dave Tweed N3AOA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
