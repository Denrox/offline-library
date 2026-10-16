# Single-sideband modulation

In radio communications, **single-sideband modulation** (**SSB**) or **single-sideband suppressed-carrier modulation** (**SSB-SC**) is a type of signal modulation used to transmit information, such as an audio signal, by radio waves. A refinement of [amplitude modulation](Amplitude%20modulation.md), it uses transmitter power and bandwidth more efficiently. Amplitude modulation produces an output signal the bandwidth of which is twice the maximum frequency of the original baseband signal. Single-sideband modulation avoids this bandwidth increase, and the power wasted on a carrier, at the cost of increased device complexity and more difficult tuning at the receiver.

### Basic concept

In conventional amplitude modulation (AM), an audio signal controls the amplitude of a radio-frequency carrier, producing a carrier plus two mirror-image sidebands. Each sideband contains a complete copy of the original information, while the carrier itself conveys none. Consequently, an AM signal occupies a bandwidth equal to twice the highest audio frequency and expends a large fraction of the transmitted power on the carrier and redundant sideband. This spectral structure of AM is described in classic radio texts, including Everitt's treatments of modulation theory.

Single-sideband modulation (SSB) is derived directly from AM by removing this redundancy. Since either sideband alone contains the entire modulating signal, SSB transmits only one sideband and usually suppresses the carrier. Compared with AM, SSB requires approximately half the bandwidth and uses transmitter power more efficiently. SSB signals are typically generated at low power using filtering or phase-cancellation techniques and then amplified linearly.

Because the carrier is suppressed, SSB reception requires reinsertion of a locally generated carrier and greater frequency stability than AM. AM can be generated and received with relatively simple equipment, while SSB is used primarily where efficiency and range are important. In amateur radio, prior to widespread digital voice, most HF voice operation moved from AM to SSB.

### Mathematical formulation

Single-sideband has the mathematical form of quadrature amplitude modulation (QAM) in the special case where one of the baseband waveforms is derived from the other, instead of being independent messages**:**

- $$s_\text{usb}(t) = s(t) \cdot \cos\left(2\pi f_0 t\right) - \widehat{s}(t)\cdot \sin\left(2\pi f_0 t\right),\,$$

where $$s(t)\,$$ is the message (real-valued), $$\widehat{s}(t)\,$$ is its Hilbert transform, and $$f_0\,$$ is the radio carrier frequency.

To understand this formula, we may express $$s(t)$$ as the real part of a complex-valued function, with no loss of information:

$$
s(t) = \operatorname{Re}\left\{s_\mathrm{a}(t)\right\} = \operatorname{Re}\left\{s(t) + j \cdot \widehat{s}(t)\right\},
$$

where $$j$$ represents the imaginary unit. $$s_\mathrm{a}(t)$$ is the analytic representation of $$s(t),$$ which means that it comprises only the positive-frequency components of $$s(t)$$:

$$
\frac{1}{2}S_\mathrm{a}(f) = \begin{cases} S(f), &\text{for}\ f > 0,\\ 0, &\text{for}\ f < 0, \end{cases}
$$

where $$S_\mathrm{a}(f)$$ and $$S(f)$$ are the respective Fourier transforms of $$s_\mathrm{a}(t)$$ and $$s(t).$$ Therefore, the frequency-translated function $$S_\mathrm{a}\left(f - f_0\right)$$ contains only one side of $$S(f).$$ Since it also has only positive-frequency components, its inverse Fourier transform is the analytic representation of $$s_\text{usb}(t):$$

$$
s_\text{usb}(t) + j \cdot \widehat{s}_\text{ssb}(t) = \mathcal{F}^{-1} \{S_\mathrm{a}\left(f - f_0\right)\} = s_\mathrm{a}(t) \cdot e^{j2\pi f_0 t},\,
$$

and again the real part of this expression causes no loss of information. With Euler's formula to expand $$e^{j2\pi f_0 t},\,$$ we obtain **Eq.1**:

$$
\begin{align} s_\text{usb}(t) &= \operatorname{Re}\left\{s_\mathrm{a}(t)\cdot e^{j2\pi f_0 t}\right\} \\ &= \operatorname{Re}\left\{\,\left[s(t) + j \cdot \widehat{s}(t)\right] \cdot \left[\cos\left(2\pi f_0 t\right) + j \cdot \sin\left(2\pi f_0 t\right)\right]\,\right\} \\ &= s(t) \cdot \cos\left(2\pi f_0 t\right) - \widehat{s}(t) \cdot \sin\left(2\pi f_0 t\right). \end{align}
$$

