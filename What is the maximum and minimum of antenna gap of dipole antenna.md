# What is the maximum and minimum of antenna gap of dipole antenna?

*Tags: antenna, antenna-theory, antenna-system · score 3*

## Question

Consider the picture below is design of half wave length (λ) dipole antenna. I read some explanations saying that it is the best design to get the optimum transmit power. Half wave length (λ) is from tip to the tip of the two elements (you know it).

But my concern here is, what is the minimum or maximum distance of the gap as in the picture? Gap between the two elements which the feeder line is connected? Some say that it should be as small as possible. But unfortunately, I don't have mathematical justification for that reason even it make sense. I expect that the explanation is in λ. But if you really need the used frequency, then just put 2,100 MHz. If needed, the feeder line is RG6 75 ohm.

## Answer (score 2, by Aleksander Alekseev - R2AUK)

The gap is neglectable in terms of λ. Let's say you are making a 20m (14 MHz) dipole and you decided to use a large gap, let's say 10cm. This is only 0.0005λ. For 2m band (144Mhz) it's 0.005λ. If you choose an even larger gap it means there will be some wires that will connect the arms of the dipole to the feed line. These wires will just work as parts of the arms. Once again - there is no significant gap except the distance between the center of the coax and the shield of the coax.

In other words just connect the arms to the coax the way it's comfortable and then trim the length of the arms to get minimum SWR in the center of the band.

[Richard Fry is the author of the following paragraph and graphic.] Below is a NEC4.2 study of a 40m, 1/2WL, center-fed, free space dipole with a 0.2m gap for an insulator at the feedpoint. NEC sources themselves are applied at a single point on a conductor, but this approach or a variation of it might lead to a reasonable, practical solution for most amateur radio operators and applications.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15038/what-is-the-maximum-and-minimum-of-antenna-gap-of-dipole-antenna, by Sitorus, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
