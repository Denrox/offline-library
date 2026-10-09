# Why does the ionosphere reflect some frequencies and not others?

*Tags: propagation, frequency, physics · score 5*

## Question

Why is it that some frequencies transmitted at some known direction are reflected back to earth, yet others transmitted at the same direction, power and polarity pass through into space with no reflection?

## Answer (score 4, by Phil Frost - W8II)

Skywave propagation is closely related to total internal reflection. This is easily demonstrated with visible light (which is also electromagnetic radiation) through a block of acrylic:

Total internal reflection occurs when the angle of incidence is above a critical angle, which is a function of the refractive indexes of the two materials:

$$ \theta_c = \arcsin\left( n_2 \over n_1 \right) $$

As the angle of incidence decreases beyond the critical angle, some of the incident wave is refracted and passes though the interface, and less of it is reflected. Obviously for terrestrial communication we want to maximize the reflected part and minimize the refracted part.

You can observe total internal reflection and refraction with something as simple as a glass of water. At some angles, it will look like a mirror. At others, it's almost transparent. For communication, we want it to look like a mirror, or as close as possible.

This reflection (or not) occurs at the interface between any two materials with a different index of refraction. This might seem like it should apply to optics but not to radio propagation, but the disconnect isn't one of physics, but one of terminology. For non-magnetic materials with relative permeability of 1, then the wave impedance ($Z$) and refractive index ($n$) are simply related by:

$$ Z = Z_0 / n $$

...where $Z_0$ is the impedance of free space. Wave impedance is simply the square root of the ratio of permeability ($\mu$) to permittivity ($\epsilon$):

$$ Z = \sqrt{\mu \over \epsilon} $$

Another way to define the index of refraction is in relation to the relative permeability and relative permittivity of a material:

$$ n = \sqrt{\epsilon_r \mu_r} $$

So for any material with a permittivity different than free space, (like the ionosphere) this material will also have a refractive index different than that of air (or vacuum, which is very close to that of air), and thus, reflection can occur. We don't necessarily need *total* internal reflection, though that certainly makes things easier.

To answer your question of why this doesn't occur for all frequencies, there are several reasons, but one is that refractive index (or permittivity) depend on frequency. In optics this is called chromatic dispersion but the concept applies to lower frequencies of electromagnetic waves as well. A prism illustrates the effect clearly:

The separation of colors is due to each frequency component of white light being refracted to a different degree, due to the frequency dependency of the refractive index.

Because the refractive index of the ionosphere varies by frequency, at higher frequencies the refractive indexes of the ionospheric layers is such that there isn't enough reflection from the ionosphere for good communication. Most of the incident wave from the transmitter just passes through the ionosphere and is lost to space.

Of course, this is just but one thing relevant to ionospheric propagation. The actual picture is more complex because the ionosphere is not cleanly separated from the rest of the atmosphere like a block of acrylic. Nor is the ionosphere homogeneous: it consists of many layers which are constantly undulating. In addition, the ionosphere can absorb radiation as well as reflect or refract it. But the main point still stands: the refractive index, and other properties such as absorption, are frequency dependent, and thus, only at some frequencies is reflection sufficient for communication.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3620/why-does-the-ionosphere-reflect-some-frequencies-and-not-others, by BenAlabaster, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
