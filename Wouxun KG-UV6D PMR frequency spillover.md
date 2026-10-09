# Wouxun KG-UV6D PMR frequency "spillover"

*Tags: uhf, frequency · score 4*

## Question

So I recently bought a pair of Wouxun KG-UV6D. We don't have the license required to operate outside of PMR frequencies, but that's fine, as we will be using these for airsoft. The programming of 8 standard PMR frequencies used is pretty straight forward, but for some reason, I am experiencing "spillover". The channels I am programming into them are these:

- PMR 1:446,00625
- PMR 2:446,01875
- PMR 3:446,03125
- PMR 4:446,04375
- PMR 5:446,05625
- PMR 6:446,06875
- PMR 7:446,08125
- PMR 8:446,09375

But when I have one set to 446,00625 and the other to 446,01875, if I send with the 446,01875-radio, the other radio will pick up a lot of static noise. So far, I have tried setting squelch level to the least tolerant level, and channged the bandwidth from wide to narrow, but it is still picking up the static. Aside from that, the static seems to interfere with my laptop, randomly interacting with my media keys (fan boost, bluetooth etc.). I have set the step to 6.25K, and I will not be using this radio to access any repeaters. Also, I need to send with a TXP of 0.5, but seeing as the radio only has HIGH (4W) and LOW (1W), I stick to the low setting.

I am programming manually, and I am very, very green to radios. What am I doing wrong?

Edit: I made a short demonstrational video of what this interference sounds like: https://www.youtube.com/watch?v=TE7MekFMx-o - Take note that I am on the wrong frequencies in this video: I misread 446.- for 466.-

## Answer (score 2, by scivision)

The filtering for nearby frequencies in any radio is finite. According to the UV6D Specifications, the 12.5 kHz selectivity is 60 dB. The 0.8uV squelch threshold specification is -109 dBm. 1 Watt is 30 dBm.

You're getting less than 30 dB isolation from transmitter to receiver in those tests based on the very short separation, so you're feeding about 0 dBm into the receiver from the transmitter, and the specified 12.5kHz selectivity is about 60 dB, with a squelch threshold of -109dBm, tallying up to:

0 dBm - 60 dB = -60 dBm >> -109 dBm ==> Static noise when transmitting on channels 12.5 kHz apart in the same room.

Neglecting the legality issues other answers discussed, a solution is to use the most widely separated (in frequency) channels when radios not wanting to communicate to each other are in close proximity. For example, if you have a golf course, put the caddies on channel 1 and the host staff on channel 8, and so on.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1776/wouxun-kg-uv6d-pmr-frequency-spillover, by David Skødt Lauritsen, scivision. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
