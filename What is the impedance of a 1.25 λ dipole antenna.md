# What is the impedance of a 1.25 λ dipole antenna?

*Tags: antenna, wire-antenna, impedance, antenna-theory, dipole · score 5*

## Question

I would like to make a dipole antenna. This particular antenna is used for reception only; no transmission is involved. I would like to receive as much power as possible by this antenna as it is used in energy harvesting.

I read that a length of 1.25 λ (i.e. each leg length is 5/8 λ) has more gain. To match it with a load, I need to create a matching circuit. So, what is the impedance of a 1.25 λ length dipole antenna?

## Answer (score 3, by Phil Frost - W8II)

If you want a closed-form function, Wikipedia gives those:

\begin{align} R &= \frac{Z_m}{2 \pi \sin^2(kL/2)} \Big\{ \gamma + \ln(kL) - \operatorname{Ci}(kL) + \tfrac{1}{2}\sin(kL) \big[\operatorname{Si}(2kL)- 2\operatorname{Si}(kL)\big] \\ &\qquad\qquad\qquad\qquad + \tfrac{1}{2}\cos(kL)\big[ \gamma + \ln(kL/2) + \operatorname{Ci}(2kL) - 2\operatorname{Ci}(kL) \big] \Big\} \\ X &= \frac{Z_m}{ 4 \pi \sin^2(kL/2)} \Big\{ 2 \operatorname{Si}(kL) + \cos(kL)\big[ 2 \operatorname{Si}(kL) - \operatorname{Si}(2kL) \big] \\ &\qquad\qquad\qquad\qquad - \sin(kL)\big[ 2 \operatorname{Ci}(kL) - \operatorname{Ci}(2kL) - \operatorname{Ci}(2ka^2/L) \big] \Big\} \end{align}

I'm not even going to try to explain those equations since they are so hairy. Easier, and more insightful is to see a graph of the equations (from the same Wikipedia article):

In theory, a 5/8 monopole has an impedance of something like $(75-425j)\:\Omega$, and the impedance of a dipole is twice that of the equivalent monopole, so $(150-850j)\:\Omega$. Eyeballing that on the graph looks about right.

However, the thing to note here is that around 1.25λ, the slope of both the real and imaginary components of the impedance is pretty steep, meaning small changes in length make large changes in impedance. Also note that this graph is valid only for a conductor diameter of 0.001λ. Thicker or thinner conductors can also make a significant difference. The sensitivity of the impedance to these parameters explains the variance in the numbers given by various sources.

Consequently, to successfully build this antenna you will need some way to measure the impedance and adjust accordingly.

## Answer (score 2, by tomnexus)

The impedance is double that of a 5/8 wave monopole, which is well studied, there's lots of information out there.

From the ARRL Antenna Compendium:

"The input impedance of a 5/8-wave whip above a ground plane 1/2 wavelength or more in diameter has a resistive component close to 50 ohms, and a capacitive reactance that depends considerably on the whip diameter, typically in the range of 50 to 150 ohms.

The impedance of your 1.25 wavelength dipole will be about 100 -j100 to -j300 Ohms.

Two comments on this choice of antenna:

- higher gain only means more power if you aim the antenna at the source. If you're harvesting in general, rather use a low gain antenna.
- this is a fairly narrow band antenna, so only really useful if you know the frequency of the signal you are harvesting. Its impedance will change quickly with frequency, and the matching inductors change the other way.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3783/what-is-the-impedance-of-a-1-25-l-dipole-antenna, by Shiva Mudide, Phil Frost - W8II, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
