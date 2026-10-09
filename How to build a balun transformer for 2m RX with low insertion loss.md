# How to build a balun transformer for 2m RX with low insertion loss

*Tags: balun, toroid, transformer · score 5*

## Question

I'm looking into ways to match a 137MHz RX dipole antenna to an unbalanced coax + amplifier. I know there are several types of baluns which can be categorized under magnetic baluns (where there are separate primary and secondary windings) and current baluns which are essentially chokes.

I was hoping I could build a transformer type balun, since this would allow me to choose almost any impedance matching ratio I want. I have FT50-61 and FT50-63 toroid cores, which are advertised to work as wideband transformers from 10 MHz - 200 MHz.

I tried winding a few 1:1 transformers for measuring purposes and the results were pretty bad, I got at least -3.5 dB insertion loss. I tried using between 2 and 8 windings of different diameters of copper and silver for both primary and secondary.

This is a typical response (depending on how close the windings are and how many I put on it, I can move the peak left and right by a few ten MHz only):

Now I'm wondering if there is a systematic approach to getting good insertion loss, maybe by moving the peak of the curve to 137 MHz.

Any tips are appreciated.

## Accepted answer (score 3, by Glenn W9IQ)

VHF transmission line baluns are very difficult to construct due to interwinding capacitance. As a result, the balun will have an undesirable self resonant point and will not typically reach the desired transformation ratio. Note that a balun does not consist of simple primary and secondary turns but rather primary and secondary transmission lines (2 parallel wires of a specific characteristic impedance). If a balun is made simply with conventional primary and secondary windings then the core flux plays an active role. Such a design will also have a limited number of practical impedance ratios due to the requirement of a low number of turns to minimize capacitance.

Transformer capacitance consists of capacitance between turns, capacitance between windings, capacitance between layers, and stray capacitance. These can generally be modeled as a capacitor in parallel with each winding.

A better approach is to use a choking balun for common mode suppression and a lumped L, T, or Pi network to achieve the desired impedance transformation ratio. In some cases, a transmission line transformer may also be suitable for impedance transformation. In order to minimize losses, the matching network should be placed directly at the antenna feedpoint, followed by the choking balun.

At VHF frequencies, a choking balun consisting of #31 or #43 ferrite mix beads slipped over the outer coax jacket will be the most effective since any attempt to wind the coax through a toroid form will suffer from interwinding capacitance effects. Consider using 20 or more beads on the coax.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9425/how-to-build-a-balun-transformer-for-2m-rx-with-low-insertion-loss, by Felix S, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
