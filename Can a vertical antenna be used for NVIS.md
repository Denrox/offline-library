# Can a vertical antenna be used for NVIS?

*Tags: vertical-antenna, nvis · score 5*

## Question

I know that verticals are normally chosen for their low angles of radiation without obscene heights, but I'm not especially interested in DX and am primarily looking for local coverage via NVIS. I've not had great luck with dipoles at my home (parallel 5kV power lines under a wavelength away for 20m and below, I think, are the reason here). I was reading an old question and saw [an answer](What%20is%20the%20attraction%20of%20vertical%20antennas%20for%20HF.md) that talked about using a vertical for NVIS, which I've never heard of.

Knowing that 1/4λ verticals are known in VHF/UHF applications to have nearly isotropic patterns, I'm not sure how to reconcile that with the "verticals are great for DX" thing for HF. What gives and how can I do 160/80/40m NVIS with a vertical?

## Accepted answer (score 6, by Glenn W9IQ)

Knowing that 1/4λ verticals are known in VHF/UHF applications to have nearly isotropic patterns

This is not a valid assertion. A UHF/VHF vertical antenna has > 0 dBi gain (more succinctly a directivity >1) so by definition it cannot have nearly an isotropic pattern. Its primary directivity is toward the horizon at about a 22 degree elevation (although highly dependent on the the ground plane and the elevation of the antenna).

I'm not sure how to reconcile that with the "verticals are great for DX" thing for HF

You cannot reconcile it because the two conditions are not both true. A well constructed vertical antenna will have its primary gain toward the horizon which is what gives it its desired DX characteristics. A 1/2 wave dipole antenna needs to be mounted about 1/2 wavelength above ground to achieve a similar effect.

What gives and how can I do 160/80/40m NVIS with a vertical?

NVIS with a vertical antenna is not a practical application as @mikewaters points out. The general concept for NVIS is to erect an antenna that directs most of its energy "straight up" so that the atmospheric reflections come back to earth in close proximity to your station. The vertical antenna actually has a hole (negative gain) in its pattern in the vertical direction.

I've not had great luck with dipoles at my home

It would be helpful if you could give a more complete description as to what this means. That could be a starting point for getting your NVIS station working properly.

## Answer (score 3, by Mike Waters)

If you want NVIS (predominately high-angle radiation, for closer-in stations rather than DX), **then you don't want a vertical.**

Instead, you want something like a **horizontal** dipole (or inverted-vee), or a horizontal loop.

The antenna that that post described was a top-loaded vertical. Its top was connected to the mid-point of the horizontal wire. In that configuration, the horizontal wire will radiate very little.

I have used inverted-L antennas with great success. The majority of the radiation is vertically-polarized at low angles (great for DX). However, there is enough high-angle radiation from the horizontal, sloping section to work closer-in stations. See this page about my 160m inverted-L. It was built for 160m, but I was amazed at the performance on 75, 40, and 20 meters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9731/can-a-vertical-antenna-be-used-for-nvis, by William, Glenn W9IQ, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
