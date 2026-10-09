# how to stack parabolic antennas?

*Tags: antenna-construction, antenna-system, eme · score 4*

## Question

I've read that the distance between stacked antennas should be 0.5 to 1 wave lengths - does it mean stacking of parabolic antennas as e.g. for 13 cm EME is not possible?

If yes then the only way to avoid large dishes is to build an array using yagi antennas?

## Accepted answer (score 4, by tomnexus)

The spacing of the elements of an array needs to consider a few things:

First and most important, the antenna apertures shouldn't overlap (too much) otherwise the performance of each antenna will be affected, reducing the total gain.

The effective aperture of an antenna is $A_e={G\lambda^2/{4\pi}}$ so if you assume it's roughly circular then the diameter of the aperture would be about $D_e={\sqrt{G}\lambda/{\pi}}$, with G in linear units not dB.  
For a short 3-element yagi (10 dBi) this is about $1\lambda$, for a long yagi (say the M2 43215WL with 21.5 dBi) this is $3.8\lambda$. M2 actually recommend 96" which is 3.5 wavelengths.

An aside about apertures... a few antennas (like a pyramidal horn) have a completely filled aperture, where the physical aperture is equal to the effective aperture, and the field strength is about the same across the whole aperture. Horns are arrayed with the edges touching.  
But most antennas, including the yagi and the dish, have a tapered aperture, so the field or power distribution is not uniform across the aperture - it's strongest in the centre and drops away on the sides. In a dish antenna the effectiver aperture is only 70% of the physical aperture, and the field at the edges is about 30% of the field in the centre (10 dB taper).

Second, you want the spacing as close as possible so that the primary or central beam of the array is as large as possible. Moving the antennas apart makes the beam narrower, and at larger spacings a whole lot of narrow beams form (within the primary beam envelope). Although the peak gain is the same, the narrower pattern is not ideal for many reasons.

Finally, spacing is mechanically difficult and expensive, so we want it to be as small as possible.

It is possible to form an array of dish antennas. It might be possible to overlap them slightly, but you'd probably do it so they don't physically overlap. You could mount them on some sort of frame so they all move together, or they could be on their own independent mounts, which requires a more complex method of feeding them in phase.

But for EME applications, by far the best solution is to simply *build a bigger dish* and get the increased aperture and gain that way. You avoid all the pain of feeding multiple antennas in phase, the feedline loss between antennas and LNA, and the general complexity that comes with an array. A larger dish still has only one feedpoint.  
Doubling the diameter of a dish will increase its gain by 6 dB, its wind area by 4x, the dish surface mass by 4x but the whole dish probably only 2x.  
Arraying four smaller dishes will probably only achieve 4 dBi of extra gain because of the cable loss and phasing imperfections. Mass and wind area will go up more than 4x. And system noise performance will go up less than 4 dB because on a cold sky target every dB of feedline loss before the LNA costs you more than a dB of sensitivity.

It's only when the single dish gets too large to be manouverable, that it's worth creating an array... for example the Goldstone DSN 70 m dish is arrayed with several (smaller) dishes to improve the signal from Voyager, and many radio telescopes use an array of smaller dishes instead of one big dish (for increased area but for other reasons too).

One last point about amateur EME - there is a clear winner at each amateur band. 6m, 2m, 70 cm are almost always Yagis, 23 cm mostly dishes, above this always dishes. There are outliers, but the optimum is quite constrained by our power levels, signal bandwidth, and space/budget constraints. With 100x the budget, on 70 cm you would also build a dish. With 10 W and JT44 on 23 cm you might get by with one long yagi. At 13 cm yagis are getting quite fiddly, and you'd need a lot of them to get enough gain.

## Answer (score 2, by user10489)

Stacked antennas have to be phase matched.

Passive phase matching is done by a combination of spacing between the antennas and a phasing harness that takes into account that distance, so that the wave fronts emitted by all the antennas are aligned in the direction of interest.

This does not have to be 0.5 - 1.0 wavelengths, but the phase angles do have to match, and this is the shortest distance range it will work for.

It would also be possible to do active phase matching, by either separately generating the same signal at each dish or using some active device to adjust the phase variation between antennas. This is how phased array antennas work. However, this makes less sense for something as directional as a dish.

Note that radio telescopes stack dishes. For example, https://en.wikipedia.org/wiki/Square_Kilometre_Array

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23017/how-to-stack-parabolic-antennas, by Romeo Kienzler, tomnexus, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
