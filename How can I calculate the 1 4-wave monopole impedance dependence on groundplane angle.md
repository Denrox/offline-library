# How can I calculate the 1/4-wave monopole impedance dependence on groundplane angle?

*Tags: antenna, antenna-theory, impedance · score 5*

## Question

I watched this video of a very nice explanation of a *simple dipole* and *1/4-wave monopole*. In that video they show how you can impedance match the *1/4-wave monopole* by bending the 4 (*virtual ground plane*) pins downwards at an angle, $\theta$, from the horizontal plane. Doing this we can get any impedance ($Z$) between 25 and 70 $\Omega$. This is also very well explained here. However, on the previous page of that last explanation, the impedance also varies somewhat (between 20 to 40 $\Omega$), with the height, $h$, above true ground of the antenna.

I would like to see a *accurate* equation, perhaps in the functional form of: $Z = f(h, \theta)$. Or maybe even more applicable, as $\theta = g(h, Z)$.

- **Is there such an equation available?**
- (*If not, how would I go about finding one?*)

(Picture from here.)

**EDIT**: I found this paper, but the derivation doesn't *properly* include the angle dependence. Also, I don't trust the derivation, as they say the currents are cancelling in the radials, but if they are not at right angles to the radiator, I guess they can't cancel in that direction perpendicular to the horizontal plane?

## Accepted answer (score 7, by Glenn W9IQ)

Once a ground plane antenna is 0.5 wavelengths or so above ground, there is no significant effect from the ground on the impedance of the antenna so it can be ignored.

A close approximation of the real part of the feedpoint impedance in ohms of a 1/4 wave ground plane antenna in free space is given by:

$$Z_{real}=20+\frac{2}{3}\theta \tag 1$$

where $\theta$ is the degrees of radial drop (0=horizontal) and 0$\le\theta\le$60.

The imaginary impedance in ohms can also be closely approximated by:

$$Z_{imag}=-29+0.7\theta \tag 2$$

Here is a simulation of the complex impedance of such an antenna:

You can see that at ~45 degrees of droop, the real part of the impedance is ~52 ohms. It can also be observed that at other angles there can be an appreciable imaginary impedance for which compensation could be added to negate its effect on SWR.

Recall, however, that impedance or SWR is not a figure of merit for an antenna. The highest gain of this type of antenna in free space occurs when the radials droop 90°. In this configuration, the antenna can be viewed as a vertical, 1/2 wave dipole or a 1/4 wave sleeve antenna if the feedline enters from within the bounds of the extremities of the radial field.

**A Deeper Examination**

In comments now moved by the moderator, the OP bemoaned the notion that amateur radio operators have lost their technical edge as no one was able to give fundamental equations to support the observable effect of impedance change due to ground plane droop.

I participate on this board to help mentor hams as well as to learn from the many other willing regulars and even the visitors on this site. Since this is obviously a volunteer effort, I differentiate the level of effort I put into my responses from the type of response I would give in a professional setting. However in the spirit of helping the OP to gain a broader understanding, I offer the following.

The graph that I presented above is done with a technique called moment method. In the distant past as a student, I was required to demonstrate that I could calculate this long hand. But just as I no longer calculate a square root by hand, I used a computer tool to quickly get to the answer.

Another technique that can be used to derive the complex radiation resistance is to integrate the Poynting vector over a large sphere and then equate this power to:

$$(I_o/\sqrt{2})^2R_o \tag 3$$

where $R_o$ is the radiation resistance at the current maximum point and $I_o$ is the peak time value of current at that point.

Yet another approach is to use the induced EMF method but this can only determine the self impedance and it will be limited to length to diameter ratio > ~100. It is, however, a closed form calculation. To fully calculate the self impedance with this method requires a 40 step or so derivation which I will not execute here. But the interesting result is that for a 1/2 wave dipole (recall that this is the realized configuration of a 90 degree drop of the radials) the real part of the self impedance is:

$$R_{11}=30Cin(2\pi) \tag 4$$

Note that the function $Cin(2\pi)$ evaluates to 2.44.

The same method applied to a quarter wave radiator over a large ground plane results in:

$$R_{11}=15Cin(2\pi) \tag 5$$

Take note that this lengthy computation results only in a simple change of the constant. This method closely agrees with the moment method presented above. It should also be recognized that this is another demonstration of the well known feedpoint impedance comparison of a 1/4 wave antenna over a large ground plane and 1/2 wavelength, center fed antenna.

The imaginary part of the self impedance can be similarly calculated with the induced EMF method if this information is required.

**

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10040/how-can-i-calculate-the-1-4-wave-monopole-impedance-dependence-on-groundplane-, by not2qubit, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
