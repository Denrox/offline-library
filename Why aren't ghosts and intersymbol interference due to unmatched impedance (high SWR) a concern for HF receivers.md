# Why aren't "ghosts" and intersymbol interference due to unmatched impedance (high SWR) a concern for HF receivers?

*Tags: hf, receiver, impedance-matching · score 7*

## Question

In amateur radio, we care about impedance matching when we need to keep the load within the equipment's specification (for best performance, or just to avoid damaging a transmitter), when we want to maximize the power delivered into the load, or when a minimum noise figure is desiable.

When the reasons above are not a concern, impedance matching can be ignored. For example, in the question [What is the relationship between SWR and receive performance](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md), Phil Frost answered that "There is no relationship between SWR and receive performance". Surely, modern electronics have a lot of gain, and on HF, the inherent noise from the environment is often already much greater than noise floor of the radio receiver, as long as the SNR is reasonable, a HF receiver will happily receive everything coupled into it, even a random wire works, in this case, matching is pointless or sometimes counterproductive.

Nevertheless, they are not the only reasons for wanting a matched impedance or low SWR. In video engineering and high-speed digital systems, impedance termination (often by a resistor) is usually **mandatory**, even if it decreases the power delivered into the load, because of another reason: the reflection on the transmission line causes signal distortion. In analog video, the reflection causes "ghosting" on a TV screen. In digital systems, the reflection causes intersymbol interference that increases the error rate of the transmission, or creates unacceptable overshoot and ringing.

However, I don't see this issue discussed by any amateur radio publication. Why?

I assume it's not important, either because it's

1.

Only relevant for higher-frequency signals above HF. Within HF, the wavelength is long, so these adversary transmission line effects don't show up.

2.

It's only the case for high speed, wide bandwidth (a few megahertz or more) signals. On HF, bandwidth of a signal is measured in kilohertz. We never use wide-bandwidth signal on HF.

But I'm not sure which one is the case.

## Accepted answer (score 11, by Phil Frost - W8II)

Intersymbol Interference (ISI) — or analog equivalents, like ghosting — are relevant only when the difference in time of arrival between the primary and reflected signal are significant compared to the symbol duration.

For example, PSK 31 has a symbol rate of 31.25 baud, meaning each symbol is 32 ms long. If the difference in arrival time is significantly less than 32 ms, the reflection will arrive before the next symbol, so there's no significant ISI.

100 meters of feedline, with a 65% velocity factor, introduces a round-trip delay of about 0.001 ms. Being much less than 32 ms, this wouldn't introduce any significant ISI for PSK31.

What about modes with a faster symbol rate?

Generally, they don't get too much faster on HF. This is because the typical HF skywave channel is already a multipath channel. Unlike a line-of-sight channel where there's just one path from receiver to transmitter, an ionospheric channel has multiple paths, each with a different lengths. This is because the ionosphere isn't a smooth mirror, but rather an undulating, multi-layer ionized gas.

ITU Recommendation F.1487 quantifies the *differential time delay* for various HF channels, that is the time difference between the first arrival of the signal and the last. It's 0.5 ms under the very best conditions, and as high as 7 ms under poor conditions.

HF modems typically cope with this issue by using a slow symbol rate. For example, FreeDV uses a 1450 bit/s modem, quite fast by amateur HF standards. But it does so at a symbol rate of 50 baud, meaning each symbol is 20 ms long. DRM broadcasts have several modes, with the fastest symbol duration being 16.66 ms.

These long symbol durations make the differential time delay of the HF channel, as well as any additional delay added by feedline reflections, relatively insignificant.

## Answer (score 3, by hobbs - KC2G)

Some of both, but I think the second effect is dominant. The rest of this post is all my analysis from scratch as a non-EE, so hopefully it makes sense.

Let's say we have an antenna at the end of a 100-meter (electrical length) lossless transmission line that's mismatched to the antenna by a 10:1 SWR. We'll assume that there's perfect reflection at the transmitter end of the feedline (so the transmitter is a perfect current source, doesn't dissipate anything, and can withstand whatever voltage is necessary).

10:1 VSWR is an 0.82 voltage reflection coefficient, which amounts to a 0.67 power reflection coefficient. If we send a pulse from the transmitter, 33% of power goes into the antenna and 67% of power gets reflected down the feedline, reflected again, and comes back for another try, 33% of that 67% is absorbed by the antenna, etc. etc. Those two trips along the feedline take 667 nanoseconds. $ 0.67^2 \approx 0.45 $, so after 1.5 round trips, over half of the power has made it into the antenna. Those 1.5 round trips take 1 microsecond, so any modulating signal with a bandwidth less than 1MHz will survive pretty much intact. $ 0.67^{12} < 0.01 $, so after 11.5 round-trips, more than 99% of the power has been delivered, and anything under 130kHz is going to have pretty much undetectable distortion. Since our signals on HF are almost always under 6kHz wide (and usually under 3kHz) this seems pretty safe.

Modifying our simplified system by adding loss in any part of it, or making the mismatched section shorter than 100m, or making the SWR lower than 10:1, all make the reflections die down that much faster, giving a more favorable result.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15508/why-aren-t-ghosts-and-intersymbol-interference-due-to-unmatched-impedance-high, by 比尔盖子, Phil Frost - W8II, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
