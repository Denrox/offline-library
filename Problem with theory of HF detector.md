# Problem with theory of HF detector

*Tags: diy, electronics, measurement, theory, swr-meter · score 5*

## Question

I'm currently trying to build my own SWR power Meter. This design is based on the so known HT detector with schottky diode BAS70. For my understanding, and for easy purpose, I'm currently focusing on 50 MHz.

First, I found a nice theory called "The Square Law Region" which can be found here on page 115 of the book Radio Frequency & Microwave power measurement.

It says that voltage out of the HF detector is $$V=\frac{25e}{kTn}P_{RF}$$

where $e$ is the charge of an electron ($-1.602 \times 10^{-19}$ C), $k$ is the Boltzmann constant $1.38064852 \times 10^{-23} m^2 kg \cdot s^{-2} K^{-1}$, $T$ the temperature in degrees Kelvin, $n$ the ideality factor, and $P_{RF}$ the power in Watts.

I found that Spice says $n=1.018$ for BAS70 diode. If my calculation is correct, for P = -30dBm (1µW) lead to out voltage to 950µV. Is that correct?

At 50MHz, with BAS70, 47nF, it tried this set up...my measure leads to about 10mV...wich is far away for...let's say 1mV of theory. Is this theory correct ?

Then I also tried to set up in simulation with Qucs. I faced another problem: Qucs failed to simulate this situation.

First, I must say that I see different delay of response regarding the input level. For +10dBm, voltage out tends to 1.5V in about 300µS. For -30dBm, voltage is not stable before 1mS (see jpg joined file). I understand that it could come from the time needed by capacitor...but also, timing response should not depend on the input level for a basic RC filter. Right?

What should I do to simulate my HF detector at low level?

## Answer (score 3, by Ryuji AB1WX)

I can’t see exactly what you did—your link to the book is restricted, and your GitHub repo has vanished like a magician’s rabbit. So, I’m stuck relying on textbook assumptions.

Here’s the deal: the voltage at the detector output depends on a few players other than the BAS70—load resistance, input power at a 50-ohm line, the diode’s saturation current (think reverse bias leakage), and that good old $V_{T} = kT/q$, which is 26mV at 300K.

$$ i_{D} = I_{S} \exp(\frac{v_{s}}{\eta V_{T}} -1) $$

The square law detector? It’s straightforward stuff, in theory. Derived from the Shockley equation and a MacLaurin series expansion, it starts simple. The zeroth-order constant term gets killed by Shockley's -1. Gone. The first-order term is just RF feedthrough, swept away by the RC network like solder crumbs off a bench. The quadratic term? That’s the juicy part.

The RF input, being a sinusoid, gets squared and, through the magic of trig identities, splits into DC and second harmonic bits. We care only about the DC bit—the flavorful one.

$$ V_{L} = \frac{I_{S} R_{S} R_{L}}{(\eta V_{T})^2} P_{S} $$

Now, when I ran the numbers (-30dBm, 10mV, 50$\Omega$ source impedance, $I_{S} \approx 10^{-7}$), I got a load impedance in the ballpark of 1 M$\Omega$. Maybe you skipped explicitly loading the detector? Pro tip: slap on a load resistor (10k or 100k ohms, say) to make math and life easier.

As for Qucs? No clue. It’s like trying to speak Estonian without ever hearing it spoken.

Now, the square law detector works beautifully only when the input power is so small that MacLaurin's third-order term stays asleep. But crank the power—somewhere around -20 or -10dBm—and that pesky third-order wakes up. Then, the detector flips jobs and becomes an envelope detector. At that point, the output stops caring about proportionality and does its own thing.

Oh, and about response times? Those depend on the RC filter’s time constant, the R of which, in turn, depends on the diode’s equivalent series resistance at the operating point. More power means less resistance, and less resistance means the detector starts reacting like a caffeinated squirrel. Faster, but not always better.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16499/problem-with-theory-of-hf-detector, by F4BJH, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
