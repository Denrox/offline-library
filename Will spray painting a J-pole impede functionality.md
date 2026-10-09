# Will spray painting a J-pole impede functionality?

*Tags: antenna, antenna-construction, j-pole · score 3*

## Question

I'm building a J-pole antenna like the one specified here: https://www.sysjolt.com/2022/building-a-j-pole

As you can see it's made of copper pipe and I'd like to camouflage the antennae a little bit.

Will using spray paint degrade the performance of the J-pole? Is there some paint I can use that won't?

## Accepted answer (score 3, by user10489)

TL;DR: Probably not.

If you cover the J-pole with something non-conductive, it will act like a dielectric. This can detune the antenna but generally won't otherwise degrade performance. (If it has a high ESR too, that could be bad in multiple ways.) For instance, if you put the antenna in a PVC pipe, you will need to retune it. However, a layer of paint shouldn't be thick enough for this to even be measurable.

If you cover the J-pole with something conductive that is electrically connected with the radiating section (not shorting the matching section), it will become part of the antenna. This has two effects. It increases the diameter of the radiating element, which would increase the bandwidth of the antenna. (Again, this would not be measurable for a layer of paint.) Secondly, due to skin effect, more of the RF would be in the surface of the radiating element than in what is underneath. If the layer you add is more conductive than the body, this is good. If it is less conductive (like a partially conductive paint), it adds resistance. This won't affect performance a lot for a very thin layer, but it could reduce the radiation of the antenna measurably. How much it reduces it depends on the skin depth at the frequency. (If the layer is thinner than the skin depth, some energy goes to the new layer, some goes to what is underneath. This effect is logarithmic vs. depth.) Skin depth is not very large, especially at VHF frequencies, so a layer of conductive paint may be significant.

In both cases, if the outer layer is resistive (either ESR or direct resistance), it will absorb some of the energy of the signal. In extreme cases, it could heat up and possibly melt or burn off. For conductive paint, this probably won't be an issue, but it might still be measurable. For non-conductive paint, it would have to have a super high ESR to matter. Something like styrofoam (which is rumored to be RF absorbing) could be very bad, even in very close proximity, not just covering.

## Answer (score 2, by David Hoelzer)

As long as the paint you are using has no metal content you should be just fine. Avoid metallic spray paints. From what you say, though, that's probably not what you have in mind. :)

Just make sure you tape off the connectors/terminals.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21780/will-spray-painting-a-j-pole-impede-functionality, by john_ham_radio, user10489, David Hoelzer. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
