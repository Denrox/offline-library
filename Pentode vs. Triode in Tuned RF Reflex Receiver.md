# Pentode vs. Triode in Tuned RF Reflex Receiver

*Tags: receiver, equipment-design, vacuum-tubes · score 6*

## Question

I'm planning on building a multi-band vacuum tube receiver. I've got a circuit diagram in hand for a two triode twin reflex with optional regeneration (P.E. Edelman, *Reflex Radio Receivers*, 1924, Fig. 35, also discussed here), and expect to use modernized plug-in coils to cover broadcast AM through at least 40 m (possibly 15 m if I can get it to tune that high). I will most likely also use regeneration drawn from one or the other RF stage.

A "reflex" circuit, in this context, makes one or both tubes do double duty; in this case, both tubes act as RF amplifiers (with tuned input and a tuned crystal detector), then the detector output is fed back to the first tube's grid, and from that plate to the second grid, with the (intended) result to get a radio with both the high sensitivity and selectivity of a two-staged tuned RF input, and the ability of a two-stage audio amp to directly drive a speaker. Capacitors, chokes, and audio transformers are used to ensure the RF and AF get appropriately routed through the tubes. Double tuning and separate regeneration control promise a "three hands" operation experience (and reflex receivers are also known as "unstable", prone to oscillation and "motorboating"), but the final performance makes it worth attempting.

I've got a pair of tubes in hand: 1T4 miniature pentodes. They use relatively low plate voltage (22.5 up to 90 V B+), compared to the older types, but with two amplification stages in RF and two more in AF, I should still get good results. However, as noted, these are pentodes, and the original circuit (which dates from the 1920s) called for triodes. The manufacturer documentation for this tube type calls it an RF "remote shutoff" -- apparently because the screen grid voltage can be manipulated to control gain.

The suppression grid in this type is internally connected to the filament/cathode, and I've seen a number of examples showing the screen grid connected to B+ (i.e. plate voltage), so that some portion of B+ acts to accelerate electrons after they pass the control grid. The general rule is that a pentode can potentially produce much higher gain than an otherwise similar triode, without the "kink" in response seen in standard tetrodes and with almost zero screen current due suppression of secondary emission.

Is there anything else I need to watch out for in converting this kind of reflex/regen receiver from triodes to pentodes?

## Answer (score 3, by Brian K1LI)

It is a pleasure to follow your adventures with vacuum tubes. A number of references indicate that "triode-strapped pentodes" can be directly substituted in regenerative receiver circuits. In Sound Practices Issue 2 (Fall 1992), Herb Reichert of Eddy Electronic Inc. wrote in *Triode Connected Pentodes*, "The Williamson amp ... triode connected *[push-pull pentodes]* gave ... the low-distortion loadline of triodes with some of the gain and efficiency of beam power tubes. This circuit and its siblings became the most popular tube amps of all time. It also created the most popular tube modification of all time: triode connecting multigrid power output tubes." While this reference pertains only to audio amplifiers, it does appear to support the idea of testing the configuration in reflex receivers.

On the other hand, there are numerous examples using pentodes in their native habitat. Sir Douglas Hall's *Twin Pentode Receiver* seems to be a good fit for the two pentodes you have on hand. Two simpler designs are found in *One Valve Receivers*, volume 99, number 1 (1951): the "Midget Pentode Receiver" on pp. 8-9 and the "Oscillodyne" on pp. 12-13. The single-tube circuits might play better to your goals by allowing you to compare two designs side-by-side.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12586/pentode-vs-triode-in-tuned-rf-reflex-receiver, by Zeiss Ikon, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
