# What happens to the transmitted power cancelled out by a yagi antenna's reflector?

*Tags: antenna, antenna-theory · score 3*

## Question

For a yagi antenna, for transmit, does the waveform traveling away from the driven element towards the reflector get cancelled out by the reflector and then simply disappear ? Or is that cancelled power then 'available' to be added to the power radiated in the opposite direction ?

The reason i ask this question is this.

1. If power radiated in a direction opposite to the direction of maximum gain is just cancelled out due to the interference between the incident wave and the re-radiated wave from the reflector, then the only advantage good front to back ratio gives is less noise and the ability to reduce the strength of signals from unwanted directions. Then a yagi could just be designed for maximum gain and front to back ratio ignored.
2. If power radiated in a direction opposite to the direction of maximum gain is cancelled out but then 'added' to the rest of the lobes, then better front to back ratio means more gain in the forward direction because the power not radiated out the back is added to that radiated towards the front.

And the above would also all be true for receive.

## Accepted answer (score 7, by Cecil - W5DXP)

Total radiated power is approximately the same in a low-loss beam antenna as it is in a dipole. The beaming effect is the result of constructive interference in one direction accompanied by destructive interference in other directions. Constructive interference energy equals destructive interference energy so the total energy remains the same. The energy "lost" to destructive interference, like squeezing a balloon, is added as constructive interference in the beaming direction. That's why a beam has gain over a dipole in the beaming direction. Energy cannot be lost. It can only be redirected or transformed, e.g. to heat. Any antenna with a gain higher than 0 dBi is undergoing constructive/destructive interference.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12708/what-happens-to-the-transmitted-power-cancelled-out-by-a-yagi-antenna-s-reflec, by Andrew, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
