# IC-7200 S-meter behaves strangely - why?

*Tags: equipment-troubleshooting, icom · score 3*

## Question

I have Icom IC-7200 and can't get it to work properly. It works fine for TX and RX on FT-8 on 20 m, but when I try to use it the old fashioned way in SSB, I got some strange behavior:

- S-meter shows same ridiculously high(9..9+10) reading at quiet place between stations and at loud stations
- When I adjust RF gain to more, my S-meter shows less points

Reception is fine though. When I connect my G-90 to the same cable - I have S2-3 noise level, S9-9+ on loud stations, and similar reception, so probably my noise levels and antenna are fine.

Is this a normal behavior for 7200? Am I missing some crucial setting? Or is my TRX just broken?

## Accepted answer (score 2, by hobbs - KC2G)

Yes, that's normal behavior. When you turn the RF gain down, you're reducing te receiver's sensitivity, which means the lowest signal level it can detect goes up — and the lowest meter reading you see goes up accordingly. If it sits at S9 in a "quiet spot", that means that stations below S9 will be attenuated enough to be basically inaudible.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22933/ic-7200-s-meter-behaves-strangely-why, by someanonimcoder, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
