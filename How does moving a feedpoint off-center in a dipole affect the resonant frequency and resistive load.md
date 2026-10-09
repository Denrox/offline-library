# How does moving a feedpoint off-center in a dipole affect the resonant frequency and resistive load?

*Tags: antenna, impedance, dipole, antenna-theory · score 19*

## Question

Specifically, I understand that OCF dipoles change the SWR, but does it do this via reactance or resistance, or both?

## Accepted answer (score 13, by Phil Frost - W8II)

I'm going to assume we are discussing *ideal*, *resonant* dipoles.

Consider what's happening inside the dipole. Say you are transmitting a carrier. Say at one point in this carrier's cycle, the voltage is shoving all the charge carriers to the left.

What makes the dipole *resonant* is this: those charge carriers get pushed down the wire. As the approach the end, they get compressed because they have nowhere to go. This over-abundance of charge carriers means a high voltage at the end of the wire. They can't shoot out the end of the wire, so that wave of force bounces back. In a center-fed half-wavelength dipole, the wave reaches the feedpoint after having bounced off the end at precisely when the transmitter has changed phase 180 degrees, and is now trying to push the charge carriers in the other direction. Thus, the natural bouncing back and forth action in the antenna is in phase with the transmitter, helping it to move more current, with less voltage.

This explains two things on the FCC test:

- The voltage distribution in a half-wave dipole is highest at the ends and lowest in the middle.
- The current distribution is highest in the middle and lowest at the ends.

We know that our center-fed half-wavelength dipole has a feedpoint impedance of 75Ω. That means at the feedpoint, for every ampere, there are 75 volts (think of Ohm's law). This is true both of RMS measurements, and any instantaneous measurement.

This last bit, that the instantaneous current or voltage at any time also have a ratio of 75V to 1A (that is, 75Ω), is just another way of saying that the feedpoint impedance is purely resistive. Our ideal dipole doesn't actually have any resistance: this resistance is the radiation resistance of the antenna. The antenna creates the illusion of a pure resistance from a tuned system of reactive components which, *at resonance*, cancel each other to leave only a resistive impedance.

*But what if the feedpoint isn't in the center?*

This actually doesn't change the resonant frequency: it just changes the impedance, which remains resistive. Consider what happens if we move the feedpoint just a little closer to one end: we also get farther from the other end. We know that in the center of a half-wave dipole, current is at a maximum. This makes sense, because after the charge carriers pass the center, they are now closer to the other end, building up voltage there, which serves to slow them down. So, if we aren't in the center, we get less help with current, but we get more help with voltage. That is, impedance goes up. We can couple energy just as efficiently into this antenna, provided we can match its impedance.

The common choice of the center of a half-wave dipole is usually selected because it's close enough to 50Ω coax that losses are acceptable without any additional matching. Wikipedia gives the math to calculate the impedance at an arbitrary point for a half-wave dipole:

$$ R_r = \frac{75\ \Omega}{\sin^2(2 x \pi / \lambda)} $$

Where:

- $x$ is the distance from the end of the dipole, and
- $\lambda$ is the wavelength (twice the length of the dipole).

For example, say we have a dipole for $\lambda = 100\:\mathrm m$. Fed at the center, $x = 25$ because this half-wave dipole is 50m long, so the middle is half of that, 25m from the end:

$$ R_r = \frac{75\ \Omega}{\sin^2(2 \cdot 25 \cdot \pi / 100)} = 75\:\Omega $$

Fed 1/3rd of the way from the end, $x=50/3=16.67$:

$$ R_r = \frac{75\ \Omega}{\sin^2(2 \cdot 16.67 \cdot \pi / 100)} = 100\:\Omega $$

Further reading:

- Dipole antenna feed impedance, radio-electronics.com
- 200 Ohm Feed Point Off-centre Fed Dipole, amateurradio.com

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/95/how-does-moving-a-feedpoint-off-center-in-a-dipole-affect-the-resonant-frequen, by Bill - K5WL, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
