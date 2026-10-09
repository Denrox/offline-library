# Superheterodyne receiver

The **superheterodyne receiver**, commonly called the **superhet**, is a [radio receiver](Radio%20receiver.md) that uses heterodyning to convert incoming radio-frequency (RF) signals to a fixed intermediate frequency (IF). The signal is then amplified and filtered at that fixed frequency. This arrangement separates tuning from most of the gain and filtering: the RF circuits make an initial, relatively broad selection of the desired station, while the IF stages provide most of the amplification and the selectivity needed to separate it from adjacent stations.

The design became important during the rapid growth of broadcast radio in the 1920s. As [amplitude modulation](Amplitude%20modulation.md) (AM) stations multiplied, receivers had to handle crowded bands and signals that ranged from strong local stations to weak distant ones. Many earlier sets required several tuning controls to be adjusted together, and their performance varied widely. The superheterodyne offered a more practical path to stable gain, sharper selectivity, and simpler operation, especially as vacuum tubes (valves) improved and became cheaper.

The principle had been developed earlier, but the superheterodyne did not become widely used until the mid-1920s, when receiver designs and vacuum tubes improved enough for practical mass production. Patent control and licensing also played a role. The Radio Corporation of America (RCA) and associated companies held key rights and influenced which receiver types could be manufactured. By the early 1930s, as licensing issues eased, the superheterodyne largely replaced earlier receivers.

### Why the superheterodyne displaced other technologies

Up to 1930, non-superheterodyne receivers still dominated the market. By 1933, however, superheterodyne sets accounted for 96 percent of sales. A contemporary study of interference effects therefore concluded that only superheterodyne receivers needed to be considered.

The superheterodyne became dominant because it separated functions that proved difficult to perform together. Earlier receivers had to amplify, select, and tune the signal at the received frequency, often requiring several tuned stages to track together. By moving most amplification and filtering to a fixed intermediate frequency, the superheterodyne made gain, selectivity, and stability easier to obtain. Higher-order filters could be used at the fixed IF, while the RF stages only needed to make a coarser initial selection. These advantages became clear as broadcast bands became crowded.

Early superheterodyne receivers were expensive because they required extra tubes, including a local oscillator and mixer. As vacuum tubes improved and became cheaper, this disadvantage became less important. Radios became easier to use as single-control tuning and automatic volume control reduced knobs and adjustments.

Herold later identified the years from about 1927 to 1936 as the period when the superheterodyne became the universal receiver circuit. Better tubes made AC operation, single-knob tuning, automatic gain control, and multigrid converter stages practical. Those changes removed much of the early penalty for using a more complex receiver, while preserving the superheterodyne's advantages in gain and selectivity.

Commercial adoption was also shaped by RCA licensing. Converter tubes combined the oscillator and mixer, reducing cost. Low-cost superheterodynes such as the All American Five proliferated as the superheterodyne became the standard. By World War II, the superheterodyne was "recognized as the most efficient receiving circuit..."

### Principle of operation

A superheterodyne receiver converts an incoming radio-frequency signal to a fixed intermediate frequency, where most of the amplification and selectivity are applied. The received signal from the antenna is first filtered, then combined with a locally generated oscillator signal in a mixer to produce new frequencies equal to the sum and difference of the two. One of these, the intermediate frequency, is selected and amplified by tuned stages optimized for a single frequency. The modulation is then recovered by a detector and passed to an audio or other output stage. By concentrating gain and filtering at a fixed frequency rather than at the received frequency, the superheterodyne design allows consistent selectivity and sensitivity over a wide tuning range.

#### Example: medium-wave broadcast receiver

The AM medium-wave broadcast band covers 531–1602 kHz in Europe, with the channels spaced by 9 kHz. The 540–1700 kHz band is used in North America, with a 10 kHz spacing. By the mid-1930s, new multi-grid vacuum tubes allowed the intermediate frequency to increase to 455 kHz, a standard for broadcast receivers. This frequency offers a balance between image rejection and high selectivity, achievable with LC tuned circuits.

