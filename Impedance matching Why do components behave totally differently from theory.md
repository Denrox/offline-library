# Impedance matching: Why do components behave totally differently from theory?

*Tags: impedance-matching · score 3*

## Question

I got stuck with impedance matching for an antenna. Any added components in the matching network gave a result totally different from what a Smith chart predicts. Let me explain this clearer.

1.

First, by shortening L2,C8,L5,C23, I measured my antenna "raw" impedance (without matching) at ANT1 terminal (please see attached my matching network). It gave Za_raw = 133 +j 226 (ohm). RF+ is the input feed line of my antenna. There is a SMA connector at ANT1. It connects the rest of my circuit to the antenna.

2.

Then, if I replace C23 with an inductor L = 47nH, the measured impedance at ANT1 terminal is 60 + j160 (ohm)!!! But using Smith chart, with Zload = Za_raw, a serial added L of 47nH would give Za = 133 + j 496 (ohm). You can see this in the following figure.

All measurements were conducted using a VNA. 1-port calibration was done before measuring. Any suggestions are highly appreciated.

Modified on 17 Oct.**

Here is my construction. I shorten L2, C8, L5 & C23 using wires. The physical length of the feed line is about 29.5mm.

- The reason for the complicated matching network is that, at first, I would like to make 2 measurement points: at ANT11 and ATN1. ANT1 should be the input impedance of my circuit, while ANT11 should be the antenna input impedance. But later, I thought I don't need to do that. I just need to tune the input impedance of the whole circuit (with all components soldered) at ANT1 to be 50 ohm!
- Why 50ohm? In my measurement, at the resonant frequency (around 915 MHz), the impedance at ANT1 is 50ohm!

Am I right?

## Answer (score 6, by Glenn W9IQ)

Firstly, at 900+ MHz, shorting out components to take antenna impedance measurements is not a good practice as the lead length can be a substantial portion of a wavelength. Stray inductance and capacitance must also be avoided.

Secondly, your matching network appears horribly complicated for an impedance matching circuit. Generally, a simple "L" network (one inductor and one capacitor) will accomplish the match. If you are attempting to do something else with the network, such as bandpass shaping, please edit your question to explain this. You should also state the desired final impedance of your antenna system.

Thirdly, without seeing your physical construction, it is likely that the wires or traces of your shorted out matching network are acting as a transmission line. Any transmission line length that is not a multiple of 1/2 wavelength will transform the antenna impedance. At 915 MHz, even a 30 mm length of transmission line has relevant transformative properties. In order to properly model this, you would need to know the electrical wavelength and the characteristic impedance of this unintended transmission line. This is yet another reason to take the impedance measurement directly at the antenna feed point.

So start by taking a better impedance measurement of your antenna. Then to see how a simple L matching network functions, plug your measured impedance value into this on-line calculator. You can then take the reported L network values and put them in your Smith chart to help you visualize the effect of the two matching components. If later you then would like to see the math behind this on-line calculator, open another question to that effect.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11999/impedance-matching-why-do-components-behave-totally-differently-from-theory, by Minh Lam, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
