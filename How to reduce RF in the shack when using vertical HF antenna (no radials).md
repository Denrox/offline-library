# How to reduce RF in the shack when using vertical HF antenna (no radials)

*Tags: hf, vertical-antenna, rfi · score 11*

## Question

What can be done to reduce RF in the shack (riding back along the coax) when using a vertical 10M antenna (without radials due to space constraints)? The antenna is an IMax-2000 at 32' elevation (20' over roof) with a 125' coax LMR-400, SWR is under 1.5 across 10M band. No balun, no tuner. Cable length is required to reach the shack room (basement). Max power 100 W with interference level increasing with greater power output.

This is causing interference with capacitive touch lamps (on, off on transmit); as well as causing speakers around the house (even when turned off) to broadcast the operator's voice (a ghoulish combination with the flickering lights).

The height of the mast was adjusted from 1' to its present 32' over ground level, with no change to SWR or interference as described above. The mast was tried with and without grounding (to an 8' ground rod at its base), no effect to SWR or interference level.

## Accepted answer (score 15, by Phil Frost - W8II)

You may be surprised to hear this, but the antenna you describe isn't *actually* a vertical, but a dipole. One half of the dipole is the IMax-2000, and the other half is your feedline.

You can not simply not have radials and still have an antenna. An antenna works by making EM fields between two things. A dipole has two halves. A vertical works because the ground plane under it creates an image antenna under it, making it appear as a dipole.

To get the RF currents off of the feedline, you have to give it some other place to go. You could:

- install a dipole
- install elevated radials
- mount the vertical on the ground

You can also put a high impedance on the feedline to make that path less desirable to RF currents. An easy and effective way to do this is to slip ferrite beads over the coax. However, if you don't first provide a more desirable place for them to go, then you are just putting ferrite beads on your antenna, which will reduce the RF in the shack, and also everywhere else.

I would also point out that a SWR of 1.5:1 does not in itself indicate that the antenna is working well. SWR only indicates that that the antenna is decently matched to the feedline, and thus accepting (and not reflecting) power: it doesn't indicate that the power accepted is actually being radiated as intended. One way to make an antenna get a good match across a wide band is to make it very lossy. As an extreme example, I have a dummy load that has a 1:1 SWR from DC up to beyond the capability of my test equipment.

## Answer (score 3, by Ron J. KD2EQS)

(a partial self-answer)

Bad grounding on the mast was part of the problem. After reconnecting the ground wire to ensure a clean contact on both mast end and ground rod - the blinking lights stopped. The RF return was almost eliminated (slight deflection on FS meter against coax but I think that is to be expected).

Per Phil Frost's answer, I believe the shack ground was providing a better RF ground since the mast was improperly grounded, causing the RF to ride back indoors. Once connections were sandpapered and tightened to the outside grounding rod, it took the shorter route to ground.

Update after getting my General and attempting to go beyond the 10m band with this vertical antenna. Testing SWR on 12m (SWR 1:2) and 17m (SWR 1:3) both resulted in the same common current RF problem - and the lights getting turned on and off. Will update again after I try using an antenna tuner.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/601/how-to-reduce-rf-in-the-shack-when-using-vertical-hf-antenna-no-radials, by Ron J. KD2EQS, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
