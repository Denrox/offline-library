# Gain difference between half-wave and infinitesimal dipole?

*Tags: antenna-theory, gain · score 4*

## Question

In discussion around another Q&A here, [Glenn W9IQ commented](Can%20this%20960%20MHz%20CelWave%20fiberglass%20antenna%20be%20retuned%20for%20the%2070cm%20band.md):

The directive gain difference between a half wavelength dipole and an infinitesimal dipole is only 0.39 dB

I'm curious where this number comes from. I recall from e.g. the FCC amateur licensing tests the relationship between dBi and dBd; to summarize that Wikipedia link:

- dB(isotropic) – the forward gain of an antenna compared with the hypothetical isotropic antenna, which uniformly distributes energy in all directions.
- dB(dipole) – the forward gain of an antenna compared with a half-wave dipole antenna. **0 dBd = 2.15 dBi** [emphasis mine]

Based on a naïve understanding of "half wavelength dipole" and "infinitesimal dipole" I would expect the the gain difference to be 2.15 dB, not 0.39 dB. What am I missing?

## Accepted answer (score 5, by Phil Frost - W8II)

Infinitesimal and isotropic are not the same thing.

*Infinitesimal*: an indefinitely small quantity; a value approaching zero. In the case of an infinitesimal dipole, we're talking about the length of the dipole. Kinda. More on that below.

*Isotropic*: having a physical property that has the same value when measured in different directions. In the case of antennas, we're talking about radiant intensity.

An isotropic antenna, that is, one which radiates with equal intensity in any direction, is not realizable. The mathematical proof comes from the hairy ball theorem.

Someone with a radio background will hear "dipole" and think "two wires". But someone with a physics background thinks a different thing. An electric dipole is two equal but opposite electric point charges separated by some distance. An *infinitesimal* dipole is the limiting case when the distance between these charges approaches, but does not reach zero.

The electric field looks like this:  
By Geek3 CC BY-SA 3.0, from Wikimedia Commons

In practice, these separated charges come from the charge accumulation at the ends of the antenna as current takes charge away from one end while charge is being deposited in the other end. Of course in a real antenna the charge is distributed throughout the antenna: the infinitesimal dipole is a simplification with just two points, defined only by a direction and a moment.

If an infinitesimal dipole oscillates as an antenna does, then it can be shown with a lot of math derived from Maxwell's equations that the electric far-field is proportional to:

$$ E(\theta, \phi) = {1 \over r} \sin(\theta) $$

where the antenna is along the z axis, and:

- $\theta$ (theta) is the angle away from the z axis,
- $\phi$ is the angle away from the x axis (irrelevant here, since the dipole is omnidirectional),
- $r$ is the distance away from the antenna

So the field is strongest when $\theta = \pi/2$, corresponding to the horizon, if the antenna is vertical. The electric field decreases with $1/r$, and since power is proportional to the square of voltage this means power would decrease with $1/r^2$, the inverse square law.

The corresponding formula for a half-wave dipole is:

$$ E(\theta, \phi) \propto { \cos\left( \pi \cos \theta \over 2 \right) \over r \sin\theta }$$

As you can see graphically, the half-wave dipole is just a little more "pointed":

Thus, if the two antennas have equal efficiency, the half-wave dipole will have just a little more gain.

Why so? No one actually builds infinitesimal dipoles: theoretically their gain is about the same but in practice their efficiency is extremely low. However, they are mathematically simple, and a very good approximation of real antennas can be made by modeling them as a collection of infinitesimal dipoles. The caveat is the infinitesimal dipole model assumes uniform current throughout, so we must divide the antenna into pieces small enough that each individual piece has mostly uniform current.

Thinking of a half-wave dipole in this way, you can now consider it sort of a colinear array of infinitesimal dipoles. It isn't physically large enough to yield a lot of gain, but it does yield just a little: 0.39 dB. We see that in the graph above.

## Answer (score 3, by Brian K1LI)

This is well explained on the Wikipedia entry for dipole antenna.

The "infinitesimal" dipole to which you refer is also called a Hertzian dipole. As shown in the Wikipedia entry, this theoretical construct has a gain of 1.5. The gain of the half-wave dipole is 1.64. The dB ratio of (1.64/1.5) is 0.39dB.

## Answer (score 2, by Kevin Reid AG6YO)

An infinitesimal dipole is not the same thing as an isotropic antenna.


An isotropic antenna is a mathematical notion for comparing antenna patterns. **It cannot exist** — not just as a matter of physical construction, but also of arrangement of electromagnetic fields — because there is no possible arrangement of *polarization* of the wave which covers the sphere of all directions away from the antenna (mathematically, this is the hairy ball theorem).


An infinitesimal dipole (also known as a Hertzian dipole) has a dipole radiation pattern — for a dipole of any length whatsoever, the radiated field goes to zero along the axis of the dipole. (This pair of zero points means that a consistent polarization pattern can exist.)

Therefore, more of the radiation must go out in other directions, compared to an isotropic antenna, and so the design must have gain over an isotropic antenna.

I don't know the theory to explain where the figure of 2.15 dBi comes from, but I hope this explains why there is a difference at all.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12012/gain-difference-between-half-wave-and-infinitesimal-dipole, by natevw - AF7TB, Phil Frost - W8II, Brian K1LI, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
