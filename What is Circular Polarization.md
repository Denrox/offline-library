# What is Circular Polarization?

*Tags: satellites, circular-polarization · score 3*

## Question

So I just learned that a satellite does not send out a circularly polarized signal, it just switches orientation slowly when it topples through space. I thought that because they were spinning, the signal would be circularly polarized.

What exactly is circular polarization?

## Answer (score 9, by Phil Frost - W8II)

First, consider that everywhere, there is an electric field. For every point in space, this field defines a vector that describes the direction and magnitude of force that would be experienced by a mobile test charge at that point.

In practice, the mobile charges are electrons in our antenna. Radio works by creating waves in the electric field. These waves propagate through free space until they reach the receiving antenna and cause the electric charges in it to move. Our receivers then detect, amplify, and demodulate this current.

Linear polarization exists when at some point, the direction of the electric field alternates between one direction, then the opposite direction. The frequency of this oscillation is the frequency of our radio signal. For a vertically polarized signal, the electric force alternates between up and down.

We can have force in any direction, but it's convenient to break it down into two components: horizontal and vertical. Just like any point on a plane can be described with an X and Y coordinate, any direction can be described by some amount of horizontal and vertical direction, added together. For example, a 45 degree angle is equal parts horizontal and vertical. This is a form of vector addition, where the vectors are orthogonal.

Circular polarization is what you get when you have both a horizontal and vertical component, but oscillating in quadrature. That is, which a 90 degree phase shift between them.

Notice how when the blue line is at a maximum, the green line is at zero. Put mathematically, one of these lines is tracing $\sin(t)$, and the other is tracing $\cos(t)$. If you plot these functions, you get a circle.

If you were a movable charge (say, a mobile electron in an antenna) in this field, you would experience a force pushing you in a circle: first up, then to the right, then down, then to the left, then up again. The magnitude of the force remains the same throughout; only the direction changes.

This is why if you receive a circularly polarized signal with any linearly polarized antenna you get a 3dB loss. A 3dB loss is a halving of power. If you had a vertically polarized antenna, then you are receiving only the blue portion, and not the green portion at all. That is, the green (horizontal) component just pushes the charge in the dipole to the side, and that doesn't result in any current at the feedpoint.

The win is that the orientation of your antenna doesn't matter. If it's horizontal instead of vertical, it's still just a 3dB loss. If it's at 45 degrees, still just 3dB. This is really great if the satellite is spinning, otherwise you'd get fading as it spins an your polarizations align and unalign.

To avoid the 3dB loss, you can use circular polarization on each end. The cost is a more complicated antenna. In this case it's important that each end uses the same sense, right-hand or left-hand. If they are different, the result is the same as trying to link between a horizontal and vertical polarization: extreme attenuation.

## Answer (score 2, by PearsonArtPhoto)

The spinning happens the same as the frequency. So a 144 MHz signal is spinning 144 million times per second.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1558/what-is-circular-polarization, by Skyler 440, Phil Frost - W8II, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
