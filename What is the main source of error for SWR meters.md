# What is the main source of error for SWR meters?

*Tags: transmission-line · score 3*

## Question

I have updated this question to make it simpler because i haven't seen an acceptable answer yet.

New Question.

The impedance seen at any point on a transmission line is E/R. If the SWR isn't 1:1 then the impedance changes along the length of the line. Does the departure away from 50 +j0 ohms of the impedance on the transmission line caused by the SWR not being 1:1 affect the accuracy of a SWR meter which is designed to work at 50 + j0 ohms ?

A swr meter is designed to work with a specific impedance transmission line, that usually being 50 ohms. The meter is calibrated to be correct for 50 ohms and it won't read correctly if the transmission line impedance isn't 50 ohms and won't read anything if there's no RF current flowing along the transmission line. And a 50 ohm transmission line has a characteristic impedance of 50 ohms. But the real impedance seen by the swr meter when there is RF current is E / I which is not the same as the characteristic impedance, in particular when there is a mismatch between transmission line and antenna where the impedance seen on the transmission line becomes a function of the frequency and changes along the length of the line. So then if the swr meter only reads accurately when the impedance is 50 ohms, it wont read correctly if the swr isn't perfect and the reading will change if you move the meter along the transmission line because the actual impedance seen by the meter and as determined by E / I is also changing.

Is that right ?

Does that also mean if the swr isn't perfect and E / I isn't 50 ohms at the swr meter then there will be secondary reflections at the swr meter ?

## Accepted answer (score 1, by Brian K1LI)

"Is the measurement accuracy made by an SWR meter affected by the fact that the actual impedance E/ I seen on the line during operation is not the same as the characteristic impedance if standing waves exist?"

Assuming your SWR meter employs a variant of the Bruene Coupler$^1$, perhaps the most popular topology in use today, the short answer to your question is, "No," because your SWR meter is not measuring impedance. Rather, SWR is evaluated using the well-known relationship: $$SWR=\frac{V_f+V_r}{V_f-V_r}$$ where $V_f$ and $V_r$ *represent* the forward and reverse voltages at the point of measurement. Developing the *representations* of the forward and reverse voltages *does not* require "separating" forward and reverse waves traveling on a transmission line.

As described in The Bruene Directional Coupler and Transmission Lines by Gary Bold, ZL1AN:

The operation of the Bruene coupler is traditionally derived as if it's inserted *in* a transmission line, using the concepts of "forward" and "reflected" waves, which are assumed to exist on the line *before* and *after* it, and which flow *through* it. But the coupler also works when connected to: the *input* of a line; where there is no line on the "input" side; or when connected to a transmatch; or even to a pure resistance - which must always be done to calibrate it. There are no standing waves inside a transmatch or resistance, and the coupler itself doesn't contain a transmission line.

The Bruene Coupler - notice, it is not called a "bridge" - sums voltages to produce relative measurements of forward and reflected power. A capacitive divider ($C_1$ and $C_2$, below) across the input develops a sample of the RF voltage. Samples of the RF current from two halves of the center-tapped secondary winding of the toroid transformer pass through a resistor ($R$) to develop corresponding voltage representations of the RF current:

(Note that the voltage induced by the current sample results from $R$ rather than from $2R$ because, by virtue of circuit symmetry, the potential at the "center" of resistor $2R$ in the diagram is the same as the potential at the center tap of the transformer secondary. This connection is explicitly made in some designs.)

$V_m$, the "Reverse" meter voltage being measured in the diagram, comprises the *difference* between these two voltages. $V_m$ on the "Forward" half of resistor $2R$ comprises the *sum* of the two voltages because the voltage induced in $R$ by its half of the transformer secondary is $180^\circ$ out of phase with the voltage induced on the "Reverse" half of $2R$.

Bold and David Knight, G3YNH, in his article on Reflectometry, discuss sources of error in SWR meters based on the capacitive divider.

1. Bruene, Warren, "An Inside Picture of Directional Wattmeters," *QST*, vol. 43 no. 4 (American Radio Relay League), April 1959, pp. 24-28

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13313/what-is-the-main-source-of-error-for-swr-meters, by Andrew, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
