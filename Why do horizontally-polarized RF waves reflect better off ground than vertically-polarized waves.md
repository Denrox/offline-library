# Why do horizontally-polarized RF waves reflect better off ground than vertically-polarized waves?

*Tags: antenna-theory, hf, polarization · score 4*

## Question

It's a well-known fact among hams who use HF frequencies that horizontally-polarized RF waves reflect better off of ground than vertically-polarized waves. This explains why ground conductivity is so important to the performance of a vertical monopole antenna, and not as important for a horizontally-polarized antenna. Can someone explain, hopefully in layman's terms, why this is so?

I would also like to know why vertically-polarized waves propagate much better via ground-wave propagation than horizontally-polarized waves. My intuition tells me that this question is the other side of the same coin as the first question. (But my intuition is often wrong.) If the same explanation can easily answer both questions, great; if not, then I'll ask my second question separately.

## Accepted answer (score 6, by hobbs - KC2G)

It's a well-known fact among hams who use HF frequencies that horizontally-polarized RF waves reflect better off of ground than vertically-polarized waves. This explains why ground conductivity is so important to the performance of a vertical monopole antenna, and not as important for a horizontally-polarized antenna.

I don't think this is true. Actually, vertical and horizontal waves reflect from the ground about equally. The difference is that when a vertically-polarized wave reflects off of the ground, the reflected wave is *in phase* with the incident wave, but when a horizontally polarized-wave reflects off of the ground, the reflected wave is *180° out of phase* with the incident wave at that point. (This is the opposite of what my intuition tells me, but it's true.)

For a vertical monopole, the in-phase reflection is a good thing; it means that the reflected image of the antenna forms the "missing half" of a vertical dipole. If the ground was lossless, the signal reflecting off the ground at a given point would be exactly the same as if the ground didn't exist and the antenna continued below ground level. Since a vertical dipole has peak gain towards the horizon, this phenomenon makes DXers happy. Making the ground lossy is like putting a big resistor between the halves of this imaginary dipole (this is a cheap explanation but close enough for the moment) — it doesn't take very many ohms for the ground loss to start competing with the radiation resistance and eating most of your power. We use radials to artificially enhance the ground conductivity and decrease this loss.

For a horizontal antenna, the out-of-phase reflection from the ground is a mixed bag. In the case of a low dipole, once you get far away, the reflection and the original signal are basically "coming from the same place", so the in-phase original and the out-of-phase reflection add up and cancel out. A low dipole has maximum gain straight up, because that's the direction that maximizes the path length difference between the original and the reflected signal, so the phase difference at the receiver will be less than 180° and the cancellation will be less complete.

Once you raise the horizontally polarized antenna more than a quarter-wavelength above the ground, though, you make it so that there is some angle where the length of the reflected path to a distant point will be a *half wavelength longer* than the direct path to the same point. The 180° shift from the path length difference adds to the 180° shift from the reflection to give 360° (or 0°), which means the signal is reinforced instead of canceled. By placing an antenna at just the right height, you can make the ground contribute to DX performance instead of detracting from it.

So it's not that horizontal signals reflect better, it's that reflection is *less important* to the whole antenna system. A vertical antenna with no reflections is a dummy load. A horizontal antenna with no reflections is... just fine (the best the reflection could ever do is give you +3dB, and other times it's actively harmful). Horizontally polarized antennas still have to deal with induced ground losses if they're low, but that's not a question about *reflections*, and I've already said enough :)

I would also like to know why vertically-polarized waves propagate much better via ground-wave propagation than horizontally-polarized waves.

Ground waves propagate "half in and half out" of the ground. The portion of the wave that's underground travels slower than the portion that's above ground (dirt and rock and stuff has a higher dielectric constant than air), so the wave "bends down" and follows the curvature of the earth, allowing it go go beyond line of sight. But the ground loss is attenuating the signal as it goes, and at higher frequencies, the groundwave is completely dissipated before it goes any useful distance. Horizontally polarized signals don't propagate at all through groundwave because they can't be "half in and half out" in the same sense... any measured groundwave propagation of a horizontal signal is either direct-path (not groundwave), or groundwave propagation of a scattered vertically-polarized component (the signal bounced off of something that converted it to partially vertically polarized) or a residual vertically-polarized component (the antenna wasn't *perfectly* level to begin with, so a small fraction of its output is vert pol).

## Answer (score 4, by Richard Fry)

RE: *"I would also like to know why vertically-polarized waves propagate much better via ground-wave propagation than horizontally-polarized waves."*

This subject is treated in various textbooks relating to antennas and propagation. An example clip from one of them is shown below.

The last sentence in the column on the far right-hand side of the clip is especially relevant, here.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16859/why-do-horizontally-polarized-rf-waves-reflect-better-off-ground-than-vertical, by rclocher3, hobbs - KC2G, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
