# How would I calculate antenna gain?

*Tags: antenna, antenna-theory, j-pole, gain · score 8*

## Question

The concept of antenna gain is pretty important for calculation of link budget and is something I've had contact with. I know that it tells me how focused the waves emitted by the antenna are and I know how to read antenna gain charts.

What I don't know is how to calculate antenna gain for a given antenna.

So what are the general steps required in order to calculate antenna gain?

If it matters, I'd like to calculate gain of a J-pole antenna, but I'd like to keep this question general, if possible.

**UPDATE:** Just to be clear, what I really want to know is how to actually do the calculations, not just how to use already calculated results. I do expect the "perfect" answer to be extremely long and complicated. Because of that, I'm willing to accept answers which list the necessary steps and provide information in which direction I should do research next for the required steps.

## Answer (score 7, by Phil Frost - W8II)

So what are the general steps required in order to calculate antenna gain?

In the general case, calculating the gain requires solving Maxwell's equations, for whatever antenna geometry you have.

It's exceptionally hard, and no one does it without the assistance of a computer, except for very simple antennas, such as dipoles. For these simple antennas, you can find the solutions at places like antenna-theory.com.

For arbitrary antennas, the solution usually involves breaking the antenna into a large number of smaller conducting elements connected together, then using the boundary element method to solve the underlying equations. A number of popular implementations are based on NEC.

Gain can also be determined empirically. In practice, this is how it's frequently done, because it is more accurate. The antenna is placed in an anechoic chamber and fed with a known power. A field strength meter is then moved around the antenna, and these readings compared to the theoretical field strength at the same distance of an isotropic radiator. The ratio of these is the antenna gain.

## Answer (score 3, by Rory Alsop)

Interestingly, while in an ideal world a J-Pole will perform exactly like a half-wave dipole (as it is one), in reality the configuration of your build makes gain incredibly difficult to calculate.

This great page at w8ji.com shows field charts for J-Poles with small differences in build where the low angle gain can vary by 5dB. They do state though:

None of this means the J-pole won't work, have a low SWR, and make contacts. It simply shows the pattern is unpredictable because the feedline, mast, and grounding significantly affects performance.

So you should work under the assumption that your J-Pole will be not quite as good as a half-wave dipole and go with that.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1519/how-would-i-calculate-antenna-gain, by AndrejaKo, Phil Frost - W8II, Rory Alsop. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
