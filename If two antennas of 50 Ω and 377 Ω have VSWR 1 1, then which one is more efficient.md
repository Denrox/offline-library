# If two antennas of 50 Ω and 377 Ω have VSWR=1:1, then which one is more efficient?

*Tags: antenna, impedance, antenna-theory · score 9*

## Question

If there are two antennas of 50 Ω and 377 Ω (same as the intrinsic impedance of air) impedance with 0 $\Omega$ ohmic resistance, and they are exactly matched with their transmission line, then which antenna is more effective in terms of radiating R.F. power into space?

That is, if both antennas have VSWR = 1:1, then which one is more efficient?

Note: that the term 'efficiency' in above, does not mean the definition of antenna-efficiency. I know that antenna-efficiency is 100%, since there are ZERO ohmic loss and $\infty$ return-loss. So, from "efficient", I mean the effectiveness of the antenna in radiating energy in space.

## Accepted answer (score 15, by Phil Frost - W8II)

With the information you've provided, there is no way to tell. Feedpoint impedance and VSWR have no relationship to antenna efficiency. See [What is the relationship between SWR and receive performance?](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md)

The feedpoint impedance also has no relationship to antenna efficiency. A "50Ω antenna" means the impedance *at the feedpoint* is 50Ω. The impedance at other points is probably something very different. In a dipole, for example, the impedance is about 72Ω at the feedpoint, and very much higher at the ends. This is why current is at a maximum at the feedpoint (low impedance), and at a minimum at the ends (high impedance).

*Is there an advantage to an antenna with a feedpoint impedance equal to the impedance of free space?* No. An antenna of any design transforms between the impedance of free space to its feedpoint impedance. An antenna can be designed to work at any feedpoint impedance. The losses come from things like resistance in the antenna wire and coils, and dielectric losses in tuning capacitors. To the extent that you don't have these things, an antenna can be efficient. A dipole, vertical, loop, or any other kind of antenna constructed from ideal materials is already 100% efficient.

This can easily be seen by considering the law of conservation of energy. If your antenna isn't getting hot, yet you are putting 100W of power into it, only two things can happen to that energy. It can be be:

1. stored in reactance of the antenna
2. radiated away

If the antenna has a purely resistive impedance, then there is no reactance to be storing energy, so it must be radiating away. The feedpoint impedance is irrelevant.

## Answer (score 6, by OH2FXN)

The antenna efficiency refers the ratio of radiated power and the power fed to the antenna. The rest of the fed power is transformed to heat by the losses in the antenna. Thus, the antenna efficiency is not directly linked to the radiation resistance alone, but also to the (resistive or dielectric) losses in the antenna. Higher radiation resistance does not necessarily mean higher efficiency.

You can improve the radiation efficiency of your antenna by choosing more conductive materials (copper or copper coated steel over aluminum) and thicker wires (thick wire has more "surface area" decreasing the loss resistance). These changes improve your antenna efficiency while having only minor effect on the antenna impedance, as seen by your radio. However, the increasing resistance does not seem to reduce the performance of typical HAM antennas too dramatically: http://personal.ee.surrey.ac.uk/Personal/D.Jefferies/antennexarticles/newantennexarticles/efficiency.pdf

You can the behavior of an antenna with circuit model. The simplest circuit model for a resonant dipole would be a series RLC circuit. The circuit model transforms all impedances as they are seen in the feedpoint of the antenna. With the circuit model of the figure, the radiation efficiency becomes: $\eta = \frac{R_{rad}}{R_{rad}+R_{loss}}$, where $R_{rad}$ is the radiation resistance (power radiated to the far field) and $R_{loss}$ is loss resistance (power transformed to heat). $C$ and $L$ represent the reactive fields near the antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1243/if-two-antennas-of-50-o-and-377-o-have-vswr-1-1-then-which-one-is-more-efficie, by kaka, Phil Frost - W8II, OH2FXN. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
