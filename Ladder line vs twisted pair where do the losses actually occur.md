# Ladder line vs twisted pair: where do the losses actually occur?

*Tags: feed-line · score 4*

## Question

I don't understand why 14 AWG XHHW-2 wire would work fine when used in ladderline for high-power HF transmission, but the same wire would exhibit higher losses when used in a twisted pair configuration.

Can anyone explain to me why ladderline has lower loss than twisted pair?

## Answer (score 5, by webmarc)

You should also check out this answer to a related (but not duplicate) question over on electronics SE; in relevant part:

The main limiter of the bandwidth is from the attenuation, which increases as the frequency of the signal increases (mainly due to the skin effect).

Skin effect is a culprit here, though there may be others. Because ladder line has a higher characteristic impedance, there is less current and less opportunity for skin effect losses at a given power input.

With the legs of the transmission line now **much** closer together, greatly increased capacitive coupling (and dielectric losses as a result) are probably a contributor also, but I'm starting to get out of my depth on that topic and invite others to edit this as appropriate.

The upside to TP is that it's far less sensitive to environmental considerations: you could get away with running TP near metallic objects that would more drastically impact ladder line.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22386/ladder-line-vs-twisted-pair-where-do-the-losses-actually-occur, by Mark K1LSB, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
