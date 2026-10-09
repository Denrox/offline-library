# Is there a best ratio of L to C in a resonant circuit?

*Tags: electronics, oscillator · score 6*

## Question

When designing a resonant circuit, for example as a local oscillator, the product of $L$ and $C$ determine the resonant frequency according to $$f_{res} = \frac{1}{2\pi \sqrt{L C}}.$$

This means that we can reach a frequency of $7030 \text{ kHz}$ for example with

- $L = 2.33 ~\mu H$ and $C = 220~pF$, or
- $L = 23.3 ~\mu H$ and $C = 22~pF$, or
- $L = 513 ~nH$ and $C = 1~nF$, etc.

If we increase the inductance, the quality factor of the circuit should increase, since $$Q = \frac{X_L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}.$$

Does the quality of the $LC$ circuit continuously increase with increasing $L$, or is there a maximum that can be reached at some $L$-to-$C$ ratio? How do I find this ratio and wit this pick the best combination of $L$ and $C$ for my circuit?

## Accepted answer (score 7, by Glenn W9IQ)

There is no hard and fast rule. Consider that in some LC circuit applications, a lower Q may be desirable in order to achieve a wider bandwidth. In other cases, a very high Q may be desirable for narrow selectivity, for example.

Both the inductor and the capacitor in a resonant circuit may affect the Q of the circuit.

The Q of the inductor is determined by its inductive reactance divided by its series resistance.

$$Q_L=\frac{X_L}{R_L} \tag1$$

Since inductance is generally a factor of turns squared and since the resistance of the inductor is a factor of turns, this first order analysis indicates that the lower the inductor value for a given wire type/diameter and for a given construction method, the higher the Q of the inductor. The higher the Q of the inductor, the higher the Q of the resonant circuit.

The Q of a capacitor is determined by its capacitive reactance divided by its effective series resistance.

$$Q_C=\frac{X_C}{ESR_C} \tag2$$

In most practical cases, the ESR of the capacitor is a factor only in series resonant circuits. In a parallel resonant circuit, generally the series resistance of the inductor will dominate the Q.

In a series resonant circuit, the resistive losses of the inductor and capacitor are simply added. Since you quoted the formula for a series resonant circuit, this should be your approach.

$$Q=\frac{1}{R_L+ESR_C} \sqrt{\frac{L}{C}} \tag3$$

Before selecting a final inductor value, make certain that its self resonance will not negatively affect your circuit.

The insertion loss under this scenario is given as:

$$ \text{Insertion Loss} = 20\log\left({1-\frac{Q}{Q_L}}\right) \tag 4$$

where QL is as noted above and Q is the series circuit Q as noted in the equation in your question.

Other factors that may come into play, depending upon the application, are the inductance and the Q of the inductor over a wide frequency range; the stability of the capacitor over a wide temperature range; and the size, weight, tolerance, cost and availability of the components.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12284/is-there-a-best-ratio-of-l-to-c-in-a-resonant-circuit, by DK2AX, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
