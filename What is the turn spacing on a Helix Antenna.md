# What is the turn spacing on a Helix Antenna?

*Tags: antenna-theory, antenna-construction, satellites · score 3*

## Question

I want to do some satellite communication so I thought why not build my own helix antenna.

I found this page:

Helix antenna design and construction details

The most things are clear except for the turn spacing.

My guess is that it gives a divisor of the wavelength which is used for one turn of the helix.

But I don't know, after some thinking, that this makes no sense because the wave length is given by the frequency and the turns are given as a separate input.

## Accepted answer (score 6, by Glenn W9IQ)

During his long career, J.D. Kraus studied, and experimented extensively with, helix antennas. There is a large body of published work in college text books on this subject. The following summarizes some of the key construction details.

The ideal circumference of each turn of the helix antenna is given as:

$$C=\lambda \tag 1$$

where $\lambda$ is the free space wavelength of the frequency for which the antenna is designed.

The circumference of a circle is related to diameter by:

$$D=C/\pi \tag 2$$

Substituting equation 2 into equation 1, we have the diameter of each helix turn:

$$D=\lambda/\pi \tag 3$$

The distance between each turn of the helix is given as:

$$S=0.225\lambda \tag 4$$

Kraus found that an optimum reflector for a helix fed with 50 ohm coax cable is a metalic cup with a diameter of 0.75$\lambda$ and a rim around the cup with a height of 0.375$\lambda$. The helix is centered inside the cup with the center of the coax attached to the helix through a hole in the bottom of the cup and the shield of the coax connected to the cup.

The cup can be used to fix non-conductive supports for the helix in order to improve the mechanical rigidity.

The number of turns control the half power beamwidth (HPBW) and thus the directivity and gain of the helix. The HPBW in degrees is approximated as:

$$\text{HPBW}\cong\frac{52}{C_\lambda \sqrt{nS_\lambda}} \tag 5$$

where n is the number of turns.

For example, a 16 turn helix constructed with the above dimensions will result in a HPBW of ~26° and with efficient construction >15 dBi gain. The polarization will be nearly circular.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10127/what-is-the-turn-spacing-on-a-helix-antenna, by maxbit89, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
