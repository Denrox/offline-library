# Closest antenna to an isotropic?

*Tags: antenna · score 3*

## Question

What is the closest antenna ever made to an isotropic antenna? That is, has the same gain in every direction in free space?

## Answer (score 3, by Phil Frost - W8II)

An isotropic antenna *can not exist*. Asking how "close" we can get doesn't really make sense. It's like asking how close we can get to any other impossible thing, like creating perpetual motion. Can we say one thing is *closer* to violating the laws of thermodynamics than another? No: all things ever observed obey these laws, no exceptions. Likewise, all antennas ever observed obey Maxwell's equations, so none can be isotropic. Not even a little bit. No exceptions known to science.

How do Maxwell's equations forbid isotropic antennas? I'll explain by analogy. Imagine a ball with some hair on it. Is there any way to comb this hair flat on the ball such that there is not at least one tuft?

There isn't. This is the hairy ball theorem, which states "there is no nonvanishing continuous tangent vector field on even-dimensional n-spheres."

Now, imagine that the hairs are the electric or magnetic field radiating from your antenna. We are looking for a vector field on a sphere, so the "tuft", where the hair sticks straight out, is a vector of zero magnitude. This is a point where there is no radiation.

Why does the hairy ball theorem apply? Because electromagnetic waves are transverse waves. This is why the tufts count as vectors of zero magnitude and not as vectors sticking out: the *only* direction the lines of force can go in a field that you want to radiate away from that sphere are tangential to the sphere.

Contrast this with sound waves, which are longitudinal waves. For these, the lines of force must be perpendicular to the sphere, and an isotropic radiator is easily realized: just make the hair stick straight out everywhere.

So, the consequence of this is that any antenna must not radiate it at least one direction. Beyond that, arbitrary radiation patterns are possible, but none of them are close to isotropic.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1846/closest-antenna-to-an-isotropic, by Skyler 440, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
