# PSK31

**PSK31** or "Phase Shift Keying, 31 Baud", also **BPSK31** and **QPSK31**, is a popular computer-sound card-generated [radioteletype](Radioteletype.md) mode, used primarily by [amateur radio operators](Amateur%20radio%20operator.md) to conduct real-time keyboard-to-keyboard chat, most often using frequencies in the [high frequency](High%20frequency.md) amateur radio bands (shortwave). PSK31 is distinguished from other digital modes in that it is specifically tuned to have a data rate close to typing speed, and has an extremely narrow bandwidth, allowing many conversations in the same bandwidth as a single voice channel. This narrow bandwidth makes better use of the radio frequency (RF) energy in a very narrow space thus allowing relatively low-power equipment (5 watts) to communicate globally using the same [skywave](Skywave.md) [propagation](Radio%20propagation.md) used by [shortwave radio stations](Shortwave%20listening.md).

The International Telecommunication Union designates this type of emission as 60H0J2B, often abbreviated as J2B.

### Use and implementation

A PSK31 operator typically uses a [single-sideband](Single-sideband%20modulation.md) (SSB) transceiver connected to the sound card of a computer running PSK31 software. When the operator enters a message for transmission, the software produces an audio tone that sounds, to the human ear, like a continuous whistle with a slight warble. This sound is then fed through either a microphone jack (using an intermediate resistive attenuator to reduce the sound card's output power to microphone levels) or an auxiliary connection into the transceiver, from which it is transmitted.

From the perspective of the transmitter, the sound amounts to little more than somebody whistling into the microphone. However, the software rapidly shifts the phase of the audio signal between two states (hence the name "phase-shift keying"), forming the character codes. These phase shifts serve the same function as the two tones used in traditional RTTY and similar systems.

To decode PSK31, the audio whistle received from the transceiver's headphone output is fed into a computer sound card's audio input, and software decodes it. The software displays the decoded text.

Because PSK31 was developed for use through a computer's sound card, many programs have since been created to use the same technology for other modes, such as RTTY, Hellschreiber, and Olivia MFSK. So, once it has been set up to run PSK31, a computer can be used for a variety of digital message transmission modes.

Aside from a standard radio transceiver and a computer with a sound card, very little equipment is required to use PSK31. Normally, an older computer and a few cables will suffice, and many PSK31 software applications are free and open source. Many operators now use a commercially available interface/modem device (or "nomic" ) between their computers and radios. These devices incorporate the necessary impedance matching and sound level adjustment to permit the sound card output to be injected into the microphone input, send the radio's audio output to the sound card input, and handle the radio's transmit-receive switching. Sound card to radio interfaces typically use isolation transformers on both the send and receive audio paths to eliminate hum caused by ground-loops. Many interfaces also incorporate their own sound card and can be powered and run from the computer via a single USB connection. Some modern transceivers have these interfaces built in, requiring only a USB connection from the computer to the radio.

### Resistance to interference

Like [other narrow band digital modes](List%20of%20amateur%20radio%20modes.md), PSK31 can often overcome interference and poor [propagation](Radio%20propagation.md) conditions in situations where voice or other methods of communication fail. However, PSK31 was designed only for leisure use by amateurs, and due to its relatively slow speed and limited error control, is not suitable for transmitting large blocks of data or text, or critical data requiring high immunity from errors.

PSK31 works well over propagation paths that preserve phase, and resists fading ([QSB](Q%20code.md)) well. However, it can be adversely affected by propagation modes—such as transpolar paths—where auroral "flutter" or [multipathing](Multipath%20propagation.md) can disrupt the signal phase continuity. In such cases the use of QPSK (see below) is often beneficial.

Some software supports PSK10 and PSK05 variants, running at 10 baud and 5 baud, respectively. These slower speeds sacrifice throughput to provide greater resistance to noise and other interference. Conversely, PSK63 is increasingly used for faster exchanges, especially during amateur radio contest operating.

### Technical information

PSK31 is typically created by software that generates an amplitude- and phase-modulated waveform that is converted to an audio frequency analog signal by a sound card. In the most-commonly-used variant, BPSK31, binary information is transmitted by either imparting a 180-degree phase shift (a binary "zero") or no phase shift (a binary "one") in each 32ms symbol interval. The 180-degree phase shift for a "zero" bit code occurs at a null amplitude.

As shown in the figure, a cosine filter is used to smooth the rise and fall times of the audio waveform and eliminate key clicks. All subsequent amplification of the signal must be linear to preserve the modulation waveform and ensure minimum occupied bandwidth. In practice, this means limiting the transmit audio volume to below the level where the transmitter generates Automatic Level Control (ALC) feedback and disabling any audio compression or speech processing.

The Varicode is a kind of Fibonacci code where the boundaries between character codes are marked by two or more consecutive zeros. Like all Fibonacci codes, since no character code contains more than one consecutive zero, the software can easily identify the spaces between characters, regardless of the length of the character. The idle sequence, sent when an operator is not typing, is a continuous sequence of phase-shifts, which do not print on the screen. Martinez arranged the character alphabet so that, as in [Morse code](Morse%20code.md), the more frequently occurring characters have the shortest encodings, while rarer characters use longer encodings. He named this encoding scheme "varicode".

PSK31's symbol rate of 31.25 Hz was chosen because a normal typing speed of about 50 words per minute requires a bit rate of about 32 bits per second, and specifically because 31.25 Hz could easily be derived from the 8 kHz sample rate used in many DSP systems, including those used in the computer sound cards commonly used for PSK31 operation (31.25 Hz is 8 kHz divided by 256, and so can be derived from 8 kHz by halving the frequency eight times in succession).

### BPSK31 and QPSK31 variants

Colloquial usage of the term 'PSK31' in [amateur radio](Amateur%20radio.md) usually implies the use of the most commonly used variant of PSK31: binary phase shift keying (BPSK). The BPSK variant of PSK31 uses no error control. QPSK31, the variant based on quadrature phase shift keying (QPSK), uses four phases instead of two. It is simple to switch from BPSK to QPSK if difficulties arise during a contact; QPSK31 has the same number of symbols per second, and hence the same bandwidth as the BPSK variant. In a coherent receiver, the bit error probability of QPSK is the same as for BPSK operating at the same power, making QPSK31 the generally preferable mode for the purpose of robustness, and thus reach.

Using four instead of two constellation points provides twice the physical layer bit rate, which allows addition of redundant information to provide a degree of forward error correction. When QPSK is used, after encoding into varicode, the bits of the binary data signal is subject to a rate-1/2 channel code, which means that for every information bit, two code bits are calculated and transmitted. For that, a convolutional code with constraint length 5 (i.e. the last five bits from the input are incorporated to select two output bits per input bit) is used.

The resulting bits are mapped to a quaternary set of phases. At the receiver, a decoder for the convolutional code needs to be used, typically the Viterbi Algorithm, which is able to reconstruct the most likely sent sequence, even if multiple symbols were received incorrectly. Optimal decoding must take into account the same constraint length of information bits as encoding, yielding a 5-symbol decoding delay, which corresponds to 160 ms of delay.

### Spectrum efficiency compared to other modes

PSK31's efficiency and narrow bandwidth make it highly suitable for [low-power](QRP%20operation.md) and crowded-band operation. PSK31 contacts can be conducted at less than 100 Hz separation, so with disciplined operation at least twenty simultaneous PSK31 contacts can be carried out side-by-side in the 2.5 kHz bandwidth required for just one SSB voice contact.

### Common frequencies

The following [amateur radio](Amateur%20radio.md) frequencies are commonly used for transmitting and receiving PSK31 signals. They normally occupy the lower edge of each band's digital modes section. PSK31 operators generally use upper sideband (USB), even on frequencies below 10 MHz where the convention normally calls for lower sideband. This is because (a) signals then spread upwards into the digimode section from the "base" frequency, and (b) using QPSK requires both stations to use the same sideband.

PSK31 Frequencies
- Frequency   [Amateur Band](Amateur%20radio%20frequency%20allocations.md)
- 1.838 MHz   160 meter
- 3.580 MHz   80 meter
- 7.035 MHz*   40 meter *(region 3)*
- 7.040 MHz*   40 meter *(regions 1)*
- 7.070 MHz*   40 meter *(regions 2)*
- 10.142 MHz   30 meter
- 14.070 MHz   20 meter
- 18.097 MHz**   17 meter
- 21.080 MHz*   15 meter
- 24.920 MHz   12 meter
- 28.120 MHz   10 meter
- 50.290 MHz   [6 meter](6-meter%20band.md)
- 144.144 MHz   2 meter
- 222.07 MHz   1.25 meter
- 432.2 MHz   70 centimeter
- 909 MHz   33 centimeter

* Current usage as of 2010, based on observation, is centered on 7,070.15 and 21,070.15. 7,035.15 is commonly used in Region 2 as of 2012. There is no authoritative list, as the frequencies are determined by common convention.

** PSK has moved from 18.100 to 18.097 due to FT8 use of the 18.100 frequency as of November, 2019.

The IARU Region 1 Bandplan was revised in March 2009 to reflect the expanded 40 meter band. The CW-only section within Europe, Africa, the Middle East and the former USSR is now 7.000 to 7.040. Region 2 - The Americas - followed in September 2013. Region 3 - South Asia and Australasia - has not yet synchronised its bandplan with Regions 1 and 2.

---

*Source: Wikipedia, PSK31 (https://en.wikipedia.org/wiki/PSK31), by Wikipedia contributors, CC BY-SA 4.0.*
