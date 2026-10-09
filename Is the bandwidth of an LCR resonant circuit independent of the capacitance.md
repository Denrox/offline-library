# Is the bandwidth of an LCR resonant circuit independent of the capacitance?

*Tags: frequency, impedance, bandwidth · score 8*

## Question

Is the bandwidth of an LCR resonant circuit independent of the capacitance, if the inductance and its series resistance are kept the same, and the Q is high?

This question and the calculation associated with it were originally posted by a radio amateur Anthony G3LAA, who deserves credit for spotting it.

At resonance the reactances of L and C are the same and Q is equal to that reactance divided by the series R of the inductor. If we take Q equal to f0/B where B is the bandwidth, and substitute the usual formulae for Q and the resonant frequency f0 in terms of L, C and R,then C cancels out and we are left with B proportional to 1/L. This is true, for all practical purposes (fapp) at moderate frequencies for both series and parallel circuits, and implies that changing the C in the LCR circuit, although this changes the resonant frequency, the bandwidth remains constant.

I realise that there are a lot of simplifying assumptions in the formulae, both electrical and mathematical, but, fapp, this looks correct to me. Please, am I right?

It has an obvious practical advantage in, say, a TRF receiver, with fixed inductance and a variable capacitor to do the tuning, keeping the bandwidth constant over the tuning range.

(The following is added in response to @Phil Frost's comment, thanks.)

Here is the maths — I assume that the formulae for $Q$, $\omega_0 = 2\pi f_0$ and bandwidth, are familiar enough not to need explanation, except that I use $B$ for bandwidth and brevity. I also accept that the formulae depend on many simplifying assumptions, but, fapp, they are good enough, for high $Q$, above about 10.

$$Q = \frac{1}{\omega_0RC} = \frac{\omega_0L}{R}$$

Reactances equal at resonance, $Q$ is reactance over $R$.

$$\omega_0=\frac{1}{\sqrt{LC}} \tag{1}$$

Substituting for $\omega_0$ in each $Q$ formula we get:

$$Q=\frac{\sqrt{LC}}{RC} = \frac{L}{R} \cdot \frac{1}{\sqrt{LC}}$$

Both of these simplify to

$$Q=\frac{1}{R}\sqrt{\frac{L}{C}} \tag{2}$$

For bandwidth $B$ (frequency difference at half power level) we have $Q=\omega_0/B$ or

$$B=\frac{\omega_0}{Q} \tag{3}$$

Substituting in (3) for $\omega_0$ from (1) and $Q$ from (2) we finally get

$$B = \frac{1}{\sqrt{LC}}\cdot R\cdot\sqrt{\frac{C}{L}}$$

which simplifies to $B=R/L$ i.e. Bandwidth is independent of the capacitor value over the range of resonant frequencies for the inductor.

Is this correct? I now think so and will give that as an answer

## Accepted answer (score 0, by Harry Weston)

I am now convinced that the maths is correct,

Thank you @Kevin, for tidying it all up. I was going to transfer the maths here as an answer, but I will leave it in the question

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1517/is-the-bandwidth-of-an-lcr-resonant-circuit-independent-of-the-capacitance, by Harry Weston. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
