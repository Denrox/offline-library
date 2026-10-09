# Why is antenna aperture a function of wavelength?

*Tags: antenna, math · score 11*

## Question

Wikipedia says:

It can be shown that the aperture of a lossless isotropic antenna, which by definition has unity gain, is:

$$ A_{\mathit{eff}} = \frac {\lambda^2}{4 \pi}$$

We also see this emerge as a $\lambda$ term in the [Friis transmission equation](What%20does%20the%20Friis%20transmission%20equation%20represent%20and%20how%20is%20it%20derived.md):

$$ {\frac {P_{r}}{P_{t}}}=G_{t}G_{r}\left({\frac {\lambda }{4\pi R}}\right)^{2} $$

This would suggest that longer wavelength antennas are more efficient collectors of electromagnetic energy. Why is this? Wikipedia says it can be shown. Show me.

## Accepted answer (score 6, by Glenn W9IQ)

This is a topic that troubles most students and even finds it way into many technical papers and textbooks in the form of incorrect assertions and conclusions. While you will find some reasonable references to thermodynamic equivalencies in some texts, it seems the genesis of the isotropic effective aperture equation has been rarely published.

The answer to the question lies buried in the mechanisms of Fresnel (near field) and Fraunhoffer (far field) zones of antennas. The Fresnel zone is the specific area of interest. The non-radiating, non-dissipating (thus reactive) part of the Fresnel zone is generally considered to extend 1∕(2π) times the wavelength from the surface of the antenna. In a more general sense, this is considered the maximum distance from which EM (electromagnetic) waves can couple to a nearby object. This coupling is why the energy is not radiated or dissipated by a transmitting antenna.

Now we turn our attention to the elusive isotropic antenna. It is considered a point source - small enough in dimension compared to any other incorporated dimensions that it is dimensionless and infinitesimally small. By definition, the isotropic antenna radiates equally in all directions. By the theory of reciprocity, the isotropic antenna must then receive equally in all directions.

Now consider an EM plane wave approaching the isotropic antenna. The isotropic antenna cannot "look ahead" and see the plane coming when the plane wave is in its far field because the EM plane wave is not yet having any effect on the isotropic antenna. But as the EM plane wave gets very close to the isotropic antenna, it begins to cause current to flow in the isotropic antenna. How close does the EM plane need to be? The distance of the non-radiating Fresnel zone which, as stated previously, is considered to be 1∕(2π) times the wavelength of the frequency in question.

As the plane wave intersects the isotropic antenna (that is, the isotropic point is on the plane), the spherical receiving pattern of the isotropic antenna has the maximum possible coupling with the EM plane wave. Since the isotropic antenna is a point lying on the intersecting plane with its receive sphere bisected by the plane, the resulting pattern is a circle defined by a radius that originates at the isotropic antenna and extends for a radius of 1∕(2π) times the wavelength. This circle is the Ae (effective aperture) of the isotropic antenna. That is, it is generating current from EM waves within that radius.

But with any receiving antenna, we are more interested in determining the total power the receive antenna is able to make available to the receiver. This is a function of the radiative flux which is given in SI units of W/m. While we do not know the radiative flux in this case, we can compute the normalize power received (the amount of power received if radiative flux = 1 watt/m) by simply computing the area of the the Ae. Since the aperture is a circle and the area of a circle is given by:

$$ A_\text{circle} = \pi r^2 $$

we can substitute the radius of the isotropic $A_e$:

$$ A_e = \pi \left({ \lambda \over 2 \pi}\right)^2 $$

and simplify:

$$ A_e = {\lambda^2 \over 4\pi} $$

Thus emerges the standard definition of the Ae of an isotropic antenna, always with a gain of one. The dependency on λ is simply due to the minimum radius at which the isotropic antenna (or any antenna for that matter) can begin to receive or emit EM waves.

If you now consider the effect of gain by any other type of antenna, you can see that it is simply increasing the area of the Ae of the isotropic antenna by the magnitude of the gain. Since the Ae is multiplied by the radiative flux and now the gain of the antenna, the received or transmitted power is scaled proportionally. It should be noted however, that the gain of an antenna does not physically extend the radius at which an EM wave can generate current in the antenna as this boundary condition is immutable. The gain and pattern of most amateur radio antennas is determined by the current vector patterns of the antenna.

If you find this explanation to be helpful and wish to requote it, I ask that you kindly give attribution to me, Glenn Schulz W9IQ.

Footnote: The Hairy Ball Theorem has been mentioned in this thread. The Theorem states that given a ball completely covered in hair, you cannot comb the hair in such a way as to have no partline. I can prove the theorem wrong: take a comb and do a 'fro on the ball. Hair is combed - no partline. Quod erat demonstrandum.

## Answer (score 3, by Jacob F. Davis C-CISO)

This would suggest that longer wavelength antennas are more efficient collectors of electromagnetic energy. Why is this?

I think of it like in optics. A larger lens will collect more light because more light is incident on the lens. More photons hit the lens.

A radio antenna is a lens for a different wavelength of light, i.e. radio waves, not visible light. Therefore, the (electrically) larger the antenna, the more photons are incident on the conductor, the more energy will be collected.

Said differently: If you had 2 antennas of the same length, you would collect twice as much energy as a single antenna. If you had two lenses of the same size, you would collect twice as much light as a single lens. Instead of 2 antennas, you could have a single antenna of twice the length and collect twice the energy of the original antenna. Same for the optical lens.

## Answer (score 2, by Paul)

This is simpler than the Friis equation makes it out to be.

The longer wavelength isotropic antenna is bigger, and aperture measures the effective electrical size of the antenna as a radiator. It is no surprise that the electrical size of an antenna that is physically larger is also larger.

Half-wave Dipoles have a constant gain, but are similarly larger at longer wavelengths.

The Friis equation is a particular algebraic expression of a conservation-of-energy equation, in a theory where all radiated energy is either received or radiated into space in a sphere.

The Gains in the Friis equation are generally lambda-dependent. Once again, it is common radio wisdom that smaller wavelengths, higher frequencies, require smaller elements for yagis or smaller reflectors for dishes to have the same gain. Thus if the antenna size stayed constant then as frequency increases, and lambda decreases, the gain should rise. This suggests gain depends on some inverse or perhaps inverse power of lambda.

For example, a the gain of a parabolic reflector dish of, say 3m diameter, will depend on the frequency and thus lambda. Wikipedia:Parabolic Reflector notes that the gain scales as 1/lambda^2. The Friis equation needs the gain of both antennas (receiving and transmitting), and so with dishes the transmit power received would scale as lambda^-2 * lambda^-2 * lambda^2 = lambda^-2 which provides a very different impression of what frequencies are best.

It is important to realize the Friis equation is a free space theory where the signal can spread out in a sphere.

It neglects the Earth, and with it all absorption or reflection by terrain, multipath reflections which can interfere constructively or destructively resulting in hot spots and dead zones, changes of media (e.g. trees, clouds), and various engineering requirements which may play a role at very low or high frequencies.

For instance, in the parabolic reflector example, we could move from microwaves to lasers to reduce lambda and increase power received according to the Friis equation. But this may not work out. Why? Aiming is much more critical with the laser, which relateds to the change in gain with a misaligned receive or transmit antenna. The parabolic antenna must now be a parabolic mirror of good quality instead of, say, stressed wire screening. And, a solid object such as a tree or bird is known to block a laser beam while a microwave might still be received.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1530/why-is-antenna-aperture-a-function-of-wavelength, by Phil Frost - W8II, Glenn W9IQ, Jacob F. Davis C-CISO, Paul. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
