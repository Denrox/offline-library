# Required SSB sideband and carrier suppression?

*Tags: united-states, legal, ssb · score 8*

## Question

Is there a legal (U.S. FCC) or a commonly accepted standard requirement for SSB opposite sideband and and carrier suppression for either manufactured or kit built transmitters?


Does the 43+ dB down spurious emissions CFR 97.307 rule apply? Or some other metric? (for new stuff, not pre-mid-70’s tube transmitters).


How well did the old tube transmitters do in this regard?

Added: If there is no legal or regulatory requirement, what might be considered "good practice" on HF amateur bands when attempting to transmit SSB (e.g. not AM or DSB) from a home-built or experimental transmitter.

## Accepted answer (score 4, by Mike Waters)

There is no such specific legal requirement, because AM and double-sideband suppressed carrier (DSBSC) are allowed.

*Different emission types occupy different bandwidths*, as the FCC clearly acknowledges below.

**§ 97.307 Emission standards.**

(a) No amateur station transmission shall occupy more bandwidth than necessary for the information rate and **emission type** being transmitted, in accordance with good amateur practice.

There is a vague phrase that says that an amateur's signals should conform to 'good engineering practices'. However, there are in fact very wide emissions such as ESSB (8 kHz wide), and the FCC does not cite stations for that.

When I was in high school, I found plans in an amateur radio publication for converting a WWII surplus Command Set transmitter to DSBSC (which I successfully built). It is highly doubtful that the articles would have been published if that were an illegal mode.

## Answer (score 3, by Brian K1LI)

Collins was the long-established "gold standard" for amateur radio equipment. The 32S-3 quotes carrier and unwanted sideband suppression at -50dB; the later, solid-state KWM-380 improved opposite-sideband suppression to -55dB. The Signal/One CX-7 made a big splash in the amateur market; carrier and unwanted-sideband suppression are listed at -60dB. Modern rigs like the Elecraft KX-3 use less expensive modern digital and mixed-signal means to deliver 60dB or better suppression without using crystal or mechanical filters.

In the era of the 32S-3, amateurs in the US were limited to 1000W DC *input* power. At the roughly 50% practical efficiency of class AB amplification, the legal output limit would be around 500 watts. 50dB of suppression would have limited the opposite-sideband power to approximately 10 *milliwatts*! This would have been extremely unlikely to disturb adjacent stations unless they were very close to the transmitter. In the current era, 60dB of suppression means that a 1500W legal-limit signal would be reduced to 1.5 *milliwatts*!

INRAD still produces crystal filters for such "vintage" equipment. In addition to the IF frequency, these units are characterized by "shape factor," the ratio of the bandwidth at -60dBc to the bandwidth at -6dBc. A typical 8-pole, 2.1kHz filter exhibits a 1.5:1 shape factor:

Clearly, the attenuation continues past -60dBc, but this demonstrates the useful limit as perceived by companies' marketing departments!

For comparison, here is the shape of a 5-pole crystal filter shipped by one of today's leading amateur equipment manufacturers:

Note the much gentler "skirts" on the filter passband, resulting in a shape factor of about 3:1. "Baseband" filters, whether analog or DSP, may be used to combat interference and/or restricted emitted bandwidth.

Despite the relatively high cost compared to "phasing" gear, nearly all SSB transmitting equipment used the filter method, to take advantage of its superior opposite-sideband suppression performance. (Note: carrier suppression results from the use of balanced modulators.) It may be speculated that the "transceiver" owes its existence to the desire to control product cost and improve receiver performance by sharing the expense of the IF crystal or mechanical filter between transmitting and receiving duties. The low cost and high performance possible with modern digital and mixed-signal technologies may encourage a return to separate receiver and transmitter units to permit independent optimization of the respective signal chains.

## Answer (score 2, by K7PEH)

Answer (one example) to the third question: How well did the old tube transmitters do in this regard.

In summer after high-school I started building a Phasing type SSB exciter based on a circuit that appeared in the 1965 ARRL Handbook. This exciter was of course tube based. It used a set of coils and trimming capacitors for each band (80,40,20) and I only did the 20-meter band as it was the easiest to do.

I finally got it to work during the summer after my freshman year in college (summer of 1966). One of the tests described in the article that appeared in the Handbook (and I still have my copy) says that the lower side band and carrier (20-meters operating on USB) should be down at least 30 dB from the tuned USB. Assuming 6 dB per S-unit, that is about 5 S-units on my receiver's S-meter and I rememember looking at that and then adjusting the trimming capacitors for a deeper suppression of the signal. I had work to do because I was not quite reaching 5 S-units. My receiver was Hammarlund HQ-170AC.

Unfortunately, I never did finish that project as college got too busy and I dropped out of my ham radio hobby and either sold or gave away all my equipment. Also, as I remember my time doing that, the accuracy of my testing experiments might have been compromised a little by having the cover off the SSB exciter and sitting on the work bench right next to my receiver. So, I most likely was also hearing signals before the circuits designed to suppress carrier and opposite sideband.

The article in 1965 ARRL Handbook (A Phased Single Sideband Exciter, page 286) does not refer to any official FCC requirements on carrier suppression or sideband.

P.S. I have a photo of this exciter although it does not show much more than the front panel.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15007/required-ssb-sideband-and-carrier-suppression, by hotpaw2, Mike Waters, Brian K1LI, K7PEH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
