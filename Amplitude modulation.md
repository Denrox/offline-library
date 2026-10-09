# Amplitude modulation

**Amplitude modulation** (**AM**) is a signal modulation technique used in electronic communication, most commonly for transmitting messages with a radio wave. In amplitude modulation, the instantaneous amplitude of the wave is varied in proportion to that of the message signal, such as an audio signal. This technique contrasts with angle modulation, in which either the frequency of the carrier wave is varied, as in [frequency modulation](Frequency%20modulation.md), or its phase, as in phase modulation.

AM was the earliest modulation method used for transmitting audio in radio broadcasting. It was developed during the first quarter of the 20th century, beginning with Roberto Landell de Moura and Reginald Fessenden's radiotelephone experiments in 1900. This original form of AM is sometimes called **double-sideband amplitude modulation** (**DSBAM**), because the standard method produces sidebands on either side of the carrier frequency. [Single-sideband modulation](Single-sideband%20modulation.md) uses bandpass filters to eliminate one of the sidebands and possibly the carrier signal, which improves the ratio of message power to total transmission power, and permits better bandwidth utilization of the transmission medium.

AM remains in use in many forms of communication in addition to AM broadcasting: [shortwave radio](Shortwave%20radio.md), [amateur radio](Amateur%20radio.md), [two-way radios](Two-way%20radio.md), [VHF aircraft radio](Airband.md), [citizens band radio](Citizens%20band%20radio.md), and in computer modems in the form of quadrature amplitude modulation (QAM).

### Foundation

In electronics and telecommunications, modulation is the variation of a property of a [continuous wave](Continuous%20wave.md) carrier signal according to an information-bearing signal, such as an audio signal which represents sound, or a video signal which represents images. In this sense, the carrier wave, which has a much higher frequency than the message signal, *carries* the information. At the receiving station, the message signal is extracted from the modulated carrier by demodulation.

In general form, a modulation process of a sinusoidal carrier wave may be described by the following equation:

$$
m(t) = A(t) \cdot \cos(\omega t + \phi(t))\,
$$

*A(t)* represents the time-varying amplitude of the sinusoidal carrier wave and the cosine-term is the carrier at its angular frequency $$\omega$$, and the instantaneous phase deviation $$\phi(t)$$. This description directly provides the two major groups of modulation, amplitude modulation and angle modulation. In angle modulation, the term *A*(*t*) is constant and the second term of the equation has a functional relationship to the modulating message signal. Angle modulation provides two methods of modulation, [frequency modulation](Frequency%20modulation.md) and phase modulation.

In amplitude modulation, the angle term is held constant and the first term, *A*(*t*), of the equation has a functional relationship to the modulating message signal.

The modulating message signal may be analog in nature, or it may be a digital signal, in which case the technique is generally called amplitude-shift keying.

For example, in AM radio communication, a continuous wave radio-frequency signal has its amplitude modulated by an audio waveform before transmission. The message signal determines the *envelope* of the transmitted waveform. In the frequency domain, amplitude modulation produces a signal with power concentrated at the carrier frequency and two adjacent sidebands. Each sideband is equal in bandwidth to that of the modulating signal, and is a mirror image of the other. Standard AM is thus sometimes called "double-sideband amplitude modulation" (DSBAM).

A disadvantage of all amplitude modulation techniques, not only standard AM, is that the receiver amplifies and detects noise and electromagnetic interference in equal proportion to the signal. Increasing the received signal-to-noise ratio, say, by a factor of 10 (a 10 [decibel](Decibel.md) improvement), thus would require increasing the transmitter power by a factor of 10. This is in contrast to [frequency modulation](Frequency%20modulation.md) (FM) and digital radio where the effect of such noise following demodulation is strongly reduced so long as the received signal is well above the threshold for reception. For this reason AM broadcast is not favored for music and high fidelity broadcasting, but rather for voice communications and broadcasts (sports, news, talk radio etc.).

AM is inefficient in power usage, as at least two-thirds of the transmitting power is concentrated in the carrier signal. The carrier signal contains none of the transmitted information (voice, video, data, etc.). Its presence provides a simple means of demodulation using envelope detection, providing a frequency and phase reference for extracting the message signal from the sidebands. In some modulation systems based on AM, a lower transmitter power is required through partial or total elimination of the carrier component, however receivers for these signals are more complex because they must provide a precise carrier frequency reference signal (usually as shifted to the intermediate frequency) from a greatly reduced "pilot" carrier (in reduced-carrier transmission or DSB-RC) to use in the demodulation process. Even with the carrier eliminated in double-sideband suppressed-carrier transmission, carrier regeneration is possible using a Costas phase-locked loop.

