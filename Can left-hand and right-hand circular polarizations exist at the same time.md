# Can left-hand and right-hand circular polarizations exist at the same time?

*Tags: circular-polarization · score 3*

## Question

I read [in a comment](Long%20range%20HF%20polarization.md):

it doesn't matter which circular polarization you choose, because they are both present, and the whole point here is to select one of them instead of receiving both and getting mixing.

The premise of the point being made seems to be that an HF signal received after making a pass or passes through the ionosphere will be *both* left-hand and right-hand circularly polarized, and so a receiving antenna of either chirality will not be subject to fading as a linearly polarized antenna would be.

Is this possible, for a signal to be *both* left- and right-hand polarized?

## Accepted answer (score 3, by Marcus Müller)

Is this possible, for a signal to be both left- and right-hand polarized?

Yes, it's very much possible:

While the superposition of two orthogonal circular polarizations might¹ indeed look linear (just as the superposition of a horizontal and a vertical polarized wave at appropriate phasing is a circularly polarized wave), of course that means that a linearly polarized wave is at the same time circularly polarized in both directions.

Technically, this is widely exploited: Satellite receivers use polarization multiplex. That is awesome, because you get two totally independently useful "subchannels", as long all media the wave travels through is a largely a linear medium and isotropic. (And the microwave frequencies geostationary satellite downlink channel fulfills that pretty well.)

Even if that's not the case, you still get *some* isolation between RHCP and LHCP, and can use that for MIMO techniques to increase your data rate or robustness beyond what you can do on a single polarization.

¹ might because that's not necessarily the case. Remember the Poincaré sphere:

When you add waves of different polarizations, you wander on the surface of that sphere; only when you add RHCP and LHCP with the same magnitude, you end up with a linear polarization. The angle of that is then defined by the phase between the two constituent waves; every other combination, every attenuation that affects one rotational sense more than the other, will produce an elliptic polarization.

Let me rephrase your question:

Is this possible, for a *wave* to be both left- and right-hand polarized at the same time?

No, that's not possible, because any wave can only occupy **one** point in polarization space.

## Answer (score 4, by Phil Frost - W8II)

No, it's not possible. The electric field vector can only point in one direction at a time, so there's no way it could simultaneously rotate in two directions.

However it is possible to consider any possible polarization as a superposition of left- and right-handed circular polarization.

When there are multiple radiation sources, either because there are multiple transmitters or because the same signal is being received through multiple paths, then the result at the receiver is the addition of each source. Adding two circular polarizations of opposite chirality together produces a linear polarization.

This can be shown graphically as a 3D parametric plot:  
(editable source)

On the left in yellow, we have:

$$ \left\{ \begin{aligned} x(t) &= \cos(t) \\ y(t) &= \sin(t) \end{aligned} \right. $$

On the right in blue we have:

$$ \left\{ \begin{aligned} x(t) &= -\cos(t) \\ y(t) &= \sin(t) \end{aligned} \right. $$

And the middle in green is the addition of these two:

$$ \left\{ \begin{aligned} x(t) &= \cos(t) - \cos(t) \\ y(t) &= \sin(t) + \sin(t) \end{aligned} \right. $$

It's pretty plain to see this simplifies to $x(t) = 0$ as the opposite electric fields along the x axis cancel each other.

As the two sources change in relative phase, the plane of the resulting linear polarization rotates:  
(editable source)

Here, green is showing

$$ \left\{ \begin{aligned} x(t) &= \cos(t+2) - \cos(t) \\ y(t) &= \sin(t+2) + \sin(t) \end{aligned} \right. $$

While it's not so immediately obvious to see the cancellation, it remains true that opposite helices like this will cancel each other in *some* plane, as long as they are equal in amplitude.

If the two sources are not equal in amplitude, then the result is elliptical polarization:  
(editable source)

It is true that the ionosphere is time-variant, and so at one time the signal as received may be left-handed, and some time later right-handed. But is impossible for it to be *both at the same time*, although one could consider a linear polarization to be the superposition of both circular polarizations in equal amplitude.

The problem is an ionospheric channel does not guarantee equal amplitude. Thus, a circularly polarized receive antenna will still be subject to fading as the signal randomly wanders between left- and right-handed chirality, as well as linear and all the points between (elliptical polarizations).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16898/can-left-hand-and-right-hand-circular-polarizations-exist-at-the-same-time, by Phil Frost - W8II, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
