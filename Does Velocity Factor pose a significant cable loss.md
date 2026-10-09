# Does Velocity Factor pose a significant cable loss?

*Tags: antenna-theory, coaxial-cable · score 3*

## Question

We know that a lower Velocity Factor translates to using shorter runs of cable in resonant circuits. That apparently means that there is resistance to the flow of electrons, slowing them down.

So does that resistance mean that we're also seeing a higher energy loss in the form of heat?

Given a choice of these two cables, which one has the most loss? Is the loss significant in choosing a feedline?

1. Cable having a VF of 66%
2. Cable having a VF of 82%

## Answer (score 6, by tomnexus)

Velocity factor is not the cause of cable loss, but it is related.

Signals in a coaxial cable travel as transverse electromagnetic waves with currents in the copper and electric fields in the dielectric. In the case that the dielectric is air (or vacuum) with a relative permittivity of 1.0 the wave will travel at the speed of light, VF = 1.0.  
If the dielectric has a higher permittivity than free space then the wave will travel slower, with the relationship $\text{VF}=\frac{1}{\sqrt{\epsilon_r}}$ which by the way is true for all electromagnetic waves in free space too, like light in glass or water.  
There are electrons moving in the metal, but their motion and speed is not really related to the speed of the electromagnetic wave, which travels in the space between the conductors [see [this video]](https://www.youtube.com/watch?v=bHIhgxav9LY).

The loss in coaxial cables comes from these non-ideal components.

- the copper has some resistance 1
- the dielectric has some loss which can be modelled as though it is slightly conductive 2
- there can also be some leakage if the cable braid is too sparse

The power lost to the first two is dissipated as heat, the third is radiated away.

Now in the design of coaxial cables, there are only two ways to reduce the loss caused by the dielectric:

1. Use a higher-quality dielectric, meaning a lower loss at the frequency of interest, while still meeting the mechanical needs of the cable. Cheap cables use polyethylene which is already extremely low loss. Better cables use PTFE (teflon) which is not much lower loss but is much stronger and more heat resistant.
2. Use *less of the dielectric, more air* which can be done in several ways: extruding a cellular structure, using a foam, using a helical structure, using thin supporting discs spaced far apart, or using no supports at all (except for the ends). All of these can be seen in practice, and have the effect of reducing the dielectric loss at the expense of some mechanical complexity and reduced ruggedness.

And the key thing is that when the effective quantity of dielectric is reduced, the velocity factor is also increased. **So along with the cable diameter, the velocity factor of a cable is in fact a fairly good indication of the cable loss** (keeping all other things constant). Cables with 82% VF (foam PE) will have about half the loss per length than cables of the same diameter with 66% VF (solid PE).

The copper loss can be improved by making the cable larger (which also increases its power handling) and slightly improved by using silver plating. The leakage is usually an insignificant cause of loss but cable can be made less expensive by using a very sparse braid over a layer of aluminimum foil or aluminised mylar.

Notes:

1. The resistive loss in the copper is made larger by the skin effect which forces the current to flow in quite a thin layer on the surface,
2. The dielectric loss might arise from other molecular effects - for example the [loss tangent of water [PDF]](https://www.ijert.org/research/dielectric-properties-of-water-at-microwave-frequencies-IJERTCONV3IS03027.pdf) rises with increasing temperature, and frequency, having a first peak at 24 GHz.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21748/does-velocity-factor-pose-a-significant-cable-loss, by Dax, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
