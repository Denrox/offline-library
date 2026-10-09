# Decibel

- decibel
- Unit system Non-SI metric unit
- Symbol dB
- Named after Alexander Graham Bell
- Conversions
- 1 dB *in ...* *... is equal to ...*
- bel  0.1 bel

The **decibel** (symbol: **dB**) is a relative unit of measurement equal to one tenth of a **bel** (**B**). It expresses the ratio of two values of a power or root-power quantity on a logarithmic scale. Two signals whose levels differ by one decibel have a power ratio of 10 (approximately 1.26) or root-power ratio of 10 (approximately 1.12).

The strict original usage above only expresses a relative change. However, the word decibel has since also been used for expressing an absolute value that is relative to some fixed reference value, in which case the dB symbol is often suffixed with letter codes that indicate the reference value. For example, for the reference value of 1 volt, a common suffix is "V" (e.g., "20 dBV").

As it originated from a need to express power ratios, two principal types of scaling of the decibel are used to provide consistency depending on whether the scaling refers to ratios of power quantities or root-power quantities. When expressing a power ratio, the corresponding change in decibels is defined as ten times the logarithm with base 10 of that ratio. That is, a change in *power* by a factor of 10 corresponds to a 10 dB change in level. When expressing root-power ratios, a change in amplitude by a factor of 10 corresponds to a 20 dB change in level. The decibel scales differ by a factor of two, so that the related power and root-power levels change by the same value in linear systems, where power is proportional to the square of amplitude.

The definition of the decibel originated in the measurement of transmission loss and power in telephony of the early 20th century in the Bell System in the United States. The bel was named in honor of Alexander Graham Bell, but the bel is seldom used. Instead, the decibel is used for a wide variety of measurements in science and engineering, most prominently for sound power in acoustics, in electronics and control theory. In electronics, the gains of amplifiers, attenuation of signals, and signal-to-noise ratios are often expressed in decibels.

### Definition

- dB   Power ratio   Amplitude ratio
- 100   10000000000     100000
- 90   1000000000     31623
- 80   100000000     10000
- 70   10000000     3162
- 60   1000000     1000
- 50   100000     316  .2
- 40   10000     100
- 30   1000     31  .62
- 20   100     10
- 10   10     3  .162
- 6   3  .981 ≈ 4   1  .995 ≈ 2
- 3   1  .995 ≈ 2   1  .413 ≈ √2
- 1   1  .259   1  .122
- 0   1     1
- −1   0  .794   0  .891
- −3   0  .501 ≈ ⁠1/2⁠   0  .708 ≈ ⁠1/√2⁠
- −6   0  .251 ≈ ⁠1/4⁠   0  .501 ≈ ⁠1/2⁠
- −10   0  .1   0  .3162
- −20   0  .01   0  .1
- −30   0  .001   0  .03162
- −40   0  .0001   0  .01
- −50   0  .00001   0  .003162
- −60   0  .000001   0  .001
- −70   0  .0000001   0  .0003162
- −80   0  .00000001   0  .0001
- −90   0  .000000001   0  .00003162
- −100   0  .0000000001   0  .00001
- An example scale showing power ratios *x*,  
amplitude ratios √*x*, and dB equivalents 10 log10 *x*

The IEC Standard 60027-3:2002 defines the following quantities. The decibel (dB) is one-tenth of a bel: 1 dB = 0.1 B. The bel (B) is ⁠1/2⁠ ln(10) nepers: 1 B = ⁠1/2⁠ ln(10) Np. The neper is the change in the level of a root-power quantity when the root-power quantity changes by a factor of *e*, that is 1 Np = ln(e) = 1, thereby relating all of the units as nondimensional natural *log* of root-power-quantity ratios, 1 dB = 0.11513... Np = 0.11513.... Finally, the level of a quantity is the logarithm of the ratio of the value of that quantity to a reference value of the same kind of quantity.

Therefore, the bel represents the logarithm of a ratio between two power quantities of 10:1, or the logarithm of a ratio between two root-power quantities of √10:1.

Two signals whose levels differ by one decibel have a power ratio of 10, which is approximately 1.25893, and an amplitude (root-power quantity) ratio of 10 (1.12202).

The bel is rarely used either without a prefix or with SI unit prefixes other than *deci*; it is customary, for example, to use *hundredths of a decibel* rather than *millibels*. Thus, five one-thousandths of a bel would normally be written 0.05 dB, and not 5 mB.

The method of expressing a ratio as a level in decibels depends on whether the measured property is a *power quantity* or a *root-power quantity*; see *Power, root-power, and field quantities* for details.

#### Power quantities

When referring to measurements of *power* quantities, a ratio can be expressed as a level in decibels by evaluating ten times the base-10 logarithm of the ratio of the measured quantity to the reference value. Thus, the ratio of *P* (measured power) to *P*0 (reference power) is represented by *L**P*, that ratio expressed in decibels, which is calculated using the formula: $$L_P = \frac{1}{2} \ln\!\left(\frac{P}{P_0}\right)\,\text{Np} = 10 \log_{10}\!\left(\frac{P}{P_0}\right)\,\text{dB}$$

