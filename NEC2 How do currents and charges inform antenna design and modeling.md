# NEC2: How do "currents" and "charges" inform antenna design and modeling?

*Tags: antenna, antenna-theory, antenna-modeling · score 3*

## Question

## Question

- How would you reason about charge and current density in your design to better tune (and understand) your antenna?

## Background

According to the NEC2 documentation,

*"The output may include induced currents and charges, near electric or magnetic fields, and radiated fields."*

but I can't find a discussion about how to *reason* about currents vs charges in a practical sense.

Below are the charge and current colorizations for a coax-fed Yagi from xnec2c. Generally speaking, how are currents and charges useful? How do you use one vs the other to understand an antenna simulation?

Please note: Below there is an *example* of what it looks like in xnec2c, but my question is generic:

This question is not specific to the model below, but about charges and currents in general, and how to utilize them. I'm asking about the practical *use* of viewing charges/currents on a structure, and how to use them in antenna design. In application, what do they inform?

### Charges

### Currents

### NEC2 Code

Here is the NEC2 file. It is based on a design by Martin DK7ZB and the gain/VSWR were optimized by xnec2c-optimize.

```
CM Initial dimensions by Martin Steyer, DK7ZB
CM http://www.qsl.net/dk7zb/PVC-Yagis/5-Ele-2m.htm
CE
GW 1000 21  0.52145 0   0   -0.52145    0   0   0.002
GW 1001 21  0.4899  0   0.1949  0.005   0   0.1949  0.002
GW 1001 21  -0.4899 0   0.1949  -0.005  0   0.1949  0.002
GW 1002 21  0.4721  0   0.2949  -0.4721 0   0.2949  0.002
GW 1003 21  0.4671  0   0.7764  -0.4671 0   0.7764  0.002
GW 1004 21  0.4485  0   1.249   -0.4485 0   1.249   0.002
GW 1    1   0   0   0   0   0   0.005   0.002171
GW 2    80  0   0   0   1.1849  0   0   0.002171
GW 3    80  0   0.005   0   1.1849  0.005   0   0.0004342
GM 0    3   90  0   0   0   0   0   3
GA 4    4   0.005   0   360 0.0004342   0   0   0
GM 0    0   0   0   90  0   0   0   4
GM 0    19  0   0   0   0.059245    0   0   4
GA 5    4   0.005   0   360 0.0004342   0   0   0
GM 0    0   0   0   90  1.1849  0   0   5
GM 0    0   0   -90 0   0   -0.005  -1  1
GW 20   1   0.005   -0.005  0   0   0   0   0.002
GW 21   1   0   -0.005  0.1849  0.005   0   0.1949  0.002
GW 22   1   -0.005  -0.005  0.1849  -0.005  0   0.1949  0.002
GE 0    0   0   0   0   0   0   0   0
EX 0    1   1   0   1   0   0   0   0   0
RP 0    19  37  1000    0   0   10  10  0   0
NH 0    0   0   0   0   0   0   0   0   0
NE 0    0   0   0   0   0   0   0   0   0
ZO 50   0   0   0   0   0   0   0   0   0
FR 0    32  0   0   144 0.129032258064516   0   0   0   0
EN 0    0   0   0   0   0   0   0   0   0

```

## Accepted answer (score 2, by hobbs - KC2G)

"Charges" will tell you where the high-voltage points in your design are. If high-voltage points get too close to other parts of the structure that are at a different potential, or too close to much of anything else, you could have problems with arcing.

Current distribution is useful in different ways, for example:


If you're designing a parasitic array like a Yagi or log-periodic, it tells you which elements are "doing the most work". An element that doesn't get much current over your frequency range might be a candidate for removal.


A wire with unexpectedly low current might also just be an error in your model: you thought it was connected to something, but it's not.


It can help you optimize the structural design, by showing you where you benefit most from thicker wire/tubing and where you can get away with tapering the diameter down.


If you see currents going in opposite directions in wires that are near each other, that's likely to indicate an efficiency problem.


If you're free to move your feedpoint along a wire (as in an OCFD), the current plot will help: moving it towards higher current will give you a lower impedance, and towards lower current will give you a higher impedance.

And probably a lot more: it's one of those "when you have a feel for it, uses will pop up" things.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22736/nec2-how-do-currents-and-charges-inform-antenna-design-and-modeling, by KJ7LNW, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
