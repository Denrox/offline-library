# Resistive impedance with frequency

*Tags: antenna, impedance · score 4*

## Question

Full disclosure, I'm a little dyslexic. Concepts that are easy to most people usually seem ambiguous to me. I also have a had time expressing myself through writ so please forgive me if this seems like an odd question.

I've been reading my ARRL hand book and many items on the internet in an attempt to form a good working understanding of antennas. I think I may have finally grasped it but I want to check it against a human who can give me and clear answer.

I'll post a hypothetical:

Say I have a stationary dipole and my antenna analyzer gives me a reading of 100 +j12 Ω at it's resonant frequency. I want to match it to my 50Ω unbalanced feed line so I place both a capacitor that gives -j12Ω at the resonant frequency, and a 1:2 balun at the feed point.  
Now lets say I want to go off the resonant frequency, this will change the reactive component of the impedance and my conjugate -j12Ω will no longer perfectly match the antenna. But, will the 1:2 balun still correct for the resistive portion of the impedance just as it did at resonance?

I think what I'm trying to ask is, will the resistive impedance change with frequency as the reactive impedance does? That seems like such a simple question but I have not been able to find a clear answer to it which leads me to believe It's a bad or meaningless question like "whats the color of the number two". I honestly can't tell.

.

## Accepted answer (score 4, by Phil Frost - W8II)

If you antenna were actually a *resistance*, then the impedance would not change with frequency. Resistance is anything that obeys Ohm's law:

$$ V = I R $$

A real example that you may encounter is a dummy load. These are just a $50\Omega$ resistor, which provides a $(50 + 0j)\Omega$ over a broad range of frequencies (ideally, all frequencies).

Antennas are not just a simple resistance. Rather, they are a complex impedance. Antennas are complex to analyze, so let's first consider a simpler circuit, the LC circuit. Here's one such circuit:

What is the impedance of this circuit? Well, the impedance of a capacitor is:

$$ Z_C = -j\frac{1}{\omega C} $$

And an inductor:

$$ Z_L = j \omega L $$

$\omega$ is the angular frequency, which is just $\omega = 2\pi f$. It's just a different way of expressing frequency that doesn't require the equations to contain a $2\pi$ term all over the place.

Series impedances add, so the impedance of this series circuit is:

$$ -j\frac{1}{\omega 50\cdot 10^{-9}} + j \omega 10.3\cdot 10^{-9} $$

If we pick some frequency, we can simplify this more. Let's try $f=10\:\mathrm{MHz}$, or equivalently $\omega=2\pi 10\:\mathrm{MHz} \approx 62831853$:

$$ -j\frac{1}{62831853 \cdot 50\cdot 10^{-9}} + j 62831853 \cdot 10.3\cdot 10^{-9} \\ = -j0.3183 + j0.6472 \\ = (0+j0.3289) \Omega $$

If we try again at 7 MHz, we get a slightly different answer. I won't write out all the math, but the answer is $(0-j0.0017)\Omega$. In fact, if we pick just the right frequency, then the impedances of the capacitor and the inductor cancel, and the circuit looks like a dead short. But only at that one frequency.

This is what we are doing when we tune the antenna: by adjusting the length of the antenna or changing the operating frequency, we are trying to find the point where the reactive components (capacitance and inductance) of the antenna cancel.

But wait, what antenna looks like a dead short? Any effective antenna will have another impedance in the circuit, the radiation resistance. If electrical power is the product of current and voltage, then we need to both move a current, and move it against some voltage, to do work. If we are radiating energy, then against what is the transmitter working? Radiation resistance is that thing.

The radiation resistance looks like a resistor to the transmitter, but unlike a resistor it doesn't get hot because the energy is radiated away. Calculating the radiation resistance in general involves solving Maxwell's equations for your antenna and all the space around it. That's hard, but we can find solutions for common antenna types. For example, antenna-theory.com gives the radiation resistance of a short dipole as:

$$ R_{rad} = 20\pi^2 \left(L\over\lambda\right)^2 $$

This is for a *short* dipole, which is one that is less than a tenth of a wavelength long, which allows us to make the simplifying assumption of constant current throughout the entire antenna. Usually we use half-wave dipoles which are not short so this simplification does not apply, and the equation is more complex. However, notice there is a wavelength ($\lambda$) term in the equation, which means radiation resistance is frequency dependent.

So, as you can see, every term that goes into calculating an antenna impedance is frequency dependent. Even though the real part of the complex impedance is sometimes called the "resistive" part, this means it looks like a resistance at that one frequency. It does not mean it is a resistance, which is frequency independent.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2435/resistive-impedance-with-frequency, by Turingrad, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
