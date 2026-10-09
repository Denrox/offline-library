# How can RF exposure hurt you?

*Tags: safety · score 14*

## Question

In studying for the exam, one question came up about RF Exposure.

```
G0A
07
What effect does transmitter duty cycle have when evaluating RF exposure?

```

My understanding of Radio is that it is non ionizing electromagnetic radiation. How can RF be damaging?

## Answer (score 14, by WPrecht)

The direct effects of RF on people are:

1. Tissue Heating
2. Electric shock (shocks and burns) and electrocution (death)
3. Interference with implanted medical devices

The General test question quoted is about evaluating the exposure for the purposes of tissue heating. I assume everyone "gets" not grabbing a wire you are pumping 1500W into.

Tissue heating is a problem because unlike being in a hot place, where the heat is outside the body, the heating is internal. The only mechanism for the body to deal with this is blood flood, so areas with little flow (for instance, the eyes) are particularly vulnerable.

To give you an idea of how you absorb the RF, consider this: the human body, standing and somewhat grounded, is a 1/4 wave vertical antenna, resonant at 4x your height. But is somewhat lossy and high impedance compared to a metal antenna. Of course, that high impedance is the problem, the RF is "lost" as heat, in you.

Safety experts consider the most the human body can tolerate is 4W/kg of heating. To put this in perspective, you generate about 1W/kg sleeping, 2-3W/kg in heavy exercise. Exceed this and you body has trouble dumping the extra heat and the core temperate begins to rise. Cell death begins to occur at 107 deg F (that's why 105 def F is a tripwire in fevers). Natually you can tolerate some of this. Depending on for how long and what's getting heated. I don't recommend some organs like the brain, liver, kidneys, things you occasionally need.

A somewhat wordy reference can be found here: http://hps.org/hpspublications/articles/rfradiation.html

## Answer (score 4, by Phil Genera)

Heating; it can burn you the same way a microwave cooks food, or UV from the sun gives you sun burn. The wikipedia article about radiation burns generally covers RF a bit: http://en.wikipedia.org/wiki/Radiation_burn

## Answer (score 3, by DevlshOne)

There is a government doctrine on this very subject entitled OET-65.

You must remember that RF exposure is cumulative and does the most damage over a long period of time. The symptoms of over-exposure to RF are stomach pains, scratchy/sandy feeling eyes, the internal feeling of overheating (possibly followed by stroke). The most effective ways of avoiding the effects of RF exposure are limiting your exposure times, RF reflective clothing and wearing an exposure badge.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/558/how-can-rf-exposure-hurt-you, by spuder, WPrecht, Phil Genera, DevlshOne. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