Coherent demodulation of $$s_\text{ssb}(t)$$ to recover $$s(t)$$ is the same as AM: multiply by $$\cos\left(2\pi f_0 t\right),$$ and lowpass to remove the "double-frequency" components around frequency $$2 f_0$$. If the demodulating carrier is not in the correct phase (cosine phase here), then the demodulated signal will be some linear combination of $$s(t)$$ and $$\widehat s(t)$$, which is usually acceptable in voice communications (if the demodulation carrier frequency is not quite right, the phase will be drifting cyclically, which again is usually acceptable in voice communications if the frequency error is small enough, and amateur radio operators are sometimes tolerant of even larger frequency errors that cause unnatural-sounding pitch shifting effects).

#### Lower sideband

$$s(t)$$ can also be recovered as the real part of the complex-conjugate, $$s_\mathrm{a}^*(t),$$ which represents the negative frequency portion of $$S(f).$$ When $$f_0\,$$ is large enough that $$S\left(f - f_0\right)$$ has no negative frequencies, the product $$s_\mathrm{a}^*(t) \cdot e^{j2\pi f_0 t}$$ is another analytic signal, whose real part is the actual *lower-sideband* transmission**:**

$$
\begin{align} s_\mathrm{a}^*(t)\cdot e^{j2\pi f_0 t} &= s_\text{lsb}(t) + j \cdot \widehat s_\text{lsb}(t) \\ \Rightarrow s_\text{lsb}(t) &= \operatorname{Re}\left\{s_\mathrm{a}^*(t) \cdot e^{j2\pi f_0 t}\right\} \\ &= s(t) \cdot \cos\left(2\pi f_0 t\right) + \widehat{s}(t) \cdot \sin\left(2\pi f_0 t\right). \end{align}
$$

The sum of the two sideband signals is:

$$
s_\text{usb}(t) + s_\text{lsb}(t) = 2s(t) \cdot \cos\left(2\pi f_0 t\right),\,
$$

which is the classic model of suppressed-carrier double sideband AM.

### Practical implementations and considerations

#### Bandpass filtering

One method of producing an SSB signal is to remove one of the sidebands via filtering, often by a crystal filter, leaving only either the **upper sideband** (**USB**), the sideband with the higher frequency, or less commonly the **lower sideband** (**LSB**), the sideband with the lower frequency. Most often, the carrier is reduced or removed entirely (suppressed), being referred to in full as **single sideband suppressed carrier** (**SSBSC**). Assuming both sidebands are symmetric, which is the case for a normal [AM](Amplitude%20modulation.md) signal, no information is lost in the process. Since the final RF amplification is now concentrated in a single sideband, the effective power output is greater than in normal AM (the carrier and redundant sideband account for well over half of the power output of an AM transmitter). Though SSB uses substantially less bandwidth and power, it cannot be demodulated by a simple envelope detector like standard AM.

#### Hartley modulator

In addition to filter-based approaches, single-sideband signals can be generated by the **phasing method**, which uses phase relationships to cancel one sideband. The approach was described in Ralph V. L. Hartley's 1928 patent, which outlined generating single-sideband suppressed-carrier (SSBSC) signals by combining two paths of the modulating signal with a 90° phase difference and carrier signals in quadrature, so that one sideband reinforces and the other cancels. In practice, the audio is split into two channels with a 90° phase difference, each channel driving a balanced modulator fed by one of two quadrature carrier signals. When the two modulator outputs are summed or differenced, the unwanted sideband is cancelled, producing a single-sideband signal without the need for sharp RF filtering. The method was popular in the days of vacuum tube radios, but later gained a bad reputation due to poorly adjusted commercial implementations. Modulation using this method is again gaining popularity in the homebrew and DSP fields.

In 1946, R. B. Dome published low-component-count all-pass RC phase-shift networks in *Electronics* magazine, including a six-resistor, six-capacitor circuit suitable for voice communications using the Hartley phasing method. Experimental amateur implementations soon followed, with *QST* reporting phasing-based SSB transmitters and receivers in the late 1940s. In 1954, Stanford University student Donald K. Weaver published in *IRE Transactions* network-synthesis techniques for designing arbitrary all-pass phase-shift networks, including Chebyshev-optimized realizations. He presented a mathematical derivation of the 6R–6C network and showed that the approach could be extended to wider bandwidths, including full audio bandwidth if desired. This work formalized the design of audio phase networks; Weaver's later modulation method, which avoids audio quadrature networks entirely, is described separately.

This method, utilizing the Hilbert transform to phase shift the baseband audio, can be done at low cost with digital circuitry.

#### Weaver modulator

Another variation, the Weaver modulator, uses low-pass filtering combined with two stages of quadrature frequency translation. Weaver described this approach in “A Third Method of Generation and Detection of Single-Sideband Signals” (*Proceedings of the IRE*, December 1956), published two years after his early phasing paper.

In Weaver's method, the band of interest is prefiltered, removing low frequencies (for speech, typically below about 300 Hz). The signal is then translated upward by quadrature modulation at a convenient offset (for speech, commonly around 2 kHz). This produces a complex signal in which the desired sideband appears at lower frequencies while the unwanted sideband appears at higher frequency.

