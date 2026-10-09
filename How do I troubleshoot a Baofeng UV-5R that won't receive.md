# How do I troubleshoot a Baofeng UV-5R that won't receive?

*Tags: baofeng, ht, equipment-troubleshooting, uv-5r, chirp · score 13*

## Question

I have a couple of Baofeng UV-5R radios. I have a profile in Chirp that works great on one of them, and I foolishly pushed that profile straight over to a UV-5R without checking firmware versions. Chirp crashed, and now the radio won't receive. I've tried resetting it to factory settings, downloading the factory settings in chirp, and then importing a csv of my channel configs, but it still doesn't make noise when I transmit.

I have noticed that it *does* receive when I hold the MONI button, but there's no indication of reception if I don't hold that button down. It appears to behave like the squelch setting is too high, but it's currently set to 3.

For what it's worth, the radio still transmits just fine.

## Accepted answer (score 14, by Benson)

I did a bit more reading, and it seems that the new version of the firmware meant I needed to use a different chirp profile. The solution that worked for me was to find a factory image from a radio with the firmware version I have (which Chirp reported), then import my channels via csv, and clone that resulting image onto the radio.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2127/how-do-i-troubleshoot-a-baofeng-uv-5r-that-won-t-receive, by Benson. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