The base-10 logarithm of the ratio of the two power quantities is the number of bels. The number of decibels is ten times the number of bels (equivalently, a decibel is one-tenth of a bel). *P* and *P*0 must measure the same type of quantity, and have the same units before calculating the ratio. If *P* = *P*0 in the above equation, then *L**P* = 0. If *P* is greater than *P*0 then *L**P* is positive; if *P* is less than *P*0 then *L**P* is negative.

Rearranging the above equation gives the following formula for *P* in terms of *P*0 and *L**P*: $$P = 10^\frac{L_P}{10\,\text{dB}} P_0$$

#### Root-power (field) quantities

When referring to measurements of root-power quantities, it is usual to consider the ratio of the squares of *F* (measured) and *F*0 (reference). This is because the definitions were originally formulated to give the same value for relative ratios for both power and root-power quantities. Thus, the following definition is used: $$L_F = \ln\!\left(\frac{F}{F_0}\right)\,\text{Np} = 10 \log_{10}\!\left(\frac{F^2}{F_0^2}\right)\,\text{dB} = 20 \log_{10} \left(\frac{F}{F_0}\right)\,\text{dB}$$

The formula may be rearranged to give $$F = 10^\frac{L_F}{20\,\text{dB}} F_0$$

Similarly, in electrical circuits, dissipated power is typically proportional to the square of voltage or current when the impedance is constant. Taking voltage as an example, this leads to the equation for power gain level *L**G*: $$L_G = 20 \log_{10}\!\left (\frac{V_\text{out}}{V_\text{in}}\right)\,\text{dB}$$ where *V*out is the root-mean-square (rms) output voltage, *V*in is the rms input voltage. A similar formula holds for current.

The term *root-power quantity* is introduced by ISO Standard 80000-1:2009 as a substitute of *field quantity*. The term *field quantity* is deprecated by that standard and *root-power* is used throughout this article.

#### Relationship between power and root-power levels

Although power and root-power quantities are different quantities, their respective levels are historically expressed in the same units, typically decibels. A factor of 2 is introduced to make *changes* in the respective levels match under restricted conditions such as when the medium is linear and the *same* waveform is under consideration with changes in amplitude, or the medium impedance is linear and independent of both frequency and time. This relies on the relationship $$\frac{P(t)}{P_0} = \left(\frac{F(t)}{F_0}\right)^2$$ holding. In a nonlinear system, this relationship does not hold by the definition of linearity. However, even in a linear system in which the power quantity is the product of two linearly related quantities (e.g. voltage and current), if the impedance is frequency- or time-dependent, this relationship does not hold in general, for example, if the energy spectrum of the waveform changes.

For differences in level, the required relationship is relaxed from that above to one of proportionality (i.e., the reference quantities *P*0 and *F*0 need not be related), or equivalently, $$\frac{P_2}{P_1} = \left(\frac{F_2}{F_1}\right)^2$$ must hold to allow the power level difference to be equal to the root-power level difference from power *P*1 and *F*1 to *P*2 and *F*2. An example might be an amplifier with unity voltage gain independent of load and frequency driving a load with a frequency-dependent impedance: the relative voltage gain of the amplifier is always 0 dB, but the power gain depends on the changing spectral composition of the waveform being amplified. Frequency-dependent impedances may be analyzed by considering the quantities power spectral density and the associated root-power quantities via the Fourier transform, which allows elimination of the frequency dependence in the analysis by analyzing the system at each frequency independently.

#### Conversions

Since logarithm differences expressed in these units often represent power ratios and root-power ratios, values for both are shown below. The bel is traditionally used as a unit of logarithmic power ratio, while the neper is used for logarithmic root-power (amplitude) ratio.

Conversion between units of level and a list of corresponding ratios
- Unit  In decibels  In bels  In nepers  Power ratio  Root-power ratio
- 1 dB  1 dB  0.1 B  0.11513 Np  10 ≈ 1.25893  10 ≈ 1.12202
- 1 B  10 dB  1 B  1.151 3 Np  10  10 ≈ 3.162 28
- 1 Np  8.68589 dB  0.868589 B  1 Np  e ≈ 7.38906  e ≈ 2.71828

#### Examples

- Calculating the ratio in decibels of 1 kW (one kilowatt, or 1000 watts) to 1 W yields: $$L_G = 10 \log_{10} \left(\frac{1\,000\,\text{W}}{1\,\text{W}}\right)\,\text{dB} = 30\,\text{dB}$$
- The ratio in decibels of √1000 V ≈ 31.62 V to 1 V is: $$L_G = 20 \log_{10} \left(\frac{31.62\,\text{V}}{1\,\text{V}}\right)\,\text{dB} = 30\,\text{dB}$$

(31.62 V / 1 V) ≈ 1 kW / 1 W, illustrating the consequence from the definitions above that *L**G* has the same value, 30 dB, regardless of whether it is obtained from powers or from amplitudes, provided that in the specific system being considered power ratios are equal to amplitude ratios squared.