In a typical arrangement the local oscillator is operated above the received frequency (high-side injection), so that the intermediate frequency is given by *f*IF = *f*LO − *f*RF. The resulting frequency relationships at the lower and upper ends of the band are shown below.

Example frequency planning for 455 kHz IF
- Received frequency   Local oscillator   Image frequency
- 531 kHz (Europe, lower band edge)   986 kHz   1441 kHz
- 1700 kHz (North America, upper band edge)   2155 kHz   2610 kHz

Across the band, the local oscillator must tune from approximately 986 kHz to 2155 kHz, a range slightly greater than 2:1. If low-side injection were used instead, the oscillator would have to tune from 76 kHz to 1245 kHz, a much wider ratio that is difficult to realize with a single tuned circuit. This is one reason high-side injection became standard in broadcast receivers.

The RF tuned circuits are primarily responsible for attenuating relatively distant interferers, including the image frequency, while the IF stages provide most of the selectivity against nearby channels. This separation allows each stage to be optimized for a different problem: the RF stage for image rejection over a wide frequency range, and the IF stage for narrowband selectivity.

The image frequency is separated from the desired signal by twice the intermediate frequency (2 × 455 kHz = 910 kHz). At the upper end of the band this places the image well above the broadcast band, while at the lower end it falls within the band. The RF input circuit must therefore attenuate these image frequencies while still passing the desired signal, which requires the RF tuning to track the local oscillator.

Because broadcast channels are spaced only 9 or 10 kHz apart, the selectivity cannot be achieved without multiple LC circuits, which would be impractical to implement in a tuned RF stage. Instead, the superheterodyne architecture concentrates gain and filtering at the fixed intermediate frequency, where multiple tuned stages can be optimized to separate the desired channel from adjacent ones. The RF stage then serves primarily to limit image response and strong out-of-band signals, while tracking the local oscillator as the receiver is tuned across the band.

#### RF stage

The RF stage provides the initial frequency-selective filtering and, in some designs, gain for the received signal. Its primary function is to attenuate the image frequency and other out-of-band signals that would otherwise be converted to the intermediate frequency by the mixer. This operation is often called preselection.

The filtering is typically provided by one or more tuned circuits. In receivers that tune over a wide frequency range, the RF tuning tracks the local oscillator so that both remain tuned together as the receiver is tuned. This tracking may be achieved with mechanically ganged variable capacitors or electronically using varicap diodes.

An RF amplifier may be included to improve sensitivity, but at lower frequencies it is often unnecessary when external noise exceeds the internal noise of the receiver. In such cases the RF stage provides little or no gain, and most of the amplification is obtained at the intermediate frequency.

The RF stage must also remain sufficiently linear to handle strong signals without overload. Nonlinear operation can produce intermodulation products that fall within the passband and interfere with reception of nearby channels.

In earlier tuned radio-frequency (TRF) receivers, all gain and selectivity were applied at the received frequency, requiring multiple tuned stages to track together. The superheterodyne instead concentrates most of the gain and selectivity at a fixed intermediate frequency, allowing higher overall gain with improved stability.

The total voltage gain of a receiver, from microvolt-level input signals to several volts at the audio output, may exceed 100 dB. In the superheterodyne this gain is distributed between RF and IF stages, reducing the likelihood of instability due to unintended feedback.

The RF stage also serves to limit radiation of the local oscillator signal from the antenna, which could otherwise cause interference to nearby receivers.

#### Local oscillator and mixer

Herold described frequency conversion in superheterodyne receivers as a modulation process in which the local oscillator periodically varies the transconductance of the signal path, producing an intermediate-frequency output.

The received signal is combined with a signal from a local oscillator (LO) in a nonlinear device called a mixer. The mixer produces signal frequencies at the sum and difference of its input frequencies. Those signals each carry the original modulation. For an input at $$f_{\mathrm{RF}}$$ and an oscillator at $$f_{\mathrm{LO}}$$, the principal outputs are $$f_{\mathrm{RF}} + f_{\mathrm{LO}}$$ and $$\left|f_{\mathrm{RF}} - f_{\mathrm{LO}}\right|$$. In an ideal multiplier driven by a sinusoidal LO, only these two components are produced, but practical mixers also generate higher-order intermodulation products. Early mixers summed the LO and RF signals into a nonlinear device, usually square-law, to do the conversion. Modern IC mixers use a balanced mixer configuration to produce fewer interference products.

