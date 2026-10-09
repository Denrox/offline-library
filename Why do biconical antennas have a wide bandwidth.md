# Why do biconical antennas have a wide bandwidth?

*Tags: antenna-theory · score 6*

## Question

Why does a horizontal biconical antenna have a wider bandwidth than a dipole of similar length? What's the physics behind the biconical geometry having a bandwidth uncoupled from its length in wavelengths, as for a (near) resonant half-wave dipole.

## Answer (score 5, by Andrew)

Hotpaw.

In general dipole antennas with thicker elements have larger bandwidth than those with thinner elements.

The main reason is that for a given length, the rate of change in self inductance as per change in frequency of an antenna element decreases as its cross-sectional area increases, and self inductance is one of the parameters which determines the resonant frequency.

For antenna elements with a circular cross sectional area, self inductance is described by the following formula, where it is apparent that the larger the diameter the smaller the self inductance.

$L_{wire}$ is the inductance in H, $D$ is the diameter in cm, $L$ is the length in cm, $μ$ = permeability.

The impedance of a half wave dipole can be calculated by these next two formulas, where it's clear that self inductance is a determining factor.

$L$ is dipole length, $a$ is the radius of the conductors, $k$ is the wave number $\frac{2πf}{c}$, $η_0$ denotes the impedance of free space = 377Ω, and $\gamma_e$ is Euler's constant = 0.57721566

The Q of an antenna $Q = \frac{XL}{R}$ or $Q = \frac{2πFL}{R}$ shows that bandwidth increases with decreasing inductance, however it is the rate of change of self inductance versus change in frequency that mostly determines the actual bandwidth, which for a given length decreases with increasing element cross sectional area.

In simpler terms, if you imagine a half wave dipole element as a long thin cylindrical tube which has a cross sectional area and volume, there is a range of lengths that will 'fit' into this depending on where you measure from, eg; from center of the left end to center of the right end, or looking side on, from top left to bottom right.

So it makes sense that a thicker antenna can fit a larger range of wavelengths into it's three dimensional shape than a thinner antenna.

In theory, an infinitely thin dipole with zero cross sectional area and zero volume would have infinite self inductance and a bandwidth of zero Hz.

Hope that makes sense !

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21168/why-do-biconical-antennas-have-a-wide-bandwidth, by hotpaw2, Andrew. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
