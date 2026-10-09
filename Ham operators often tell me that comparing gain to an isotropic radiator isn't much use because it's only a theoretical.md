# Ham operators often tell me that comparing gain to an isotropic radiator isn't much use because it's only a theoretical antenna, is this true?

*Tags: antenna-theory, radiation-pattern · score 3*

## Question

When you look down on an isotropic radiator from above, ie : the azimuth view radiation pattern, it's a circle. The same as looking down on any omni directional antenna. So when comparing the gain of a yagi antenna in the azimuth view at 0 degrees elevation to an isotropic radiator's azimuth view gain at 0 degree, this gives a good practical indication of gain over a real omni directional antenna such as a 1/4 wave ground plane antenna, is that right ?

## Accepted answer (score 9, by Glenn W9IQ)

Ham operators often tell me that comparing gain to an isotropic radiator isn't much use because it's only a theoretical antenna, is this true?

No, that is not true. I generally find that hams that denigrate or choose to ignore the isotropic antenna or references to it, simply don't understand its central place in antenna engineering. Certainly the isotropic antenna only exists theoretically but it is the basis for a great deal of the fundamentals principles of antenna engineering and the related formulas. It is a shame that more hams don't take the time as you are to strengthen their knowledge in this field. I applaud you for digging into this subject.

So when comparing the gain of a yagi antenna in the azimuth view at 0 degrees elevation to an isotropic radiator's azimuth view gain at 0 degree, this gives a good practical indication of gain over a real omni directional antenna such as a 1/4 wave ground plane antenna, is that right ?

There is a confusion in terminology in your question that is common place regarding omnidirectional for a vertical antenna and radiating equally in all directions for an isotropic antenna.

An isotropic antenna radiates equally in all directions. The best way to think about this is to place the isotropic antenna inside, and at the center, of a large sphere. Then apply power to the isotropic antenna and imagine the power "illuminating" the surface of the sphere in the same way a light bulb might. Since the isotropic antenna radiates equally in all directions, the entire sphere would be uniformly lit - no bright spots and no dark spots.

Now take the isotropic antenna out of the sphere and replace it with an omnidirectional vertical antenna. When we apply the same power to the vertical, we would not see a uniformly lit sphere. Instead, the "poles" of the sphere would be nearly dark and the "equator" of the sphere would be brightly lit. Clearly the "omni" part of the description is referring to the equal "illumination" in the area near and around the equator.

Since spheres are not the easiest to render in our 2D literature, we tend to take a slice through the sphere and talk about that. For ham radio, the two most common slices are azimuth (a slice parallel to the equator) and elevation (a slice parallel to the poles). The azimuth and the elevation plots for an isotropic antenna would always show a uniform and equal, circular radiation pattern for all such slices. By contrast the omnidirectional vertical would show uniform radiation in the azimuth plot but in the elevation plot, most of the power would be concentrated near the horizon with very little power near 90 degrees of elevation. So the omnidirectional term only applies to the azimuth pattern.

Computer modeling has brought about the ability to more easily generate graphics that have a 3D appearance to them. Here is such a rendering of a 1/4 wave ground plane antenna with a relatively small ground plane from the Antenna Theory website:

The correct technical term for the illumination of the surface of the sphere is "irradiance". This is typically expressed as watts per square meter (W/m). So the isotropic antenna causes the entire surface of the sphere to have the same W/m but since the omnidirectional vertical focuses more of its power near the equator, the W/m in the equator region would be greater than at the poles. So the dBi gain of the omnidirectional vertical can be thought of as the comparison of its greatest irradiance value that is found near the equator compared to the irradiance value (at the same power level and same size of sphere) of the irradiance at any location for the isotropic antenna:

$$Gain_\text{dBi}=10 \log \left(\frac{E_{e\text{ Omni}}}{E_{e\text{ Isotropic}}}\right) \tag 1$$

where Ee is the irradiance in W/m for the respective antenna.

Unless specifically stated otherwise, dBi gain refers to the maximum irradiance of the antenna in question compared to that of the isotropic antenna. For example, a 1/2 wavelength dipole in free space has a 2.15 dBi gain. Our knowledge of the radiation pattern of a dipole would allow us to equate this gain to the direction that is perpendicular to the direction of the arms of the dipole.

Finally, don't forget that the gain of an antenna includes the effect of any losses in the antenna. In fact gain (in linear form) is:

$$Gain=Directivity*Efficiency \tag 2$$

So while the free space directivity of a small, "magnetic" loop antenna is nearly the same as a free space 1/2 wavelength dipole, the poor efficiency of the small loop compared to a dipole causes it to have much less gain than the dipole. The isotropic antenna is always considered to be 100% efficient.

