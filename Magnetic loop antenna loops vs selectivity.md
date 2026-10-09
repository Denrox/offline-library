# Magnetic loop antenna : loops vs selectivity

*Tags: antenna, antenna-theory, antenna-construction, magnetic-loop · score 3*

## Question

I've built 2-turn magnetic loop RX antenna using 5 meters of 6.5mm copper tube. I was able to tune it with a variable air-spaced capacitor in the range of 1.8-10Mhz, but I noticed that as tuning frequency goes to 7MHz and above - selectivity gets less significantly, reception peak gets wider and much less visible (around 300-500kHz wide, which is extremely wide for magloop as far as I understand). Tried 2 different variable capacitors - result is the same. Everything is soldered.

I assume there is an optimal length of the loop / number of turns to get the highest selectivity. But how to identify this optimal number of loops / length of 1 loop?

What causes this drop of Q-factor / selectivity at higher frequencies, where capacitor value gets smaller than ~20pF?

## Accepted answer (score 4, by user10489)

The ideal length of a small loop is 1/10 wavelength to 1/4 wavelength.

Below 1/10 wavelength, the gain drops too much and the bandwidth starts to become unreasonably narrow.

Above 1/4 wavelength, the antenna stops acting like a small loop and becomes more like a halfwave or full wave loop and the selectivity drops and the radiation pattern changes drastically and the impedance changes drastically.

7MHz is roughly 40m, making a 5m loop 1/8 of a wavelength. 10MHz is roughtly 30m, 5m is 1/6 wavelength.

## Answer (score 7, by Phil Frost - W8II)

Two factors explain the wider bandwith:

Firstly, as the frequency increases, bandwidth will necessarily increase even if the Q factor remains constant. There are a number of ways to define Q factor, but the result is the same so consider this definition:

$$ Q = {f_r \over \Delta f} $$

rearranged:

$$ \Delta f = {f_r \over Q} $$

So as $f_r$ (the resonant frequency) increases, $\Delta f$ (the bandwidth) must increase as well if $Q$ is constant.

Secondly, as frequency increases the loop becomes larger relative to the wavelength. This increases the radiation resistance, which increases the damping, reduces $Q$, and increases bandwidth.

Intuitively, consider what happens as the loop continues to get larger: eventually it becomes a full-wave loop or some kind of stretched-out folded dipole, and at this point the bandwidth is relatively large.

If the objective is maximum selectivity, the theoretically optimal size of the loop is infinitesimal, because this maximizes the reactance of the antenna and minimizes the damping. Of course practial issues in utilizing infinitesimal antennas, so in practice the optimal size is "as small as possible."

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16420/magnetic-loop-antenna-loops-vs-selectivity, by BarsMonster - R2AYN, user10489, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
