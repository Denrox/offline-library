# How do I design a round or square coaxial transmission line to have a specific impedance?

*Tags: diy, coaxial-cable, impedance, transmission-line · score 10*

## Question

Certain Hex Beam antennas use a coaxial center support post to send the RF to each antenna section, which is superior, in terms of maintenance, to a post with screw terminals connected by short lengths of coax used in previous designs.

I'd like to use off the shelf stainless steel tubes and rods to accomplish this, but I have access to enough machining equipment that I can adjust some parts to give me better dimensions.

Specifically, if I'm aiming for a 1.5" square outer stainless steel tube, what dimension should the inner stainless steel conductor be to attain 50Ω impedance, assuming air as the insulator between the two? The tube has a 0.065" thick wall, so the inner dimensions are 1.37" x 1.37".

Generally, what are the equations I need to design such transmission lines with different dimensions, conducting materials, and impedance in the future?

## Accepted answer (score 8, by Phil Frost - W8II)

#### Executive Summary

Assuming:

- air dielectric (insulator)
- 50Ω characteristic impedance

Then for round coax, make the inside diameter of the outside conductor 2.302 times larger than the diameter of the inside conductor.

If the shield is square, and the inner conductor is still round, make the inside length of one side of the shield 2.134 times larger than the diameter of the inside conductor.

#### Explanation, for Round Coax

A coaxial transmission line has some inductance per unit length $L$, and some capacitance per unit length $C$. The conductors also have some (very low) resistance $R$, and the dielectric has some (very low) conductance $G$. Though it's important to note that these properties are distributed throughout the entire length of the transmission line, lumping them all together we can model a transmission line as:

The characteristic impedance is then:

$$ Z_0=\sqrt{\frac{R+j\omega L}{G+j\omega C}} $$

where:

- $R$ is the resistance per unit length, considering the two conductors to be in series,
- $L$ is the inductance per unit length,
- $G$ is the conductance of the dielectric per unit length,
- $C$ is the capacitance per unit length,
- $j$ is the imaginary unit, and
- $\omega$ is the angular frequency.

If we assume a good conductor and dielectric, then $R$ and $G$ are negligible. The equation then simplifies to:

$$ Z_0 \approx \sqrt{\frac{L}{C}} $$

For *round* coaxial transmission lines, we can calculate $C$ and $L$ as:

$$ C = {2 \pi \epsilon_0 \epsilon_r \over \ln(D/d)} $$

$$ L = {\mu_0 \mu_r \over 2 \pi} \ln(D/d) $$

where:

- $d$ is the diameter of the inner conductor,
- $D$ is the inside diameter of the outer conductor,
- $\epsilon_0$ is the permittivity of free space, approximately $8.854 \cdot 10^{−12} F \cdot m^{-1}$
- $\mu_0$ is the permeability of free space, approximately $1.256 \cdot 10^{-6} H \cdot m^{-1}$
- $\epsilon_r$ is the relative permittivity of the dielectric, and
- $\mu_r$ is the relative permeability of the dielectric.

Putting these together and simplifying we get:

$$ \begin{align} Z_0 &\approx \sqrt{\frac {{\mu_0 \mu_r \over 2 \pi} \ln(D/d)} {{2 \pi \epsilon_0 \epsilon_r \over \ln(D/d)}} } \\ &\approx \sqrt{\frac {\mu_0 \mu_r \ln(D/d)^2} {(2 \pi)^2 \epsilon_0 \epsilon_r} } \\ &\approx \sqrt{\frac {\mu_r} {\epsilon_r} } \sqrt{\frac {\mu_0} {(2 \pi)^2 \epsilon_0} } \ln(D/d) \\ &\approx \sqrt{\frac {\mu_r} {\epsilon_r} } 59.96 \ln(D/d) \\ \end{align} $$

For an air dielectric, $\epsilon_r$ and $\mu_r$ are so close to 1 than you can further simplify:

$$ Z_0 \approx 59.96 \ln(D/d) $$

You can also see that only the *ratio* of the diameters of the conductors are relevant, so it doesn't matter what units of length are used, as long as they are the same.

We can solve for $D/d$, and set $Z_0 = 50 \Omega$:

$$ \begin{align} 56.40 \ln(D/d) &\approx Z_0 \\ \ln(D/d) &\approx \frac{Z_0}{59.96} \\ D/d &\approx e^{Z_0/59.96} \\ D/d &\approx e^{50/59.96} \\ D/d &\approx 2.302 \end{align} $$

#### Explanation, for Square Shield with a Round Center Conductor

This is a rather less common situation. Kevin Schmidt, W9CF has a full explanation. The equations are rather more complex, owing to the more complex geometry of the conductors, and are most easily solved by computer. However, a good approximation for impedances around 50Ω, with an air dielectric, is:

$$ Z_0 \approx 59.96 \ln(1.079 D/d) $$

or solved for $D/d$:

$$ D/d \approx {e^{Z_0/59.96} \over 1.079} $$

Where:

- $d$ is the diameter of the inner conductor, and
- $D$ is the inside length of one side of the shield.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1304/how-do-i-design-a-round-or-square-coaxial-transmission-line-to-have-a-specific, by Adam Davis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