- The ratio in decibels of 10 W to 1 mW (one milliwatt) is obtained with the formula: $$L_G = 10 \log_{10} \left(\frac{10\text{W}}{0.001\text{W}}\right)\,\text{dB} = 40\,\text{dB}$$
- The power ratio corresponding to a 3 dB change in level is given by: $$G = 10^\frac{3}{10} \times 1 = 1.995\,26\ldots \approx 2$$

A change in power ratio by a factor of 10 corresponds to a change in level of 10 dB. A change in power ratio by a factor of 2 or ⁠1/2⁠ is approximately a change of 3 dB. More precisely, the change is ±3.0103 dB, but this is almost universally rounded to 3 dB in technical writing. This implies an increase in voltage by a factor of √2 ≈ 1.4142. Likewise, a doubling or halving of the voltage, corresponding to a quadrupling or quartering of the power, is commonly described as 6 dB rather than ±6.0206 dB.

Should it be necessary to make the distinction, the number of decibels is written with additional significant figures. 3.000 dB corresponds to a power ratio of 10, or 1.9953, about 0.24% different from exactly 2, and a voltage ratio of 1.4125, about 0.12% different from exactly √2. Similarly, an increase of 6.000 dB corresponds to a power ratio of 10 ≈ 3.9811, about 0.5% different from 4.

### Properties

The decibel is useful for representing large ratios and for simplifying representation of multiplicative effects, such as attenuation from multiple sources along a signal chain. Its application in systems with additive effects is less intuitive, such as in the combined sound pressure level of two machines operating together. Care is also necessary with decibels directly in fractions and with the units of multiplicative operations.

#### Reporting large ratios

The logarithmic scale nature of the decibel means that a very large range of ratios can be represented by a convenient number. For example, 50 dB is easier to say than "the two powers bear a 100,000 to 1 ratio" or that "one power is 10 the other". Decibels express huge changes of a quantity with few digits of dB.

#### Representation of multiplication operations

Level values in decibels can be added instead of multiplying the underlying power values, which means that the overall gain of a multi-component system, such as a series of amplifier stages, can be calculated by summing the gains in decibels of the individual components, rather than multiply the amplification factors; that is, log(*ABC*)  = log(*A*) + log(*B*) + log(*C*). Practically, this means that, armed only with the knowledge that 1 dB is a power gain of approximately 26%, 3 dB is approximately 2× power gain, and 10 dB is 10× power gain, it is possible to determine the power ratio of a system from the gain in dB with only simple addition and multiplication. For example:

- A system consists of 3 amplifiers in series, with gains (ratio of power out to in) of 10 dB, 8 dB, and 7 dB respectively, for a total gain of 25 dB. Broken into combinations of 10, 3, and 1 dB, this is:

25 dB = 10 dB + 10 dB + 3 dB + 1 dB + 1 dB

With an input of 1 watt, the output is approximately

1 W × 10 × 10 × 2 × 1.26 × 1.26 ≈ 317.5 W

Calculated precisely, the output is 1 W × 10 ≈ 316.2 W. The approximate value has an error of only +0.4% with respect to the actual value, which is negligible given the precision of the values supplied and the accuracy of most measurement instrumentation.

However, according to its critics, the decibel creates confusion, obscures reasoning, is more related to the era of slide rules than to modern digital processing, and is cumbersome and difficult to interpret. Quantities in decibels are not necessarily additive, thus being "of unacceptable form for use in dimensional analysis". Thus, units require special care in decibel operations. Take, for example, carrier-to-noise-density ratio *C*/*N*0 (in hertz), involving carrier power *C* (in W) and noise power spectral density *N*0 (in W/Hz). Expressed in decibels, this ratio would be a subtraction (*C*/*N*0)dB = *C*dB − *N*0 dB. However, the linear-scale units still simplify in the implied fraction, so that the results would be expressed in dB-Hz.

#### Representation of addition operations

According to Mitschke, "The advantage of using a logarithmic measure is that in a transmission chain, there are many elements concatenated, and each has its own gain or attenuation. To obtain the total, addition of decibel values is much more convenient than multiplication of the individual factors." However, for the same reason that humans excel at additive operation over multiplication, decibels are awkward in inherently additive operations:

if two machines each individually produce a sound pressure level of, say, 90 dB at a certain point, then when both are operating together we should expect the combined sound pressure level to increase to 93 dB, but certainly not to 180 dB!; suppose that the noise from a machine is measured (including the contribution of background noise) and found to be 87 dBA but when the machine is switched off the background noise alone is measured as 83 dBA. [...] the machine noise [level (alone)] may be obtained by 'subtracting' the 83 dBA background noise from the combined level of 87 dBA; i.e., 84.8 dBA.; in order to find a representative value of the sound level in a room a number of measurements are taken at different positions within the room, and an average value is calculated. [...] Compare the logarithmic and arithmetic averages of [...] 70 dB and 90 dB: logarithmic average = 87 dB; arithmetic average = 80 dB.

