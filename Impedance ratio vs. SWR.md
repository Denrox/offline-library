# Impedance ratio vs. SWR

*Tags: impedance, impedance-matching · score 9*

## Question

The specs of the Elecraft T1 tuner say, that it can match a 10:1 SWR.

- What does that mean in terms of impedance ratio?
- What antenna impedance can it match to 50 Ohm then?
- Or is it not that easy?

## Accepted answer (score 4, by Marcus Müller)

Short detour:

There's a so-called *reflection coefficient* $\Gamma$ that says "OK, for this mismatch, so and so much of the power is reflected back where it came from".

We can calculate it as, based on load impedance $Z_L$ and conduction line impedance $Z_0$:

$$ \Gamma =\frac{Z_L - Z_0}{Z_L + Z_0}$$

Also, the VSWR is a *result* of things getting reflected back:

\begin{align} \DeclareMathOperator{\vswr}{VSWR} \vswr &= \frac{1+\lvert\Gamma\rvert}{1-\lvert\Gamma\rvert}\\ &\implies\\ \lvert\Gamma\rvert &= \frac{\vswr-1}{\vswr +1}\\ &\iff\\ \left\lvert\frac{Z_L - Z_0}{Z_L + Z_0} \right\rvert &=\frac{\vswr-1}{\vswr +1} \end{align}

Assuming $Z_L>Z_0$:

\begin{align} \frac{Z_L - Z_0}{Z_L + Z_0} &=\frac{\vswr-1}{\vswr +1}&& \lvert\vswr=10, Z_0 = 50\,\mathrm\Omega\\ &=\frac{9}{11}\\ &\implies\\ \frac{Z_L - Z_0}{Z_L + Z_0} - \frac9{11} &= 0 && \lvert\cdot (Z_L+Z_0)\\ 0 &=Z_L - Z_0 - \frac9{11}(Z_L + Z_0) \\ &=\frac2{11}Z_L -\frac{20}{11}Z_0 &&\lvert\cdot11:2\\ &=Z_L -10 Z_0\\ Z_L&= 10 Z_0 \\ &= 500\,Ω \end{align}

Assuming $Z_L<Z_0$:

\begin{align} \frac{Z_0 - Z_L}{Z_L + Z_0} &=\frac{\vswr-1}{\vswr +1}&& \lvert\vswr=10, Z_0 = 50\,\mathrm\Omega\\ &=\frac{9}{11}\\ &\implies\\ \frac{Z_0 - Z_L}{Z_L + Z_0} - \frac9{11} &= 0 && \lvert\cdot (Z_L+Z_0)\\ 0 &=Z_0 - Z_L - \frac9{11}(Z_L + Z_0) \\ &=\frac2{11}Z_0 -\frac{20}{11}Z_L &&\lvert\cdot11:2\\ &=Z_0 -10 Z_L\\ \frac1{10}Z_0&= Z_L \\ &= 5\,Ω \end{align}

So, 5 Ω to 500 Ω are "specification-wise" matchable.

This is assuming a *real-valued* antenna impedance. That's often not given. For the complete region of applicable values, see (and upvote!) Cecil's answer.

However, impedance matching doesn't happen on a "reflection coefficient level"; it happens by having an adjustable matching network (typically takes the shape of an adjustable LC filter). Things actually get rather interesting there, because the matches you get from that typically aren't wideband and typically aren't all real and typically aren't all within a "nice" shape in the real world. So, assuming the best, the SWR range is but a thing that the manufacturer has tested to work, and special complex impedances outside the circle from Cecil's answer can be matched too.

## Answer (score 10, by Cecil - W5DXP)

As you can see from the following equation, it is definitely not that easy. What I would do is draw a 10:1 SWR circle on a Smith Chart and assume that your tuner can match all of the infinite number of impedances inside that 10:1 SWR circle. If you don't know how to read impedances from a Smith Chart, it would be worth your while to learn how. The green area below on the Smith Chart normalized to 50 ohms is the advertised matching range for your tuner.

## Answer (score 2, by Scott Earle)

When a tuner in a radio says it can match 3:1 and below, they sometimes say that it can match 16.7-150 ohms.

I would take this to mean that a tuner that can match 10:1 and below, can match 5-500 ohms.

There is an example of a tuner that can match some bands to 10:1 on this page. they specify:

**FrequencyTypical Matching Range and Power Limit**

3 — 30 MHz 600W into 5 to 500 Ohms (10:1 SWR)

 1000W into 16 to 150 Ohms (3:1 SWR )

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14665/impedance-ratio-vs-swr, by Dominik Heidler, Marcus Müller, Cecil - W5DXP, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
