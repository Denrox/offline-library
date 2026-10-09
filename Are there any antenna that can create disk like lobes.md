# Are there any antenna that can create disk like lobes?

*Tags: antenna, antenna-theory, radio-programming · score 3*

## Question

Are there any antenna that have disk like lobes :

Or are there any antenna that have very thin directivity, say lobes be no more wide than few mm.

## Accepted answer (score 13, by Brian K1LI)

The answer from a theoretical purist is probably, "No," because your diagram specifies zero radiation outside of the disk. Practically speaking, there will always be some radiation above and below the disk and the shape of the disk will not be as perfect as you describe.

A well known solution that approaches your requirements comprises multiple collinear elements with carefully-chosen current amplitudes and phases. Here are plots from a NEC-2 simulation of a simple example with three elements:

Each element is 0.615$\lambda$ long, the vertical spacing between the element feedpoints is 0.6275$\lambda$ and the center element is driven with twice the current amplitude of the outer elements. Notice the not-perfectly-disk-shaped pattern and the deeply-attenuated side-lobes.

Varying any of these parameters will affect the results, as well as the driving-point impedance of each element, to a greater or lesser degree according to your needs.

## Answer (score 8, by Phil Frost - W8II)

Achieving such a sharp radiation pattern is difficult. There are many effects that can can cause the radiation pattern of an antenna to be less "sharp". Some of them can be fixed through engineering, such as by manufacturing components to tighter tolerances. Others are unavoidable physical limits. In the best case, diffraction will limit the maximum sharpness of the disk. The very sharpest sources of electromagnetic radiation are lasers, which achieve a beam divergence approaching:

$$ \theta = {\lambda \over \pi w} $$

where $\theta$ is the angle between the edges of the beam, $\lambda$ is the wavelength, and $w$ is the diameter of the "waist" of the beam, that is the beam's diameter at its narrowest point. Often, this is the aperture of the laser cavity.

It follows then if you want a laser with very low beam divergence, and thus, a very "sharp" radiation pattern, you require a very large aperture.

Radio antennas aren't lasers, but like lasers they are emitters of coherent electromagnetic radiation. But very significantly, the wavelength ($\lambda$) of radio waves is much greater than in a laser. Thus, achieving a smaller beam divergence requires a much larger aperture.

Not all antennas have an obvious physical aperture, but some do, such as dish antennas. An antenna with a larger dish will have a sharper radiation pattern than a smaller dish. Likewise, the same dish size at a higher frequency will be sharper than a lower frequency.

If you want a disk and not a beam, you're looking for a low beam divergence in just one dimension. You could achieve that with a custom reflector, and the bigger you can make the reflector the sharper the disk will be. Alternately, you can use a co-linear array like Brian K1LI suggests. The more elements in the array, the sharper the radiation pattern becomes.

But if your objective is to detect the position of a falling object (with some kind of radio transmitter on it, I presume), you can do even better by using an array of antennas as an interferometer.

XKCD: Interferometry

The idea is to compare the *phase* of the received signal at two or more antennas. The difference in phase corresponds to the difference in path length between them, and from that you can triangulate the position of the object.

## Answer (score 4, by Marcus Müller)

antenna that have disk like lobes

The pattern of an antenna is *never* going to be disk-shaped (because the directivity is angle-dependent, not limited to a volume).

But: an omnidirectional antenna (in azimuth) with a very high directive gain in elevation approximates what you want.

A simple vertical stack of vertical half-wavelength dipoles, driven in phase, gets that directivity. See: "array gain".

Notice that

- the more gain an antenna has in one direction (here: vertical), the longer it has to be in that direction.
- Building antennas with high gain that also have the same pattern for a large range of frequencies is very hard to physically impossible

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17333/are-there-any-antenna-that-can-create-disk-like-lobes, by user3769778, Brian K1LI, Phil Frost - W8II, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