Addition on a logarithmic scale is called logarithmic addition, and can be defined by taking exponentials to convert to a linear scale, adding there, and then taking logarithms to return. For example, where operations on decibels are logarithmic addition or subtraction and logarithmic multiplication or division, while operations on the linear scale are the usual operations: $$87\,\text{dBA} \ominus 83\,\text{dBA} = 10 \cdot \log_{10}\bigl(10^{87/10} - 10^{83/10}\bigr)\,\text{dBA} \approx 84.8\,\text{dBA}$$ $$\begin{align} M_\text{lm}(70, 90) &= \left(70\,\text{dBA} + 90\,\text{dBA}\right)/2 \\ &= 10 \cdot \log_{10}\left(\bigl(10^{70/10} + 10^{90/10}\bigr)/2\right)\,\text{dBA} \\ &= 10 \cdot \left(\log_{10}\bigl(10^{70/10} + 10^{90/10}\bigr) - \log_{10} 2\right)\,\text{dBA} \approx 87\,\text{dBA} \end{align}$$ The logarithmic mean is obtained from the logarithmic sum by subtracting $$10\log_{10} 2$$, since logarithmic division is linear subtraction.

#### Fractions

Attenuation constants, in topics such as optical fiber communication and [radio propagation](Radio%20propagation.md) [path loss](Path%20loss.md), are often expressed as a fraction or ratio to distance of transmission. In this case, dB/m represents decibel per meter, dB/mi represents decibel per mile, for example. These quantities are to be manipulated obeying the rules of dimensional analysis, e.g., a 100-meter run with a 3.5 dB/km fiber yields a loss of 0.35 dB = 3.5 dB/km × 0.1 km.

### Uses

#### Perception

The human perception of the intensity of sound and light more nearly approximates the logarithm of intensity rather than a linear relationship (see Weber–Fechner law), making the dB scale a useful measure.

#### Acoustics

The decibel is commonly used in acoustics as a unit of sound power level or sound pressure level. The reference pressure for sound in air is set at the typical threshold of perception of an average human and there are common comparisons used to illustrate different levels of sound pressure. As sound pressure is a root-power quantity, the appropriate version of the unit definition is used: $$L_p = 20 \log_{10}\!\left(\frac{p_{\text{rms}}}{p_{\text{ref}}}\right)\,\text{dB},$$ where *p*rms is the root mean square of the measured sound pressure and *p*ref is the standard reference sound pressure of 20 micropascals in air or 1 micropascal in water.

Use of the decibel in underwater acoustics leads to confusion, in part because of this difference in reference value.

Sound intensity is proportional to the square of sound pressure. Therefore, the sound intensity level can also be defined as: $$L_p = 10 \log_{10}\!\left(\frac{I}{I_{\text{ref}}}\right)\,\text{dB},$$

The human ear has a large dynamic range in sound reception. The ratio of the sound intensity that causes permanent damage during short exposure to that of the quietest sound that the ear can hear is equal to or greater than 1 trillion (10). Such large measurement ranges are conveniently expressed in logarithmic scale: the base-10 logarithm of 10 is 12, which is expressed as a sound intensity level of 120 dB re 1 pW/m. The reference values of I and p in air have been chosen such that this corresponds approximately to a sound pressure level of 120 dB re 20 μPa.

The original choice of the decibel over the bel as a log unit of change of intensity is because a single change in a property of sound which is below the just-noticeable difference (JND) does not affect perception of the sound. For amplitude, the JND for humans is around 1 dB.

Since the human ear is not equally sensitive to all sound frequencies, the acoustic power spectrum is modified by frequency weighting (A-weighting being the most common standard) to get the weighted acoustic power before converting to a sound level or noise level in decibels.

#### Telephony

The decibel is used in telephony and audio. Similarly to the use in acoustics, a frequency-weighted power is often used. For audio noise measurements in electrical circuits, the weightings are called psophometric weightings.

#### Electronics

In electronics, the decibel is often used to express power or amplitude ratios (as for gains) in preference to arithmetic ratios or percentages. One advantage is that the total decibel gain of a series of components (such as amplifiers and attenuators) can be calculated simply by summing the decibel gains of the individual components. Similarly, in telecommunications, decibels denote signal gain or loss from a transmitter to a receiver through some medium (free space, waveguide, [coaxial cable](Coaxial%20cable.md), fiber optics, etc.) using a link budget.

The decibel unit can also be combined with a reference level, often indicated via a suffix, to create an absolute unit of electric power. For example, dBW uses a 1 W reference, while [dBm](DBm.md) uses a 1 mW reference (*m* being short for *milliwatt*). A power level of 0 dBm corresponds to one milliwatt, and 1 dBm is one decibel greater (about 1.259 mW).

In professional audio specifications, a popular unit is the dBu. This is relative to the root mean square voltage that delivers 1 mW (0 dBm) into a 600-ohm resistor, or √1 mW × 600 Ω ≈ 0.775 VRMS. When used in a 600-ohm circuit (historically, the standard reference impedance in telephone circuits), dBu and dBm are identical.

#### Optics

In an optical link, if a known amount of optical power, in [dBm](DBm.md) (referenced to 1 mW), is launched into a fiber, and the losses, in dB (decibels), of each component (e.g., connectors, splices, and lengths of fiber) are known, the overall link loss may be quickly calculated by addition and subtraction of decibel quantities.

In spectrometry and optics, the blocking unit used to measure optical density is equivalent to −1 B.

#### Video and digital imaging

