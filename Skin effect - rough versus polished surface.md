# Skin effect - rough versus polished surface

*Tags: antenna, antenna-theory · score 3*

## Question

Considering "skin effect", does the surface finish of Aluminum tubing have any practical effect on antenna efficiency at HF frequencies (5-30 MHz)? For example: Aluminum tubing as manufactured - rough surface, etc, versus the same tubing but polished. Specifically referring to small transmitting magnetic loop antennae.

## Answer (score 4, by Glenn W9IQ)

If the variation in the surface finish is less than 10% of the skin depth for the frequencies involved, the effect will be minimal. The skin depth will be the most shallow at your upper 30 MHz limit of your question. In aluminum this translates to a skin depth of ~15 $\mu $m. Here is a graph of the attenuation effect (from microwaves101.com)

An RMS or RA finish of ~64 (ISO 9) or better (smaller) would be required to stay under the 10% of skin depth rule. When the surface roughness is 1 skin depth, you can experience ~60% more loss in the conductor. For reference, sanding your aluminum with 240 grit sandpaper will leave a surface roughness of ~0.47 $\mu$m - well below the 10% of skin depth rule.

So in general, the more you polish your aluminum in a low efficiency application like a loop, the better the antenna efficiency, and thus gain, will be but anything approaching a mirror like finish is overkill on HF. Do not forget to clear coat it once you are done or the formation of aluminum oxide will discount your earlier polishing efforts.

You may also wish to consider using pure copper tubing. While the skin depth is slightly less (~12 $\mu$m), its lower resistivity brings efficiency gains.

Increasing the diameter of the tubing also reduces the resistive losses. So before you attempt a mirror like finish, you may wish to consider larger diameter tubing as a more practical approach.

Also recall that the larger in diameter that you make your loop, the more efficient it becomes. The rate of increase in radiation resistance is faster than the rate of increase of resistive losses so it is worth considering.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10210/skin-effect-rough-versus-polished-surface, by DaveG, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
