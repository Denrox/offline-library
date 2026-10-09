# Relation between antenna physical size and gain

*Tags: antenna-theory, gain · score 3*

## Question

I would like to know whether increasing the size of the antenna help increase its gain. Does this hold only for certain kinds of antennas like parabolic or horn antennas? And if it is true, can you please provide a solid paper reference?

## Answer (score 6, by Phil Frost - W8II)

Gain and size are correlated, but not rigorously.

For example, a Beverage antenna is larger than a half-wavelength dipole, but has lower gain. The Beverage does however have higher directivity.

Another example, a Hertzian dipole is a theoretical antenna that's infinitesimal, and yet has only very slightly less gain than a half-wave dipole. It's efficiency however is a different story: as a dipole gets smaller its impedance becomes more reactive, thus necessitating a matching network that must deal with more reactive power and associated loss.

Extending a dipole beyond a half-wavelength does increase gain, but not usually in a very useful way: the pattern grows a bunch of lobes pointing in weird directions. For most antennas we want orderly lobes pointing in useful directions, maybe one specific direction or maybe we want to direct radiation at the horizon but not so much up or down.

These are examples that are contrary to the typical correlation. A final example that is more typical is a phased array, like a Yagi. Adding more elements to a Yagi increases the gain, and the Yagi is usually designed so all the gain goes towards a large forward lobe with minimum gain in any other direction.

It is however important that the elements are correctly positioned and phased. Adding more elements to an array and incorrectly phasing them can result in an array that's no better than, or perhaps worse than a single element.

It's worth considering two points:

1. Gain is the product of directivity and efficiency. A Beverage has low gain and high directivity because it has low efficiency.
2. If the efficiency is already as high as it can be made practically, then the only way to increase gain is to increase directivity, and that usually requires making the antenna larger. A higher directivity means higher gain in the intended direction, but necessarily a lower gain in some other direction. This is a simple consequence of energy conservation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16518/relation-between-antenna-physical-size-and-gain, by ResearcherW, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