## Answer (score 6, by Cecil - W5DXP)

dBi is useful for comparing gains of real world antennas. For instance, an 80m mobile antenna may be -10 dbi, a 1/4WL vertical ground plane may be 0 dbi, a dipole may be 6 dbi, and a beam may be 10 dbi. So we can say that the beam has 20 dB gain over the 80m mobile antenna using dBi as the reference dimension.

## Answer (score 4, by Phil Frost - W8II)

Those that complain that dBi isn't useful because an isotropic antenna is only theoretical often advocate an alternate unit such as dBd, or decibels relative to a dipole.

There are a couple arguments that could be made from here.

One argument is that a dBd is typically defined as 2.15 dBi, because that's the directive gain of a half-wavelength dipole in free space. That is, to convert dBi to dBb, just subtract 2.15. If you want to be pragmatic, this is hardly something to get worked up about.

But wait a minute, a dipole in free space is *also* a theoretical antenna. In practice, reflections from ground, ground losses, feed issues, interactions with the tower, misalignment of the antenna, and myriad other issues result in a dipole's gain being something other than 2.15 dBi. For any terrestrial communication scenario, interactions with the ground are relevant.

In some cases, especially on VHF and higher frequencies where the antenna can be many wavelengths high, it may be acceptable to assume 2.15 dBi gain, and model the ground with a simple model like the two-ray reflection model. Or perhaps the link budget simply contains sufficient fade margin that it's not important to have a very precise model.

But on HF it can become quite difficult to get the dipole more than a quarter wavelength high, and this means both that the ground has the potential to create constructive interference though the image antenna created, and also reduce gain through ground losses. Depending on ground conductivity and height, it can make quite a difference for better *or* worse.

Furthermore, a dipole's gain even in free space isn't 2.15 dBi in all directions: that's only its gain in the most favorable direction. How frequently is the dipole rotated to the ideal angle for a given path? And even given a rotatable dipole, how frequently is the height of that dipole optimized to give the ideal takeoff angle?

You see, trying to distill antenna performance into a single number that's realistic in practice rapidly becomes a very complex problem. Wouldn't it be nice if we had a simpler number, something which was insensitive to direction, polarization, ground interactions, and all the other gotchas; something which is mathematically simple and universally applicable? Then we can use this as the starting point, and then add as many correcting factors to account for real-world effects as we desire until we are satisfied our model is sufficiently accurate to meet our needs?

That "simple" model is the isotropic antenna. To show why it's simple, I pose a simple question: if a 1 W transmitter is 10 km distant from the receiver, how much power is received?

If we assume the transmitting antenna radiates equally in all directions, is in free space, and is 100% efficient, then this is a simple geometry problem. Simply imagine a sphere centered on the transmitter, with a radius of 10 km. Radiated power from the transmitter can only intersect the sphere, so the power flux of the entire sphere must be 1 W. Since the antenna radiates equally in all directions, the power flux density must be equal everywhere on the sphere. So calculating the surface area of this sphere, then dividing the transmit power by this quantity, yields the power flux density.

$$ { 1 \:\mathrm{W} \over 2 \pi (10 \:\mathrm{km})^2 } = 1.59 \:\mathrm{nW/m^2} $$

If we want to know the power received then we only need to know how big of an "energy net" the receiving antenna presents. This is called the [effective aperture](Why%20is%20antenna%20aperture%20a%20function%20of%20wavelength.md), which as it turns out is just another way to express gain:

$$ A_e = {\lambda^2 \over 4\pi} G $$

where $A_e$ is the effective aperture, $\lambda$ is wavelength, and $G$ is the antenna gain (as a linear number, not decibels).

This is the basis of the [Friis transmission equation](Why%20is%20antenna%20aperture%20a%20function%20of%20wavelength.md) and finds practical application in calculating [link budgets](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md). Granted, it's based on a theoretical antenna, the mathematical simplicity of the isotropic antenna allows the mathematics to be simple when simple is all we need, and more complex when necessary by adding additional terms to the equation.

If we were to eschew the isotropic antenna and use the dipole as the reference antenna, we would gain little. Some might argue the results are "more realistic", but as previously stated the gain of a dipole is not constant. We'd have to add terms to the fundamental equations to account for at least the orientation of the dipole. And if the objective is realism, even that is insufficient. It's a slippery slope that has neither the mathematical simplicity of an isotropic reference nor the accuracy of a real-world model.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13012/ham-operators-often-tell-me-that-comparing-gain-to-an-isotropic-radiator-isn-t, by Andrew, Glenn W9IQ, Cecil - W5DXP, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
