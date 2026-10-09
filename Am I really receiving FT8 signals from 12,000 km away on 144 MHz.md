# Am I really receiving FT8 signals from 12,000 km away on 144 MHz?

*Tags: digital-modes, united-kingdom, ft8 · score 11*

## Question

I have been using an Ettus B200 SDR to receive FT8 transmissions in the 2-meter band (144.174 MHz) using the WSJT-X software. Signals are received using a telescopic antenna inside on a window ledge with approximately 1 m of cable. I have made no effort to ensure the antenna is tuned, e.g., by adjusting the length.

I am located in the UK in grid square IO91. As expected, I mostly receive signals from the same grid square, and occasionally the grid squares adjacent. I see replies to messages which originated further away (based on the call sign).

Some received messages are obviously "incorrect", for example:

```
210113_084530   144.174 Rx FT8    -18  1.0 1545 Z50H+TSKY-JHO
210115_114630   144.174 Rx FT8    -17 -1.6  685 SIDE LOBE

```

Others seem like they might be real, but they are located in grid squares more than 10,000 km away.

```
210111_195445   144.174 Rx FT8    -16  0.3 1728 VI7JOW/P TO7JRB R BO96
210113_163545   144.174 Rx FT8    -17  1.3 1247 J06NQY A68ITS/R R QM30
210114_100830   144.174 Rx FT8    -18  1.0 2653 YI7ORO VD7XLO R CK63
210115_051015   144.174 Rx FT8    -23  1.8 2388 8L9VCM 3K9WKZ/P MF32

```

The call signs don't appear to be real. Is it safe to assume the message is corrupt? Or is there another explanation?

## Accepted answer (score 11, by Phil Frost - W8II)

I'd say these are simply corrupt. Take for example:

```
210113_163545   144.174 Rx FT8    -17  1.3 1247 J06NQY A68ITS/R R QM30

```

A68ITS doesn't seem to be a real call, but if it was, it would be a UAE call. The grid QM30 is in the Pacific ocean, about 800 km off the coast of Japan. This is a pretty unlikely combination.

The FT8 protocol includes error correction which reduces, but does not eliminate the possibility of false decodes. The nature of the coding also means when there are errors it doesn't change a character or two, but scrambles the entire message. The compression used by the WSJT protocols, which is optimized for the canonical WSJT QSO format, also means random garbage is biased towards producing something that looks like a QSO.

So while you shouldn't see this sort of thing day-to-day, if you search your logs for outliers you'll certainly find some.

## Answer (score 10, by hobbs - KC2G)

210115_114630 144.174 Rx FT8 -17 -1.6 685 SIDE LOBE

This is probably the one real one of the bunch, actually! The odds of random noise decoding as a freetext message with sensible English, especially radio jargon, in it are vanishingly small. This was probably from someone who worked someone on 2m FT8, and then after exchanging their grid squares, sent a followup message to say "that wasn't even off the front of the beam!" But since freetext messages don't carry a callsign or a grid square, you don't really know where it came from, unless you observed other messages on the same frequency nearby in time.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17891/am-i-really-receiving-ft8-signals-from-12000-km-away-on-144-mhz, by David, Phil Frost - W8II, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