The local oscillator is tuned so that the difference component equals the intermediate frequency:

$$
f_{\mathrm{IF}} = \left|f_{\mathrm{LO}} - f_{\mathrm{RF}}\right|
$$

If $$f_{\mathrm{LO}} > f_{\mathrm{RF}}$$, the arrangement is called *high-side injection*; if $$f_{\mathrm{LO}} < f_{\mathrm{RF}}$$, it is *low-side injection*. High-side injection is commonly used in broadcast receivers because it results in a more practical tuning range for the oscillator.

The mixer processes all signals present at its input, including adjacent channels and strong out-of-band signals. After conversion, the IF filter selects the desired component at $$f_{\mathrm{IF}}$$ and rejects the others. This separation of frequency conversion and selectivity is a key advantage over earlier tuned radio-frequency (TRF) designs.

The conversion stage was historically called heterodyne detection or first detection, but by the 1940s the process was commonly described as frequency conversion; Herold used *converter* for the complete frequency-changing stage and *mixer* or *modulator* for the tube section that performed the mixing when the oscillator was separate. In vacuum-tube receivers, the oscillator and mixer functions were often combined in a single device, such as a pentagrid converter, reducing component count and cost. The mixing stage is sometimes referred to as the *first detector*, while the demodulator that recovers the modulation at the IF is called the *second detector*. In receivers with multiple conversion stages, these terms extend to *third detector* and beyond.

#### IF amplifier

The stages of an intermediate-frequency amplifier ("IF amplifier" or "IF strip") are tuned to a fixed frequency that does not change as the receiving frequency changes. This simplifies optimization of the amplifier and its associated filters. The IF amplifier is selective around its center frequency $$f_{\mathrm{IF}}$$. Because this frequency is fixed, the stages can be carefully adjusted for best performance, a process known as alignment. Most of the gain of the receiver occurs in the IF stage.

Early receivers used LC tuned circuits for IF filtering, usually double-tuned, meaning two LC circuits per stage. Later designs employed mechanical and crystal filters for improved selectivity and stability.

In early designs, the IF center frequency $$f_{\mathrm{IF}}$$ was typically chosen to be lower than the range of received frequencies $$f_{\mathrm{RF}}$$, since high selectivity is easier to achieve at lower frequencies.

Standard intermediate frequencies include 455 kHz for medium-wave AM receivers, 10.7 MHz for broadcast FM, 38.9 MHz (Europe) or 45 MHz (United States) for television, and 70 MHz for satellite and terrestrial microwave systems. The widespread use of these values led to de facto standardization of IF components.

In early superheterodyne receivers, the IF stage was sometimes implemented as a regenerative circuit, providing both gain and selectivity with fewer components. Such receivers were referred to as super-gainers or regenerodynes. A related technique is the Q multiplier, which increases the effective selectivity of an IF stage by controlled feedback.

#### IF bandpass filter

The IF stage includes a filter and/or multiple tuned circuits to provide the required selectivity. The passband is chosen to accommodate the bandwidth of the desired signal, while attenuating adjacent channels. Ideally, the filter provides high attenuation outside the passband while maintaining a relatively flat response across the signal spectrum. Reduction of bandwidth or uneven response can degrade sound fidelity; excessive bandwidth or shallow roll-off permits interference from adjacent channels.

This selectivity may be obtained using one or more dual-tuned IF transformers, a quartz crystal filter, or a multipole ceramic filter. In some receivers the IF bandwidth is adjustable, allowing a trade-off between fidelity and noise or interference rejection.

In television receivers, the IF filter must produce the asymmetrical response required for vestigial sideband reception, as used in systems such as NTSC, first standardized in the United States in 1941.

By the 1980s, multi-component LC filters were increasingly replaced by precision electromechanical surface acoustic wave (SAW) filters. SAW filters can be manufactured to tight tolerances, are stable in operation, and are well suited to high-volume production.

#### Demodulator

