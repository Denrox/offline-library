# Is it possible to make a shield that blocks time-varying electric fields, but not time-varying magnetic fields?

*Tags: antenna, antenna-theory · score 3*

## Question

Take, for example, a [shielded loop antenna](What%20does%20the%20addition%20of%20a%20shield%20to%20a%20small%20loop%20accomplish.md). It is [often](What%20does%20the%20addition%20of%20a%20shield%20to%20a%20small%20loop%20accomplish.md) claimed that the antenna is inside the shield, and the shield blocks electric fields from reaching the antenna, while allowing magnetic fields to pass through to the antenna. This in turn reduces noise in environments heavy in electrostatic noise, the argument goes.

Is this physically possible? Can a shield block time-varying electric fields while allowing time-varying magnetic fields to pass unchanged?

## Accepted answer (score 4, by Phil Frost - W8II)

No, it's not possible. Anything that is good at blocking time-varying electric fields will also be good at blocking time-varying magnetic fields of a similar frequency.

First let's consider a vertically polarized, radiated wave incident upon a conductive plane:

Since this wave is vertically polarized, the electric field vector points alternatively up and down. Because it's a radiated wave, it's also accompanied by a magnetic wave, in phase, but horizontal.

The varying electric field will pull the charge carriers in the conductive plane up and down, along with the field. Assuming an infinite, perfectly conductive plane, the electric field won't penetrate the plane at all, because the charges in the plane rearrange themselves to cancel the electric field. This is the principle behind a Faraday cage.

But wait...the charges in the plane are moving with the field. That's a current, right? And when there's a current in a conductor, there's an associated magnetic field, right? The current is vertical, and the magnetic field is concentric with the current, so it will be in the horizontal plane. So is the magnetic field associated with the electric field incident upon the plane.

If you do the math, as it turns out, these magnetic fields cancel.

OK, but what if it isn't a radiated wave, but just a magnetic wave incident upon the plane? Maybe there is a solenoid nearby, which we are driving with an alternating current. Will the plane block that?

Yes, it will. The time-varying magnetic field will induce eddy currents in the plane which cancel the magnetic field. Faraday's law of induction explains these eddy currents. It is this very same effect that is responsible for skin effect.

W8JI has a good experimental demonstration of this. He puts a connector in a copper sheet and drives it with a signal generator. He then probes the electric and magnetic fields at increasing distances on the front and then around the back of the sheet. For both the electric and magnetic fields, the field weakens with increasing distance, and by the time he gets around to the back of the sheet, directly behind the connector, neither the electric nor magnetic fields are measurable.

This seems odd, because a sheet of copper has no particularly obvious magnetic properties, and classically we think of separate magnetic forces and electric forces. How can a copper sheet have any effect on the magnetic force? When Maxwell made his equations, he didn't know either: it was just experimentally found to be true.

The development of special relativity provided more insight. The magnetic force is really just the consequence of special relativity and the electric force in a moving frame of reference. So you see, there really isn't a magnetic force. There's only an electric force, and special relativity. Knowing this, it is intuitively less surprising that a sheet of copper, which has obvious electrical properties, can have magnetic properties.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2455/is-it-possible-to-make-a-shield-that-blocks-time-varying-electric-fields-but-n, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