In connection with video and digital image sensors, decibels generally represent ratios of video voltages or digitized light intensities, using 20 log of the ratio, even when the represented intensity (optical power) is directly proportional to the voltage generated by the sensor, not to its square, as in a CCD imager where response voltage is linear in intensity. Thus, a camera signal-to-noise ratio or dynamic range quoted as 40 dB represents a ratio of 100:1 between optical signal intensity and optical-equivalent dark-noise intensity, not a 10,000:1 intensity (power) ratio as 40 dB might suggest. Sometimes the 20 log ratio definition is applied to electron counts or photon counts directly, which are proportional to sensor signal amplitude without the need to consider whether the voltage response to intensity is linear.

However, as mentioned above, the 10 log intensity convention prevails more generally in physical optics, including fiber optics, so the terminology can become murky between the conventions of digital photographic technology and physics. Most commonly, quantities called *dynamic range* or *signal-to-noise* (of the camera) would be specified in 20 log dB, but in related contexts (e.g. attenuation, gain, intensifier SNR, or rejection ratio) the term should be interpreted cautiously, as confusion of the two units can result in very large misunderstandings of the value.

Photographers typically use a base-2 log unit, the stop, to describe light intensity ratios or dynamic range.

### Suffixes and reference values

Suffixes are commonly attached to the basic dB unit in order to indicate the reference value by which the ratio is calculated. For example, dBm indicates power measurement relative to 1 milliwatt.

In cases where the unit value of the reference is stated, the decibel value is known as "absolute". If the unit value of the reference is not explicitly stated, as in the dB gain of an amplifier, then the decibel value is considered relative.

This form of attaching suffixes to dB is widespread in practice, albeit being against the rules promulgated by standards bodies (ISO and IEC), given the "unacceptability of attaching information to units" and the "unacceptability of mixing information with units". The IEC 60027-3 standard recommends the following format: *L**x* (re *x*ref) or as *L**x*/*x*ref, where *x* is the quantity symbol and *x*ref is the value of the reference quantity, e.g., *L**E* (re 1 μV/m) = 20 dB or *L**E*/(1 μV/m) = 20 dB for the electric field strength *E* relative to 1 μV/m reference value. If the measurement result 20 dB is presented separately, it can be specified using the information in parentheses, which is then part of the surrounding text and not a part of the unit: 20 dB (re 1 μV/m) or 20 dB (1 μV/m).

Outside of documents adhering to SI units, the practice is very common as illustrated by the following examples. There is no general rule, with various discipline-specific practices. Sometimes the suffix is a unit symbol ("W","K","m"), sometimes it is a transliteration of a unit symbol ("uV" instead of μV for microvolt), sometimes it is an acronym for the unit's name ("sm" for square meter, "m" for milliwatt), other times it is a mnemonic for the type of quantity being calculated ("i" for antenna gain with respect to an isotropic antenna, "λ" for anything normalized by the EM wavelength), or otherwise a general attribute or identifier about the nature of the quantity ("A" for A-weighted sound pressure level). The suffix is often connected with a hyphen, as in "dB‑Hz", or with a space, as in "dB HL", or enclosed in parentheses, as in "dB(HL)", or with no intervening character, as in "dBm" (which is non-compliant with international standards).

### List of suffixes

#### Voltage

Since the decibel is defined with respect to power, not amplitude, conversions of voltage ratios to decibels must square the amplitude, or use the factor of 20 instead of 10, as discussed above.

**dBV**  — dB(VRMS) – voltage relative to 1 volt, regardless of impedance. This is used to measure microphone sensitivity, and also to specify the consumer line-level of −10 dBV, in order to reduce manufacturing costs relative to equipment using the much larger +4 dBu line-level standard.

**dBu or dBv**  —  0 dBu is defined as the RMS voltage that would dissipate 0 dBm (1 mW) in a 600 Ω load. Per Ohm's law, this voltage equals:$$\begin{align} \sqrt{R P} &= \sqrt{600\ \mathsf{\Omega} \ \cdot\ 0.001\, \mathsf{W}\;} \\[1ex] &= \sqrt{0.6} \ \mathsf{V_{RMS}} \approx 0.7746\ \mathsf{V_{RMS}}\, . \end{align}$$where $$R$$ is the resistance and $$P$$ is the power. Therefore, 1 VRMS corresponds to: $$20 \cdot \log_{10} \left( \frac{ 1\ \mathsf{V_{RMS}}}{\sqrt{0.6}\ \mathsf{V_{RMS}}} \right) \approx 2.218\ \mathsf{dB_u} ~.$$Originally called dBv, it was changed to dBu to avoid confusion with dBV. According to Rupert Neve, the *u* originated from the volume *unit* displayed on a VU meter. The *u* has also been interpreted as *unloaded*.  
In professional audio, equipment may be calibrated to indicate a "0" on the VU meters some finite time after a signal has been applied at an amplitude of +4 dBu. Consumer equipment typically uses a lower "nominal" signal level of −10 dBV. Therefore, many devices offer dual voltage operation (with different gain or "trim" settings) for compatibility. A switch or adjustment that covers at least the range between +4 dBu and −10 dBV is common in professional equipment.

