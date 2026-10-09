# What happens if I “open” a folded dipole so that the two wires are not connected anymore?

*Tags: antenna, dipole, folded-dipole · score 5*

## Question

A folded half wave dipole consists of two wires in parallel with only one of the wires driven, but the ends of the two wires electrically connected. As I understand it (and I may well be wrong there) the folded dipole still behaves similarly to a regular half wave dipole because effectively an almost identical current gets induced in the parallel wire without the feed point. However because only one wire is directly fed, meaning the feed point sees only half the current, impedance is quadrupled (half the current at the same power means quadrupled impedance).

If that’s “all”, I wonder whether it matters if the wires are actually connected. If I remove the connection between the two, having essentially a normal dipole with a parallel parasitic dipole next to it, will the antenna exhibit similar characteristics as a folded dipole?

Or did I misunderstand completely?

## Accepted answer (score 2, by hobbs - KC2G)

If I remove the connection between the two, having essentially a normal dipole with a parallel parasitic dipole next to it, will the antenna exhibit similar characteristics as a folded dipole?

No, it becomes very different, and the reason why it does is the same reason why the folded dipole has 4x the impedance of the regular dipole. The mutual inductance between the two wires creates an emf which makes current in the parallel element flow in the *opposite* direction of the driven element, so that the voltages at the ends of each element would also be opposite in sign. By connecting up the elements end-for-end, we force them to have the *same* voltage at each end, and to have current in the *same* direction. By the very same principle, once we've done so, the current in the parallel element creates an emf that opposes the current in the driven element, and you can see that as the reason for the increase in the feedpoint impedance.

When the element ends are disconnected, the opposite happens. The current in the driven element induces an opposite current in the parallel element; the current in the parallel element creates an emf which doesn't oppose but *coincides with* the feedpoint voltage, and so the feedpoint impedance *drops* drastically. The fields from the two close-spaced parallel conductors with opposite currents cancels almost 100% in the far-field (as with a parallel transmission line), so the antenna is a very poor radiator.

I did NEC2 simulation of a 40m folded dipole made of 14AWG wire at a height of 75' above average ground and an element spacing of 6", and optimized for resonance at a frequency of 7.15 MHz, which gave a length of 66'3" (20.2 m). Its feedpoint impedance was 252+j0.5 ohms and the pattern was classic dipole. With the connecting wires removed, the main elements had to be lengthened to 68'9" (21.0m) to get resonance, the feedpoint impedance became 0.02+j0.4 ohms, and the pattern showed some gain in the direction of the driven element, indicating that the parallel element was acting as a reflector.

So what you get is technically a yagi, with a yagi's directionality, and reduced impedance compared to a dipole. But it's a very bad yagi. A good yagi uses spacing between the parallel elements, and different length elements, to create a phase shift between the elements which gives improved gain in one direction, and prevents the impedance from dropping so very low. With close-spaced equal-length elements, the phase shift is very small (about one degree) so you get something that would rather be a resonator than an antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21093/what-happens-if-i-open-a-folded-dipole-so-that-the-two-wires-are-not-connected, by anyfoo, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
