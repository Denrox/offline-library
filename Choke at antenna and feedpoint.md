# Choke at antenna and feedpoint?

*Tags: antenna, feed-line, coaxial-cable · score 3*

## Question

I'm planning on putting up a G5RV. From the ladder line I connect 5m coax to the shack; would it be worth doing a common mode current choke at both the antenna feedpoint and the coax feedpoint? (I read somewhere that it's recommended at the coax.)

## Accepted answer (score 4, by on4aa)

### Avoid common-mode sheath currents

Common-mode sheath currents on the coaxial feed line should be avoided because:

- At the antenna feed point or the transition point of balanced line to coax, common-mode currents interfere with your radiation pattern.
- In the shack, common-mode sheath currents will interfere with your electronic equipment (RFI).

### Origin of the common mode

Most often, the common mode on the coaxial feeding cable is a continuation of the standing wave that exists over the length of most antennas. (Aperiodic resistive antennas and leaky-wave antennas are notable exceptions.)

This standing wave, in turn, results from the abrupt change in conductivity $\sigma$ and/or permitivity $\epsilon_{r}$ that is encountered at the antenna ends. This is called *the boundary condition* in technical literature.

Being a standing wave implies that, for any given frequency, the common mode will show current minima every halve wavelength, starting from the antenna ends. Without a current balun and/or a sheath current choke, these current minima will repeat further down the coaxial feed line.

### Optimal placement of a sheath current choke

A sheath current choke typically inserts only about 500Ω impedance in series with the sheath of the coaxial cable. This means that sheath current chokes are ineffective at places along the feed line where the common mode wave has a current minimum, because the common mode impedance there will be high (typically about 2kΩ). **Sheath current chokes are most effective at common-mode current maxima.**

### Practical considerations

1. By all means, use a decently made, properly rated (frequency and power) **current balun** at your antenna feed point. This will be a first, **broadband** defence against common-mode sheath currents.
2.

Current baluns tend to be less effective at lower frequencies because they produce their common-mode series impedance from inductance. Therefore, common-mode sheath current rejection may not be sufficient at the lower frequency bands. A **sheath current choke** may be placed **at current maxima** of the lowest frequency band, i.e.:

 - At $\frac{\lambda}{4}$ distance measured from the antenna ends, where $\lambda$ is the wavelength of the lowest frequency band, and/or
 - At odd multiples of this length, i.e. $\frac{3\lambda}{4}$, $\frac{5\lambda}{4}$, ...

This will normally also handle the common-mode wave rejection for the second lowest frequency band if this is a harmonic of the lowest.

3.

Sheath current chokes close to the antenna feed point will help to preserve the radiation pattern of the antenna. Sheath current chokes closer to shack may help more against RFI.

4.

If you can, connect the coax sheath to earth at both ends and place the coaxial cable on or below ground.

## Answer (score 2, by WPrecht)

A canonical answer is difficult, a lot depends on the antenna location and it's environment. There is a ton of information on common mode chokes and baluns in the answer @Phil Frost linked above. Some of these references suggest at the feed point is all you need, other say both the feed point and the shack entry point, still others say all of the above, plus points along the coax to break up potential 1/4 wave lengths that could pick up RF.

Five meters is pretty short run. If it were me, I would put one at the feed point and see what I got. If you have more ferrite laying around, add one at the shack end and measure the effects.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/877/choke-at-antenna-and-feedpoint, by s3c, on4aa, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
