# How do I evaluate and use a toroidial core for my HF double-balanced mixer?

*Tags: hf, ferrite, toroid · score 6*

## Question

Last year, I planned to make a double-balanced mixer covering the entire 3-30 MHz band as an upconverter for my RTL-SDR receiver, mainly for learning RF circuits and ham radio. Naturally, it requires two RF transformers as baluns, possible 4:1 or 9:1 baluns.

In the United States, it appears that Type 43 and Type 61 toroids are the most commonly used cores among the entire ham radio community. One can find a lot of existing designs and materials. Unfortunately, they are not widely available outside US. It seems unworthy to purchase some toroidals cores from the US via Digikey when the local industry at home has something to offer. Or so I thought.

When I received some large toroidal cores, I realized I don't have any knowledge nor experience - a balun is much more difficult than I thought, a lot of electromagnetism terminology and tricky parameters to consider. I tried winding three baluns but it seemed none worked, and none of the rule-of-thumbs or spreadsheet calculator could help me because I wasn't using a well-known core. I didn't even have a signal generator to test it properly. So I finally abondoned the project and built a single-ended mixer instead, with poor LO rejection.

I recently got a signal generator for my bench, and I regain the courage to try it again. Could anyone help me explaining my questions?

1. The toroidal core manufacturer claims it's suitable for HF applications and provided tho following data:

**Model**: NXO-40

**Outer diameter**: 31 mm

**Inner diameter**: 18 mm

**Height**: 7mm

**Initial permeability ($\mu_i$)**: 40 ± 20%

**Relative loss factor ($\tan \delta / \mu_{i}$)** : 8MHz, 92 ($\times 10^{-6}$)

**Temp. Coefficient ($\alpha_{\mu}$)**: 1200 (20-60 °C, $\times 10^{-6}$ / °C)

**Curie Temperature ($T_{c}$)**: 300 °C

**Resistivity ($\rho$)**: $10 \times 10^6$ Ω cm

**Saturation Flux Density ($B_s$)**: 290 mT

**Remanent Induction ($B_r$)**: 90 mT

**Coercive Force ($H_c$)**: 0.32 KA/m

**Applied Frequency ($f$)**: 40 MHz

What information can I learn from these parameters? Is it a good toroidal core to use for a HF receiver? A good balun for transmitters? What about using it as a EMI/RFI chock? A low-wattage 50 Hz power transformer?

1.

It's common to characterize toroidal cores in terms of $A_{L}$ and $u_H$. What are they useful for (obviously, useful for calculating the inductance, but what purposes do it serve for RF transformers)? They are not given by the manufacturer, how can I calculate them from the known parameters of the core?

2.

If I need to replace a toroidial core from an American design in the future, for example, FT37-43, which parameters should I look, and what calculations should I do to find an equivalent substitution?

3.

What measurements can I take with an 100 MHz oscilloscope (w/ FFT) and a 10 MHz signal generator to test whether my balun is working as intended after I winded it?

4.

Are there any resources for beginners like me to get started?

Thanks!

## Answer (score 3, by 比尔盖子)

My biggest mistake was keeping my search on everything about ferrite and balun online, and receiving various piece of confusing information of mixed quality. Meawhile, I didn't even take a look at the most basic and authoritative reference material: *The ARRL Handbook for Radio Communication*.

Today, I just obtained a copy of the 2014 edition, and immediately even before open the book, I saw six toroidial cores on the hardcover, aha! I think I can answer most of my questions now. If you are reading this, please help me to check whether my answer is correct, thanks.

First, we assume the transformer required is (1) for reception only, so temperature/heat dissipation is not an issue, and (2) not a transmission-line transformer, but a conventional transformer, which should be enough for our purpose [Note 1] as a beginner's project.

### 1. Is it a good toroidal core to use?

1. What information can I learn from these parameters? Is it a good toroidal core to use for a HF receiver?

The most important parameter is the initial permeability, μi = 40. In *Chapter 5: RF Techniques* of the *ARRL Handbook*, it advice that...

**5.7.3 Broadband Ferrite RF Transformers**: [...] The core-material permeability plays a vital role in designing a good broadband transformer. The effective permeability of the core must be high enough to provide ample winding reactance at the low end of the operating range. As the operating frequency is increased, the effects of the core tend to disappear until there are scarcely any core effects at the upper limit of the operating range. The limiting factors for high frequency response are distributed capacitance and leakage inductance due to uncoupled flux. A high-permeability core minimizes the number of turns needed for a given reactance and therefore also minimizes the distributed capacitance at high frequencies.

