# Voltages in a beam antenna's passive elements?

*Tags: antenna, antenna-theory · score 4*

## Question

This [question](What%20is%20the%20peak%20voltage%20at%20the%20tips%20of%20a%20dipole%20antenna.md) has good answers for the voltages reached in portions of a dipole antenna during transmit.

In a beam (Yagi or Yagi-Uda) antenna, do points along passive or parasitic elements (reflectors and directors, etc.) also reach similarly high peak voltages? If so, by what relationship to the driven element?

## Accepted answer (score 2, by Brian K1LI)

I used EZNEC (NEC2) to model a λ/2 dipole in free space. The program reports the voltage very close to the end of the dipole as 3910 volts with 100 watts of driving power.

The resonant frequency of this dipole was 14.27MHz. Moving to 14MHz resulted in 5392 volts at the end for the same 100W power input to the feedpoint. Moving to 14.54MHz resulted in 4536 volts.

EZNEC includes an example 5-element 20m yagi design. The currents on the first two directors are surprisingly close in magnitude to the current in the driven element, while the current in the reflector is about 30% of the driven. These figures correlate with the deviations of the element lengths from the antenna's design frequency: the closer an element's resonance to the design frequency, the higher the current. These should give you an idea of the voltages at the ends of those elements.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15382/voltages-in-a-beam-antenna-s-passive-elements, by hotpaw2, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
