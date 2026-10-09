# What is the peak voltage at the tips of a dipole antenna?

*Tags: antenna, antenna-theory, wire-antenna · score 20*

## Question

What is the peak voltage present at the very end tips of half-wave dipole antenna in free space, and how might this peak voltage relate to transmitter type, transmitter power, RF frequency vs. antenna half-wave frequency mismatch, feed line, SWR, wire diameter, and etc.

## Answer (score 18, by WPrecht)

I'm going to approach this a little differently starting from roughly the same place. Here I am going to use a resonant $\lambda$/2 20m dipole driven by 100 W as the model.

Let's compute the *current* at the feed point of a dipole at resonance, this is found with the input power (100 watts) and the feed point impedance; which for our dipole is assumed to be the theoretical 73 $\Omega$ :

$$ I = \left(\frac{W}{R}\right)^{\frac{1}{2}} = \left(\frac{100 \mathrm W}{73 \Omega}\right)^{\frac{1}{2}} = 1.17 \: \text{amps (RMS)} $$

Therefore the driving voltage can be calulated with Ohm's Law:

$$ V_\text{feed} = I \cdot R = 1.17 \mathrm A_\text{RMS} \cdot 73 \Omega = 85.44 \:\mathrm V_\text{RMS} $$ (unmodulated signal)

The voltage at the end of the dipole would require us to calculate the Q and solve the following:

$$ V_\text{end} = \frac{Q\:V_\text{feed}}{2} $$

Trying to minimize the hand-waving, we can use some approximations from transmission line theory to give us the Q. (See Edmund Laport's Radio Antenna Engineering for a complete (and math heavy) explanation) To do this we need the characteristic impedance of the dipole (considered as a transmission line). That is given by:

$$ Z_{0} = 276 \cdot \log_{10}\frac{l}{p} = 972.31 \Omega $$

Where $l$ is the total length of the dipole and $p$ is the radius of the conductor (all in the same units). I am going to ignore calculating the exact length here, we know it's approximately 5% shorter than the real wavelength to make up for velocity factor and end effects. This next bit leans on transmission line theory and can turn into a bag of snakes, if you want to know more about where these equations come from, check the reference quoted above. $Q$ here is the ratio of the voltage of the direct wave and the reflected wave:

$$ Q = \frac{1+m}{1-m} $$

and $m$ is calculated from the feed point impedance $R$ and the characteristic impedance $Z_0$:

$$ m = \frac{Z_0-R}{Z_0+R} $$

When I calculate $\ Z_0 $, I am going to assume our dipole is made with 3mm wire. Now to crank through the numbers:

$$ m = \frac{972\Omega-73\Omega}{972\Omega+73\Omega} = .86 $$

$$ Q = \frac{1+.86}{1-.86} = 13.29 $$

Now we can solve for $ V_\text{end} $:

$$ V_\text{end} = \frac{(13.29 \cdot 85.44 \mathrm V)}{2} = 568 \:\mathrm V_\text{RMS} $$

Again, this is the RMS voltage we should convert to peak voltage:

$$ 568 \:\mathrm V_\text{RMS} \cdot \sqrt{2} = \pm 804 \:\mathrm V_\text{peak} $$

This is all for 100W, if we instead plug 1500W into the above math, we come up with

$$ 4397 \:\mathrm V_\text{RMS} \:\text{or} \: \pm 6200 \:\mathrm V_\text{peak} $$

That's a pretty hefty jolt. So getting back to the OP's other questions, the input power has a substantial effect on the voltage. The rest of the factors are all the same as for maximizing antenna efficiency (resonance, conductor size, etc.)

**EDIT:** Most of the above equations come from the section on Circuital Design in the reference listed above. The book is more math heavy than typical amateur radio references, but not as bad as some of the more modern engineering texts. It's slow going, but a worthwhile read.

## Answer (score 7, by Phil Frost - W8II)

It's really hard to say, because it depends on so many things. Analyzing the antenna in free space simplifies some things, but we'd still have to consider the exact geometry of the antenna (How thick are the wires? Are they bent at all?) and the material from which they are made (any resistance will decrease the Q factor of the antenna, reducing the peak voltage).

However, if you look to analysis of end-fed dipoles, you can find that it's been determined empirically and by modeling that the impedance at the end of a real half-wave dipole is somewhere between 1800 to 5000 ohms.

Knowing this, we can calculate what the voltage is for a given power into the antenna. If we are putting 100W into the antenna, and we figure the impedance at the ends is 4000 ohms, then:

$$\begin{align} P &= V^2/R \\ 100\mathrm W &= V^2 / 4000\Omega \\ \sqrt{100\mathrm W \cdot 4000 \Omega} &= V \\ V &\approx 632 \mathrm V \end{align} $$

This is an RMS value. Knowing that our transmission is approximately sinusoidal, then the peak voltage is something like:

$$ 632 \cdot \sqrt{2} = \pm 894 \mathrm V $$

From the above equations, we can see that power is proportional to the square of voltage:

$$ P \propto V^2 $$

This is the power delivered to the antenna. Transmitter type and the match to the antenna (SWR) are relevant only to the extent that they change the power delivered to the antenna.

This is all assuming that the antenna is operated at resonance. As the frequency moves away from resonance, the peak voltage decreases. The reason why is simple: this high voltage is attainable because each cycle reinforces the previous. If you take a limiting case where the antenna is operated at DC, the voltage at the ends is equal to the voltage at the feedpoint, because there is no resonance to reinforce the voltage at the ends.

## Answer (score 2, by Cecil - W5DXP)

For those of you with EZNEC or some other antenna modeling software, there is a way to answer this question using EZNEC. Model a 1/4WL stub in free space taking care not to violate any geometry checks. Put a 100w source at one end of the stub and a 10 megohm load at the other end of the stub. Adjust the stub length and user defined wire loss to obtain the resistive feedpoint impedance of a dipole looking into the stub. Then display the load data. It will tell you the voltage at the end of a dipole. I set my 4 MHz stub for 70 ohms and got 879 volts across the 10 megohm load resistor. The additional user defined wire loss is equivalent to the power lost from the dipole through radiation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1410/what-is-the-peak-voltage-at-the-tips-of-a-dipole-antenna, by hotpaw2, WPrecht, Phil Frost - W8II, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
