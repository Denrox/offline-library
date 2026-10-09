# What is the proper way to electrically wire in a loading coil to a vertical antenna?

*Tags: antenna-theory, hf, vertical-antenna, impedance-matching · score 5*

## Question

I am trying to put together a vertical pole style antenna with a loading coil housed at the base using a plan very similar to the one described in this ARRL article. I am trying to understand how to electrically wire it though.

For convenience, the wiring schematic from that article is shown here:

In this build, the author used a switch to control where he tapped the coil to tune his antenna for the different bands as shown. Here's what I don't understand about this though.

*Why does the bottom of the coil bypass S1?*

I understand generally that the 80 meter band needs more coil windings tapped than the 40/15 tuning, and the 10 meter band bypasses the coil altogether. But why have that connection from S1 to the first coil of L1 at all? Is that required for some reason?

What is the proper way to electrically wire in a loading coil to a vertical antenna?

## Accepted answer (score 4, by tomnexus)

I don't think it's correct to connect the end of the coil to the common point of S1.

Shorted turns, because they're magnetically coupled to the active turns in the coil, increase the loss in the inductor. Loading coils need to be kept away from metals, and unused turns should be left open. I suggest that if you're building a new coil, you should tap it like this:

The extra turns on the inductor make sense for this reason: when making a loaded antenna like this, you don't know exactly how much inductance is required. You wind the coil so that it is definitely resonant *below* 3.5 MHz, and then *on your particular ground system or vehicle* find the correct tap positions for 80 m, 40 m, 20 m.

The bottom turns are wasted, but it's better to have too many than too few, so you have no choice but to build it like this.

## Answer (score 3, by Brian K1LI)

Simulation indicates that there is an error in the diagram.

Shortened antennas exhibit capacitive reactance which can be compensated by adding series inductive reactance as shown in the diagram. However, shortened antennas also exhibit lower driving-point *resistance*, for which compensating reactance is no cure. The "cold" end of the coil should be connected to the radial system. The feed point is then "tapped up" the coil to form an "L" network.

Simulation shows that the driving-point impedance of a 25-ft 1" diameter vertical with four (4) 25-ft #14 radials is 6.4-j609 ohms. (These values are only significant for purposes of illustration; actual measured values may vary substantially, but those effects are outside the scope of this question.)

Entering these values into *SimSmith* and choosing appropriate inductance values shows that we can achieve a match on 80 meters by tapping up a ~27uH coil:

A different *total* inductance will be needed on each band and it is possible that a good match on some bands will require capacitance in the L network. A follow up item to this effect was published in *QST*'s "Technical Correspondence" column a few months after the original article.

## Answer (score 3, by Kevin Reid AG6YO)

This is similar to a common technique applicable to potentiometers used as variable resistors, and I'm guessing that it is done for similar reasons. However, it probably isn't a good idea to implement as drawn.

Consider a potentiometer connected like so:

Ideally, the connection between the wiper and the left end of the potentiometer would do nothing, since the portion of the potentiometer to the left of the wiper is shorted out at all times, and without that connection would be open circuit at all times.

In practice, a potentiometer may lose connection between the wiper and track momentarily as it is turned, or an extremely worn one have “dead” spots of no connection even when not being turned. Therefore, the extra connection ensures that the resistance between A and B is always *no greater than* the end-to-end resistance of the potentiometer. This is important if a too-high resistance or open circuit could damage the circuit (for example, if A is ground and B is connected to a voltage source would, by itself, raise point B to a voltage that would damage other components), and more generally means that the potentiometer's "output" cannot become "out of range" in the event of dead spots (unless the potentiometer's track/winding breaks entirely).

In your case, you do not have a potentiometer but a switch — therefore, unless it is a make-before-break type (which might be a good choice anyway), it **will always** behave like the worn potentiometer, causing J1 to become open-circuit as you make the change. Thus, the extra connection ensures that **the antenna is always connected to J1, regardless of what is done with the switch.** It might present a poorly-matched load, but not a pure open circuit.

But, there's a catch — instead of shorting out portions of a resistor we're shorting out portions of an *inductor*. All turns of an inductor are coupled together (though more separated ones less so), so there are now shorted turns, which will waste power in eddy currents rather than radiating.

Therefore, the presented design with a tapped inductor is not a good idea. You could fix it by using *separate* inductors for each stage, arranged to minimize coupling between them (perpendicular axes, keeping them apart).

To address your broader question of *what is the proper way to electrically wire in a loading coil to a vertical antenna* — I don't have any personal recommendations, but I do think that the extra wire that you were puzzled by is plausibly a good idea. Whether it's worth the complications of implementation, I can't say.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14540/what-is-the-proper-way-to-electrically-wire-in-a-loading-coil-to-a-vertical-an, by SandPiper, tomnexus, Brian K1LI, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
