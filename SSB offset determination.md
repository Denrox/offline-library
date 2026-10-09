# SSB offset determination?

*Tags: software-defined-radio, ssb · score 6*

## Question

Is there any algorithmic way to determine if the mixed frequency offset in an SSB SDR demodulator is wrong (too high or low), other than listening for funny sounding voices? (perhaps by checking to see if voiced vowel spectral overtones fall in a harmonic series or seem inharmonic?)

## Answer (score 3, by Mike Waters)

**According to this 2010 Icom patent, there may indeed already be a way to do this.**

This method uses no pilot tone, carrier, etc. A brief excerpt:

In contrast with the above prior art, the invention requires no modifications to the transmitter and so a receiver equipped with this invention can be used with any SSB transmitter in use today. It can also correct for much larger tuning errors. As discussed in detail below, this invention analyzes the properties of the transmitted human voice, independent of language and retunes the receiver to the actual transmitted signal frequency with a high degree of accuracy. This can be done faster than a trained operator can retune the radio.

Apparently, this has never been put into production, which casts some doubt about the claims made there.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7180/ssb-offset-determination, by hotpaw2, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
