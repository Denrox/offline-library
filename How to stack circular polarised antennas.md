# How to stack circular polarised antennas

*Tags: antenna, antenna-theory, phased-array, circular-polarization · score 6*

## Question

I'm interested in stacking a pair of circularly polarized "crosshair" antennas. Do I construct such as both antennas are in phase with one another then match the two signals in phase via the coax line, *i.e.* equal length, or should I rotate one by say 180 degrees then use the coax to provide a phase shift? I'm new to RF but pretty eager to learn.

## Accepted answer (score 4, by Phil Frost - W8II)

The important thing is that the antennas are in phase. That is, at the instant the electric field is pointing up on one antenna, it's pointing up on the other antenna. Otherwise, they won't add constructively. In the worst case, they are 180 degrees out of phase and they *cancel*.

Keeping the antennas in phase can be accomplished any number of ways. If the coax length to each antenna is equal, the phase shift introduced by the feedline will be equal, so the antennas will be in phase as long as you don't rotate either one.

If you were to rotate one to be ahead 180 degrees in phase, you could compensate by adding an extra half-wavelength (at the appropriate velocity factor for your cable) of feedline, which adds 180 degrees of delay. The result would be a net zero phase shift, so the antennas would still be in phase.

Note this isn't much different from stacking linearly polarized antennas. One way to think of it is that you have a stack of horizontally polarized antennas, and another stack of vertically polarized antennas, and they just happen to be on the same booms and be 90 degrees out of phase. [That's all circular polarization is](What%20is%20Circular%20Polarization.md), and stacking doesn't fundamentally change the picture.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1752/how-to-stack-circular-polarised-antennas, by Ben, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
