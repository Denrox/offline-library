# Does a halfwave (or multiple) length of coax duplicate the load impedance of one end at the other end?

*Tags: coaxial-cable, impedance-matching, antenna-tuner · score 3*

## Question

Ignoring the possibility of multiple radiators and phasing harness(es), consider the following example:

If I have a short inductor-loaded vertical antenna that I have not carefully matched to 50 ohm coax at its feedpoint, and the feedpoint impedance of the antenna itself is, say, 4 ohms at the target frequency of operation, then if I have a length of 50 ohm coax from the antenna feedpoint to the radio, and that coax length is some multiple of half wave lengths, such as 3 half wave lengths long based on the target center frequency of operation (including the velocity factor), what then is the impedance at the coax connector that connects to the radio, that is, the impedance that is presented to the SO-239 on the radio, assuming no ATU is being used? Would it be 4 ohms, or 50 ohms, or something else?

If it is something other than 50 ohms, of what significance is this for achieving the best possible, and safe, performance with the radio, if no ATU is available at or in the radio?

Asked another way: if the antenna is not properly matched to a 50 ohm coax feedline, such as the example above, and there is no ATU at or in the radio, of what relevance is the length of the coax wrt the target center frequency of operation?

I have been told that 50 ohm coax is 50 ohm at both ends, and 50 ohms all along its length, and it is 50 ohms that is presented to anything to which it is connected, and the length of it does not matter at all. I suspect that statement may be missing some very significant details that are being silently assumed. What are the important issues to consider in this example?

## Accepted answer (score 9, by hobbs - KC2G)

I have been told that 50 ohm coax is 50 ohm at both ends, and 50 ohms all along its length, and it is 50 ohms that is presented to anything to which it is connected, and the length of it does not matter at all.

Any length of 50 ohm coax will present a 50 ohm load at one end *if it's terminated in 50 ohms at the other end*. If the load impedance is anything other than the coax's characteristic impedance, then what you get on the other end depends on the length of the coax.

When plotted on a Smith chart, adding a length of coax *rotates* an impedance around the origin by twice as many degrees as the electrical length of the coax (90° for a 1/8 wavelength, 180° for a quarter wavelength, etc.) The trick here is that the coax's own impedance is found at the *center* of the Smith chart, so it's the one value that isn't affected by rotation.

If I have a short inductor-loaded vertical antenna that I have not carefully matched to 50 ohm coax at its feedpoint, and the feedpoint impedance of the antenna itself is, say, 4 ohms at the target frequency of operation, then if I have a length of 50 ohm coax from the antenna feedpoint to the radio, and that coax length is some multiple of half wave lengths, such as 3 half wave lengths long based on the target center frequency of operation (including the velocity factor), what then is the impedance at the coax connector that connects to the radio, that is, the impedance that is presented to the SO-239 on the radio, assuming no ATU is being used? Would it be 4 ohms, or 50 ohms, or something else?

Since a half wavelength involves a rotation of 360° on the Smith chart, the answer will be 4 ohms, if we can make the assumption that the coax is lossless, or that the loss is insignificant. If coax loss becomes a factor, then the impedance actually "spirals in" towards the center of the Smith chart rather than just rotating — which, in your case, means that you would get a value somewhat higher than 4 ohms, with how much depending on the coax loss.

If it is something other than 50 ohms, of what significance is this for achieving the best possible, and safe, performance with the radio, if no ATU is available at or in the radio?

With no ATU and no matching system of any kind (not even fixed components), there's not a lot of significance. If your radio is 50 ohms, and the coax is 50 ohms, then all of the points that the impedance rotates through as you change the coax length form a *circle of constant SWR*, changing the feedline length doesn't really do anything useful for you. Adding more feedline just adds more loss.

But if we do assume some matching at the radio, then there are some interesting things that you can play with. For instance, whatever your feedpoint impedance, there will be two points on that constant-SWR circle that have a 50-ohm resistive component plus some reactance (meaning that you can bring it to 50 with a single series inductor or series capacitor), and two points that have some non-50-ohm resistance but zero reactance (meaning that you could match them with a transformer).

And if you have some particular kind of ATU (L-match, T-match, etc.), and get to know it well, you might realize that it tunes some impedances more easily / more efficiently than others, *even if they have the same SWR*. In such cases you can sometimes tweak the feedline length to make the tuner happier at your frequencies of interest.

Recommended reading: Antenna-theory.com on Smith charts (it's really not just about the chart, there's a good amount of practical explanation there).

## Answer (score 3, by AG5CI)

If the impedance of the load is $Z_L$ and the characteristic impedance of the transmission line is $Z_0$, then the impedance at the input to a length $l$ of transmission line connected to the load is:

$$ Z_{in} = Z_0\displaystyle{\frac{Z_L+jZ_0\tan(\beta l)}{Z_0+jZ_L\tan(\beta l)}} $$

where $\beta$ is the *phase constant*, equal to $2\pi/\lambda_g$, where $\lambda_g$ is the wavelength in the transmission line. The wavelength inside the transmission line will be a factor of $1/v_f$ longer than in free space, where $v_f$ is the *velocity factor* of the line.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21840/does-a-halfwave-or-multiple-length-of-coax-duplicate-the-load-impedance-of-one, by always_learning, hobbs - KC2G, AG5CI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
