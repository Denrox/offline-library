# Why are proprietary codecs used in amateur radio?

*Tags: united-states, legal, encoding · score 18*

## Question

This may be slightly off topic (maybe there's a Legal Stack Exchange :-D), but how is it that codecs like Yaesu's C4FM are allowed to be proprietary while still being used on Amateur bands? At the very least, this does not seem to be in keeping with the nature of Amateur Radio.

## Accepted answer (score 11, by Zeiss Ikon)

The requirement on the FCC side of this is that transmissions may not be encrypted in order to hide their content. In the case of C4FM (or the other protocol mentioned in another answer, DMR, or as well in JT8/JT4) anyone can either obtain software or buy a device that supports these protocols and listen to the transmission. There would only be a violation of the FCC regulation against encryption of amateur transmissions if (one of) these protocols used a key or other means to prevent unintended recipients from decoding the transmission -- and that is apparently not the case, at least with DMR, JT8, or C4FM.

Even Morse code could be seen as a "transmission protocol" -- and one that "hides the content" from those who can't copy code. However, the code is public, and (in theory) anyone can learn to read and send Morse. Even if JT8/JT4 or C4FM aren't "public" in the meaning that anyone can write computer code to read the content of a JT8 or C4FM transmission, they are "public" in that anyone with an amateur radio license (of high enough grade) and money can buy the equipment or software that does this.

## Answer (score 4, by rclocher3)

There are lots of proprietary codecs used in amateur radio. They are allowed in most countries for amateur use simply because they have not been made illegal. But I don't think that's what you're asking.

I think most of us would agree that proprietary codecs are generally against the spirit of amateur radio; we prefer open protocols that anyone can use, adapt, and improve. So why does amateur radio not shun such proprietary codecs?

Every digital phone (voice) protocol in broad amateur or commercial use that I can think of, such as P25, DMR, and D-STAR, uses a proprietary codec, for the simple reason that at the time each protocol was developed, there was no alternative codec with the necessary performance. D-STAR was designed by the Japan Amateur Radio League (JARL), the Japanese national amateur radio association, in partnership with Icom.

Remember that one of the founding principles of amateur radio is "to contribute to the advancement of the radio art", to quote US government law 47 CFR § 97.1. The designers of D-STAR had to choose between advancing the radio art and the principle that amateur radio protocols should be open and free. The designers must have found the choice difficult: everything about D-STAR is open except the codec.

It should be mentioned that there are now free and open codecs, which didn't exist when D-STAR was created, that aim to compete with the proprietary codecs. FreeDV, a digital phone protocol for HF, uses the free and open codec Codec 2. WINMOR competes with PACTOR for sending digital messages over HF in the Winlink system.

## Answer (score 2, by Brian K1LI)

There is a legal corner of StackExchange, but the basic answer you seek is not very complicated. I am not a lawyer, but I am the inventor of a number of patented ideas, so I have experience in this area.

DMR is another proprietary CODEC used by hams, so C4FM is not unique. "Proprietary" in this context simply means that it embodies intellectual property (IP) whose ownership has been claimed by an inventor and granted by a governing authority. In general, you must obtain the IP owner's permission to use it. The owner may allow you to use the IP for free, or may require that you pay, or may set other conditions to use it. The fact that you are using "owned" IP in an activity that must be conducted "without pecuniary interest" does not pertain; the development, manufacturing and distribution of the technologies that enable the activity are not covered by this limitation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18280/why-are-proprietary-codecs-used-in-amateur-radio, by Joshua Nozzi W4JLN, Zeiss Ikon, rclocher3, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