This does not work for single-sideband suppressed-carrier transmission (SSB-SC), leading to the characteristic "Donald Duck" sound from such receivers when slightly detuned. Single-sideband AM is nevertheless used widely in [amateur radio](Amateur%20radio.md) and other voice communications because it has power and bandwidth efficiency (cutting the RF bandwidth in half compared to standard AM). On the other hand, in medium wave and short wave broadcasting, standard AM with the full carrier allows for reception using inexpensive receivers. The broadcaster absorbs the extra power cost to greatly increase potential audience.

#### Shift keying

A simple form of digital amplitude modulation which can be used for transmitting binary data is on–off keying, the simplest form of amplitude-shift keying, in which ones and zeros are represented by the presence or absence of a carrier. On–off keying is likewise used by radio amateurs to transmit [Morse code](Morse%20code.md) where it is known as continuous wave (CW) operation, even though the transmission is not strictly "continuous". A more complex form of AM, quadrature amplitude modulation is now more commonly used with digital data, while making more efficient use of the available bandwidth.

#### Analog telephony

A simple form of amplitude modulation is the transmission of speech signals from a traditional analog telephone set using a common battery local loop. The direct current provided by the central office battery is a carrier with a frequency of 0 Hz. It is modulated by a microphone (*transmitter*) in the telephone set according to the acoustic signal from the speaker. The result is a varying amplitude direct current, whose AC-component is the speech signal extracted at the central office for transmission to another subscriber.

#### Amplitude reference

An additional function provided by the carrier in standard AM, but which is lost in either single or double-sideband suppressed-carrier transmission, is that it provides an amplitude reference. In the receiver, the automatic gain control (AGC) responds to the carrier so that the reproduced audio level stays in a fixed proportion to the original modulation. On the other hand, with suppressed-carrier transmissions there is *no* transmitted power during pauses in the modulation, so the AGC must respond to peaks of the transmitted power during peaks in the modulation. This typically involves a so-called *fast attack, slow decay* circuit which holds the AGC level for a second or more following such peaks, in between syllables or short pauses in the program. This is very acceptable for communications radios, where compression of the audio aids intelligibility. However, it is absolutely undesired for music or normal broadcast programming, where a faithful reproduction of the original program, including its varying modulation levels, is expected.

### ITU type designations

In 1982, the International Telecommunication Union (ITU) designated the types of amplitude modulation:

- Designation  Description
- A3E  double-sideband a full-carrier – the basic amplitude modulation scheme
- R3E  single-sideband reduced-carrier
- H3E  single-sideband full-carrier
- J3E  single-sideband suppressed-carrier
- B8E  independent-sideband emission
- C3F  vestigial-sideband
- Lincompex  linked compressor and expander (a submode of any of the above ITU Emission Modes)

### Analysis

The carrier wave (sine wave) of frequency *fc* and amplitude *A* is expressed by

$$
c(t) = A \sin(2 \pi f_c t)\,
$$

The message signal, such as an audio signal that is used for modulating the carrier, is *m*(*t*), and has a frequency *fm*, much lower than *fc*:

$$
m(t) = M \cos\left(2\pi f_m t + \phi\right)= Am \cos\left(2\pi f_m t + \phi\right)\,
$$

where *m* is the amplitude sensitivity, *M* is the amplitude of modulation. If *m* < 1, *(1 + m(t)/A)* is always positive for undermodulation. If *m* > 1 then overmodulation occurs and reconstruction of message signal from the transmitted signal would lead in loss of original signal. Amplitude modulation results when the carrier *c(t)* is multiplied by the positive quantity *(1 + m(t)/A)*:

$$
\begin{align} y(t) &= \left[1 + \frac{m(t)}{A}\right] c(t) \\ &= \left[1 + m \cos\left(2\pi f_m t + \phi\right)\right] A \sin\left(2\pi f_c t\right) \end{align}
$$

In this simple case *m* is identical to the modulation index, discussed below. With *m* = 0.5 the amplitude modulated signal *y*(*t*) thus corresponds to the top graph (labelled "50% Modulation") in figure 4.

Using prosthaphaeresis identities, *y*(*t*) can be shown to be the sum of three sine waves:

$$
y(t) = A \sin(2\pi f_c t) + \frac{1}{2}Am\left[\sin\left(2\pi \left[f_c + f_m\right] t + \phi\right) + \sin\left(2\pi \left[f_c - f_m\right] t - \phi\right)\right].\,
$$

Therefore, the modulated signal has three components: the carrier wave *c(t)* which is unchanged in frequency, and two sidebands with frequencies slightly above and below the carrier frequency *fc*.

### Spectrum

