# MF band mixer - feasible parameters

*Tags: mixer, mf · score 5*

## Question

Trying to build an homebrew receiver for MF band broadcast (Navtext).

Usually working on VHF, where all parts are easily found as an IC, but here I'm trying to get back to roots, so I may be missing something.

I'm considering a superhet schema and up-counting the IF to reasonable values (7 or 9 MHz). However - here's my worry. The first-stage MF mixer would have really large difference between the input and oscillator ( 0.518 MHz and 8.482 MHz) and small difference between the oscillator and IF output. Would it work anyway? Is there a better option?

## Accepted answer (score 4, by Brian K1LI)

Based on a quick internet search, other experimenters have successfully used the scheme you propose. At this low frequency, stray capacitance is a much smaller concern than you have experienced at VHF. You may need to isolate the output and oscillator sections by separating components and/or orienting them at right angles. 630-m receive systems typically use an off-the-shelf diode ring mixer or integrated circuit with IFs from zero (direct conversion) to ~10-MHz.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18614/mf-band-mixer-feasible-parameters, by gusto2, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
