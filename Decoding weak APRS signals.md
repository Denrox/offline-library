# Decoding weak APRS signals

*Tags: aprs · score 5*

## Question

I've recently started looking into APRS, and can easily receive some APRS signals from my station - however, I can't seem to decode them using QTMM or any similar software.

Is this because they're too weak / noisy, or am I doing something else wrong? I presume it's picking up an APRS envelope but failing a checksum or something similar - if there's any way to just get partial packet data I'd be interested in that as well.

## Accepted answer (score 2, by berry120)

I never did manage to decode the signal reliably, which I believe to be a combination of two factors - the radio I was using was attenuating the upper frequency somewhat, and there was some additional interference in the area. APRS also uses AX25 which is hardly the most resilient protocol - at 1200baud, you get a single sine wave oscillation for each bit, so if a slight bit of noise gets in there it's easy to see how the packet can be unreadable - there's not much room for error on the physical layer. FWIW, I've also later read that QTMM isn't the best decoding tool on the block - I didn't try many others since QTMM was so simple and appeared to work for audio clips I found online, but that could be the next port of call if I were to revisit the project.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5194/decoding-weak-aprs-signals, by berry120. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