A useful modulation signal *m(t)* is usually more complex than a single sine wave, as treated above. However, by the principle of Fourier decomposition, *m(t)* can be expressed as the sum of a set of sine waves of various frequencies, amplitudes, and phases. Carrying out the multiplication of *1 + m(t)* with *c(t)* as above, the result consists of a sum of sine waves. Again, the carrier *c(t)* is present unchanged, but each frequency component of *m* at *fi* has two sidebands at frequencies *fc + fi* and *fc – fi*. The collection of the former frequencies above the carrier frequency is known as the upper sideband, and those below constitute the lower sideband. The modulation *m(t)* may be considered to consist of an equal mix of positive and negative frequency components, as shown in the top of figure 2. One can view the sidebands as that modulation *m(t)* having simply been shifted in frequency by *fc* as depicted at the bottom right of figure 2.

The short-term spectrum of modulation, changing as it would for a human voice for instance, the frequency content (horizontal axis) may be plotted as a function of time (vertical axis), as in figure 3. It can again be seen that as the modulation frequency content varies, an upper sideband is generated according to those frequencies shifted *above* the carrier frequency, and the same content mirror-imaged in the lower sideband below the carrier frequency. At all times, the carrier itself remains constant, and of greater power than the total sideband power.

### Power and spectrum efficiency

The RF bandwidth of an AM transmission (refer to figure 2, but only considering positive frequencies) is twice the bandwidth of the modulating (or "baseband") signal, since the upper and lower sidebands around the carrier frequency each have a bandwidth as wide as the highest modulating frequency. Although the bandwidth of an AM signal is narrower than one using [frequency modulation](Frequency%20modulation.md) (FM), it is twice as wide as single-sideband techniques; it thus may be viewed as spectrally inefficient. Within a frequency band, only half as many transmissions (or "channels") can thus be accommodated. For this reason analog television employs a variant of single-sideband (known as vestigial sideband, somewhat of a compromise in terms of bandwidth) in order to reduce the required channel spacing.

Another improvement over standard AM is obtained through reduction or suppression of the carrier component of the modulated spectrum. In figure 2 this is the spike in between the sidebands; even with full (100%) sine wave modulation, the power in the carrier component is twice that in the sidebands, yet it carries no unique information. Thus there is a great advantage in efficiency in reducing or totally suppressing the carrier, either in conjunction with elimination of one sideband (single-sideband suppressed-carrier transmission) or with both sidebands remaining (double sideband suppressed carrier). While these suppressed carrier transmissions are efficient in terms of transmitter power, they require more sophisticated receivers employing synchronous detection and regeneration of the carrier frequency. For that reason, standard AM continues to be widely used, especially in broadcast transmission, to allow for the use of inexpensive receivers using envelope detection. Even (analog) television, with a (largely) suppressed lower sideband, includes sufficient carrier power for use of envelope detection. But for communications systems where both transmitters and receivers can be optimized, suppression of both one sideband and the carrier represent a net advantage and are frequently employed.

A technique used widely in broadcast AM transmitters is an application of the Hapburg carrier, first proposed in the 1930s but impractical with the technology then available. During periods of low modulation the carrier power would be reduced and would return to full power during periods of high modulation levels. This has the effect of reducing the overall power demand of the transmitter and is most effective on speech type programmes. Various trade names are used for its implementation by the transmitter manufacturers from the late 80's onwards.

### Modulation index

The AM modulation index is a measure based on the ratio of the modulation excursions of the RF signal to the level of the unmodulated carrier. It is thus defined as:

$$
m = \frac{\mathrm{peak\ value\ of\ } m(t)}{A} = \frac{M}{A}
$$

where $$M\,$$ and $$A\,$$ are the modulation amplitude and carrier amplitude, respectively; the modulation amplitude is the peak (positive or negative) change in the RF amplitude from its unmodulated value. Modulation index is normally expressed as a percentage, and may be displayed on a meter connected to an AM transmitter.

So if $$m=0.5$$, carrier amplitude varies by 50% above (and below) its unmodulated level, as is shown in the first waveform, below. For $$m=1.0$$, it varies by 100% as shown in the illustration below it. With 100% modulation the wave amplitude sometimes reaches zero, and this represents full modulation using standard AM and is often a target (in order to obtain the highest possible signal-to-noise ratio) but mustn't be exceeded. Increasing the modulating signal beyond that point, known as overmodulation, causes a standard AM modulator (see below) to fail, as the negative excursions of the wave envelope cannot become less than zero, resulting in distortion ("clipping") of the received modulation. Transmitters typically incorporate a limiter circuit to avoid overmodulation, and/or a compressor circuit (especially for voice communications) in order to still approach 100% modulation for maximum intelligibility above the noise. Such circuits are sometimes referred to as a vogad.

However it is possible to talk about a modulation index exceeding 100%, without introducing distortion, in the case of double-sideband reduced-carrier transmission. In that case, negative excursions beyond zero entail a reversal of the carrier phase, as shown in the third waveform below. This cannot be produced using the efficient high-level (output stage) modulation techniques (see below) which are widely used especially in high power broadcast transmitters. Rather, a special modulator produces such a waveform at a low level followed by a linear amplifier. What's more, a standard AM receiver using an envelope detector is incapable of properly demodulating such a signal. Rather, synchronous detection is required.