**dBmV**  — dBmV: dB(mVRMS) – root mean square voltage relative to 1 millivolt across 75 Ω. Widely used in cable television networks, where the nominal strength of a single TV signal at the receiver terminals is about 0 dB mV. Cable TV uses 75 Ω coaxial cable, so 0 dB mV corresponds to −78.75 dBW, −48.75 dBm or approximately 13 nW.

**dBmV0s**  — Defined by *Recommendation ITU-R V.574*.

**dBμV or dBuV**  — dB(μVRMS) – voltage relative to 1 microvolt. Widely used in television and aerial amplifier specifications. 60 dBμV = 0 dBmV.

#### Acoustics

Probably the most common usage of "decibels" in reference to sound level is dB SPL, sound pressure level referenced to the nominal threshold of human hearing: The measures of pressure (a root-power quantity) use the factor of 20, and the measures of power (e.g. dBSIL and dBSWL) use the factor of 10.

**dBSPL**  — dBSPL (sound pressure level) – for sound in air and other gases, relative to 20 micropascals (μPa), or 2×10 Pa, a level of 0 dBSPL is approximately the quietest sound a human can hear. For sound in water and other liquids, a reference pressure of 1 μPa is used.

An RMS sound pressure of one pascal corresponds to a level of 94 dB SPL in air.

**dBSIL**  — dB sound intensity level – relative to 10 W/m, which is roughly the threshold of human hearing in air.

**dBSWL**  — dB sound power level – relative to 10 W.

**dB(A), dB(B), and dB(C)**  — These symbols are often used to denote the use of different weighting filters, used to approximate the human ear's response to sound, although the measurement is still in dB (SPL). These measurements usually refer to noise and its effects on humans and other animals, and they are widely used in industry while discussing noise control issues, regulations and environmental standards. Other variations that may be seen are dBA or dB(A). According to standards from the International Electro-technical Committee (IEC 61672-2013) and the American National Standards Institute, ANSI S1.4, the preferred usage is to write L A = x dB. Nevertheless, the units dB(A) are still commonly used as a shorthand for A‑weighted measurements. Compare dBc, used in telecommunications.

**dBHL**  — dB hearing level is used in audiograms as a measure of hearing loss. The reference level varies with frequency according to a minimum audibility curve as defined in ANSI and other standards, such that the resulting audiogram shows deviation from what is regarded as 'normal' hearing.

**dBQ**  — sometimes used to denote weighted noise level, commonly using the ITU-R 468 noise weighting

**dBpp**  — relative to the peak-to-peak sound pressure.

**dB(G)**  — G‑weighted spectrum

#### Audio electronics

See also dBV and dBu above.

**[dBm](DBm.md)**  — dBmW – power relative to 1 milliwatt. In audio and telephony, dBm is typically referenced relative to a 600 Ω impedance, which corresponds to a voltage level of 0.775 volts or 775 millivolts.

**dBm0**  — Power in dBm (described above) measured at a zero transmission level point.

**dBFS**  — dB(full scale) – the amplitude of a signal compared with the maximum which a device can handle before clipping occurs. Full-scale may be defined as the power level of a full-scale sinusoid or alternatively a full-scale square wave. A signal measured with reference to a full-scale sine wave appears 3 dB weaker when referenced to a full-scale square wave, thus: 0 dBFS (full-scale sine wave) = −3 dBFS (full-scale square wave).

**dBVU**  — dB volume unit

**dBTP**  — dB(true peak) – peak amplitude of a signal compared with the maximum which a device can handle before clipping occurs. In digital systems, 0 dBTP would equal the highest level (number) the processor is capable of representing. Measured values are always negative or zero, since they are less than or equal to full-scale.

#### Radar

**dBZ**  — dBZ – decibel relative to Z = 1 mm⋅m : energy of reflectivity (weather radar), related to the amount of transmitted power returned to the radar receiver. Values above 20 dBZ usually indicate falling precipitation.

**dBsm**  — dB(m) – decibel relative to one square meter: measure of the radar cross section (RCS) of a target. The power reflected by the target is proportional to its RCS. "Stealth" aircraft and insects have negative RCS measured in dBsm, large flat plates or non-stealthy aircraft have positive values.

#### Radio power, energy, and field strength

**dBc**  — relative to carrier – in telecommunications, this indicates the relative levels of noise or sideband power, compared with the carrier power. Compare dB(C), used in acoustics.

**dBpp**  — relative to the maximum value of the peak power.

**dBJ**  — energy relative to 1 joule. 1 joule = 1 watt second = 1 watt per hertz, so power spectral density can be expressed in dBJ.

**dBmJ**  — energy relative to 1 millijoule, or 1 milliwatt per hertz.

**[dBm](DBm.md)**  — dB(mW) – power relative to 1 milliwatt. Usually referenced to a 50 Ω load, so 0 dBm corresponds to 0.224 volts. 0 dBm = -30 dBW.

**dBm/Hz**  — dB(mW/Hz) - power spectral density relative to 1 milliwatt per hertz, equivalent to dBmJ.

