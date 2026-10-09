# What is really happening during RF ionospheric refraction?

*Tags: propagation, ionosphere · score 3*

## Question

We all know that the ionosphere — when charged — refracts RF energy, but why? In other words, what is actually occurring at a molecular level to cause radio waves to bend back to earth because of charged particles in the atmosphere? Is it a collision of some type between waves and particles?

## Answer (score 6, by Phil Frost - W8II)

Solar radiation ionizes the atmospheric gas, creating a plasma with free electrons. The density of these free electrons varies by height, time of day, and solar conditions.

Because the electrons are free to move in the plasma, they will be displaced by an electromagnetic wave. If you want a rigorous mathematical treatment, The University of Toronto has a great paper. In summary, the presence of these free electrons has the effect of altering the relative permittivity of the medium.

Relative permittivity is also known as the dielectric constant, and is related to the refractive index:

$$ n = \sqrt{\varepsilon_\mathrm r \mu_\mathrm r} $$

where

- $n$ is the refractive index,
- $\varepsilon_\mathrm r$ is the relative permittivity, and
- $\mu_\mathrm r $ is the relative permeability.

If you have some experience engineering magnetic circuits, you may understand relative permeability in terms of magnetic dipoles within a material such as iron or ferrite which are able to align themselves with an applied magnetic field: this is why putting a core in an inductor increases the inductance. Relative permittivity is the same thing only for electric fields, and it's those free electrons in the atmosphere responsible for the change in permittivity.

Anyway, different layers of the ionosphere have different refractive indexes, which means at the interface between different layers an electromagnetic wave will be bent. The degree of bending is proportional to the difference between the refractive indexes.

If the wave skims the ionosphere at a shallow enough angle, the refraction will be sufficient to reflect the wave back out of the ionosphere. This phenomenon is called total internal reflection. You've probably seen it at the interface between water and air, which when viewed at a shallow angle appears to be a mirror:

Brocken Inaglory [CC BY-SA 4.0], via Wikimedia Commons

In this example there are two media with a distinct boundary between them, which can make it a little hard to accept. In reality, the electron density (and thus the refractive index) of the atmosphere varies smoothly with altitude. But total internal reflection can still occur. Think of it as a stack of infinitesimally thin layers, with each layer having a very slightly different index of refraction. Each interface bends the wave just a little bit, with the net effect of making the wave travel in a curved line.

A visible example of this is *mirage*:

Brocken Inaglory [Public domain], via Wikimedia Commons

Notice the inverted image of the tent. This is caused due to the temperature gradient of the air: the lower air is hotter, and the refractive index of air varies with temperature. Ionospheric refraction works the same way, only upside-down and the frequency is much lower.

## Answer (score 2, by OH2FXN)

The ionosphere contains freely moving charged particles that act like a conducting "plate". When a radio wave traveling up reaches the ionosphere, the electric field of the wave starts to move the electrons. This movement that happens at the RF frequency acts like a current and the current acts a bit like an antenna creating its own wave that is now traveling back to earth.

The original wave is mostly cancelled out by the radiation from this new current sheet in the region above the ionosphere.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15444/what-is-really-happening-during-rf-ionospheric-refraction, by Dave G, Phil Frost - W8II, OH2FXN. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
