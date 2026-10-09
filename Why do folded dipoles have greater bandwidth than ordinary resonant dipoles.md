# Why do folded dipoles have greater bandwidth than ordinary resonant dipoles?

*Tags: antenna, dipole, bandwidth, folded-dipole, antenna-theory · score 19*

## Question

This is something I've read in passing, but never encountered an explanation of why. For example, Wikipedia says:

Another common place one can see dipoles is as antennas for the FM band; these are folded dipoles. The tips of the antenna are folded back until they almost meet at the feedpoint, such that the antenna comprises one entire wavelength. This arrangement has a greater bandwidth than a standard half-wave dipole.

Wikipedia isn't the only one with this notion: see comments to [this answer](80%20160m%20Shortened%20Dipole%20Trap%20Questions.md):

it was my understanding that a folded dipole is still full length, just doubled over to increase bandwidth. Am I incorrect?

antenna-theory.com, which I'd consider at least three times more reliable than Wikipedia, doesn't say anything about bandwidth, but does say this:

Because the characteristic impedance of twin-lead transmission lines are roughly 300 Ohms, the folded dipole is often used when connecting to this type of line, for optimal power transfer. Hence, the half-wavelength folded dipole antenna is often used when larger antenna impedances (>100 Ohms) are needed.

I could then see how, if you had to use 300Ω transmission line, you might get better bandwidth with a folded dipole as you wouldn't need a matching network, which might limit bandwidth or incur additional loss, but that's a long guess.

So, really why do folded dipoles have greater bandwidth? Or is that just an unsubstantiated rumor?

## Answer (score 11, by on4aa)

## Loaded $Q$-factor

Like any resonant circuit, the bandwidth of an antenna is determined by its loaded quality factor, defined by $Q_{\ell}\overset{.}{=}\frac{X}{R}$.

**The lower the loaded $Q$-factor, the broader the antenna's bandwidth will be:** $BW_{-3dB}=\frac{f_{res}}{Q_{\ell}}$, with $f_{res}$ the resonant frequency.

## Analysis of the loaded $Q_{\ell}$ of a folded dipole in free space

#### Resistance $R$ (identical to that of an ordinary dipole)

In above formula for $Q_{\ell}$, the resistance $R$ in the loaded resonant circuit will be half the radiation resistance $R_{rad}$ when the antenna is perfectly matched. Hence, $R=\frac{R_{rad}}{2}$. Note that this value is not any different from that of an ordinary dipole, even though the input impedance $R_{in}$ of a folded dipole is four times that of an ordinary dipole. The higher input resistance $R_{in}$ is merely due to the impedance transforming property of closely spaced parallel wires. In conclusion, **$R$ provides no explanation for the higher bandwidth.**

#### Reactance $X$ (lower than that of an ordinary dipole)

Now, let us evaluate reactance $X$ in above formula for $Q_{\ell}$. For a dipole in free space, $X$ is determined by the self-reactance of the antenna conductor. This will be a combination of self-inductance of the element conductor and self-capacitance between the two element halves.

The closely spaced parallel conductors of a folded dipole **should really be seen as one very thick conductor.** Hence, **its self-inductance will be lower and its self-capacitance higher** than that of an ordinary dipole. Both effects result in a **lower reactance $X$.**

Therefore, the loaded $Q_{\ell}\overset{.}{=}\frac{X}{R}$ will be lower, which broadens the bandwidth of the folded dipole.

## Answer (score 11, by G8HQP)

The increased bandwidth of a folded dipole is almost entirely due to the extra thickness. Two parallel elements behave as a thicker single element. There is a small contribution too from the combination of the reactances of the transmission-line mode and radiator-mode acting in opposite directions.

## Answer (score 8, by WPrecht)

A little capacitive reactance is what gives you the greater bandwidth.

In a regular ½λ dipole, the current that flows along the conductors are in phase. When we add the second conductor in a folded dipole, what we are really doing is extending the dipole. As a result the current in the new section flows in the same direction as those in the original dipole. The currents along both the half-waves are therefore in phase and the antenna will radiate with the same characteristics as a regular simple ½λ dipole.

Perhaps an illustration will help (ARRL Extra Class License Manual):

Remember, this is AC current. At points B and C (the ends of a simple dipole) it drops to zero. Since a folded dipole is like extending a dipole by a 1/4λ at each end, we will observe the current reversing at B & C as we start a new cycle.

Since the current is now evenly divided into the two sections, the impedance must increase according to Ohm’s Law (W = I^2R) by a factor of 4. This makes the folded dipoles an attractive option to hams that like to use twin lead or ladder line for feed lines.

Another way to look at the situation is that the impedance of the dipole appears in parallel with the impedance of the folded sections. At a frequency away from resonance, the reactance of the dipole is of the opposite form from that of the folded section and as a result there is some reactance cancellation at the feed point of the antenna.

So in essence you get some “free” matching right at the feedpoint of the antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/830/why-do-folded-dipoles-have-greater-bandwidth-than-ordinary-resonant-dipoles, by Phil Frost - W8II, on4aa, G8HQP, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
