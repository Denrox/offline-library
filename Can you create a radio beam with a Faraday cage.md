# Can you create a radio beam with a Faraday cage?

*Tags: antenna-theory, propagation, theory · score 4*

## Question

Imagine we have an isotropic antenna at the origin emitting a steady sine wave at frequency $f$. Encompassing the antenna is a sphere of radius $r$ made of a fine copper mesh (with holes $\ll\frac\lambda{10}$, making it a Faraday cage).

From this sphere we remove a patch of material of size $n^{\circ}\times n^{\circ}$.

What would the far-field pattern look like? Is there any combination of the variables ($f$, $r$, $n$) that would create a tight beam from the removed patch of material? What if instead of removing a patch of material we removed a slit from pole to pole with width $n^{\circ}$?

## Accepted answer (score 3, by Marcus Müller)

No, there would not be a narrow beam.

There's multiple ways you can show that, but most intuitively, I think is the follow:

- consider every point on that patch to be a source of an elemental wave
- in the center of that patch, these will interfere in a manner so that only the "straight" radial path has a propagating wave front. (think about it: if it wasn't straight, then it would destructively interfere with the neighboring wave sources, which excludes anything but straight)

 - even this alone would not lead to a narrow beam, but simply to a beam with your $n^\circ$ opening angle
- Close to the edges of that patch, however, there's no neighboring sources. So, the propagation happens "bent away" from the core of the patch.

That phenomenon is called diffraction, and when you think about it, your experiment is just what people usually do to demonstrate diffraction:

Have an experiment with a planar wave front approaching a slotted obstacle. In your case, "planar" is to be interpreted with respect to a polar coordinate system with the origin in the center of your sphere, but other than that: classical slit experiment.

In other words, this is basically a patch aperture, and there's nothing about single patch antennas that gives you a narrow beam. To make things worse, the smaller you choose $n$, the wider that beam becomes.

You'd pretty much do the *opposite* when trying to create a narrow beam (to build an antenna with high directional gain): Finding a surface where the phase difference for plane waves is constant, and other directions quickly experience destructive interference. Take that patch you removed from your mesh sphere, throw away the rest of the sphere, flip the patch inside out, pushing it a bit so that it's parabolic and use it as a reflector. That shape should remind you of an emitter type you might already know:

mesh parabolic antenna, Wikimedia Commons, photograph oescalona

## Answer (score 4, by sm5bsz)

I think that if the sphere is very large in wavelengths. Maybe 1000 wl and if the opening is small, maybe 10x10 wl, you would create a fairly narrow beam. Such a small opening in such a big sphere would be close to a hole in a flat surface. The phase would be the same over the entire 10x10 wl area. It would however be better to make a 10x10 wl equiphase wavefront by shaping a 10x10 area as a parabolic surface and irradiate it properly (not so easy) but a 20x20 surface would easily produce a similar beam as the big sphere. The big sphere would have an extremely ugly frequency response. It would be a resonator with a very small leakage through the hole.

I understand the question as purely accademic....

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9507/can-you-create-a-radio-beam-with-a-faraday-cage, by Jerald Thomas, Marcus Müller, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