One of the most common ferromagnetic transformers used in amateur circuits is the conventional broadband transformer. Broadband transformers with losses of less than 1 dB are employed in circuits that must have a uniform response over a substantial frequency range, such as a 2 to 30 MHz broadband amplifier. In applications of this sort, the reactance of the windings should be at least four times the impedance that the winding is designed to look into at the lowest design frequency.

[...] Ferrite cores with a permeability of 850 are common choices for transformers used between 2 and 30 MHz. Lower frequency ranges, for example, 1 kHz to 1 MHz, may require cores with permeabilities up to 2000. Permeabilities from 40 to 125 are useful for VHF transformers.

In principle, there's **nothing** to prevent one from constructing a RF transformer for HF using a core with μi = 40, however, due to its low permeability...

1.

It requires one to wind **much more turns than necessary** to obtain the same inductance required, which is a a quite labor-intensive process.

2.

As the number of turns increases, distributed capacitance and leakage inductance increases, which cause *the high-frequency response of transformer to deteriorate.*

3.

Given the same number of turns, a lower permeability implies poorer low-frequency performance, because it provide lower inductance.

Furthermore, the vendor claims the operating frequency of the core is 3-100 MHz, which is consistent with *The ARRL Handbook*'s advise that "Permeabilities from 40 to 125 are useful for VHF transformers".

A good balun for transmitters?

Unlike receivers, transformers used for transmitters must handle significant power (and temperature rise). Cores with low permeabilities often have a much higher Curie temperature. Thus, transmitters have to use cores with much lower permeabilities. A presentation from Amateur Radio New South Wales (ARNSW) claims "permeability above 250 is not recommended as this will degrade high frequency performance", and that the T200-2 iron powder core with μi = 10 can well be used for "baluns from about 7 MHz to 50 MHz", but recommends FT240-61 (μi = 125) for 3 MHz to 30MHz.

Also, *Transmission Line Transformers, 4th Edition* by *Jerry Sevick, W2FMI* suggests in Chapter 11,

Generally, the lowest-permeability nickel-zinc ferrites yield the highest efficiencies. These have permeabilities in the range of 40 to 50. But, these ferrites can limit the low-frequency response. [...] Limited measurements on 4C4 material (μi = 125) [...] showed the best efficiency at the 200-ohm level. Table 11-2 lists some suggested power ratings [...] These ratings should generally hold for permeability below 300.

It is quite consistent with ARNSW's recommendations, shows their claims should be reliable.

What about using it as a EMI/RFI chock?

Not a good option. The material from Fair-Rite's Type #67, a similar core, shows they are only useful for suppressing interference above 1 GHz.

A low-wattage 50 Hz power transformer?

Absolutely not. A power transformer requires large inductance.

In *Chapter 7: Power Transformer Design* of the book *Transformer and Inductor Design Handbook, Third Edition* by *Colonel McLyman* showed various candidates for transformer cores. The 50 Hz transformer candidates all have permeabilities greater than 1500.

#### Remarks 1.1


This toroidal ferrite core is only suitable for winding high-Q inductors. It can be used as a wideband transformer, but best be used for VHF, not HF.


It's not a good EMI/RFI choke.


In general, do not use build a transformer with ferrite cores that have permeabilities lower than 125 for transmitters, 850 for receivers.

In conclusion, the local vendor of the MXO series of ferrite offers cores of higher permeabilities, better cores should be purchased from the vendor for building a balun for the double-balanced mixer.

### 2. Calculating Inductance

It's common to characterize toroidal cores in terms of AL and uH. What are they useful for (obviously, useful for calculating the inductance, but what purposes do it serve for RF transformers)?

Already mentioned and explained, and the ARRL Handbook continued to show...

Example: What should be the winding reactances of a transformer that has a 300-Ω primary and a 50-Ω secondary load? Relative to the 50-Ω secondary load:

$$ X_{S} = 4 Z_{S} = 4 \times 50 \Omega = 200 \Omega $$

and the primary winding reactance ($X_{P}$) is:

$$ X_{P} = 4 Z_{P} = 4 \times 300 \Omega = 1200 \Omega $$

They are not given by the manufacturer, how can I calculate them from the known parameters of the core?

The article *Magnetic Materials for Broadband Transmission Line Transformers* from *High Frequency Electronics, January 2005*, by *Jerry Sevick* says...

If a toroid is used for the core, the magnetizing inductance $L_{m}$ (in henrys) is:

