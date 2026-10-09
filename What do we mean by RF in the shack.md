# What do we mean by "RF in the shack"?

*Tags: coaxial-cable, balun, antenna-system · score 3*

## Question

What does "RF in the shack" mean? How does it interfere with devices around coax?

## Accepted answer (score 3, by K7PEH)

RF in the shack refers to the EM radiation that comes off of the outside of the conductor (usually) of coaxial cable. Coaxial cable is actually three conductors: center conductor, inside of the braided shield conductor, outside of the braided shield conductor. Due to the "skin effect" RF currents are limited to a thin outer layer of a conductor. This allows for the current to be separate on the inside and outside of the braided shield conductor.

Current on the outside of the shield can easily radiate and even act like an antenna. Other conductors that are close to this coaxial cable in the shack are affected and you can build up a potential that results in RF "shocks or burns" merely by touching metal objects. When I was a young kid back in 1961 or 1962 I had such a strong RF in the shack condition that when I keyed down I could light up the florescent lights hanging from the ceiling (my shack was in the garage).

This outer conductive current is known as a "Common Mode" current and is usually produced from an imbalance in the antenna system. One typical imbalance is connecting coaxial cable directly to a Dipole Antenna. A Dipole Antenna is a balanced antenna and coaxial cable is unbalanced so that results in currents flowing in Common Mode on the outside of the shield conductor.

The solution to resolve this problem and eliminate the common mode currents is to use a choke balun between the antenna and the coaxial cable. Alternatively, you can use balanced transmission like, such as 450 ohm ladder line and that can attach (in the shack to a balanced load antenna tuner which then acts like a choke balun or a current balun (aka choke) which allows you to then attach coaxial line.

If you do use 450-ohm ladder line you will have a mismatch between the Dipole antenna and the transmission line and this mismatch results in reflections. This is not too much of a problem in itself since ladder line is low-loss however you do have to match this to your transmitting equipment, nominally at 50 ohms, which will require a tuned circuit such as an antenna tuner or coupler circuit. The variable control of an antenna tuner is much nicer to adjust for match at various frequencies (or, even various bands).

For example, I use an 80-meter dipole antenna on bands 80, 40, and 30 meters. Most of my transmission line, about 80 feet, is 450 ohm ladder line. Just outside of the shack it interfaces with the balanced side of a 4:1 transforming balun (from DX Engineering) and then coaxial cable (LMR400) the remaining 15 feet to my KAT500 (Elecraft) antenna tuner.

Common mode currents radiate so this is the cause of the primary problems resulting in both "RF in the shack" but also altered radiation patterns from the interference with the antenna itself. I have modeled this condition using NEC4 (mathematical modeling software), to observe the actual impact and in a worse case (although, with high power), it can create nulls in your radiation pattern where you don't expect them (on the broadside of a dipole antenna) in certain physical arrangements of the antenna and feed line.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6416/what-do-we-mean-by-rf-in-the-shack, by Aparna B, K7PEH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