This initial translation creates a spectral gap (in the speech example, from 1.7 kHz to 2.3 kHz), which simplifies low-pass filter design. A matched pair of low-pass filters (one in each quadrature path) removes the undesired sideband. Finally, the resulting single-sideband signal is translated a second time, using another pair of quadrature mixers, to the desired radio-frequency.

#### SSB tuning

Since SSB-SC has no carrier for the receiver to reference, receivers must use BFOs for demodulation. Therefore, both the transmitter and receiver must have very accurate tuning (with a tolerance of approximately ±125Hz for voice). If either part of the system isn't inside this tight range, voice can either sound metallic and robotic if the receiver is below the transmitter frequency in USB and vice versa on LSB, or what can be better described as if the speaker had inhaled helium if the receiver is above/below the transmitter using the same logic. The narrow latitude also causes frequency drifts affect considerably the quality, requiring periodic retuning in some cases.

### Demodulation

The front end of an SSB receiver is similar to that of an [AM](Amplitude%20modulation.md) or [FM](Frequency%20modulation.md) receiver, consisting of a superheterodyne RF front end that produces a frequency-shifted version of the radio frequency (RF) signal within a standard intermediate frequency (IF) band.

To recover the original signal from the IF SSB signal, the single sideband must be frequency-shifted down to its original range of baseband frequencies, by using a product detector which mixes it with the output of a beat frequency oscillator (BFO). In other words, it is just another stage of heterodyning. For this to work, the BFO frequency must be exactly adjusted. If the BFO frequency is off by more than 30 Hz, the output signal will be frequency-shifted (up or down), making speech sound strange and "Donald Duck"-like.

As an example, consider an IF SSB signal centered at frequency $$F_{\text{if}}\,$$ = 45000 Hz. The baseband frequency it needs to be shifted to is $$F_b\,$$ = 2000 Hz. The BFO output waveform is $$\cos\left(2\pi \cdot F_{\text{bfo}} \cdot t\right)$$. When the signal is multiplied by (aka *heterodyned with*) the BFO waveform, it shifts the signal to $$\left(F_{\text{if}} + F_{\text{bfo}}\right)$$, *and* to $$\left|F_{\text{if}} - F_{\text{bfo}}\right|$$, which is known as the *beat frequency* or *image frequency*. The objective is to choose an $$F_{\text{bfo}}$$ that results in $$\left|F_{\text{if}} - F_{\text{bfo}}\right| = F_b\,$$ = 2000 Hz. (The unwanted components at $$\left(F_{\text{if}} + F_{\text{bfo}}\right)\,$$ can be removed by a lowpass filter; for which an output transducer or the human ear may serve).

There are two choices for $$F_{\text{bfo}}$$: 43000 Hz and 47000 Hz, called *low-side* and *high-side* injection. With high-side injection, the spectral components that were distributed around 45000 Hz will be distributed around 2000 Hz in the reverse order, also known as an inverted spectrum. That is in fact desirable when the IF spectrum is also inverted, because the BFO inversion restores the proper relationships. One reason for that is when the IF spectrum is the output of an inverting stage in the receiver. Another reason is when the SSB signal is actually a lower sideband, instead of an upper sideband. But if both reasons are true, then the IF spectrum is not inverted, and the non-inverting BFO (43000 Hz) should be used.

### SSB as a speech-scrambling technique

During WWII, spectral inversion techniques related to SSB were sometimes used to scramble voice but it was very easily defeated. The need for secure communications between Franklin D. Roosevelt, Harry Truman, and Winston Churchill led to the development of the first digital vocoder system SIGSALY by Bell Telephone Laboratories.

### Suppressed carrier (SSB-SC), double-sideband suppressed carrier (DSB-SC), and vestigial sideband (VSB)

Single sideband is also referred to as single sideband suppressed carrier, in which the carrier and one sideband are suppressed by frequency or phase (Hilbert Transform) discrimination. Though more complex and costly, it is used for two-point dedicated communications requiring less bandwidth and power. In double sideband suppressed carrier, only the carrier is suppressed, generating one hundred percent modulation efficiency, but with additional cost and complexity. It is used for television and FM stereo broadcasts. A vestigial sideband has been only partly suppressed, with only 25 to 30 percent of one bandwidth being used. It is used for television.

### Compatible single side-band

A compatible transmission refers to one in which the receiver is capable of instantaneous amplitude demodulation. This could be a double sideband or a single sideband transmission. As an example, Leonard R. Kahn introduced an independent sideband (ISB) stereo scheme, in which the lower sideband transmitted the left channel, and the upper sideband the right. Kahn commercialized this AM stereo as the STR-77 and STR-84.

