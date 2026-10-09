# Antenna design - Ground plane in simulation and in practice

*Tags: antenna-construction, measurement · score 3*

## Question

For monopole antennas, the ground plane acts as another arm of an equivalent dipole antenna. I'm wondering how we can expect the behavior of that antenna in practice, because the ground plane is usually used for components soldered on it. For instanse, please have a look at the following photo (Source: THE STUDY AND IMPLEMENTATION OF MEANDER-LINE ANTENNA FOR AN INTEGRATED TRASNSCEIVER DESIGN).

I have 2 questions:

1/ The antenna is matched to be 50 ohm at **A** (Fig. a). So, to measure it in practice, the author designed a 50-ohm transmission line which connects **A** to **B**. Am I right?

2/ With some components soldered on the ground plane in Fig. d, I think the input impedance and the performance of that antenna, if measured again at **A**, must be changed compared to those of the antenna only in Fig. b and c. That kind of antenna is significantly dependent on the ground plane. So, how can we know, when designing an antenna, an antenna will perform better or worse with integrated components like Fig. d? I understand that we just can design and measure the antenna performance without these components.

Any suggestions would be highly appreciated.

## Accepted answer (score 3, by Glenn W9IQ)

The antenna is matched to be 50 ohm at A (Fig. a). So, to measure it in practice, the author designed a 50-ohm transmission line which connects A to B. Am I right?

The antenna by itself is not a 50 ohm, resonant antenna. It will likely have a complex impedance that needs to be transformed to a 50 ohm purely resistive impedance (typically). That is the job of the matching network. I believe you can see the matching network in picture B just above the highlight box you added.

From the matching network, the designer has used a transmission line known as a GCPW (Grounded Coplanar Waveguide). Like any transmission line, the goal is to conduct RF current from point A to point B without radiating any RF energy while minimizing losses (attenuation). In this case, the GCPW has likely been designed to have a ZO of 50 ohms.

In the ideal case, the output impedance of the transmitter or receiver is specified as 50 ohms impedance and the antenna impedance has been transformed to a 50 ohm impedance. This minimizes the losses along the 50 ohm transmission line and allows the specified power to be conducted between the two points with minuscule radiation from the GCPW.

I think the input impedance and the performance of that antenna, if measured again at A, must be changed compared to those of the antenna only in Fig. b and c. That kind of antenna is significantly dependent on the ground plane. So, how can we know, when designing an antenna, an antenna will perform better or worse with integrated components like Fig. d?

The primary difference between picture B and D is that the transmitter/receiver components have been added to the board. These components are independent of the monopole portion of the antenna. The transmitter/receiver could also have been placed on another PCB (printed circuit board) but then some interconnect scheme would need to be used. This likely would reduce the reliability and increase the cost of the assembly but it may be necessary in some situations in order to meet form factor requirements.

Regarding the ground plane on the circuit board, this will inevitably form part of the antenna. A monopole antenna needs a return path for current. If a return path is not specifically provided, such as the second element in a dipole for example, the RF will find a return path through other means. In the case of this meander antenna, the ground plane on the circuit board becomes part of the antenna and thus radiates. This can be a design challenge because RF current is now flowing through the copper ground plane on the board and this can easily couple to other circuit elements. The designer needs to take care that this effect is understood through simulation and controlled in the implementation through careful attention to current path details.

## Answer (score 4, by Kevin Reid AG6YO)

The antenna is matched to be 50 ohm at A (Fig. a). So, to measure it in practice, the author designed a 50-ohm transmission line which connects A to B. Am I right?

Yes. This choice means that the difference in overall physical structure versus Fig. d is smaller than if the design used a smaller PCB.

For monopole antennas, the ground plane acts as another arm of an equivalent dipole antenna.

Remember that in the situation usually described this way, the monopole is *perpendicular* to the ground plane. On the other hand, when we speak of ground planes of PCBs we mean circuitry being laid *parallel* to the plane.

In this picture, the closest analogue of the monopole's ground plane is the *edge* of the PCB ground plane that is adjacent to the antenna. The portion that is further away from the antenna can be thought of as being “buried underground” or “in the shadow”; will still have some effect on the antenna, because the radiation and currents do propagate in that direction, but it will be much smaller.

Note also that the added components in Fig. d are placed as far away from the antenna as possible. Thus, the influence of the added components on the antenna structure is minimized. If we consider how big to make this separation — well, we're outside of my expertise, but [I've heard that](When%20and%20why%20does%20the%20size%20of%20a%20ground%20plane%20or%20radials%20matter.md) it's good for antenna ground planes/radials to be at least a quarter-wavelength in radius, which is not exactly satisfied here but is close.

And remember, any physical implementation of an antenna will have many other flaws compared to a simple model of the antenna type (e.g. the feedpoint being of a significant size rather than being a point) — one's goal should not be to make things exactly fit the ideal but to tweak the antenna so that it functions well when used in a real environment.

Finally: This is all sloppy intuitive reasoning. True answers come from antenna simulations.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10525/antenna-design-ground-plane-in-simulation-and-in-practice, by Minh Lam, Glenn W9IQ, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
