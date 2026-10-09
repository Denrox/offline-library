# The right antenna size

*Tags: antenna, dipole, math · score 3*

## Question

I'm preparing for the USA Technician exam and I was reading in the manual that the ideal size for a dipole is following this strange formula: 1/2-lambda. But based on what I read after, it seems it means 1/2*lambda. Is it right ? And does it mean that each dipole spoke is 1/4*lambda ? Then that would mean you can only emit frequencies that are harmonics to that lambda ?

Thanks,

Nicolas

## Answer (score 5, by mike65535)

The classic dipole is a half-wave antenna. This means that the total length of the antenna is lambda/2. So writing it as 1/2-lambda is OK from an English language point of view, but not IMO as a rigorous mathematical formula.

For a half-wave dipole, each side of the feedpoint is one-half of that or a quarter-wave.

## Answer (score 4, by Mike Waters)

If you make a dipole exactly a half-wavelength long, then it will be too long and out of resonance.

The formula for determining the length of a half-wavelength dipole in feet is 468÷frequency in MHz. That's shorter than the actual wavelength in free space which is 492÷MHz.

## Answer (score 3, by Glenn W9IQ)

There are already a couple of nice answers to your question. I thought I would add a little more context - no need to vote for this as it is tangential to the question.

A 1/2 wavelength (1/2 $\lambda$) long dipole is one of the most basic and easy to deploy antennas. It is popular because when it is cut and fed in the center, it very closely matches the impedance of the most popular transmission line - 50 ohm coax. This helps to minimize power lost in the coax as a result of a mismatch. Such a mismatch is also the cause of elevated SWR (standing wave ratio).

The wire on each side of the feed point of a dipole is called a "leg". In the case of a 1/2 $\lambda$, center fed dipole each leg is 1/4 $\lambda$.

The length of a dipole is not limited to 1/2 $\lambda$. If the dipole becomes significantly shorter than 1/2 $\lambda$, the mismatch to the transmission line becomes high and so the losses in the transmission line go up. The antenna also becomes inefficient in itself which results in more power converted to heat and less radiated as electromagnetic energy.

A dipole longer than 1/2 $\lambda$ can also be used. In fact, a dipole that is 10/8 $\lambda$ will actually have more gain than a 1/2 $\lambda$ dipole. The disadvantage is that it takes a little more work to make it a match for 50 ohm coax. Dipoles longer than 10/8 $\lambda$ can be used as well but they will generally not offer any more gain.

In recent years, there has been a great deal of interest in feeding a dipole at a spot other than its center. So called OCF (off center fed) dipoles offer the possibility of a multi-band dipole with reasonable matching to 50 ohm coax. Typically it is a 1/2 $\lambda$ or slightly longer dipole for the lowest frequency of interest and then at higher frequencies, it simply acts as a >1/2 $\lambda$ dipole.

Other dipoles get specific names due to their historical references such as the double Zepp (from its Zeplin origins), extended double Zepp, a doublet, the G5RV, etc. Some of these designations may also imply the use of an open wire feedline instead of coax. But in the end, they are simply another form of a dipole.

Then there is the so called "End Fed Half Wave" (EFHW) antenna. This is a piece of wire that is the length of a 1/2 $\lambda$ dipole but instead of being split somewhere to create a feed point, it is left as one solid piece of wire and the coax is attached to the end. This is a very misunderstood antenna by many hams. It takes careful construction and installation techniques to achieve performance comparable to a center fed 1/2 $\lambda$ antenna. Many of these antennas are used in a multiband configuration. Their popularity is due to the convenience of feeding it from one end.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11887/the-right-antenna-size, by Nicolas Dufour, mike65535, Mike Waters, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
