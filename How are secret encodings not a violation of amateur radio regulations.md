# How are secret encodings not a violation of amateur radio regulations?

*Tags: legal, fcc, d-star, dmr, encryption · score 13*

## Question

[This question](Why%20are%20proprietary%20codecs%20used%20in%20amateur%20radio.md) asks if proprietary encodings are "in keeping with the nature of" of ham radio. The accepted answer notes, at least in regard to FCC regulations, that if anyone can buy encoders and decoders (as hardware or software), then it's not considered encryption.

Is that a documented ruling by the FCC? (I don't doubt that it's true — I just wonder if they wrote it down.)

There is a difference between proprietary/patented/licensed and secret encodings. You can have something that is proprietary, patented and requires paid licenses, but the format is openly documented. E.g. video formats like H.264 and HEVC.

The FCC and international amateur radio regulations say that transmissions "shall not be encoded for the purpose of obscuring their meaning" (with an exception for satellite control).

My understanding is that the AMBE voice codec used by D-STAR, System Fusion, and DMR is secret.

If such an encoding is secret, then the purpose is very much to obscure the meaning. Specifically, the purpose of the obscuration is to prevent an independent implementation, requiring you to obtain a decoder from them or their licensees. Only they hold the key to unobscuring the transmission.

I can see how it would be legal to have to buy a license or a licensed device, but how is it legal to have a secret encoding that obscures the content of the transmission?

## Accepted answer (score 6, by user71659)

My understanding is that the AMBE voice codec used by D-STAR, System Fusion, and DMR is secret.

That is mostly incorrect. The IMBE/AMBE+2 codec is standardized and documented as part of P25. The same codec is also used in DMR, System Fusion and NXDN.

It is an official ANSI standard, ANSI/TIA-102.BABA. Thus, it is similar to your examples of H.264. (Search for BABA).

The original full-rate IMBE codec was published in 1992. As it is 32 years old, the codec used in conventional P25, System Fusion Voice Wide, and NXDN 12.5 kHz should be patent-free.

The half-rate AMBE+2 codec, used in DMR, P25 Phase II, System Fusion Digital Narrow, and NXDN 6.25 kHz was published in 2009 and is believed to be patent encumbered until around 2028.

The outlier is D-STAR's 3600/2400 bps codec mode, which is incompatible with either P25 mode. I do not know if that one is officially documented anywhere, but the D-STAR spec was published in 2001, it should be off-patent now or soon.

## Answer (score 4, by webmarc)

First, thank you for asking this question, it's a fun one to explore!

### Is that a documented ruling by the FCC?

I haven't found any documented ruling by the FCC on your question... but I believe your question includes some subtle mistakes in the facts available regarding 1) purpose vs effect, and 2) secret, both of which combined might explain why the FCC hasn't been moved to rule.

### Think RTTY

Before software RTTY decoders were widely available it had the exact same **effect** though obscuring comms were clearly not the **purpose** or intent. You had to buy equipment or you were not able to decode. This is after WWII and before FCC explicitly contemplated RTTY (which was make/break on HF because FSK wasn't yet an approved mode)

### USPTO has it, and so do you

I think you're mistaken regarding "is secret" : The algorithm is patented and filed with the USPTO, making it a matter of public record. It may not be commercially reproduced, but since private individuals can recreate it for their own use this seems to satisfy the spirit of the regs. There's even open source software available for decoding.

### But what if?

Because I love hypotheticals in the law, take a quick trip with me.

Even if the encoding was still secret, an argument to be made might be as follows:

The relevant reg is §97.309(b) (RTTY and data emission codes). In part:

... a station may transmit a RTTY or data emission using an unspecified digital code ... data emissions using unspecified digital codes must not be transmitted **for the purpose of obscuring the meaning** of any communication... [emphasis added]

In your question you note that:

If such an encoding is secret, then the purpose is very much to obscure the meaning

I think you're conflating **purpose** with **effect**. The purpose of Icom et al in using AMBE vocoders is not to obscure, but rather to achieve high quality digital comms (whether they hit the mark or not is outside of the scope of the question and this answer). A **side effect** of this is that people without their equipment cannot decode.

Also, a proper legal analysis would probably note that it's not Icom's intent/purpose that matters in that FCC reg... it's the Amateur Operator's intent! I would argue that an operator, by using widely available commercial technology that may be obtained by anyone with or without a license, cannot be considered "intending to obscure." I would expect that a judge would be more likely to agree than not, especially in light of the apparent decline in the Chevron Deference principle in recent SCOTUS rulings.

Now, it's certainly possible that if the codec were secret that there might be some other FCC rule or broader USC reg that would control, but I define that as out of scope for my hypothetical :-)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22768/how-are-secret-encodings-not-a-violation-of-amateur-radio-regulations, by Mark Adler, user71659, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
