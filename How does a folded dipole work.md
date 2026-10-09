# How does a folded dipole work?

*Tags: antenna, antenna-theory, folded-dipole · score 14*

## Question

A folded dipole is like an ordinary dipole, but with the ends extended and folded back, until they meet. Although it looks like a loop, I'm told it behaves similarly to a dipole.

How does this thing work? If I could see the voltages and currents in the antenna, what would they look like? Why are the currents and voltages like that?

## Answer (score 5, by KD5QLN)

As explained by antenna-theory.com:

Typically, the width d of the folded dipole antenna is much smaller than the length L.

Because the folded dipole forms a closed loop, one might expect the input impedance to depend on the input impedance of a short-circuited transmission line of length L. However, you can imagine the folded dipole antenna as two parallel short-circuited transmission lines of length L/2 (separated at the midpoint by the feed in Figure 1). It turns out the impedance of the folded dipole antenna will be a function of the impedance of a transmission line of length L/2.

Also, because the folded dipole is "folded" back on itself, the currents can reinforce each other instead of cancelling each other out, so the input impedance will also depend on the impedance of a dipole antenna of length L.

Letting Zd represent the impedance of a dipole antenna of length L and Zt represent the impedance of a transmission line impedance of length L/2, which is given by:

The input impedance ZA of the folded dipole is given by:

Folded Dipole Impedance

The folded dipole antenna is resonant and radiates well at odd integer multiples of a half-wavelength (0.5 wavelength, 1.5 wavelength ...), when the antenna is fed in the center as shown in Figure 1.

The folded dipole antenna can be made resonant at even multiples of a half-wavelength ( 1.0 wavelength, 2.0 wavelength...) by offsetting the feed of the folded dipole in Figure 1 (closer to the top or bottom edge of the folded dipole).

## Answer (score 4, by Brian K1LI)

Close coupling between the folded dipole's two long, parallel wires induces a nearly identical current in the "coupled" wire as is impressed on the "driven" wire. (Electromagnetics engineers will see this result as necessary because the boundary conditions on the ends of the two wires are the same.) Thus, half of the current from the power delivered to the antenna flows in the driven wire, half flows in the coupled wire. And, while the pattern remains the same regardless of whether the ends of the two wires are connected, the impedance is strongly affected because the phases of the voltages at the wire ends change. (Different boundary conditions at the ends, since they're not connected.)

Since the power delivered to the antenna is known, and power = current x voltage, then the voltage at the feedpoint must double to compensate for the current being cut in half.

With resistance equal to the ratio of voltage to current, doubling the voltage and halving the current at the feedpoint increases the feedpoint impedance by a factor of four over a single-wire dipole.

## Answer (score 4, by KE8FVR)

I had the same question for a while, more in reference to resonant loop antennas, but the same principle seems to apply to folded dipoles. Eventually I figured out what I think is going on, and the key is the length of the antenna vs. the wavelength of the signal.

A folded dipole or resonant loop antenna is, electrically, a full wavelength from one side of the feed point to the other. If the loop were straightened out, you'd see a standing wave with voltage nodes at each end and the middle, and current nodes at 1/4 and 3/4 of the length. If you then fold it back up, you can see that the electrical middle of the element is exactly across from the feed point; this means that the voltage in the middle of the antenna is neutral, while each end of the loop sees the peaks and troughs of the voltage wave. In contrast, the current peaks at the voltage nodes, in the middle of the antenna, and the current nodes are at the ends. It's probably pretty reasonable to imagine it as though the electrons are sloshing back and forth across the loop, being pushed by the feed point. This is the same type of resonance seen by a half-wave dipole antenna, but there's twice as much "stuff" resonating.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/919/how-does-a-folded-dipole-work, by Phil Frost - W8II, KD5QLN, Brian K1LI, KE8FVR. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
