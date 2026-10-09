# What might this "spreading" interference be?

*Tags: rfi, signal-identification, mixer · score 3*

## Question

Any idea what might be causing this signal to appear in the "panadapter" spectrogram of my Omnia SDR around the 40m band?

Every twenty seconds, I get a strong "focused" signal that then rapidly spreads out its power — like all the power is concentrated at one frequency but then gets "spiralled" out within a certain (relatively narrow) bandwidth. This signal seems somewhat symmetrical, and is repeated every 12kHz or so across my waterfall.

Its exact characteristics/"sound" seems to change occasionally — for example tonight it repeated fairly consistently every 20 seconds for a long time, then went quiet for a few minutes, then gave one isolated (and slower) buzz. A few minutes later, it began repeating every 20 seconds again. This sort of thing happened a few months ago too.

I live near a power substation, and have some neighbors who weld, but neither seem a likely culprit, particularly given the usual streaks of consistent repetition of a shaped signal.

Given its symmetrical and repetitive nature, am I right to suspect there is some sort of intermodulation involved here — i.e. the actual noise source is simply a strong sweep that's getting mixed with something in my SDR? Then what are some ways I could determine its actual frequency and get a better/cleaner look at it? And any guess as to the source based on this information? Might it be some sort of radar, or more likely just somebody's malfunctioning digital panini press?

## Answer (score 4, by rclocher3)

If nobody is able to recognize what kind of signal you're dealing with by looking at your waterfall screen shots, then perhaps your best chance of identifying the signal would be to use old-fashioned RDF (radio direction-finding) techniques. If you can, consider borrowing a portable battery-powered receiver that can do 40m, and ideally also SSB, like a shortwave broadcast receiver or a Yaesu FT-817, with a portable antenna. A portable directional antenna like a loop would be ideal; those are fairly rare though, so you'd probably need to make do with a whip antenna. A whip antenna would obviously attenuate the signal quite a bit compared to a full-sized dipole or vertical, but often the problem with RDF isn't too *faint* of a signal, but rather too *strong* of a signal.

It's quite possible that the noise is coming from your own house or apartment. For that matter the problem could be a ground loop; if so, then you shouldn't be able to hear the noise at all in a portable receiver. Phil Frost also points out that the observed signal could be intermodulation or some other mixing product or other spurious signal generated inside the receiver; in that case, there might be external RFI on a different frequency, or no external RFI at all.

If you can hear the RFI in the portable receiver, then try flipping circuit breakers off, one at a time, and see if the noise goes away suddenly; if so, then you know the RFI generator is powered by that circuit.

If you can establish that the RFI isn't coming from your house, then if you know someone with a 40m yagi, then you might ask him or her which direction the signal seems to be coming from. If nobody you know has a 40m yagi, it may still be useful to ask other people to listen for the signal because the signal may be weak but coming from someplace close by.

From there, your best bet would probably be to drive around with the portable receiver and see if you can locate the source by using the signal strength as a "hotter/colder" style indicator. Of course that can be quite a challenge if the signal is intermittent.

Good luck! If you figure out what the noise source is, please let us know.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6498/what-might-this-spreading-interference-be, by natevw - AF7TB, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
