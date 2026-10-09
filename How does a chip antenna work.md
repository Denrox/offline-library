# How does a "chip antenna" work?

*Tags: antenna, antenna-theory · score 10*

## Question

How does a tiny surface-mount "chip antenna" for the 2.x thru 5.x GHz frequency bands work? What allows such a tiny item to radiate or receive RF with some amount of efficiency? What allows a chip antenna's radiation pattern to be (somewhat?) non-directional compared to a wire antenna?

## Accepted answer (score 7, by OH2FXN)

The chip antennas use some material, usually ceramic, that has high permittivity and low losses. In a medium having high permittivity, the wavelength is shorter than in the free space. This way the antenna "sees" the structure that is comparable in the size to the wavelength in the medium, while being very small compared to the free space wavelength.

While receiving, the antenna efficiency is not very crucial parameter since less efficient antenna receive less signal but also less noise from the environment. Thus the signal to noise ratio is the same at the output of the antenna. See the related questions: [What is the relationship between SWR and receive performance?](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md) and [If two antennas of 50 Ω and 377 Ω have VSWR=1:1, then which one is more efficient?](If%20two%20antennas%20of%2050%20%CE%A9%20and%20377%20%CE%A9%20have%20VSWR%201%201%2C%20then%20which%20one%20is%20more%20efficient.md)

Generally, small antennas tend to be less directive: for example, large dishes have higher gain than Yagis that, in turn, have higher gain than dipoles. Based on empirical googling, the chip antenna manufacturers seem to promise gains approximately in the range of 0...3 dBi. However, with high permittivity substrate you can achieve large gains as well: http://iopscience.iop.org/1347-4065/53/4S/04EL09/article

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1700/how-does-a-chip-antenna-work, by hotpaw2, OH2FXN. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