Thus double-sideband transmission is generally *not* referred to as "AM" even though it generates an identical RF waveform as standard AM as long as the modulation index is below 100%. Such systems more often attempt a radical reduction of the carrier level compared to the sidebands (where the useful information is present) to the point of double-sideband suppressed-carrier transmission where the carrier is (ideally) reduced to zero. In all such cases the term "modulation index" loses its value as it refers to the ratio of the modulation amplitude to a rather small (or zero) remaining carrier amplitude.

### Modulation methods

Modulation circuit designs may be classified as low- or high-level (depending on whether they modulate in a low-power domain—followed by amplification for transmission—or in the high-power domain of the transmitted signal).

#### Low-level generation

In modern radio systems, modulated signals are generated via digital signal processing (DSP). With DSP many types of AM are possible with software control (including DSB with carrier, SSB suppressed-carrier and independent sideband, or ISB). Calculated digital samples are converted to voltages with a digital-to-analog converter, typically at a frequency less than the desired RF-output frequency. The analog signal must then be shifted in frequency and linearly amplified to the desired frequency and power level (linear amplification must be used to prevent modulation distortion). This low-level method for AM is used in many Amateur Radio transceivers.

AM may also be generated at a low level, using analog methods described in the next section.

#### High-level generation

Modern high-power AM transmitters (such as those used for AM broadcasting) are based on high-efficiency class-D and class-E power amplifier stages.

Older designs (for broadcast and amateur radio) also generate AM by controlling the gain of the transmitter's final amplifier (generally class-C, for efficiency), reflecting the strong emphasis on improving efficiency in early high-power transmitters. The following types are for vacuum tube transmitters, but similar options are available with transistors:

**Plate modulation**  — In plate modulation, the plate voltage of the RF amplifier is modulated with the audio signal. The audio power requirement is 50 percent of the RF-carrier power.

**Heising (constant-current) modulation**  — RF amplifier plate voltage is fed through a choke (high-value inductor). The AM modulation tube plate is fed through the same inductor, so the modulator tube diverts current from the RF amplifier. The choke acts as a constant current source in the audio range. This system has a low power efficiency.

**Control grid modulation**  — The operating bias and gain of the final RF amplifier can be controlled by varying the voltage of the control grid. This method requires little audio power, but care must be taken to reduce distortion.

**Clamp tube (screen grid) modulation**  — The screen-grid bias may be controlled through a *clamp tube*, which reduces voltage according to the modulation signal. It is difficult to approach 100-percent modulation while maintaining low distortion with this system.

**Doherty modulation**  — A two-tube AM amplifier in which the first tube provides the power under carrier conditions, while a second operates only for positive modulation peaks. A quarter-wave impedance inverter between the two varies the load seen by the first tube over the modulation cycle. As originally described by Doherty, the system is not itself a modulator but a high-efficiency linear power amplifier that requires a pre-modulated RF signal to drive the grids. Overall efficiency is good, and distortion is low.

**Outphasing modulation**  — Two tubes are operated in parallel, but partially out of phase with each other. As they are differentially phase modulated their combined amplitude is greater or smaller. Efficiency is good and distortion low when properly adjusted.

**Pulse-width modulation (PWM) or pulse-duration modulation (PDM)**  — A highly efficient high voltage power supply is applied to the tube plate. The output voltage of this supply is varied at an audio rate to follow the program. This system was pioneered by Hilmer Swanson and has a number of variations, all of which achieve high efficiency and sound quality.

**Digital methods**  — The Harris Corporation obtained a patent for synthesizing a modulated high-power carrier wave from a set of digitally selected low-power amplifiers, running in phase at the same carrier frequency. The input signal is sampled by a conventional audio analog-to-digital converter (ADC), and fed to a digital exciter, which modulates overall transmitter output power by switching a series of low-power solid-state RF amplifiers on and off. The combined output drives the antenna system.

### Demodulation methods

The simplest form of an AM demodulator consists of a diode configured as an envelope detector. As described by Frederick Terman in 1943, the diode rectifier was the most widely used detector for AM signals, providing a simple means of recovering the modulation envelope. In 1904, John Ambrose Fleming developed such a circuit for a radio-wave detector in the [crystal radio](Crystal%20radio.md). Adding variable capacitors to the crystal detector enables tuning to a specific frequency.

Another type of demodulator, the product detector, can provide better-quality demodulation with additional circuit complexity.

---

*Source: Wikipedia, Amplitude modulation (https://en.wikipedia.org/wiki/Amplitude_modulation), by Wikipedia contributors, CC BY-SA 4.0.*
