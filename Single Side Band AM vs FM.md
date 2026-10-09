# Single Side Band AM vs FM

*Tags: ssb, fm · score 8*

## Question

I know the difference between AM and FM, but could anyone explain to me what is the differences between single side band AM and conventional FM?

So far as I know the SSB modulation will reduce the transmitting power. But what is the exact function of SSB AM compared to FM ?

Hope someone can explain to me, thank you!

## Accepted answer (score 13, by AndrejaKo)

First of all, you're not 100% right that SSB will reduce transmit power.

I often keep talking on SE about power spectral density. So let me start with that again and first assume that we have a radio that has fixed output power of 100 W.

So let's first take a (simplified) look at AM:  We have a carrier and two sidebands. One sideband, the part in red on the picture, actually carries useful information. The carrier is not needed, if we can precisely tune to the frequency, and the other sideband is just a copy of the red sideband. What is important is that when we sum the power over the frequency, we'd get the full power that the transmitter can provide. So for 3 kHz of audio bandwidth, we have 6 kHz of RF bandwidth and 100 watts unevenly spread out over that range.

Now when we're looking into SSB, first we need to better define AM. The usual colloquial AM is actually amplitude modulation, double sideband with carrier.

SSB is also AM, just as you mentioned, but it's amplitude modulation, single sideband with suppressed carrier.

In this case, for 3 kHz of audio bandwidth, we'll have our 100 W spread over not 6 kHz, but just 3 kHz. Furthermore, the carrier is eliminated as well, reducing the wasted power even more. Also, only the useful information from the red sideband is transmitted. So we can either run SSB at lower power, and get same useful density as with AM, or we can run SSB at high power and get much higher density compared to AM, resulting in better signal.

In case of FM, we'll get a symmetrical spectrum again:

In this case, we'll usually get wider spectrum than usual AM which will be from around 10 kHz (European CB) to 25 kHz (older "wideband" FM transceivers, still used for amateur radio in some areas). The usual formula is BW=2*(Baudio+MaxDeviation). So for our 3 kHz of audio and deviation of 2 kHz, we'll need 2*(3+2)=10 kHz of bandwidth. It should also be noted that until recently, it was difficult to get low deviation values.

So again, we'll be spreading out our 100 W over wider bandwidth. On the other hand, FM does not suffer from the same issues as the AM does, so we basically get better audio quality from FM than we get from AM. The downside is that FM requires "large" bandwidth, resulting in lower power spectral density at the receiver. For line-of-sight communications, usually, the received power is more-or-less OK, so we can afford to waste some bandwidth for higher audio quality.

On the other hand, when we need to cover grater distances, this can be an issue, and that's why SSB is often used. On shortwave, we also have the problem of bandwidth. One FM channel is around 3 SSB channels, so in cases where bandwidth is highly constrained, FM can be a problem.

So why aren't we just using wide SSB on VHF/UHF, where we have plenty of bandwidth?  
Well, the reasons are a bit historical. Basically, FM is much more immune to badly adjusted transmitters and receiver frequencies, compared to SSB and it's more difficult to create stable frequency reference in a mobile rig. Furthermore, up until recently, it was a bit hard to make a small, compact, SSB transceiver. In the meantime, FM infrastructure already entrenched itself, so there's not as much demand for such devices.

## Answer (score 10, by Phil Frost - W8II)

Firstly, FM is a constant-envelope modulation, meaning the amplitude is constant. SSB, being a kind of amplitude modulation, obviously does not have a constant amplitude. Consequently, FM can employ a non-linear amplifier which is more power efficient, and thus has a longer battery life in mobile operation.

Secondly, SSB signals add with each other and also noise linearly. This can be good or bad, depending on what you are trying to accomplish. For example, aviation communications use AM so if two stations transmit at the same time, both can be heard. With FM, only the stronger station will be heard due to the FM capture effect. Bad for air traffic control, but it also means better noise rejection in the demodulated audio.

Also, SSB channels are narrower, only as wide as the baseband passband. For voice channels this is typically 4 kHz. The width of an FM channel depends on the deviation in use, but for VHF amateur use channels are usually 15 kHz wide. As the channel gets wider, the noise power in it increases, and assuming a constant transmitter power, this means signal-to-noise ratio goes down.

So as a general rule, a narrower channel means more range for every watt of transmiter power. This makes SSB a better choice for long paths on HF. On VHF and higher, range is usually limited by terrain and not power. The natural noise floor is also lower. This makes the power efficiency of SSB less important, and the increased signal quality of FM tends to win out in most applications. Long or weak path VHF applications such as moonbounce, EME, or 6M DX huntin favor SSB over FM for this reason.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6847/single-side-band-am-vs-fm, by hellojoshhhy, AndrejaKo, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
