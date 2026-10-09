# Dipole antenna radiation field equation

*Tags: antenna, dipole, radiation-pattern · score 5*

## Question

Can anybody provide me with an idealised formula that describes the radiation pattern of an omnidirectional dipole antenna?

In particular I am interested in the formula that creates a plot similar to the following:

Note: I am looking for a simplified closed-form equation, not a full field simulation.

## Answer (score 7, by Brian K1LI)

The antenna you describe is "omnidirectional" only in the *xy*-plane; it has zero radiation along the *z*-axis. Thus, your dipole is mounted vertically; i.e., *x*=0 and *y*=0 for all segments.

According to *Antennas* by John Kraus, the far *E*-field for a center-fed $\lambda/2$ dipole in free space is:

$$E = \frac{\cos\left({\pi\over 2}\cos\theta\right)}{\sin\theta}$$

In the case of a vertically mounted antenna, $\theta$=0 at the horizon of the plot.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12096/dipole-antenna-radiation-field-equation, by David, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