**dBμV/m, dBuV/m, or dBμ**  —  dB(μV/m) – electric field strength relative to 1 microvolt per meter. Related to power flux density through the impedance of free space (η0 = 376.73 Ω), so 0 dB μV/m corresponds to (1 μV/m)/η0 = 2.65x10 W/m = -145.76 dBW/m = -115.76 dBm/m.

**dBf**  — dB(fW) – power relative to 1 femtowatt.

**dBW**  — dB(W) – power relative to 1 watt. 1 dBW = +30 dBm.

**dBW/Hz**  — dB(W/Hz) - power spectral density relative to 1 watt per hertz. Equivalent to dBJ.

**dBW/m**  — dB(W/m) - power flux density (of electromagnetic radiation) relative to 1 W per square meter.

**dBk**  — dB(kW) – power relative to 1 kilowatt, 0 dBk = +30 dBW = +60 dBm. Not to be confused with dBK, temperature relative to 1 Kelvin.

**dBe**  — dB electrical.

**dBo**  — dB optical. A change of 1 dBo in optical power can result in a change of up to 2 dBe in electrical signal power in a system that is thermal noise limited.

#### Antenna measurements

**dBi**  — dB(isotropic)  – the gain of an antenna compared with the gain of a theoretical isotropic antenna, which uniformly distributes energy in all directions. Linear polarization of the EM field is assumed unless noted otherwise.

**dBd**  — dB(dipole) – the gain of an antenna compared with the gain of a half-wave [dipole antenna](Dipole%20antenna.md). 0 dBd = 2.15 dBi

**dBiC**  — dB(isotropic circular) – the gain of an antenna compared to the gain of a theoretical circularly polarized isotropic antenna. There is no fixed conversion rule between dBiC and dBi, as it depends on the receiving antenna and the field polarization.

**dBq**  — dB(quarterwave) – the gain of an antenna compared to the gain of a quarter-wavelength whip. Rarely used, except in some marketing material; 0 dBq = −0.85 dBi

**dBsm**  — dB(m) – decibels relative to one square meter: A measure of the effective area for capturing signals of the antenna.

**dBm**  — dB(m) – decibels relative to the reciprocal of a meter: measure of the antenna factor.

#### Other measurements

**dBHz**  — dB(Hz) – bandwidth relative to one hertz; e.g., 20 dBHz corresponds to a bandwidth of 100 Hz. Commonly used in link budget calculations. Also used in carrier-to-noise-density ratio (not to be confused with carrier-to-noise ratio, in dB).

**dBov or dBO**  — dB(overload) – the amplitude of a signal (usually audio) compared with the maximum which a device can handle before clipping occurs. Similar to dB FS, but also applicable to analog systems. According to ITU-T Rec. G.100.1 the level in dB ov of a digital system is defined as: $$L_\mathsf{ov} = 10 \log_{10} \left( \frac{ P }{\ P_\mathsf{max}\ } \right)\ [\mathsf{dB_{ov}}],$$ with the maximum signal power $$P_\mathsf{max} = 1.0$$, for a rectangular signal with the maximum amplitude $$x_\mathsf{over}$$. The level of a tone with a digital amplitude (peak value) of $$x_\mathsf{over}$$ is therefore $$L_\mathsf{ov} = -3.01\ \mathsf{dB_{ov}}$$.

**dBr**  — dB(relative) – simply a relative difference from something else, which is made apparent in context. The difference of a filter's response to nominal levels, for instance.

**dBrn**  — dB above reference noise. See also **dBrnCdBrnC**  — **dB(rnC)** represents an audio level measurement, typically in a telephone circuit, relative to a −90 dBm reference level, with the measurement of this level frequency-weighted by a standard C-message weighting filter. The C-message weighting filter was chiefly used in North America. The psophometric filter is used for this purpose on international circuits.

**dBK**  — **dB(K)** – decibels relative to 1 K; used to express noise temperature.

**dBK or dB/K**  — dB(K) – decibels relative to 1 K. — *not* decibels per kelvin: Used for the ⁠G/ T ⁠  (G/T) factor, a figure of merit used in satellite communications, relating the antenna gain G to the receiver system noise equivalent temperature T.

#### List of suffixes in alphabetical order

##### Unpunctuated suffixes

**dBA**  — see dB(A).

**dBa**  — see dBrn adjusted.

**dBB**  — see dB(B).

**dBc**  — relative to carrier – in telecommunications, this indicates the relative levels of noise or sideband power, compared with the carrier power.

**dBC**  — see dB(C).

**dBD**  — see dB(D).

**dBd**  — dB(dipole) – the forward gain of an antenna compared with a half-wave [dipole antenna](Dipole%20antenna.md). 0 dBd = 2.15 dBi

**dBe**  — dB electrical.

**dBf**  — dB(fW) – power relative to 1 femtowatt.

**dBFS**  — dB(full scale) – the amplitude of a signal compared with the maximum which a device can handle before clipping occurs. Full-scale may be defined as the power level of a full-scale sinusoid or alternatively a full-scale square wave. A signal measured with reference to a full-scale sine-wave appears 3 dB weaker when referenced to a full-scale square wave, thus: 0 dBFS (fullscale sine wave) = −3 dBFS (full-scale square wave).

**dBG**  — G-weighted spectrum

