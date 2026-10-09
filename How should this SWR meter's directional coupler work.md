# How should this SWR meter's directional coupler work?

*Tags: diy, rf-power, electronics, measurement, swr-meter · score 6*

## Question

I'm wrapping up a "home build" of the MFJ-941EK antenna tuner kit and having trouble getting the wattmeter calibrated. I can't use C4 to get the reflected power reading calibrated down to 0 as is supposed to happen. So now I need to figure out what I got wrong, and to do that it would help to figure out how it's supposed to work in the first place.

**UPDATE**: my theory now is that I fried D1 during initial testing and so I'm [pursuing a fix for that next. However I'd still appreciate an understanding of this circuit.]

MFJ helpfully provides the full schematic in the kit assembly manual. Here is the meter portion of the circuit. SW3a simply goes to a dummy load during calibration.

The directional coupler transformer is implemented by routing the conductor from the transmitter plug through the middle of a toroid that had the secondary windings on it already.

The bottom half of the circuit seems pretty straightforward. I imagine the diodes D1/D2 are used to "detect" the power (i.e. rectify the RF signal to a DC voltage) on each "output" of the directional coupler and the resistor networks that follow just put it into one of the two selected ranges appropriate for the galvanometers.

But how is the coupler itself working? I've watched How a Directional Coupler in an SWR meter works a few times in the past; the math makes sense but it still's a bit magic to me. And in this circuit, it's a bit more complicated, and there's only one transformer instead of two. What is the purpose of the circuit (C4/C5/L2/R2) off the center tap of the transformer?

Seems like my problem is that I'm getting a voltage to D1 when there's not actually reflected power. The intended solution is that you simply adjust C4 to make that go away — and I *can* increase/reduce the reading — but I can't zero it out.

This same circuit is also sold as a commercial product, which MFJ calibrates themselves. So I doubt its simply a matter of sometimes needing <3pF or >10pF from the trimcap; that would cause headaches on their factory floor. The trouble is that not knowing how the circuit is supposed to work, it's hard to track down where things are getting thrown off — whether the toroid got messed up, or whether an out-of-spec component could be throwing it, or what!

## Answer (score 2, by Dan Mills)

C4/C5 form a capacitive voltage divider, L2 provides a DC return path for the meter current which needs to get back to the center tap to close that loop, and I suspect R2 lowers the Q of the undesirable L2/C5 resonance.

The basic idea is that the current sense transformer develops voltage across R1 which is proportional (and in phase with) to the line current, and that this is added to the sample of the line voltage for forward power or subtracted from it for reverse power. The ratios are calculated such that with 50V and 1A flowing the voltage across R1 is twice the voltage developed by the divider network, causing the reverse power meter to read zero (Note the center tap means the subtraction of from half the voltage across R1) and the forward power meter to read 50W, if you had say 50V and 2A flowing then the voltage across R1 would be four times that developed by the divider network causing the reflected power to read 50W and the forward power to read 100W, again reasonable.

Do note that this circuit (If built with a coax line thru the sense transformer) requires that the screen on that line section be connected ONLY at one end. There should be a path that does not pass thru the toroid for the return current as the coax line section is intended to be an electrostatic shield.

## Answer (score 2, by dale durando)

Simply put, if the current and voltage are in phase, the SWR should be relatively low. They will be in phase for a non-reactive load, i.e., a purely resistive load: a 50 ohm resistance with no capacitance (such as an antenna too short) and no inductance (antenna too long).  
The voltage from the capacitor divider is applied equally to the positive and negative current transformer outputs (that are converted to voltages by the 27 ohm load resistors). The turns ratio of the transformer and the voltage divider ratio of the two capacitors are matched. When the negative side current output matches the voltage divider, they should null (reverse SWR). The positive side's current output and the divider will 'add' giving a large voltage indicating the power (or forward SWR reading). The additional components, L2, C3, R2, are tweaks to compensate the circuits to stay calibrated over the frequency range. As the SWR increases, the phase of the current won't match the voltage and no longer null the reverse side so a voltage is detected on the reverse side indicating a higher SWR. The positive side's current also will be affected the same way (they won't add properly). Somewhat simplified, but may help when trying to troubleshoot small errors.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6240/how-should-this-swr-meter-s-directional-coupler-work, by natevw - AF7TB, Dan Mills, dale durando. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
