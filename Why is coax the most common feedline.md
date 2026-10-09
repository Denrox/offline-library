# Why is coax the most common feedline?

*Tags: feed-line, coaxial-cable · score 5*

## Question

Why is coaxial cable the most common feedline in use? What are the advantages/ disadvantages of coax compared to other feedline types?

From test pool question: T9B03

## Accepted answer (score 4, by Phil Frost - W8II)

At most amateur radio frequencies, there are really only two feedline types that are readily available and effective:

1. twin-lead
2. coaxial

The goal of the feedline is to move electromagnetic energy from one end to the other without much loss. This means not absorbing it, and not radiating it.

Not absorbing EM energy is pretty easy. Use good conductors, like copper, and low-loss dielectrics, like PTFE or air.

Not radiating is harder. EM energy consists of electric and magnetic fields that *want* to radiate. You have to somehow have fields in the cable (because this is the energy you want to move) but not everywhere else. So you somehow have to make opposing fields that cancel each other everywhere outside your feedline.

Twin-lead does this in a pretty simple way: because each of the conductors carry equal and opposing currents ([or it should, if the station is operating properly](Using%20a%20balun%20with%20a%20resonant%20dipole.md)), they make equal and opposing fields. If you are far away from the cable, then the two conductors are close enough together that they mostly cancel each other out. There is no field far away from the cable, i.e., it doesn't radiate.

This is also the problem with twin-lead. If there is a significant difference between the distances to the two conductors, then you aren't far enough away for the fields to have canceled. If you are a conductive material, your charges will be pushed around by these fields, and you will alter the electrical properties of the cable, and your own electrical properties will be altered. If you are, for example, another feedline, your signal will be coupled with the signal in the other feedline. Further, the characteristic impedance of each feedline will likely be altered, making it harder to match to the transmitter, resulting in a poor SWR.

Consequently, when installing twin-lead, one must mount the feedline in such a way that it doesn't come close (relative to the spacing of the conductors) to anything conductive. Usually this means running it up the tower and into the shack with stand-offs:

*(from Stark Electronic)*

In practice, this can be a real pain. How do you get it through the wall? What if there are two antennas on the tower? What if you have a rotator? What if it snows?

Coax solves this problem. The shield acts as a Faraday cage, entirely containing the electric field between the shield and the center conductor. Thus, coax can be installed directly on a tower, bundled with other coax feedlines, or buried without significantly altering its properties. The disadvantage is a higher cost, as the coax geometry is more difficult to manufacture, and requires more copper.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/766/why-is-coax-the-most-common-feedline, by JC Hulce, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
