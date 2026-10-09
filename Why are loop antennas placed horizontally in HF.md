# Why are loop antennas placed horizontally in HF

*Tags: antenna, hf, magnetic-loop · score 3*

## Question

I am thinking of a large (circumference $\approx \lambda$) loop antenna at low (HF) frequencies. At higher frequencies the loops are used as quad antennas that have relatively high gain towards the axis of the loop. However, at HF band these are often positioned horizontally above the ground. One would think that the ground would act as a reflector and the power would be directed upwards which is obviously undesired. Are the reasons purely mechanical or is there some other reason to use horizontal loops instead of vertical ones?

## Accepted answer (score 4, by Phil Frost - W8II)

I suspect they are built horizontally simply because they are easier to construct and support, especially at HF sizes.

Due to constantly changing ionospheric conditions, the received phase of HF signals is random, so that's not a reason to prefer any particular polarization.

Further, the ground does affect radiation patterns, but it's not so simple as "reflecting" RF energy straight up. Were this the case, dipoles also wouldn't work. What the ground actually does is create an image antenna as if a second antenna appeared reflected through the ground, fed in opposite phase. This can result in peak radiation in [many patterns](What%20causes%20ground%20losses%20in%20a%20HF%20antenna%20system.md), depending on antenna height.

There is also some folk-wisdom that [horizontally-polarized antennas are quieter](Is%20a%20vertical%20noisier%20than%20a%20dipole%2C%20and%20if%20so%2C%20why.md). I think the magnitude of this effect is much less than the belief in it, but even if the technical foundations are weak, it is a reason for human behavior anyway.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1106/why-are-loop-antennas-placed-horizontally-in-hf, by OH2FXN, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
