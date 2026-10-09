# How to calculate or estimate surface area of required ground plane for a mobile antenna?

*Tags: antenna, mobile, antenna-theory, vertical-antenna · score 5*

## Question

I don't have conditions for installation of a fixed 2 m/70 cm antenna at home, so I'm thinking of using a mobile magnetically mounted antenna on a conductive plate instead.

So my question is: What are the rules of thumb for getting ground plane dimensions for a mobile antenna beyond "the bigger, the better"?

## Accepted answer (score 5, by Phil Frost - W8II)

What are the rules of thumb for getting ground plane dimensions for a mobile antenna beyond "the bigger, the better"?

There isn't one. An monopole antenna does not reach ideal performance until the ground plane is infinite, and the ground plane can be arbitrarily reduced in size and it will still work in theory (although at some point in practice, the feedline, or the Earth, becomes a better ground plane than the ground plane).

If you are making a mobile installation, then you don't have a lot of space, and you must necessarily make some compromises. However much space you have, make it that big.

If you must have a rule of thumb, a quarter wavelength is good. By this point you have most of the possible performance. If you want to be obsessive, you can go out to 1.5 wavelengths, which is typical of commercial AM broadcast stations.

Quarter-wave radials are also resonant (provided you don't bury them, or otherwise detune them), which assures that the radials have a low impedance. A low impedance is necessary for the ground plane to function as an effective counterpoise. Resonance is by no means necessary, however. Whatever impedance the radials have, it is halved each time the number of radials is doubled, so it ends up low anyway if you have many radials. If you don't have radials but instead a solid plane, this is equivalent to a very high number of radials so impedance will be low unless it is very tiny.

## Answer (score 2, by Greg)

Here is an excerpt from the Motorola radio install guide. Details the size of a ground plane for mobile radios installed in police/fire/etc vehicles.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2021/how-to-calculate-or-estimate-surface-area-of-required-ground-plane-for-a-mobil, by AndrejaKo, Phil Frost - W8II, Greg. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