The received signal is processed by the demodulator stage where the audio signal (or other baseband signal) is recovered and further amplified. AM demodulation requires envelope detection, which can be achieved by means of rectification and a low-pass filter to remove remnants of the intermediate frequency. FM signals may be detected using a discriminator, ratio detector, or phase-locked loop. [Continuous wave](Continuous%20wave.md) and single sideband signals require a product detector using a beat frequency oscillator, or other techniques used for different types of modulation. The resulting audio signal (for instance) is then amplified and drives a loudspeaker.

With high-side injection, in which the local-oscillator frequency is above the received signal, the resulting intermediate-frequency spectrum is reversed. This spectral inversion must be allowed for when receiving modulation formats in which the distinction between upper and lower sidebands is important, such as [single-sideband modulation](Single-sideband%20modulation.md).

### Multiple conversion

In many receivers designed to cover a wide frequency range, a first intermediate frequency higher than the received frequency is used in a double-conversion architecture. This approach improves image rejection and allows more practical local oscillator tuning ranges. For example, the Rohde & Schwarz EK-070 VLF/HF receiver covers 10 kHz to 30 MHz. The input is mixed to a first IF of 81.4 MHz, followed by a second IF of 1.4 MHz. The first local oscillator therefore tunes from 81.4 to 111.4 MHz, a practical range for a stable oscillator, while the second local oscillator is fixed at 80 MHz.

If the same RF range were converted directly to 1.4 MHz, the local oscillator would need to tune from 1.4 to 31.4 MHz, an impractically wide range for a single tuned circuit. By converting first to a high IF, image rejection is simplified and oscillator design is eased. For example, with a 1 MHz input signal, the first LO is at 82.4 MHz and the image occurs at $$f_{\mathrm{RF}} + 2f_{\mathrm{IF}} = 163.8\ \text{MHz}$$, a distant frequency which is easily filtered out.

The first IF stage typically includes a narrow filter, known as a roofing filter. An example is a 12 kHz wide crystal filter to limit the signal bandwidth before further conversion. This filtering attenuates many potential interferers, reducing the opportunity for overload and intermodulation distortion in subsequent amplification stages. A second conversion then translates the signal to a lower IF (for example, mixing 81.4 MHz with 80 MHz to produce 1.4 MHz), where higher selectivity is obtained.

In amateur radio receivers, intermediate frequencies around 9 MHz are commonly used, as they allow practical crystal filter implementations and convenient frequency planning with acceptable image separation. Analyses of receiver performance and architecture trade-offs, including the impact of conversion strategy on dynamic range and interference handling, are discussed in the technical literature.

### Modern designs

Microprocessor technology allows replacing the superheterodyne receiver design by a [software-defined radio](Software-defined%20radio.md) architecture, where the IF processing after the initial IF filter is implemented in software. This technique is already in use in certain designs, such as very low-cost FM radios incorporated into mobile phones, since the system already has the necessary microprocessor.

### Advantages and disadvantages

By converting signals to a fixed intermediate frequency (IF), the superheterodyne improved sensitivity, selectivity, and frequency stability compared with earlier designs. Early superheterodyne receivers required more vacuum tubes than competing designs, which increased cost and complexity. As tube performance improved and manufacturing scaled during the 1920s and 1930s, this disadvantage diminished, and with the introduction of transistors the additional circuit complexity became negligible in most applications.

The remaining limitations arise from the frequency conversion process itself. Mixing produces undesired responses, including the image frequency, which must be suppressed by RF filtering. It also introduces spurious signals and adds noise, while imperfections in the local oscillator further degrade performance. These effects set practical limits on receiver performance.

#### Image frequency (*f*IMAGE)

A fundamental limitation of the superheterodyne is the image frequency: an undesired signal offset from the desired signal by twice the intermediate frequency, which is also converted to the same IF and cannot be distinguished by the IF filter alone.

For example, a receiver tuned to 660 kHz (such as WFAN in New York) with a 455 kHz IF and high-side injection uses a local oscillator at 1115 kHz. A signal at 1570 kHz, also 455 kHz away from the oscillator, will produce the same IF and can interfere with reception. 1570 kHz was historically occupied by high-power XERF, making the effect readily observable.