### Frequencies for LSB and USB in amateur radio voice communication

When single-sideband is used in amateur radio voice communications, it is common practice that for frequencies below 10 MHz, lower sideband (LSB) is used and for frequencies of 10 MHz and above, upper sideband (USB) is used. For example, on the 40 m band, voice communications often take place around 7.100 MHz using LSB mode. On the 20 m band at 14.200 MHz, USB mode would be used.

An exception to this rule applies to the five discrete amateur channels on the 60-meter band (near 5.3 MHz) where FCC rules specifically require USB.

### Extended single sideband (eSSB)

Extended single sideband is any J3E (SSB-SC) mode that exceeds the audio bandwidth of standard or traditional 2.9 kHz SSB J3E modes (ITU 2K90J3E) to support higher-quality sound.

- Extended SSB modes  Bandwidth  Frequency response  ITU Designator
- eSSB (Narrow-1a)  3 kHz  100 Hz ~ 3.10 kHz  3K00J3E
- eSSB (Narrow-1b)  3 kHz  50 Hz ~ 3.05 kHz  3K00J3E
- eSSB (Narrow-2)  3.5 kHz  50 Hz ~ 3.55 kHz  3K50J3E
- eSSB (Medium-1)  4 kHz  50 Hz ~ 4.05 kHz  4K00J3E
- eSSB (Medium-2)  4.5 kHz  50 Hz ~ 4.55 kHz  4K50J3E
- eSSB (Wide-1)  5 kHz  50 Hz ~ 5.05 kHz  5K00J3E
- eSSB (Wide-2)  6 kHz  50 Hz ~ 6.05 kHz  6K00J3E

### Amplitude-companded single-sideband modulation (ACSSB)

Amplitude-companded single sideband (ACSSB) is a narrowband modulation method using a single sideband with a pilot tone, allowing an expander in the receiver to restore the amplitude that was severely compressed by the transmitter. It offers improved effective range over standard SSB modulation while simultaneously retaining backwards compatibility with standard SSB radios. ACSSB also offers reduced bandwidth and improved range for a given power level compared with narrow band FM modulation.

### Controlled-envelope single-sideband modulation (CESSB)

SSB can produce envelope peaks well above the average for a sinusoidal tone, even when the audio signal is peak-limited. An AM signal is purely real, ie, it lies entirely on the I (in-phase) axis but suppressing one sideband creates a Q (quadrature or imaginary) component consisting of the Hilbert transform of the I channel component. The impulse response of the Hilbert transform theoretically goes to infinity just above and below time zero so the combined amplitude $$\sqrt{I^2 + Q^2}$$, for certain modulating waveforms, can have very high peaks. For example, an ideal SSB transmission of a pure square wave has an infinite peak to average power ratio. Suitable overshoot compensation (so-called controlled-envelope single-sideband modulation or CESSB) achieves about 3.8 dB of peak reduction for speech transmission. This results in an effective average power increase of about 140%. Although the generation of the CESSB signal can be integrated into the SSB modulator, it is feasible to separate the generation of the CESSB signal (e.g. in form of an external speech preprocessor) from a standard SSB radio. This requires that the standard SSB radio's modulator be linear-phase and have a sufficient bandwidth to pass the CESSB signal. If a standard SSB modulator meets these requirements, then the envelope control by the CESSB process is preserved.

### ITU designations

In 1982, the International Telecommunication Union (ITU) designated the types of amplitude modulation:

- Designation   Description
- A3E  Double-sideband full-carrier – the basic amplitude-modulation scheme
- R3E  Single-sideband reduced-carrier
- H3E  Single-sideband full-carrier
- J3E  Single-sideband suppressed-carrier
- B8E  Independent-sideband emission
- C3F  Vestigial-sideband
- Lincompex  Linked compressor and expander

### SSB bandwidth reduction

The occupied bandwidth of single-sideband (SSB) and other AM-derived modulation techniques can be reduced by compressing the transmitted audio spectrum prior to modulation. One approach investigated in the 1970s was narrow-band voice modulation (NBVM). In NBVM, consonant energy from higher audio frequencies is shifted downward and electronically folded into spectral regions less occupied by vowels during speech, allowing a reduction in transmitted audio bandwidth while maintaining intelligibility.

NBVM was reported in the amateur radio literature in the late 1970s and evaluated experimentally on HF SSB links, with intelligible speech reported at audio bandwidths on the order of 1–1.5 kHz under favorable conditions. Related techniques were also described in the professional literature, including results presented at ICASSP in 1977. Unlike later low-bit-rate digital speech codecs, NBVM operated entirely within an analog SSB framework.

---

*Source: Wikipedia, Single-sideband modulation (https://en.wikipedia.org/wiki/Single-sideband_modulation), by Wikipedia contributors, CC BY-SA 4.0.*
