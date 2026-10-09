# Where to apply for an amateur LTE radio license in the USA?

*Tags: license · score 6*

## Question

Where do you apply for a license to operate on the LTE radio spectrum for amateur radio in the USA? Can this amateur license be used to operate a cell phone independent of a carrier?

## Accepted answer (score 13, by baumgart)

An amateur radio license only grants privileges on the amateur bands. You would need a different type of license to use other bands. The cell companies pay a premium for the license for their spectrum, and they are almost certainly not interested in relicensing it (if they even could).

Moreover, LTE is just a protocol, so there is no dedicated spectrum for LTE in general. Each company that uses LTE uses their own spectrum, which differs per carrier.

So no, an amateur radio license does not let you run your own cell phone independently of carriers. It grants you privileges to use certain modes (voice, Morse code, etc) on well defined spectrum, but does not grant privileges for what you're asking about.

## Answer (score 10, by James Body)

I am a UK licensed Radio Amateur with some 39 years experience. I also design and build LTE cellular systems for a living.

The best suited Amateur Radio spectrum for LTE operation is the 2.3 GHz band - this can easily accommodate a LTE-TDD (single frequency) system operating in LTE Band 40.

Note that both FCC (and European) regulations for Amateur Radio do not allow the transmission of ENCRYPTED communications - and that LTE is designed with encryption integrated into the system; however, this can be got around by using PUBLICALLY KNOWN keys, i.e. use keys consisting of all'0's.

I can see Amateur LTE being particularly useful in emergency/disaster situations as a means of communicating with members of the public in distress - although there are more regulatory issues involved with licensed amateurs communicating with unlicensed operators.

Alternatively, as a previous poster has indicated - it is possible to obtain an experimental license from the FCC for LTE operation. Note - it is *not* possible to run a commercial service on experimental spectrum.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1584/where-to-apply-for-an-amateur-lte-radio-license-in-the-usa, by iphoneguy38440, baumgart, James Body. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
