# Effect of using wrong injected frequency when tuning IF cans in an AM radio?

*Tags: am · score 4*

## Question

I viewed an interesting video of a restoration of an old AM portable radio. When the alignment steps were being done, the author commented he would inject a 455kHz signal into the radio (the IF of the unit) then peak the output with the tuning slugs. However, he punched in 445kHz into his signal generator and did the alignment without catching the error.

My question: it seems this would reduce sensitivity since the following parts of the circuit are working around the correct IF and the signal getting through would be on the attenuated shoulder of the tuned circuit. Is this correct?

Would there be any other effect from the error (like stations showing up 10kHz off, etc.)?

From my limited radio circuit knowledge, I think it's yes to the former and no to other effects, but a overview from an expert will be most appreciated.

## Accepted answer (score 4, by tomnexus)

A fun question to mull over. What does it mean for a receiver to be "on frequency"?

First there's the tuning dial and its indicator. This usually drives both the capacitor that resonates with the loopstick antenna, forming the first filter, and the LO tuning capacitor. You won't notice a 10 kHz offset on a tiny MW dial with its levers and pulleys, and the first filter will be much broader than 10 kHz and not track all that accurately anyway.

At the other end of the receiver, the detector is completely wideband, it will simply convert the IF voltage envelope to an AF voltage, at any reasonable frequency.

The selectivity of the receiver really comes from the fixed-frequency IF filter, which could be made in various ways. On an all-transistor receiver from before 1980? it could be a peizoelectric ceramic filter, with several coupled mechanical tuned elements forming a high order filter with good temperature characteristics, much easier done mechanically than electrically and only really surpassed by digital filtering. (see footnote)

Here is an example filter response (from Murata, quite a high performance modern part, surface mount, but no longer in production):  
  
You can see a) it's quite sharp, +10 kHz is right in the first deep null, but also b) the response rises up to only -40 dB further out, so the IF strip would benefit from some further rough filtering to protect the radio from further-out stations.

The rest of the IF strip is there to support the filter - some gain, perhaps variable gain AGC, and resonant matching transformers for the high (1500 ohm) impedance of the ceramic filter. These transformers are the ones with a ferrite tuning slug, they need to be adjusted for best performance. There might be other resonant circuits in the strip, in the amplifiers or for impedance matching.

It's surprising that the receiver could be successfully aligned a full 10 kHz away from the filter centre. The filter impedance at the null will be very different to the centre of its passband, so the tuning of the adjacent components might be way off, but I guess that as the rest of the filtering elements are fairly wide, it probably won't be too badly aligned.

So in summary, as you concluded, if the receiver has a fixed / non-adjustable IF filter, then it can't be off-frequency, only less sensitive, perhaps with a slighly asymmetrical response to nearby stations.

** About mechanical filters... see an interesting chapter of this wikipedia article about how the mechanical design of the matching network, from phonograph needle to acoustic horn, was influenced by new mathematical techniques invented for analysing electronic circuits, leading to a big improvement in sound quality of the gramophone.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22650/effect-of-using-wrong-injected-frequency-when-tuning-if-cans-in-an-am-radio, by rasher, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
