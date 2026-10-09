# Some softwares that can decode CW, AX25, RTTY, PSK etc

*Tags: software · score 4*

## Question

What are some softwares that can decode CW, AX25, RTTY, PSK etc? Hope that the softwares provided are freeware or open source.

## Accepted answer (score 3, by Adam Davis)

MultiPSK will decode most of those, however AX25 itself is not a modulation scheme, it works at the data link layer, and doesn't specify the physical layer. More importantly, other applications go on top of AX25 so decoding AX25 by itself isn't that useful.

While many "all-in-one" programs like MultiPSK exist, you may find better results with individual programs for individual modulation schemes, depending on your exact needs. If you're just casually using them, they might be good enough, but if you're going for a specific use, feature, or need, then you may find specific programs for the one or two schemes you actually use will often have better support for that scheme.

## Answer (score 5, by rhaig)

fldigi is multi-platform and will decode many digital modes and has some rig control features available. Check at http://www.w1hkj.com/Fldigi.html for more information.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1665/some-softwares-that-can-decode-cw-ax25-rtty-psk-etc, by Harold Chan, Adam Davis, rhaig. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
