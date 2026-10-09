# How does this 3 dB splitter/combiner work?

*Tags: ferrite · score 3*

## Question

I'm having difficulties to understand how does this circuit work:

Apparently T1 is a regular 50 Ohm to 22.2 Ohm autotransformer. Turns ratio 2:3 gives a 0.66**2 impedance converation. Since the load is two 50 Ohm ports in parallel, the total load impedance will be 25 Ohm. In other words T1 is just for impedance matching.

From what I know T2 and R are needed for isolation of port 2 and port 3. This is the part I don't quite understand. What happens when the circuit is used as a splitter? And what happens when it's used as a combiner? What prevent the current just to flow from port 3 to port 2 through R?

Could you please explain it?

## Accepted answer (score 4, by Brian K1LI)

SPICE modeling shows that replacing T2 and R with a 22.2-$\Omega$ resistor, the impedance looking into T1 is indeed 50-$\Omega$, as expected:

Similarly, replacing the 50-$\Omega$ generator and T1 with a 25-$\Omega$ generator shows that the impedance looking into T2 is 25-$\Omega$:

This is a result of the electrical symmetry about a "virtual ground" established by the junction of the two windings of T2 and the "midpoint" of the 100-$\Omega$ resistor. Thus, each side of T2 is terminated by two paralleled 50-$\Omega$ resistances, or 25-$\Omega$, matching the generator.

Note, though, that the composite circuit presents a slight mismatch of 56-$\Omega$ to the generator:

This is a result of the difference between the 22.2-$\Omega$ transformation of T1 and the 25-$\Omega$ input to T2. That is, 50*(25/22.2)=56-$\Omega$.

The isolation between the two output ports can be measured by driving one of the output ports, terminating the "input" port in its characteristic impedance and measuring the response at the other output port:

As shown the isolation between the two output ports is better than 30-dB as long as all ports are terminated in 50-$\Omega$. The strong coupling between the windings of T2 means that equal but opposite currents flow with respect to their connections to R1. Whereas the driving current I(V1) is split between L4 and R1, the current in L5 cancels the current flowing into node ***out2*** from R1, effectively isolating it from node ***out1***.

[Note: in LTSpice convention, I(V1), I(R1) and I(L4) are all *leaving* node ***out1***, while I(L5), I(R1) and I(RL2) are all *entering* node ***out2***.]

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16759/how-does-this-3-db-splitter-combiner-work, by Aleksander Alekseev - R2AUK, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