$$ L_m = 0.4 \pi N^2 \mu \frac{A_e}{L_e} \times 10^{-8} $$

Where $N$ is the number of turns, $\mu$ is the permeability of the core, $A_e$ (in square centimeter) is the effective cross-sectional area of the core, and $L_e$ (in centimeter) is the average magnetic path length in the core.

And according to this page, the cross-sectional area of a toroidial core is...

$$ A_e = \frac{(D_{out} - D_{in})}{2} H $$

Where $D_{out}$ and $D_{in}$ are outer diameter and inner diameter in centimeter, $H$ is the height in centimeter, and the average magnetic path length of a toroidial core is...

$$ L_e = \frac{\pi (D_{out} - D_{in})}{\ln (\frac{D_{out}}{D_{in}})}$$

Thus,

$$ A_L = \frac{L_m}{N^2} = 0.2 \mu \ln (\frac{D_{out}}{D_{in}}) H \times 10^{-8} \space \text{H}/\text{Turn}^2$$

Where $\mu$ is the permeability of the core, $\ln$ is natural logarithm, $D_{out}$ and $D_{in}$ are outer diameter and inner diameter in centimeter, $H$ is the height in centimeter.

For example, there's a 141-35 core, $D_{out} = 3.58 \space \text{cm}$, $D_{in} = 2.24 \space \text{cm}$, $H = 1.05 \space \text{cm}$, $\mu_{i} = 35$,

$$ A_L = 0.2 \times 35 \times \ln (\frac{3.58}{2.24}) \times 1.05 \times 10^{-8} \space \text{H}/\text{Turn}^2 $$

$$ A_L = 3.446 \times 10^{-8} = 34.4 \space \text{nH}/\text{Turn}^2 $$

The listed $ A_L $ in the datasheet is $ 33\space \text{nH}/\text{Turn}^2 $, showing our calculation only has an error of 5%.

#### Remarks 2.1


The reactance of the windings should be at least four times the impedance that the winding is designed to look into at the lowest design frequency.


A formula for calculating the inductance of a toroidal ferrite core from its geometric dimensions and the number of turns is given. Plug the numbers in, inductance per turn can be calculated.


Alternatively, wrapping a few turns of wires on the core and measure the inductance directly using an LCR meter is a solution.

### 3. Core Replacement

If I need to replace a toroidial core from an American design in the future, for example, FT37-43, which parameters should I look, and what calculations should I do to find an equivalent substitution?

Finding a core made of the same material with similar permeability shouldn't be hard. The question [How does one read a ferrite datasheet?](How%20does%20one%20read%20a%20ferrite%20datasheet.md) also gives good references.

### 4. Measurements

**TODO: misleading instructions, only suitable for 1:1 balun, need to fix this section.**

What measurements can I take with an 100 MHz oscilloscope (w/ FFT) and a 10 MHz signal generator to test whether my balun is working as intended after I winded it?

Turn on the signal generator, switch it to 10 MHz. Connect the primary side of the balun to the signal generator. Probe the primary side with an oscilloscope and save the waveform.

Disconnect the probe. Probe the secondary side of the balun. You should see a AC signal (without DC bias), with minimum attenuation of its amplitudes. This check confirms whether the balun is working as a transformer correctly as expected.

Possibly, feeding a tracking generator or a noise source to the primary side and checking the attenuation of the secondary side with a spectrum analyzer or oscilloscope FFT is also an option.

However, for an authoritative characterization, a Vector Network Analyzer should be used to measure the S-parameter of the balun. Currently, there are a lot of low-cost options such as MiniVNA and NanoVNA on the market, which should do its job to a reasonable level of certainty, and not out-of-reach for most people. The measurement should be done on a test rig (e.g. a copper board with all components soldered, SMD resistors) to minimize parasitic inductance and capacitance.

### 5. How to get started?

Are there any resources for beginners like me to get started?

Read the entire *ARRL Handbook*.

#### Remark 5.1

- *ARRL Handbook* has much more information and pointers to even more references than most beginners believes.

#### Notes

[Note 1] "Conventional transformers have been constructed to perform over wide bandwidths. Losses on the order of one decibel can exist over a range from a few kiloherz to over 200 MHz. Throughout a considerable portion of this band, the losses are only 0.2 dB. On the other hand, transimission line transformers exhibit far wider bandwidths and much greater efficiencies." - *Transmission Line Transformers, 4th Edition* by Jerry Sevick, W2FMI

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15261/how-do-i-evaluate-and-use-a-toroidial-core-for-my-hf-double-balanced-mixer, by 比尔盖子. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
