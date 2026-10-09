# What is the difference between an RF amplifier's DC or quiescent operating point and the RF operating point?

*Tags: amplifier · score 3*

## Question

I chose the resistor values in the following schematic to set the DC bias point of VCE=6V and IC=5mA because the transistor data sheet gave the S-parameters at 162MHz for these values. I learned how to do this by studying the book "Rf Circuit Design" by Chris Bowick. Early on in the book he mentions that stray capacitance inherent in the DC bias network resistors can effect the "RF operating point". I know what the DC operating point is ,obviously, but what is the RF operating point and how is it effected by the stray parallel capacitance of the bias network resistors? In this case I'm referring to the stray capacitance of the 3.240K Ohm resistor only because the other three resistors are RF bypassed by the .1 micro Farad capacitors. Bowick does explain how the impedance of a resistor can lessen with an increase in frequency but I just don't know what the RF operating point of the bias network is much less how the reduced impedance of the resistor effects it.

## Answer (score 3, by Buck8pe)

In typical circuit analysis, it's customary to consider the DC model (short all inductors, open all caps, resistors all ideal) and AC model separately. The AC model is simplified by assuming that resistors are ideal and that the AC component simply "rides along" on the DC op point.

However, at RF frequencies, the inherent parasitic capacitance and inductance of resistors changes the operating point (imagine a capacitor in parallel and inductor in series with the 3.24k base biasing resistor). I think this is what he means by RF operating point.

Most of the familiar equations for amplifier circuits assume ideal components (i.e., a resistor is a resistor and a capacitor is a capacitor, etc). This keeps the analysis (relatively) simple. However, as Bowick points out, if you're operating at frequencies where the fact that a resistor is really an RLC circuit matters, then the analysis gets much more complicated. The transistor at very high frequencies is pretty formidable, with internal capacitance between its leads (the one between collector and base is well-known, but there are others) and inductances in the bonding wires, etc.

If I were you, I'd simulate the model. Maybe insert some ballpark parasitic values alongside the components to see what effect they have. If you're planning to build, try to use SMD parts to reduce parasitic effects.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17769/what-is-the-difference-between-an-rf-amplifier-s-dc-or-quiescent-operating-poi, by Thomas L, Buck8pe. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
