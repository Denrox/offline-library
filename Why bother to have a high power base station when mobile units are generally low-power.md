# Why bother to have a high power base station when mobile units are generally low-power?

*Tags: rf-power · score 9*

## Question

I want to find out why, say in a GSM/cellular system, a base station can be up to 50 watts however the mobile units can be only 100mw (for example).

Surely if the base station ever uses 50w to reach a mobile at long range, the mobile will have no chance to transmit back.

I understand that on a base station receiver tech is perhaps more sophisticated / bigger and better then on a mobile unit, but why would there be such a large difference in max power? - why not limit the base stations to 5 watts or such?

**EDIT**

Note: Only using GSM as an example, but question stands for any technology. Here is what I think I know already:

- Difference between a 1W mobile and 50W base station is 17 dB.
- Base Station Diversity can add up to 5-6 dB gain, which would balance a 1W mobile to a ~4w basestation
- MIMO is on both sides, so this would be roughly equal gain and so would probably not be relevant in this topic (although the BTS with its larger antennas + better spacing may be able to get a few more dB gain).

Is the antenna technology in the base station that much better - they are larger, higher, and directional...

## Accepted answer (score 6, by tomnexus)

The link is actually balanced, because the base station receiver has *diversity gain*.

2G and 3G cellular systems use two antennas at the base station (for each coverage direction). They are either spaced a few metres apart, or more commonly, +45 and -45 degree polarisation, in the same housing. With two antennas and two receivers, the base station has a much greater probability of receiving the handset, above some threshold. If one antenna is in a null, the other might not be.

The base station also transmits from one of the antennas. Your phone doesn't have two antennas, so can't use diversity to increase its probability of receiving the signal. But the base station transmits a lot more power, and this compensates somewhat for the lack of diversity.

The phone is about 1W, but if it's close to the base station, it may be instructed to turn down its power, to save battery and to balance all the mobile signals at the base station receiver.

Diversity is related to MIMO, but is not the same thing. A diversity receiver *selects* the best signal from the two antennas. A MIMO receiver *combines* the two signals in the optimum way.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5375/why-bother-to-have-a-high-power-base-station-when-mobile-units-are-generally-l, by code_fodder, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
