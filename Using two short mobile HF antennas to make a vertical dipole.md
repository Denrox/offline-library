# Using two short mobile HF antennas to make a vertical dipole

*Tags: dipole, vertical-antenna, radial · score 3*

## Question

Instead of using a metal vehicle roof or multiple radials as the counterpose to a shortened vertical antenna, can one use two of them, one pointed downward to construct a balanced vertical dipole, and mounting the pair up higher? Are there any advantages or disadvantages to doing this over using a bunch of random length radials around the base of a lower vertical? (other than needing to string the feed-line out roughly horizontally for some lambda distance...)

## Answer (score 5, by Glenn W9IQ)

To begin the discussion, it is helpful to understand the effects of shortening any antenna to a length below resonance. In all cases, the directivity of the antenna is reduced but this tends to be a fairly uniform reduction regardless of how much shortening occurs. The reduction in length also reduces the radiation resistance of the antenna. This is significant in that as radiation resistance is reduced, the effect of losses in the antenna is amplified. Efficiency of an antenna is defined as:

$$Efficiency=\frac {R_r}{R_r+R_l} \tag 1$$

where Rr is the radiation resistance of the entire antenna (not simply the resistive component of the feedpoint impedance) and Rl are the resistive losses.

The gain of the antenna is given as:

$$Gain=Directivity*Efficiency \tag 2$$

So it becomes clear that as an antenna is shortened, the directivity is reduced and efficiency tend to go down the further the antenna is shortened, having a compound effect in reducing the gain of the antenna.

A 1/4 wave vertical antenna with a substantial ground plane over real ground and a vertical, 1/2 wave dipole over real ground will have approximately the same gain of ~ 0 dBi. This includes all of the effects listed above.

So now to the question of which is better, the answer comes down to which is the more efficient component - the vertical's ground plane or the second shortened element that makes up the dipole? This of course depends on the specific comparison and the construction elements involved. But we can generalize an answer by saying if the ground plane is highly efficient and the dipole is made up of two of the comparatively inefficient elements as used for the vertical component of the vertical antenna, the dipole will have twice the inefficiency and therefore have a gain of -3 dB compared to the vertical antenna.

Note 1:

There is a common error made in many antenna texts and on Internet postings that equate radiation resistance of a lossless antenna to the resistive component of the feedpoint impedance. While this is often the case with common amateur radio antennas, there are many exceptions. For example, as amateurs we are well versed in the lossless, center fed, 72 ohm feedpoint impedance of a 1/2 wave dipole in free space. But if we take the same antenna and feed it 1/3 from the end instead of the center, we will observe a much higher resistive component of the feedpoint impedance. But the radiation resistance of the antenna is still 72 ohms.

It is not a trivial exercise to correctly determine the radiation resistance of an antenna. Fortunately, many antenna designs have already been characterized. We are also fortunate that in the amateur radio community, most of our linear antennas are 1/2 wavelength or shorter and we tend to feed them at the current maxima point. When these conditions are met, then the resistive component of the feedpoint impedance of the antenna *generally* consists of the radiation resistance of the entire antenna plus the resistive losses of the antenna.

An example of where this knowledge can be very helpful is determining how many radials to add to a 1/4 wavelength vertical antenna in order to maximize its efficiency. If the antenna meets the earlier stated requirements, then monitoring the resistive component of the feedpoint impedance will show the increase in efficiency (reduced resistive losses) as each radial is added. When the efficiency improvement becomes asymptotic, it is no longer productive to add additional radials.

## Answer (score 3, by Phil Frost - W8II)

People can and do use a pair of mobile antennas to make shortened dipoles. A "hamstick dipole" is one example.

One application for such an antenna is in a mobile station which for whatever reason requires a horizontal polarization.

It's also a quick way to make a small antenna where space would not allow for a full-sized dipole, such as an attic antenna, or a station in an apartment.

Or, a station that needs to be portable, where radials are not easily installed and hanging a wire dipole is not feasible, perhaps for field day.

The advantages are much the same a dipoles generally, most usually that no radials need be installed. For installation on a vehicle with a metal body, the vehicle body makes a sufficient ground plane. But I can think of a few reasons a dipole may still be desirable.

For line-of-sight propagation the radio horizon is increased. For higher frequencies there's likely no need to use a shortened antenna, but perhaps on 6 and 10 meters this may be of some value for local communication.

Getting the antenna higher also reduces ground losses, by reducing ground current density. Although the metal body provides some counterpoise, the Earth ground is still significant. Since losses are proportional to the square of current (P = IR), moving the antenna away from the ground reduces ground losses.

If the antenna can be raised to at least a half wavelength, reflection from the ground will create an image antenna that is effectively a phased array which increases gain at low radiation angles.

Or if the antenna is raised to a lesser height and turned horizontal, that image antenna increases upwards radiation which may be useful for [NVIS propagation](Can%20a%20vertical%20antenna%20be%20used%20for%20NVIS.md).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9714/using-two-short-mobile-hf-antennas-to-make-a-vertical-dipole, by hotpaw2, Glenn W9IQ, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
