# Should the capacitance or inductance be varied to achieve resonance?

*Tags: diy, equipment-design, impedance · score 4*

## Question

A resonant circuit is typically composed of some resistance and reactance, the latter being provided by inductors and capacitors. The resonant frequency being calculated as the inverse square of their product.

It is therefore possible to attain resonance by varying the capacitance, inductance, or both.

At the design phase, is there a rule-of-thumb guideline on which parameter (capacitance/inductance) one should vary whilst aiming for a range of values?

## Answer (score 2, by Kevin Reid AG6YO)

I'm not an analog electronics guy, but I heard this on the Internet...

This video by W2AEW: "Basics of Capacitor & Inductor self-resonance, parasitics, etc." does not discuss *variable* inductances or capacitances, but does cover practical concerns for obtaining a given resonant frequency by selecting values of inductors and capacitors. Roughly summarized, the issue is that components are non-ideal:


They have tolerances: they are not exactly the intended value.


They have parasitics: all wires have resistance, capacitors have a little inductance in their leads, inductors have a little capacitance between their turns, etc. The effects of this increase with frequency.

Therefore, if your *designed* capacitance or inductance is *too small*, it will be swamped by the imperfections in the actual circuit.

W2AEW didn't actually say this, but it seems to me that one should therefore choose “balanced” values so that the chosen inductance is large compared to the parasitic inductance, and simultaneously the chosen capacitance is large compared to the parasitic capacitance. I could be wrong there; according to the video there could be and have been whole chapters of books written on the subject. So maybe you want to find one of those.

## Answer (score 2, by s3c)

To vary the inductance you would normally use a cored inductor that is settable in some way, this is generally more lossy than an air wound inductor and would thus have a lower Q. Variable inductors also aren't that common.

To vary the capacitance you would either need a variable capacitor (or varactor that can be varied with voltage), physically variable capacitors are hard to get exactly on frequency however (in my experience at least).

In short, I would say vary the capacitance just because physically variable capacitors are easier to find and varying it electronically is easy using varactors.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1790/should-the-capacitance-or-inductance-be-varied-to-achieve-resonance, by VU2NHW, Kevin Reid AG6YO, s3c. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
