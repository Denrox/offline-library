# Why are hand-wound coils so common if commercial inductors are available?

*Tags: inductor · score 5*

## Question

In most schematics of ham radio receivers and transmitters the inductor is mostly given specifically as the number of turns around some certain toroidal ferrite ring (for example). This corresponds to a certain inductance, which more often than not is just a standard value, say 220uH. These exist also as "lumped element" components, like the ones in the picture:

It seems a precise inductance is quite difficult to achieve (with homemade coils) and measure, whereas with store-bought inductors this problem is largely gone.

Why are hand-wound inductors so common?

Is it just a nostalgia thing? Do they tolerate more power? Why don't we need to do this with capacitors as well?

## Answer (score 2, by Scott Earle)

There is also the matter of how much current the device needs to carry. A hand-wound coil made from a few turns of relatively heavy copper (compared to the off-the-shelf devices shown in the question) will pass a lot more current than a tiny pre-bought inductor. The ones in the picture look like 1/4W or so, but you could easily put 5W into a small hand-wound coil with the same inductance.

A hand-wound coil would also have a known (or at least calculated) Q, for which the circuit was designed.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12282/why-are-hand-wound-coils-so-common-if-commercial-inductors-are-available, by DK2AX, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
