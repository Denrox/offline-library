# What are the effects of different feed-line incidence angles?

*Tags: antenna-theory, coaxial-cable, feed-line · score 5*

## Question

Consider a dipole antenna fed by a coax (say, longer than the antenna) with a signal reasonably close to the dipole's resonant frequency. Various sources say that the feed-line should approach the antenna perpendicularly.

What are the effects (SWR, radiation efficiency, pattern, etc.) if the feed-line incidence angle is different from 90 degrees, from a few degrees away from perpendicular, all the way to close to parallel to the dipole?

In the case of the feed-line being very close to parallel to the dipole, it seems like this would be geometrically similar to an end-fed antenna. If so, would a current balun placed on the coax a quarter wavelength from the dipole center help?

## Answer (score 3, by Glenn W9IQ)

When the coaxial cable is in the near field of a center fed, 1/2 wavelength dipole and it does not run perpendicular to the antenna, it is subjected to imbalanced near field currents. The coupling effect will be cos $\theta$. The result is that the exterior braid of the coax may carry common mode current. OCF and end fed antennas also promote common mode current due to their inherent imbalance. Running the coax parallel to the dipole should be avoided.

The significance of the common mode current is dependent upon factors such as coax length, the grounding of the coax, common mode chokes, the frequency of operation, imbalance of the antenna, etc. Antenna modeling programs can be used to estimate the subseptibility of a particular configuration.

The effects of common mode currents can include RF shocks in the shack, interference with home electronics, coupling of nearby RFI into the antenna, alteration of antenna resonance/SWR and an alteration of the antenna pattern and gain.

A common mode choke at the feed point of the dipole and another one at the shack entrance or at least out of the near field of the antenna can be deployed to mitigate the effects. Ferrite based common mode chokes or 1:1 current baluns tend to be the best multiband performers. Some report success by burying the coax.

It is also helpful to avoid odd multiples of 1/4 wavelength coax as this promotes the formation of common mode currents. Note that the coax velocity factor does not come into play since this current is on the exterior of the braid. Instead, use a 0.95 to 0.97 velocity factor to account for the outer coaxial jacket.

## Answer (score 2, by user10489)

Note that odd multiples of a 1/4 wave of coax are good for SWR -- in other words, that segment of coax will become part of the antenna if it is resonant.

Placing a balun at the right length may help, assuming you don't care (or desire) that the resonant section of coax will radiate and alter the radiation pattern of the antenna, and don't care about all the other effects.

The Carolina Windom (OCF dipole) places a balun at the feedpoint and another inline balun at 1/4wl down the coax assuming a wavelength of 10m. It does this specifically to add the 10m band to an antenna that would otherwise not work well on this band. (Note: if you are doing this on purpose, don't forget to use the feedline's velocity factor when calculating the length.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11908/what-are-the-effects-of-different-feed-line-incidence-angles, by hotpaw2, Glenn W9IQ, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
