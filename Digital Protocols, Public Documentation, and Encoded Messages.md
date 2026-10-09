# Digital Protocols, Public Documentation, and Encoded Messages

*Tags: digital-modes · score 4*

## Question

When is a new digital protocol considered "documented publicly" enough to be used for amateur radio transmissions?

Part 97 states the following about prohibited communications:

(a) No amateur station shall transmit: ... (4) Music using a phone emission except as specifically provided elsewhere in this section; communications intended to facilitate a criminal act; **messages encoded for the purpose of obscuring their meaning, except as otherwise provided herein;** obscene or indecent words or language; or **false or deceptive messages, signals or identification.**

[This answer](Can%20you%20base64%20encode%20or%20compress%20ham%20transmissions%20US.md) explains that it's OK to use "any technique whose technical characteristics have been documented publicly". But what counts as being documented publicly? An academic paper? Simply publishing the specification on a public website? Or is there some other standard?

**Footnotes:**

1. Apparently as per 47 CFR 97.309(b) and 97.307(f) there are certain bands where it's allowed to use an "unspecified digital code", which appears to mean encodings that are not necessarily publicly documented.

## Accepted answer (score 2, by Joshua)

**TL;DR - It comes down to the purpose of the encoding/encryption. If the purpose is to obscure the meaning of the communication, it's illegal. If the purpose of the encryption/encoding is anything else, it's fine.**

There are several examples of digital communications protocols that are actively in use, and some of them quite popular, whose encoding or decoding algorithms are not publicly available. Probably the biggest of those is D-Star.

D-STAR uses a closed-source proprietary voice codec (AMBE) that's patented by Digital Voice Systems, Inc. (DVSI)[16] because it was the highest quality and only codec available in silicon when the system was released. Amateur radio operators do not have access to the specification of this codec or the rights to implement it on their own without buying a licensed product. (https://en.wikipedia.org/wiki/D-STAR#Criticisms)

According to 47 CFR § 97.113(a)(4):

No amateur station shall transmit ... messages encoded for the purpose of obscuring their meaning, except as otherwise provided herein...

In the example of D-Star, the explanation was best said by KD0LIX:

DSTAR is a digital protocol for data and voice over RF. While there are plenty of arguments against closed or patent-encumbered protocols on amateur bands, DSTAR isn't encryption, it's just encoding. Since all DSTAR receivers can decode a DSTAR transmission on the same band, the barrier to recovering the meaning of a DSTAR message is relatively low, about \$200 for a Dv Dongle or \$500 for a transceiver. To contrast this with an encrypted radio, if you don't have the key, you're not going to be listening. (https://rsaxvc.net/blog/2014/2/1/Encryption_and_Amateur_Radio.html)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20984/digital-protocols-public-documentation-and-encoded-messages, by James KE5JOO, Joshua. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
