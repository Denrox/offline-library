# Series resonant circuit, how to calculate voltage across the capacitor?

*Tags: electronics · score 3*

## Question

This is question a3i3-1 from the practice questions in the book "amateur radio Exam Secrets":

A series resonant circuit has 10V peak across it when at resonance. At that frequency the resistance of the coil is approximately 4Ω and the Q-factor is calculated as 100. The voltage across the capacitor will be about

A 40V

B 100V

C 400V

D 1000V

I don't know the answer yet, but looking it up won't help me because I'm stuck in how to calculate the answer. How do you do it?

## Accepted answer (score 8, by Glenn W9IQ)

I encourage students to draw a simple schematic when it comes to word problems such as these. Here is an ideal series resonant circuit:

Since the problem states that the circuit is in resonance, the inductive reactance equals the capacitive reactance making this ideal circuit a dead short (0 ohms) across the signal generator.

But the real world is not ideal. The inductor is made up of multiple turns of wire. This wire has an RF resistance which must be shown in the circuit for a proper analysis. So we modify the ideal circuit to a more practical circuit to reflect this resistance:

Now the current through the circuit is limited only by the value of R1 which we are told is 4 ohms at the frequency in question. We are also told that the voltage across the series circuit is 10 volts (peak) so the current through the circuit is given by Ohm's law:

$$I=E/R \tag 1$$

This formula allows us to calculate that the current in the circuit, when it is at resonance, is 2.5 amps.

We are not given the values of L1 or C1 but we are given the Q (quality factor) of the circuit which is 100. Recall the formula for the Q in a series resonant circuit is:

$$Q=\frac{X_L}{R}=\frac{X_C}{R} \tag 2$$

where XL is the inductive reactance of the inductor, XC is the capacitive reactance of the capacitor and R is resistance of the inductor (or more generally of the series circuit). Since the problem gives us the Q and the R, we can re-arrange formula 2 to solve for XC:

$$X_C=Q*R \tag 3$$

We can now compute that the capacitive reactance at the unknown frequency is 400. The voltage across the capacitive reactance is calculated using Ohm's law:

$$E=I*R \tag 4$$

Using the 2.5 amps that was calculated earlier as the current in the circuit, we find that the voltage across the capacitor with its 400 ohm reactance is 1000 volts.

Perhaps a good lesson in sizing caps for the application!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10082/series-resonant-circuit-how-to-calculate-voltage-across-the-capacitor, by Pablo Fernandez, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
