# Are there formulae to calculate capacitance and inductance of an antenna?

*Tags: antenna-theory · score 10*

## Question

How to calculate internal impedance of a dipole antenna? Its resistance has two components ie wire resistance and radiation resistance, both these can be calculated using formula. Are there formula to calculate capacitance and inductance of an antenna? Or they are calculated empirically only?

## Answer (score 7, by Glenn W9IQ)

A couple of minor comments on terminology. It isn't so much the "internal" impedance of the antenna but it is typically the "feed point" impedance that is of concern. This is the impedance seen where the transmission line connects to the antenna. Another common impedance of interest is the radiation resistance. This is the effective resistance attributable to converting the RF signal to a radiating electromagnetic wave. This impedance is often of interest when determining the efficiency of an antenna.

Yes, there are many such formulas just like the ones in the answer you saw linked in the comments. From an academic and research perspective, the formulas are under constant improvement and refinement. This usually translates into more complexity in the formulas in exchange for greater accuracy or detail.

Most professional antenna engineers and amateur radio antenna enthusiasts have transitioned to antenna modeling software. These software packages produce extensive data such as the input impedance but also go on to produce renderings of radiation patterns and other useful information. Within an hour or so, nearly any common antenna can be extensively analyzed using such software without any knowledge of calculus.

Several of these packages are available for free or on a trial basis. Here is one popular example: 4NEC2

## Answer (score 3, by Brian K1LI)

In David Leeson's (W6NL) Nov/Dec 2018 *QEX* article, "The Story of the Broadband Dipole," he cites the work of Tang, et al, on the "Equivalent Circuit of a Dipole Antenna Using Frequency-indpendent Lumped Elements." (from *IEEE Transactions on Antennas and Propagation*, Vol 41, No. 1, Jan 1993, pp. 100-103).

Leeson recommends this schematic equivalent as an adequate representation for a center-fed dipole:

with: $h$ as the dipole **half-length** and $a$ as the wire radius, both in meters, $\omega_0$ as the resonant frequency in Hz and $R_{a0}$ the radiation resistance at resonance in ohms:

$$C_{11} = \frac{27.82\mathsf x 10^{-12} h}{ln(2h/a)-1.693}$$ $$L_{11} = \frac{1}{\omega_0^2C_{11}}+C_{11}R_{a0}^2$$ $$R_{11} = \frac{L_{11}}{C_{11}R_{a0}}$$

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11873/are-there-formulae-to-calculate-capacitance-and-inductance-of-an-antenna, by tgnhbv, Glenn W9IQ, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
