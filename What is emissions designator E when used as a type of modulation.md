# What is emissions designator "E" when used as a type of modulation?

*Tags: united-states, legal · score 10*

## Question

The FCC's rules regulating amateur radio, in 47 CFR 97.307(f), paragraph 8 defines one emissions standard/limitation as follows:

A RTTY or data emission having designators with A, B, C, D, E, F, G, H, J or R as the first symbol; 1, 2, 7, 9 or X as the second symbol; and D or W as the third symbol is also authorized.

(For context, this is describing one sort of [signal allowed at 51 MHz and above](What%20test%20transmissions%20are%20allowed%20above%2051MHz.md).)

Now, I was able to find definitions for most of these "first symbols", representing "types of modulation of the main carrier", in §2.201(c) of the FCC regulations:

- A: Double-sideband
- B: Independent sidebands
- C: Vestigial sideband
- D: Emission in which the main carrier is amplitude and angle-modulated either simultaneously or in a pre-established sequence
- F: Frequency modulation
- G: Phase modulation
- H: Single-sideband, full carrier
- J: Single-sideband, suppressed carrier
- R: Single-sideband, reduced or variable level carrier

All of the "second symbols", representing the "nature of signal(s) modulating the main carrier":

- 1: A single channel containing quantized or digital information without the use of a modulating sub-carrier, excluding time-division muliplex
- 2: A single channel containing quantized or digital information with the use of a modulating sub-carrier, excluding time-division multiplex
- 7: Two or more channels containing quantized or digital information
- 9: Composite system with one or more channels containing quantized or digital information, together with one or more channels containing analogue information
- X: Cases not otherwise covered

And the relevant "third symbols", representing the "type of information to be transmitted":

- D: Data transmission, telemetry, telecommand
- W: Combination of the above [presumably "no information", telegraphies, facsimile, data, telephony, television]

So that explains most of the allowable test transmissions for subbands that reference "paragraph 8" as an allowable emissions standard. But I can't find what "E" would mean as a first symbol! It's not in Part 2, it's not in the ITU regulations, it's not on Wikipedia…! What is §97.307(f)¶8 referring to when it allows "designators with […] E […] as the first symbol"?

## Answer (score 2, by SDsolar)

I remember back in the early 70s, when I was being trained by former WW II radio guys who were all Extra-class, and they explained that this is a confusing issue, because the common usage is not always the same as the rules. I was first licensed in 1971, when we still tuned (and were tested) in Mc (megacycles), even though MHz was the correct way to say it. Eventually the industry caught up (as the older Elmers became SKs) and now everyone says MHz.

### Answer: There is no official E in the first position.

Here it is from the horse's mouth:

### http://wireless.fcc.gov/services/index.htm?job=licensing_2&id=industrial_business&page=2

It is clear that this list is not the same as common usage. For instance, CW was regularly taught as being A1. That was the correct answer on all tests I took (the last Amateur test being in 1977, then on the General Radiotelephone test in 1983).

But we all know that Morse Code is not really CW.

The FCC's list would have a true continuous wave as being as N0.  
But the keying is considered to be a form of amplitude modulation, hence A1. So here the FCC is correct on the tests. It is us hams who are wrong to call it CW. :(

I have never encountered E in the first position.

The E designator in the third position simply means it is telephony - voice communications, which can be speech or music. Think analog.

For instance, AM is A3E. Amplitude modulation, single channel, telephony. But on the tests I took it was simply called A3. Back then it was in common usage by hams.

And most multiband ham transceivers and linear amplifiers still had the 11-meter band. Then came along CB, which required another license and more restrictions. That all changed when CB radio became too big to be licensed. (I had a mail-in CB license but then the FCC gave that up in favor of regulation). Hams that liked DXing on 11 simply moved to 10 on solar max years. (we're at a solar minimum right now - so 20 is best)

Then the hams almost completely dumped AM in favor of SSB to relieve band congestion. A lot of CBers followed suit, to get more than 23 channels. Then the FCC changed CB to include more channels - the 40 we have now, and a 12 W PEP limit for power. And they banned commercial manufacture of 11-meter switch selections for ham radio linear amplifiers, which lasted until the advent of wideband solid-state amplifiers. Then the CBers found that 12 Watts PEP on CB SSB was sufficient on solar max years to talk to the other countries (like New Zealand) who still had 11 meters for ham radio. Then the hams switched to FM on 10 meters to avoid QRN. And so on..

FM radio is F3E. Frequency modulated, single channel (even if it includes stereo encoding), telephony. If the FM station also transmits on subcarriers for SCA channels carrying entirely different programming, then that is called F8E. Stereo encoding is really a subcarrier, too, of course, but is considered part of the single channel because it is part of the same program. And we were taught that it is simply F3. Confusing enough?

Ham radio SSBSC (Single sideband suppressed carrier) has long been commonly called (and tested) as A3J because it is amplitude modulation, single channel, with suppressed carrier. SSB of this type can carry other kinds of analog audio signals such as SSTV, RTTY, AFSK, etc.

So when it is used simply to talk to other hams it is called A3J in common usage and on the tests, to differentiate it from A3 (AM).

But according to that FCC chart it would be J3E.

So here we are, 40 years later, and I would echo KL7AG, KL7AM, KL7IS and the other trainers: It is confusing, but the only time you would need to worry about this kind of thing might be for a test. In real life, just enjoy using it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6968/what-is-emissions-designator-e-when-used-as-a-type-of-modulation, by natevw - AF7TB, SDsolar. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
