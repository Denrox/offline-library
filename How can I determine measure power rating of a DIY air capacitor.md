# How can I determine/measure power rating of a DIY air capacitor?

*Tags: diy, capacitance · score 5*

## Question

I've build an air capacitor like the one described in this article, although I used 1 mm thick single side copper boards (FR4) instead of solid copper sheets. I would like to use such capacitors in my next projects, e.g. an antenna tuner and a magnetic loop antenna.

The problem is - I have no idea what is the maximum transmit power I can use with such capacitors. How would you recommend to measure it? Or maybe there is a common knowledge that such capacitors can handle power up to X (25 W, 100 W, ...) without any problems?

## Accepted answer (score 6, by Glenn W9IQ)

Congratulations on your home brew project! It is great to see experimentation of this type.

The two primary parameters for a capacitor are working voltage and ESR (effective series resistance), with the former being of primary interest in this case. How much power can be applied to a circuit containing a capacitor is a derivative of these parameters and of other elements in the circuit.

**Working Voltage**

The working voltage of a capacitor is determined primarily by the dielectric strength of the materials making up the capacitor and the construction details. In your case, this will consist primarily of the dielectric strength of FR4 material, the dielectric strength of air, and the construction details of your capacitor.

FR4 material is typically rated at 20 kV/mm. So your 1 mm thick FR4 material will breakdown (conduct) at approximately 20 kilovolts. But there are some caveats that must be taken into consideration. If you look at the cut edge of copper clad FR4 under magnification, you would see that some of the copper has been formed so as to wrap over the edge of the FR4 material. The dielectric strength of this area is no longer based on the dielectric strength of the FR4 but rather that of air. For a variable capacitor, even if the edge copper is carefully controlled, there will still be an effective air gap as the edges of the rotor and stator meet as they start to mesh. The edges of the copper also create an enhanced potential gradient. If the board is etched, instead of cut, so as to leave a perimeter of FR4 material around the rotor or stator, this condition can be better controlled.

Dry, room temperature air at sea level has a dielectric strength of approximately 3 kV/mm. Notice that this is about 1/7th of that of FR4. So unless your design is carefully controlled so as to ensure a pure FR4 interface at all times, it is better to use the 3 kV/mm value as a breakdown voltage.

When calculating a working voltage for a capacitor, consider that if the breakdown voltage is met or exceeded, it results in a catastrophic event. So typically you should build in at least a 50% safety factor to allow for construction tolerances, variation in humidity and altitude, etc. Also consider that when working with AC/RF voltages, the values are typically expressed as RMS voltages. For the capacitor, you are more concerned with peak voltages. For sinusoidal voltages:

$$V_{Peak}=V_{RMS}\sqrt{2} \tag 1$$

**Effective Series Resistance**

The ESR becomes a significant factor if the capacitor is passing large amounts of current or if the ESR is large enough so as to appreciably affect the Q of the circuit. This is typically not the case for variable capacitors. If you are interested in the more complex math for calculating ESR, indicate so in your comments and I will supplement this answer with those details.

**Power vs Voltage**

The power that can be applied to a circuit containing a capacitor is largely of matter of the other elements in the circuit. For example, a simple small loop antenna used on HF frequencies with only 100 watts of applied power can easily develop more than 5 kV across the tuning capacitor. The same type of situation can arise in an antenna tuner application.

To work through the math of a particular circuit, see this [StackExchange Question and Answer](Series%20resonant%20circuit%2C%20how%20to%20calculate%20voltage%20across%20the%20capacitor.md).

**Testing Your Design**

If you wish to do some non-destructive testing of your capacitor, search out a hipot tester. The hipot tester will limit, or terminate, the current if a voltage breakdown occurs allowing you to better quantify the voltage characteristics of the capacitor.

## Answer (score 2, by user10489)

Maximum amperage of the capacitor may also be limited by the smallest feed wire in the path and by the thickness and width of the metal in the plates of the capacitor, and possibly the skin depth of the components as well. (In other words, if the skin depth for the frequency you are using is too close to the thickness of the metal in your plates, the effective resistance will increase.)

Making any of these too small will effectively raise the resistance and ESR of the capacitor under high amperage conditions.

## Answer (score 2, by Marcus Müller)

To expand on Glenn's answer:

The ESR, i.e. the losses in your capacitor that aren't caused by ohmic heating of the copper but by conversion of change of electrical field to heat in the dielectric (i.e. the FR4 and air) can be written as

$$\text{ESR} = \frac{\tan \delta_\text{FR4}}{\omega C}$$

with $\tan \delta\approx 0.01$ being the material loss coefficient specific to (good) FR4, $\omega = 2\pi f$ being the angular frequency of operation and $C$ being capacity.

Now, what *is* your $C$? I can only guess that. Based on the (slightly disappointing) 220pF: if you manage to replace all air in that capacitor with FR4, you should be getting around 4.2 to 4.7 times that capacitance (that factor happens to be the relative dielectric constant $\varepsilon_r$ of FR4), so about 1 nF.

Assuming you operate this thing at 100 MHz, $\omega = 628\cdot 10^6 \,\text{s}^{-1}$.

Putting this all together:

\begin{align} \text{ESR} &= \frac{10^{-2}}{628\cdot 10^6 \,\text{s}^{-1} 10^{-9} \frac{\text{As}}{\text V}}\\ &= \frac{10^1}{628}\frac{\text{V}}{\text{A}}\\ &= 0.016 \,\text{Ω} \end{align}

FR-4 has a heat capacity of ca. 1300 J/°K, meaning that you can pour in about 1/4 of the energy that you'd need to put into water to heat by the same temperature.

That's nice, because you wouldn't want to heat your capacitor to more than 100°C, for touching as well as mechanical reasons (and things get dangerous at around 140°C), so simply don't put in more energy than you'd put into a cup of water ¼ the size to make that boiling hot.

So, to heat a cup of tea (that's my weight estimate for your cap, you notice how much I'm guessing here) to near-to-boiling hot, I'd put it onto a 160 W stove. So, 40 W in dielectric losses seems pretty safe for your capacitor.

That's the inherent downside of using a dielectric in your variable capacitor: Hot air simply escapes; your dielectric can't.

The big advantage is that air can't store much electrical field energy; its $\varepsilon_r$ is pretty much 1. The higher that, the smaller a capacitor of identical capacitance can get.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12323/how-can-i-determine-measure-power-rating-of-a-diy-air-capacitor, by Aleksander Alekseev - R2AUK, Glenn W9IQ, user10489, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
