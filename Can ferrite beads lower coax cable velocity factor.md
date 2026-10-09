# Can ferrite beads lower coax cable velocity factor?

*Tags: coaxial-cable, impedance, transmission-line, ferrite · score 8*

## Question

For VHF and UHF, it seems reasonable to slip ferrite beads over a coaxial cable to act as a transmission line common mode choke. It also seems reasonable to use beads with the smallest diameter possible. This can lead to ferrite-over-cable lengths on the order of 250-400mm or more with a slip-fit ferrite cover. Can this affect the cable's velocity factor or impedance?

## Accepted answer (score 8, by Brian K1LI)

No, adding ferrite beads to choke currents on the outside of the shield of a coaxial cable does not affect its impedance or velocity factor. Impedance and velocity factor are determined by the *inside* construction of the cable: the outside diameter of the inner conductor, d, the inside diameter of the outer conductor (shield), D, and the magnetic permeability, $\mu$, and dielectric constant, $\epsilon$, of the material that separates them: $$Z_0=\frac{1}{2\pi}\sqrt{\frac{\mu}{\epsilon}}ln\frac{D}{d}$$

## Answer (score 6, by Cecil - W5DXP)

For well-designed coax, the EM fields are confined to the space between the inside of the braid and the center conductor, i.e. the dielectric insulation region which affects the velocity factor. Therefore, those beads have negligible effect on the differential signals. They do have an effect on the common-mode signals on the outside of the braid which has very little to do with the differential velocity factor or characteristic impedance of the coax.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13377/can-ferrite-beads-lower-coax-cable-velocity-factor, by Chris K8NVH, Brian K1LI, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
