# Is this transmission line peak voltage formula published in CQ Magazine more accurate?

*Tags: impedance-matching, transmission-line, lightning · score 4*

## Question

In his July 2018 article in CQ magazine entitled “Lightning (and EMP) Surge Protection for HF Radios”, Steven Karty, N5SK based much of his analysis for properly specifying a GDT (Gas Discharge Tube) on an equation used by Huber+Suhner (S+H) and further promulgated by Peter Sypher, KC4SI in a paper entitled “An Improved Formula for Peak Voltage Calculation in an RF Transmission Line” dated 17 May 2017.

The formula championed by the article is:

$$V_{peak}=\sqrt{2Z_OP_{out}}*(1-\rho_L) \tag 1$$

where ZO is the characteristic impedance of the transmission line, Pout is the output power of the transmitter and $\rho_L$ is the reflection coefficient of the load.

In the N5SX article, the author took exception to a peak voltage equation referenced by K5PA in a July/August 2016 QEX article entitled “Radio Frequency (RF) Surge Suppressor Ratings for Transmissions into Reactive Loads”. The KC4SI paper also takes exception to this equation. The K5PA equation, often shown in ARRL publications and so referenced by K5PA, is:

$$V_{peak}=\sqrt{2Z_OP_{out}SWR} \tag 2$$

The author states that formula 2 is less accurate than formula 1. Is this correct?

## Answer (score 2, by Glenn W9IQ)

Equation 1 as proposed in the article has two primary shortcomings:

1. It does not address losses in the line. As a result, the formula may overstate the maximum peak voltage.
2. It requires that ZG (the output impedance of the generator) closely matches the ZO. This is rarely the case except in a controlled lab environment. As a result, the equation generally understates the maximum peak voltage.

Since the use of equation 1 was centered upon selecting an appropriate GDT for lightning/EMP protection, shortcoming #2 is the most significant since this may cause the GDT to fire under normal operating conditions.

Here is a practical example which illustrates shortcoming #2:

*Consider a ½ wavelength transmission line with a ZO of 50+j0 ohms (therefore lossless). At the end of this transmission line is a 150+j0 ohm load. At the other end of the transmission line is a 100 watt output transmitter connected to a properly adjusted, lossless impedance matching circuit (the antenna tuning unit or ATU). Since the transmission line is ½ wavelength long, the input impedance of this length of transmission line is also 150+j0 ohms. A properly adjusted ATU will therefore transform the output impedance of the transmitter to 150+j0 ohms, providing a conjugate match to deliver the maximum available power to the load. Since the condition of maximum power transfer has been satisfied, 100 watts is applied across the input impedance of the transmission line.*

Using a derivation of Ohm’s law, the peak voltage is given as:

$$V_{peak}=\sqrt{2Z_OP_{out}}=173.2 \text{ volts} \tag 3$$

Whereas equation 1 would predict:

$$V_{peak}=\sqrt{2*50*100}*(1-0.5^2)= 150 \text{ volts}$$

This represents a greater than 15% error in this case. Most concerning is that the error underestimates the maximum voltage, defeating the very purpose of referencing the equation - to properly size a GDT.

The fundamental cause of this error is due to the failure to account for the additional reflection coefficient caused by the ZG (output impedance of the generator) not matching the ZO of the transmission line. This additional reflection coefficient will cause a reflection from the load, arriving at the source, to be partially (in this case) reflected back toward the load. These reflections continue as an infinite series. The voltage reflections from the generator that are additive to the load voltage reflections increase the peak voltage on the line.

If we now apply the above example to equation 2, the result is:

$$V_{peak}=\sqrt{2Z_OP_{out}SWR}=173.2 \text{ volts}$$

which is the correct result. However, equation 2 has the following shortcomings:

1. The equation is quite accurate for low loss lines when ZG=ZIn but in all other cases, it will overstate the maximum peak voltage
2. In the case of higher loss transmission lines, the equation can overstate the peak maximum voltage even when ZG=ZIn. This is mitigated by measuring the SWR at a point near the generator.
3. For large values of SWR, the results become dubious. As SWR approaches infinity, the term under the radical approaches infinity. Clearly this would exceed all practical limitations of the generator. The significance of this shortcoming cannot fully quantified as it largely depends upon various parameters of the generator such as open circuit voltage, output impedance, protection circuits, etc.

**Conclusion**

Equation 1 is accurate for a lossless transmission line when the impedance of the generator matches the characteristic impedance of the transmission line. This would be the case in a controlled lab environment. When equation 1 is used with a configuration that includes a properly adjusted ATU, it will exhibit the following error:

Equation 2 is accurate for a lossless transmission line when the impedance of the generator matches the input impedance of the transmission line. This would be the case when a properly adjusted ATU at the transmitter end is used. When formula 2 is used with a configuration in which the generator impedance matches the characteristic impedance of the transmission line, it will exhibit the following error:

A more general formula that lacks the simplicity of the above formulas but works in any ZG to ZO or Zin relationship as well as for low loss lines is:

$$V_{peak}=\frac{1+\rho_Le^{-2\gamma l}}{1-\rho_Le^{-2\gamma l}\rho_G}\frac{\sqrt{2P_GZ_G}}{Z_G+Z_O}2Z_O \tag 4$$

where $\rho_G$ is the generator reflection coefficient, $\gamma$ is the complex propagation coefficient of the transmission line and l is the length of the line as measured from the load to the generator.

Equation 4 assumes that the generator behaves as a Thevenin source. This may not always be the case, especially if the generator has an SWR protection (foldback) feature and more generally for higher SWRs.

This Q&A has been extracted from a white paper written by W9IQ as a result of communications with the author of the CQ article. This whitepaper is available from W9IQ upon email request.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11692/is-this-transmission-line-peak-voltage-formula-published-in-cq-magazine-more-a, by Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
