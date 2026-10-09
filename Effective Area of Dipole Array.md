# Effective Area of Dipole Array

*Tags: antenna, wire-antenna, dipole, phased-array · score 6*

## Question

I'm trying to design a low frequency dipole interferometer antenna array. I am realizing how little I know about radio antennae. I'm confused by the concept of effective area $A_e$ and how it applies to arrays. I haven't been able to get a clear answer on that.

Let's say I'm using my array to receive 10MHz signals. That's $\lambda = 30\,\text{m}$, so is my effective area $A_e \approx \lambda^2/4\pi \approx 72\,\text{m}^2$? Is that for each dipole antenna? How does effective area change when I combine them?

What factors do I need (e.g. dipole length, spacing, baseline) to calculate the effective collecting area for the array as a whole?

## Answer (score 2, by Phil Frost - W8II)

For some context, the relevant part of the cited source:

The average collecting area is defined by

$$ \langle A_e \rangle \equiv {\int_{4\pi} A_e d \over \int_{4\pi}d}.$$

The effective collecting area of a receiving antenna is independent of its radiation environment, so this result applies for any type of radiation, not just blackbody radiation. Without using Maxwell's equations we have obtained the remarkable result true for *all* lossless antennas:

$$ \langle A_e \rangle = {\lambda^2 \over 4 \pi} \tag{3A6} $$

- Any antenna, from a short dipole to the 100-m diameter Green Bank Telescope, has the same average collecting area $\langle A_e \rangle$ that depends only on wavelength.

In the case of an isotropic antenna, the effective collecting area in any direction equals the average collecting area:

$$ A_e(\theta, \phi) = \langle A_e \rangle = {\lambda^2 \over 4 \pi} $$

The description follows after a description about thermodynamic equilibrium and this illustration:

*A cavity in thermodynamic equilibrium at temperature $T$ containing a resistor $R$ is coupled to an antenna, also at temperature $T$, through a filter passing frequencies in the range $\nu$ to $\nu+d \nu$.*

The discussion involves the thermodynamic equilibrium between the resistor and the antenna. This "average collecting area" is describing what should be fairly intuitive: this equilibrium holds regardless of what kind of antenna is put in the left cavity.

In other words, the average collecting area has something to do with how the antenna responds, *on average*, over all directions. It must be the same for all lossless antennas because anything else would violate conservation of energy.

Note the average collecting area is $\langle A_e \rangle$. Just $A_e$ on its own is *effective aperture*, which has an additional term $G$ added for gain:

$$ A_e = {\lambda^2 G \over 4 \pi} $$

Gain is often given as a single number, just the maximum gain for the antenna. But more completely, gain is defined as a function over direction and polarization. Since the average collecting area is the same for any lossless antenna design, and the effective aperture is the average collecting area multiplied by gain, it follows that if gain is to be increased in some direction, it must necessarily be decreased in some other direction if no laws of thermodynamics are to be broken.

For an array of $N$ antennas, the effective aperture is at best $N A_e$ where $A_e$ is the effective aperture of a single antenna. In practice it's less, due to either limited performance of the correlators, or due to overlap between the fields of the antennas.

If the antennas are several wavelengths apart, then the interactions between them will be negligible and performance will be dominated by the correlators.

If the antennas are closer than that, mutual coupling between them must be considered. The interactions are not simple or amenable to a closed form solution, so usually some antenna modelling software is used to solve the equations numerically.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13304/effective-area-of-dipole-array, by Spuds, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
