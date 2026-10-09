# Advantages of using Digital Code Squelch

*Tags: rfi, tone-squelch · score 6*

## Question

I am trying to decide whether or not I should use a CTCSS (Continuous Tone-Coded Squelch System) or a DCS (Digital Coded Squelch) for my mini repeater I just set up.

What are the advantages of using a DCS over a CTCSS?

I am in an area with a lot of RF noise, and I think DCS may help keep some of that noise out.

Which method will pick up a weaker signal?

What factors should I consider when choosing the squelch method?

## Answer (score 6, by Trevor Johns)

DCS (aka DSQ/DPL) provides a *slightly* larger range of codes to pick from compared to CTCSS. This means less chance that a nearby station will accidentally overlap with yours.

Specifically, DCS gives you 83 codes, whereas CTCSS gives you somewhere between 26-50 squelch tones depending on the radio -- manufacturers have added extra codes over time. For compatibility, you're probably best sticking to the original 26. Here's a list:

http://www.repeater-builder.com/tech-info/pl+dpl.html

(Fun fact: Technically DCS has enough address space to support 512 codes, but the majority of those are disallowed in order to prevent false positives because of the way the DCS protocol works. So 83 is what we're stuck with.)

So, those 26-ish tones vs 83 codes are the biggest difference. Practically speaking though, there's a few other considerations:

- CTCSS is compatible with older (cheaper) equipment. DCS didn't come around until much later, so it's not uncommon to find radios on eBay that only support CTCSS.
- CTCSS is a bit more forgiving to implement, since it requires less bandwidth. Again, mostly an issue with older radios.
- CTCSS is purely analog, so if you're building a radio from scratch it would probably be easier to implement. Decoding a DCS signal obviously requires a digital processor.
- DCS is less likely to trigger accidentally. Some CTCSS tones share harmonics with the local power grid, for example. Also, some old/cheap radios with noisy/slow circuits can accidentally trigger adjacent CTCSS tones, so some guides recommend only using ever-other tone.
- DCS is much less common on the amateur bands, which further reduces the chances of a collision if you use DCS.

That said, the range is about the same for both. And neither will behave differently in the face of RF noise, since the squelch is either completely open or closed at any given time.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3770/advantages-of-using-digital-code-squelch, by Skyler 440, Trevor Johns. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
