# Why is the electric field orthogonal to the magnetic field from an antenna?

*Tags: antenna, propagation · score 8*

## Question

I've read in several places that the electric field is 90 degrees orthogonal to the magnetic field, and both are orthogonal to the direction of the wave from a transmitting antenna.

What causes this? Are there *any* cases where this might not be true, or are the fields *always* 90 degrees to each other?

## Answer (score 8, by WPrecht)

The short answer is no, there are no cases where radio waves would not have orthogonal magnetic and electric fields.

In physics, a radio wave, indeed all EM radiation is called a transverse wave, meaning, by definition, that the oscillations of the waves are perpendicular to the direction of energy transfer and travel.

The electric and magnetic parts of the field stand in a fixed ratio of strengths in order to satisfy the two Maxwell equations that specify how one is produced from the other. These $\mathbf{E}$ and $\mathbf{B}$ (in physics the magnetic part uses B for some reason, I'll maintain that convention to make it easier for the physics folks to correct any errors) fields are also in phase, with both reaching maxima and minima at the same points in space.

OK, so we know this much already, but ***why***?

Ask James Clerk Maxwell; his electromagnetic wave equation is a second-order partial differential equation that describes the propagation of electromagnetic waves through a medium or in a vacuum. It is a three-dimensional form of the wave equation. The homogeneous form of the equation, written in terms of either the electric field E or the magnetic field B, takes the form:

$$ \left(\nabla^2 - { \mu\epsilon } {\partial^2 \over \partial t^2} \right) \mathbf{E} = \mathbf{0} \\ \left(\nabla^2 - { \mu\epsilon } {\partial^2 \over \partial t^2} \right) \mathbf{B} = \mathbf{0} $$

where

$$c = {1 \over \sqrt {\mu\epsilon} }$$

is the speed of light in a medium with permeability ($\mu$), and permittivity ($\epsilon$), and ∇ is the Laplace operator. In a vacuum, *c* = 299,792,458 meters per second, which is the speed of light in free space.

So that's the general theory, this can be solved for the plane wave case (the one we are interested in):

Given a plane defined by a unit normal vector: $\mathbf{n} = { \mathbf{k} \over k }$.

Then planar traveling wave solutions of the wave equations are:

$$\mathbf{E}(\mathbf{r}) = E_0 e^{ -i \mathbf{k} \cdot \mathbf{r} }$$

and

$$\mathbf{B}(\mathbf{r}) = B_0 e^{ -i \mathbf{k} \cdot \mathbf{r} }$$

where ***r*** = *(x, y, z)* is the position vector (in meters).

These solutions represent planar waves traveling in the direction of the normal vector ***n***. If we define the z direction as the direction of ***n***. and the x direction as the direction of ***E***., then by Faraday's Law the magnetic field lies in the y direction and is related to the electric field by the relation $\scriptstyle c^2{\partial B \over \partial z} \,=\, {\partial E \over \partial t}$. Because the divergence of the electric and magnetic fields are zero, there are no fields in the direction of propagation.

**References**

- The Production of EM waves (physics lecture notes)
- Wikipedia, your first stop shop for math that blows your head off
- College Physics, Volume 2

## Answer (score 2, by Phil Frost - W8II)

For radiated fields, the electric field (**E**) and (**H**) are always perpendicular. No one knows why this is more than we know any other physical law, but so far as anyone can demonstrate, it's always true. As WPrecht says, Maxwell's equations require electromagnetic waves to be this way. There's also simpler, albeit less complete mathematical explanation: the Poynting vector. This vector is simply the cross-product of **E** and **H**:

$$ \mathbf{S} = \mathbf{E}\times\mathbf{H} $$

This vector **S** represents the direction of energy transfer, so it follows that if the energy is radiating away, then the electric and magnetic fields must be mutually perpendicular to this, by the definition of the cross product operation.

You can gain some intuition into why this is true by considering the fields around a dipole. Say the dipole is vertical. The electric field lines are vertical, because the voltages are different along the length of the dipole. Meanwhile, current is flowing through the dipole, and current through a conductor makes magnetic field lines in concentric circles around that conductor. The result looks like this:

(Here they've used **B** for the magnetic field instead of **H**. There's a difference, but it will send us off on a tangent. Without compromising the understanding of this particular problem you can consider them to be the same.)

As you can see, the fields are perpendicular, and they stay that way.

If you think more about it, all moving electric charges, not just those in wires, create an associated magnetic field. This includes the displacement currents involved in radiation. And really, *create* might be the wrong word, because time-variant magnetic fields are also associated with electric fields (see Faraday's law). That magnetic fields can create electric fields and electric fields can create magnetic fields is what allow these two to self-propagate indefinitely in free space. Of course you can have electric fields with no magnetic field (capacitors) or magnetic fields with no electric fields (inductors), but these don't radiate (in the ideal case). So, the perpendicular arrangement of the fields in a dipole isn't coincidence: it's what makes it an effective antenna.

## Answer (score 2, by G4ZLZ)

The two fields do not have to be orthogonal, and in the diagram posted they are in fact NOT orthogonal everywhere (for example, what do E and H do near the ends of the antenna?). Orthogonal E and H field are the property of a propagating EM wave in free space. Around an antenna, within a few wavelengths distance, there are "near field" or "Fresnel" regions in which there are non-propagating waves. These waves do not have necessarily orthogonal fields. More detail can be found in a reference text such as Antenna Theory by Balannis.

Note also that the fields may be orthogonal and out of phase with each other. You might see this from a circularly-polarised antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1608/why-is-the-electric-field-orthogonal-to-the-magnetic-field-from-an-antenna, by Adam Davis, WPrecht, Phil Frost - W8II, G4ZLZ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
