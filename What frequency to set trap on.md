# What frequency to set trap on?

*Tags: antenna, dipole, trap · score 5*

## Question

I plan to build trapped multiband dipole so I read lots of documentation I found.

There is one thing that confuses me: various authors recommend setting resonant trap frequency differently: some say trap should be resonant just below wanted band, some says it should be resonant in middle of the band, and some say trap should resonate just above the band.

What is correct approach?

## Accepted answer (score 7, by Phil Frost - W8II)

In tuning a trap there are two concerns which are somewhat contradictory:

1. You want the trap to have a high impedance on the target band.
2. You want losses to be low.

The objective of a trap is to reduce the currents on the inactive portion of the antenna to a negligible amount. This doesn't require an impedance that's as high as possible: it requires only an impedance that's high enough.

In any LC circuit such as a trap, the current or voltage circulating between the inductor and capacitor is at a maximum at resonance. The trap is a parallel LC circuit and a high impedance (high ratio of voltage to current) at resonance. Because the capacitor and inductor are in a loop, current can flow around that loop without adding to the current through the trap. That circulating current serves to charge the capacitor to a high voltage in cooperation with the voltage applied to the trap, allowing a higher voltage to be attained with less current (the definition of high impedance). But this high circulating current means high resistive losses, and the high voltage means high dielectric losses.

Logically then, we want to tune the trap such that the impedance in the operating band is high enough, but no higher. In practice putting the the trap resonance just outside the band is effective: for any reasonable trap design this will provide an impedance that is high enough, while keeping the resonance and associated high losses where they will not be encountered in operation.

Tuning resonance to be above or below the band does not matter much. It will affect the phase shift between the active and inactive sections of the antenna, but since the inactive section of the antenna has not much current on it, this isn't very important. It will have some effect on the tuning of the antenna, and the electrical length of the antenna on bands where the trap is bypassed. But these are all things easily compensated when tuning the antenna by adjusting length, etc.

For further reading, W8JI has a good article on traps which includes some measured data for traps of several types.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7635/what-frequency-to-set-trap-on, by Pedja YT9TP, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
