# Why is the measured loss low in an antenna with high swr?

*Tags: antenna-theory, antenna-system, impedance-matching · score 3*

## Question

I'm trying to understand the basics of antenna and feedline measurements with losses. I have a background in the sciences but not specifically in engineering. Nevertheless, I was doing some testing and wanted to either confirm or understand a specific outcome of my measurements. I'll preface this with that my measurements are not fully robust but do demonstrate basic antenna theory (plus I understand that high swr may damage my transmitter so no comments needed about that).

So, the setup is as follows. I have an 66ft endfed antenna with a 49:1 unun and 50ft of RG-8X coax. The antenna is designed for resonance on 40m, 20, 15 and 10m. I wanted to measure my antenna's performance on 30m at 10.110 mhz. When measured directly at the end of the 50ft coax with a VNA the S11 return loss is about -2db or an SWR of 11:1. When a tuner is placed near the transmitter the S11 return loss is -30db when tuned (as measured from the transmitter side).

**Test 1 - Xmit Power and Measured Signal Strength:** My antenna on 30m is mostly in an NVIS orientation and I have a websdr about 300 miles away that receives my signal well. I have the tuner setup at 1:1. At 40w CW the sdr receiver measures a constant S5 signal, at 20w it measures S4.5, 10w - S4 and 5w - S3.5. This clearly matches with theory that 1/4 of the power is a drop in 6db or 1 S-unit. I performed this multiple times and it reflected theory properly.

**Test 2 - Direct xmit with 11:1 SWR:** Removed the tuner and did the same test transmitting 40w directly connected to the end of the 50ft coax to the antenna with 11:1 swr. I confirmed the transmitter was still measuring the output wattage. The remote sdr measured drop was only a bit less than 1 S-unit across 40w, 20w, 10w and 5w or about 5db. So 40w measured at S4, 20w at S3.5 etc.

So, what is really going on here? I'm only losing 5-6db of signal with 11:1 swr. My assumption is that this answer -> [What is the actual loss in a feed line with high SWR?](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md) is what is happening (or power reflecting back and forth from the transmitter to the feedpoint). I used the KV5R line loss calculator and it suggests about a 2db loss on 10.11mhz with 50ft of RG-8X at 11:1 swr (https://kv5r.com/ham-radio/coax-loss-calculator/). No idea what the higher swr effect in the 49:1 unun is - but guessing at least another 1db.

Am I understanding this observation of high swr loss correctly? I know my measurements are not using proper equipment, but the external sdr measurements are consistent after many observations.

## Answer (score 2, by Ryuji AB1WX)

As you noted in your comment, the method has limitations.

1.

Your coax had no common-mode choke so that the coax could radiate.

2.

Every tuner has some insertion loss. It could be 0.07 dB, or it could be 2 dB, depending on the tuner.

3.

You measured SWR with 50ft of RG8X. (Loss at 10MHz is 0.45 dB when matched and much worse at SWR > 10, i.e. the measured SWR of 11 is an underestimation.)

So, keep those factors as potential sources of discrepancies. However, in this particular case, those factors may partially cancel each other overall.

SWR of 11 means a mismatch loss of 5.1 dB. That means 70% of the power is reflected and absorbed by the transmitter into heat, and 30% gets radiated. That's a bit less than 1 S unit, consistent with your observation.

A better way to experiment this is to use the transmitter and the tuner at the antenna's feedpoint with a very short coax, in addition to using a common mode choke on the feedline, a separate radial wire that is attached to the feedpoint directly. This way, the cable loss and cable radiation are non-issues.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22959/why-is-the-measured-loss-low-in-an-antenna-with-high-swr, by Don James, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
