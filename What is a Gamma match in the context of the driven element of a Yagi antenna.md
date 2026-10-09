# What is a Gamma match in the context of the driven element of a Yagi antenna?

*Tags: antenna, antenna-theory, dipole, impedance-matching, yagi · score 11*

## Question

How (and why) does a Gamma match work, when used on the driven element of a Yagi antenna? As shown here:

(source: http://www.iw5edi.com/ham-radio/?2-element-yagi-for-10-meters-band,49)

The article describes a 10 meter Yagi where the driven element is one continuous conductor and not the classic dipole-halves driven by 50 ohm coax. I have seen other designs where Gamma matches were used on split folded dipole elements joined on the far end. Clearly capacitance is the key, but I don't understand how it can work efficiently.

## Accepted answer (score 15, by on4aa)

A gamma-match serves a triple purpose:

1. As a small diameter wire parallel and in close vicinity with the main radiating element, it will carry only a fraction of the main element current while being exposed to the same electrical field strength. This turns it in **an effective up-transformer of the antenna input impedance**.
2. It also forms together with the main radiating element **a closed wire stub**, adding inductance to the antenna input impedance. If this is not required for matching, the additional inductance can be cancelled out with a lumped capacitor in series.
3. Not shown on your figure but on the picture below: The sheath of the coaxial feed-line is connected to the center of the main radiating element. When properly connected, a gamma-match also serves as a balanced to unbalanced converter or **balun**.

All these functions are highly desirable for matching the unbalanced characteristic impedance of the coaxial feed-line to the much lower balanced impedance of a Yagi-antenna.

## Answer (score 19, by Phil Frost - W8II)

Clearly capacitance is the key

Capacitance is just one part of it. The gamma match in your question is three things:

1. A sort of folded dipole, performing an impedance step-up
2. A parallel shorted transmission line stub, adding shunt inductance
3. A series capacitance

An equivalent circuit is:

So let's say we have some antenna with a feedpoint impedance of $(15+j0)\Omega$. On a Smith chart, we have this:

Our goal is to move that dot to the middle of the circle. How does a gamma match accomplish that?

## sort of a folded dipole

The first point is probably the hardest to understand. Consider that in a folded dipole, the impedance is four times that of an ordinary dipole because the antenna current flows in both legs of the dipole, but only half of it in the leg where the feedpoint is. Since current is halved while radiation resistance remains essentially unchanged, impedance is quadrupled.

Now consider the gamma match: the same condition exists. Some of the current flows through the main antenna element, and some of it through the gamma bar, and this provides the same sort of impedance step-up. In fact, if you move the shorting strap all the way to the end of the antenna, it's exactly a folded dipole.

Typically, the gamma match is constructed to give an even more than 4:1 impedance step-up. By making the gamma bar smaller than the main element, the gamma bar will take an even smaller share of the total current. Even less current means a higher impedance transformation.

In terms of the equivalent circuit, the size of the gamma bar influences where the autotransformer formed by L1 and L2 is tapped. Here's the effect on the Smith chart:

## a parallel shorted transmission line

The gamma bar running parallel to the antenna element make a twin-lead transmission line. It's shorted stub, and less than $\lambda/4$ long, so it looks like an inductor. The position of the shorting bar determines the inductance, the value of L1+L2 in the equivalent circuit above.

If the shorting bar is moved all the way to the end of the antenna, then the susceptance is zero, and has no effect on the feedpoint impedance. As the shorting stub is moved closer to the feedpoint, it makes the susceptance larger, as if L1+L2 were becoming smaller inductors.

With parallel inductance added, our Smith chart looks like this:

## a series capacitance

The capacitor is formed by the aluminium tube, with the gamma rod inside it, insulated by plastic. This is an optional feature of the gamma match, and it's not always present, or configured exactly this way. But with it, we can do this:

Mission accomplished.

As configured, C1 and L1+L2 form a step-down L network. It's also possible to trim the antenna to be a bit short, in which case it will provide some capacitance, but on the other side of the inductance. In this case, you get a step-up L network.

Since antenna can also be tuned to be exactly resonant (present a purely resistive feedpoint impedance), you don't technically need to add any inductance or capacitance: just the transformation from the first point is sufficient and you could have an ordinary a folded dipole. However this frequently isn't done in practice since adjustment of the impedance transformation requires changing the diameter of either the gamma bar or the antenna element, which is tricky.

It's also the case that the gamma match works somewhat as a balun. If it steps up the impedance seen looking in from the coax, by reciprocity it also steps down the impedance looking in the other direction back into the differential mode of the coax. The common-mode is left alone but is now a relatively higher impedance. So, it might be more desirable to step-up too much, then step-down with the L network. Even so, for an antenna with high directivity some additional common-mode suppression may be necessary: combined with the gamma match it may be even more effective. G8HQP provides a more complete explanation with all the math if you want more detail.

## Answer (score 2, by sm5bsz)

The gamma match is problematic. It surely allows a perfect impedance match having two degrees of freedom, but the balun effect is questionable. The screen of the coax is connected to the center of a half wave element. That means that it is connected to two open-ended quarter-wave conductors. In free space they would have a very high impedance at the ends and consequently the impedance at the center would be very low. That means that the voltage on the coax screen would be very low so not much signal would be sent onto the screen of the coax (or not much qrm would be picked up if the coax has interference on its outside.)

A half wave dipole where two quarter wave rods are fed in anti-phase is a good radiator with Z=free space impedance (300 ohms) divided by about 6. But if one feeds them in phase, radiation from both sides will cancel and the impedance at the center goes towards zero while the impedance at the ends becomes very high. The midpoint becomes a good groundpoint.

In real life it is different. Practical experience: A friend of mine had an EME array with several long yagis on 144 MHz. They all had a gamma match which was isolated from the boom tube. There was however a performance problem. A simple test: Take one antenna, point it straight into the sky with the reflector well above ground. Put a field strength meter on the last director and look at the reading while moving the hand along the coax. Big variations were observed meaning that a substantial current is flowing on the coax screen. Add a sleeve balun. That makes the current on the screen negligible. That was long ago, but as I can recall performance was improved by more than 1 dB (That is a lot on EME) The explanation is that the physical midpoint is not the electrical midpoint. If you would make a dipole from two rods of different diameter and feed them in phase radiation would not cancel and consequently the impedance at the midpoint would not be very low. It would be necessary to make the thicker side shorter. The gamma match destroys the symmetry of the radiator so there is a substantial RF voltage at the center. This causes some loss of power and maybe more importantly pick up of conducted interference.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1804/what-is-a-gamma-match-in-the-context-of-the-driven-element-of-a-yagi-antenna, by Ron J. KD2EQS, on4aa, Phil Frost - W8II, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
