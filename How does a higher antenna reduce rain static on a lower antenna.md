# How does a higher antenna reduce rain static on a lower antenna?

*Tags: antenna, antenna-system, qrn · score 4*

## Question

I have operated at several stations - including my own - where a 40m beam is stacked above a tribander. During a rain storm, there is so much QRN on the 40m beam that the band is unusable, but the tribander seems unaffected. Conversely, a nearby tribander without a beam stacked above it is similarly useless due to QRN.

Are precipitation discharges being re-radiated out of phase from the upper antenna in the stack and cancelling the discharges in the lower antenna?

## Accepted answer (score 4, by Mike Waters)

Among other things, rain and cloud droplets interacting with each other causes a voltage gradient in the air, similar to the Kelvin water drop experiment explained here and here), with the earth being the lowest potential and increasing with height.

The noise on the highest antenna is because there is a corona (like St. Elmo's fire) emanating from sharp points on that highest antenna -which is at ground potential- to the higher voltage gradient in the air. Therefore, eliminating or covering those sharp points or edges will reduce or eliminate the corona noise. A *sharp point* could be threads, the ends of metal tubing, or sharp edges. Ideally, the ends of the boom and elements would have metal spheres or insulating caps.

But there's a better way.

As W8JI points out in his page about precipitation static, there should be a sharp, grounded point above the highest antenna, like a lightning rod. Afraid that it will attract lightning? :

My physics teacher taught that if a lightning conductor actually did "conduct" a lightning strike then it would have failed in its job. Its job, he taught, was to prevent a strike from ever occurring by dissipating the charge in the atmosphere above the conductor, thereby causing the lightning to strike elsewhere. ...

It does dissipate the charge from the ground to the atmosphere. This is fact as current can be measured flowing up through the lightning rod to the atmosphere. Any current flow will reduce the potential difference between the ground and charges in the sky thus lessening the probability of a strike. This reduction in potential also will weaken any strike that does occur (not by much but it will weaken it none the less).

**TL;DR:** Put up a "lightning rod" above your highest antenna to eliminate the noise; that will now become your "highest antenna".

**REF:** https://physics.stackexchange.com/questions/65825/does-a-lightning-rod-prevent-lightning-strikes

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15129/how-does-a-higher-antenna-reduce-rain-static-on-a-lower-antenna, by Brian K1LI, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