**dBi**  — dB(isotropic) – the forward gain of an antenna compared with the hypothetical isotropic antenna, which uniformly distributes energy in all directions. Linear polarization of the EM field is assumed unless noted otherwise.

**dBiC**  — dB(isotropic circular) – the forward gain of an antenna compared to a circularly polarized isotropic antenna. There is no fixed conversion rule between dBiC and dBi, as it depends on the receiving antenna and the field polarization.

**dBJ**  — energy relative to 1 joule: 1 joule = 1 watt-second = 1 watt per hertz, so power spectral density can be expressed in dBJ.

**dBk**  — dB(kW) – power relative to 1 kilowatt.

**dBK**  — **dB(K)** – decibels relative to kelvin: Used to express noise temperature.

**[dBm](DBm.md)**  — dB(mW) – power relative to 1 milliwatt.

**dBm or dBsm**  — dB(m) – decibel relative to one square meter

**dBm0**  — Power in dBm measured at a zero transmission level point.

**dBm0s**  — Defined by *Recommendation ITU-R V.574*.

**dBmV**  — dB(mVRMS) – voltage relative to 1 millivolt across 75 Ω.

**dBo**  — dB optical. A change of 1 dBo in optical power can result in a change of up to 2 dBe in electrical signal power in system that is thermal noise limited.

**dBO**  — see dBov

**dBov or dBO**  — dB(overload) – the amplitude of a signal (usually audio) compared with the maximum which a device can handle before clipping occurs.

**dBpp**  — relative to the peak to peak sound pressure.

**dBpp**  — relative to the maximum value of the peak electrical power.

**dBq**  — dB(quarterwave) – the forward gain of an antenna compared to a quarter wavelength whip. Rarely used, except in some marketing material. 0 dBq = −0.85 dBi

**dBr**  — dB(relative) – simply a relative difference from something else, which is made apparent in context. The difference of a filter's response to nominal levels, for instance.

**dBrn**  — dB above reference noise. See also **dBrnCdBrnC**  — represents an audio level measurement, typically in a telephone circuit, relative to the circuit noise level, with the measurement of this level frequency-weighted by a standard C-message weighting filter. The C-message weighting filter was chiefly used in North America.

**dBsm**  — see dBm

**dBTP**  — dB(true peak) – peak amplitude of a signal compared with the maximum which a device can handle before clipping occurs.

**dBu or dBv**  — RMS voltage relative to $$\ \sqrt{0.6\ }\ \mathsf{V}\ \approx 0.7746\ \mathsf{V}\ \approx -2.218\ \mathsf{dB_V} ~.$$

**dBu0s**  — Defined by *Recommendation ITU-R V.574*.

**dBuV**  — see dBμV

**dBuV/m**  — see dBμV/m

**dBv**  — see dBu

**dBV**  — dB(VRMS) – voltage relative to 1 volt, regardless of impedance.

**dBVU**  — dB(VU) dB volume unit

**dBW**  — dB(W) – power relative to 1 watt.

**dB W·m·Hz**  — spectral density relative to 1 W·m·Hz

**dBZ**  — dB(Z) – decibel relative to Z = 1 mm⋅m

**dBμ**  — see dBμV/m

**dBμV or dBuV**  — dB(μVRMS) – voltage relative to 1 root mean square microvolt.

**dBμV/m, dBuV/m, or dBμ**  — dB(μV/m) – electric field strength relative to 1 microvolt per meter.

##### Suffixes preceded by a space

**dB HL**  — dB hearing level is used in audiograms as a measure of hearing loss.

**dB Q**  — sometimes used to denote weighted noise level

**dB SIL**  — dB sound intensity level – relative to 10 W/m

**dB SPL**  — dB SPL (sound pressure level) – for sound in air and other gases, relative to 20 μPa in air or 1 μPa in water

**dB SWL**  — dB sound power level – relative to 10 W.

##### Suffixes within parentheses

**dB(A), dB(B), dB(C), dB(D), dB(G), and dB(Z)**  — These symbols are often used to denote the use of different weighting filters, used to approximate the human ear's response to sound, although the measurement is still in dB (SPL). These measurements usually refer to noise and its effects on humans and other animals, and they are widely used in industry while discussing noise control issues, regulations and environmental standards. Other variations that may be seen are dBA or dBA.

##### Other suffixes

**dBHz or dB-Hz**  — dB(Hz) – bandwidth relative to one hertz

**dBHz or dB/s**  — dB(Hz) – the squared magnitude of an impulse response (or impulse response envelope) relative to the squared magnitude of an impulse response with unity amplitude.

**dBK or dB/K**  — dB(K) – decibels relative to reciprocal of kelvin

**dBm**  — dB(m) – decibel relative to reciprocal of meter: measure of the antenna factor

**mBm**  —  mB(mW) – power relative to 1 milliwatt, in millibels (one hundredth of a decibel). 100 mBm = 1 dBm. This unit is in the Wi-Fi drivers of the Linux kernel and the regulatory domain sections.

---

*Source: Wikipedia, Decibel (https://en.wikipedia.org/wiki/Decibel), by Wikipedia contributors, CC BY-SA 4.0.*
