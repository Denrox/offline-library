# What is the velocity factor of a wire?

*Tags: antenna-construction, theory · score 6*

## Question

This is Belden 9223. It is a 50-ohm coaxial cable, velocity factor 0.56

This is Belden 8524. It is a 22 AWG hookup wire. No velocity factor in the datasheet.

Why does the coax datasheet have a velocity factor, while the hookup wire datasheet does not?

## Accepted answer (score 8, by Juancho)

A coaxial cable is a transmission line by itself, and therefore the velocity factor is known. It depends on the dielectric properties, geometry, and conductivity.

A single wire is not a transmission line. You need a return path for the current, and that will most probably be a second wire somewhere, or a ground plane.

So the geometry and dielectrics around the two conductors is unknown, and thus the velocity factor is unknown.

## Answer (score 8, by Phil Frost - W8II)

Velocity factor is a property of electromagnetic wave propagation, not wire. A transmission line (like coax) is a conduit for an electromagnetic wave in itself, so the velocity factor can be defined. In fact, the velocity factor can be derived from the lumped model of a transmission line:

Following the usual simplifying assumptions of a lossless transmission line, R and G become insignificant. If $L$ and $C$ are inductance (henry) and capacitance (farad) per meter, then the velocity of propagation in a transmission line is:

$$ v = \frac{1}{\sqrt{LC}} \tag{1} $$

The velocity factor is just this relative to the velocity of propagation in a vacuum: $v/c$.

A very similar equation is the characteristic impedance of the transmission line:

$$ Z_0 = \sqrt{\frac{L}{C}} \tag{2} $$

Thus, if we know any two of:

- characteristic impedance,
- capacitance per unit length, or
- inductance per unit length

then we can calculate the velocity factor. Let's try it for Belden 9223, which specifies in the datasheet:

$$ Z_0 = 50\:\Omega \\ C = 37\:\mathrm{pF}/\mathrm{ft} = 1.21 \cdot 10^{-10}\:\mathrm{F/m} $$

So by equation (2):

$$ \begin{align} 50\Omega &= \sqrt{\frac{L}{ 1.21 × 10^{-10} }} \\ 50^2 &= \frac{L}{ 1.21 × 10^{-10} } \\ L &= 3.03 \cdot 10^{-7}\:\mathrm{H}/\mathrm{ft} \end{align} $$

And then by equation (1):

$$ \begin{align} v &= \frac{1}{\sqrt{( 3.03 \cdot 10^{-7} )( 1.21 × 10^{-10} )}} \\ v &= 165289256 \:\mathrm{m/s} \end{align} $$

Thus the velocity factor is:

$$ v/c = 165289256 / 299792458 = 0.55 $$

The datasheet says 0.56. I attribute the discrepancy to rounding error.

So what about a single wire? What values do we use for L and C?

That depends on the geometry of the wire. In the case of coax, the wave is propagating within the dielectric between the center conductor and the shield. This dielectric has a known geometry and composition, so the manufacturer can specify a velocity factor.

In the case of a wire, the wave will be propagating between the wire, and something else. Maybe the ground. Maybe another wire. Maybe the same wire some distance away, as in the case of a dipole. Are you stretching the wire in a straight line, or winding it into a coil? The capacitance will be depend on the permittivity of the space containing the electric field. Is it air? A tree? Because there are so many variables, a wire datasheet can not possibly specify a velocity factor. And while we might measure one, we must be careful to specify what propagation mode we are talking about, and the conditions under which it was measured.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2390/what-is-the-velocity-factor-of-a-wire, by Phil Frost - W8II, Juancho. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