Image response is reduced by RF filtering ahead of the mixer. Early receivers, which often used low IF frequencies due to tube limitations, required multiple tuned RF stages to suppress images. Later designs reduced the problem by using higher first IF frequencies or multiple frequency conversions, increasing the separation between the desired signal and its image.

The ability of a receiver to reject interfering signals at the image frequency is measured by the image rejection ratio. This is the ratio (in [decibels](Decibel.md)) of the output of the receiver from a signal at the received frequency, to its output for an equal-strength signal at the image frequency.

#### Spurious responses

When the mixer is not a perfect multiplier, mixing produces additional components of the form *m*fRF ± *n*fLO, where *m* and *n* are integers. Any of these falling within the IF passband appear as spurious signals ("spurs") at the output. For example, consider an AM receiver tuned to 1000 kHz with a 455 kHz IF and a local oscillator at 1455 kHz. A signal at 955 kHz can produce a spur at the IF through a higher-order mixing product (2 × 955 − 1455 = 455 kHz). This occurs because the mixer generates harmonics and intermodulation products in addition to the desired sum and difference frequencies. Channel spacing in broadcast bands (such as 10 kHz in the United States) often places such spurs slightly offset (e.g., by 5 kHz), so they may be partially attenuated by the IF filter but can still cause audible interference.

These responses arise because practical mixers have a nonlinear transfer function rather than acting as ideal multipliers. Modern balanced and double-balanced mixer designs reduce the amplitude of many unwanted products, and integrated circuit implementations achieve improved spur performance. The beam-deflection tube (e.g., the 7360) approached more ideal multiplication and reduced intermodulation effects.

#### Local oscillator radiation

Stray radiation from the local oscillator can be difficult to suppress below levels detectable by a nearby receiver, and below levels required by standards organizations. When the local oscillator signal reaches the antenna the receiver acts as a low-power [CW](Continuous%20wave.md) transmitter, potentially interfering with other receivers. This problem was significant in early radio.

Local oscillator radiation is most prominent in receivers where the antenna is coupled directly to the mixer, which also receives the local oscillator signal, rather than in designs that include an intervening RF amplifier stage. It is therefore more significant in inexpensive receivers and in receivers operating at very high frequencies (especially microwave), where RF amplifier stages are more difficult to implement.

In intelligence operations, local oscillator radiation can be used to detect a covert receiver and its operating frequency. The method was used by MI5 during Operation RAFTER. This same technique is also used in radar detector detectors by traffic police in jurisdictions where radar detectors are illegal.

#### Mixing noise from image

Mixing degrades the signal-to-noise ratio, which is unavoidable. If the desired input to the mixer is at 1000 kHz and the local oscillator is at 1455 kHz, noise at both 1000 kHz and at the image frequency of 1910 kHz will be translated to the 455 kHz intermediate frequency. Noise from the image band therefore appears at the output even for an ideal mixer. In practical receivers, the mixer also contributes noise, and its conversion loss reduces the signal-to-noise ratio. Subsequent gain amplifies both signal and noise, preserving this reduced ratio. This is an inherent consequence of frequency conversion and sets a lower bound on achievable sensitivity.

#### Local oscillator phase noise and reciprocal mixing

The frequency conversion process does not improve the signal-to-noise ratio; it translates both the desired signal and any noise present at the input to the IF frequency. In addition, the local oscillator (LO) contributes its own noise, primarily as phase noise, a side effect of practical oscillators. During mixing, this phase noise appears as sidebands around the converted signal at the intermediate frequency. This effect, known as *reciprocal mixing*, arises because the mixer combines not only the desired input signal with the LO, but also mixes LO noise with signals present at the input. As a result, strong signals on adjacent frequencies can be converted into noise within the receiver passband, degrading sensitivity and selectivity. The phase noise of the local oscillator is therefore a critical parameter in receiver performance. Oscillator design, device noise, and circuit topology all influence phase noise.

---

*Source: Wikipedia, Superheterodyne receiver (https://en.wikipedia.org/wiki/Superheterodyne_receiver), by Wikipedia contributors, CC BY-SA 4.0.*
