# How does this W6NBC "derivative of the classical slot antenna" work?

*Tags: antenna-theory, mobile, vertical-antenna · score 5*

## Question

Via the [https://ham.stackexchange.com/a/9883/1362](Slot%20antenna%20for%202%20meter%20mobile.md) answer regarding a slot antenna for a 2m mobile application, I was introduced to this (pdf) interesting antenna design:

The designer John Portune (W6NBC) introduces it as "a derivative of the classical slot antenna" but then notes:

In contrast to a conventional slot antenna, the slot and antenna surfaces are not in the same plane. The slot, formed by the aluminum shorting bars connecting the two antenna surfaces, is orthogonal to the two planes.

Should the explanations on [How does a slot antenna work?](How%20does%20a%20slot%20antenna%20work.md) still apply to this slot antenna "derivative", or are the variations significant enough to warrant a different analysis?

In particular, a commenter on this site expressed skepticism regarding the efficiency of this design ("an extremely short vertical radiator with a large capacitor") which to me sounds like the design could be functioning more as a "dual" of a *loading coil*, rather than as the dual of a dipole like a true slot antenna?

## Answer (score 4, by tomnexus)

The antenna is most like a Planar Inverted F Antenna, or PIFA. Wikipedia has a brief introduction to them. Here is my sketch of a classic example:  
The PIFA is a wider bandwidth version of the IFA, distinguished by a radiator parallel to the ground (the upright of the F), a shorting bar at one corner or edge (the top of the F) and the feed a short distance away from it (the middle of the F).

The inductance of the short circuit compensates for the capacitance of the shortened antenna. The radiation resistance of a short or low antenna is usually quite small, but the parallel inductance raises it to 50 Ohms when properly designed.

The IFA or PIFA is unbalanced and easy to feed with coax from below the groundplane.  
It's a good antenna for a mobile phone, it can be made a lot smaller than a quarter wave in any dimension, as long as the groundplane is a reasonable size. It is quite efficient unless made extremely small or with lossy material (PCB...) but tends to radiate in all directions, not just around the car like a monopole. They can be made dual- or tri-band by cutting various slots into the top of the F, though the radiation patterns of those modes are even more strange.

Here are a few photos of IFAs and PIFAs as used on mobile phones, (scraped from patent documents so in the public domain)  
  
A google image search turns up lots of good examples too.

The QST antenna has two shorting pins at opposite corners; this could still be considered to be two slots, with one of them fed directly and the other coupled somehow.

This all said, there are many antenna geometries which defy simple explanation, but still work well. Any unconnected metal part, or gap in a metal part, can be fed in a way that will radiate, and if the structure is reasonably large it will make a fine antenna. Antennas that have become popular are usually valued as much for their mechanical simplicity and reliability as their electrical performance.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17141/how-does-this-w6nbc-derivative-of-the-classical-slot-antenna-work, by natevw - AF7TB, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
