# List of amateur radio modes

The following is a list of the modes of radio communication used in the [amateur radio](Amateur%20radio.md) hobby.

### Modes of communication

Amateurs use a variety of voice, text, image, and data communications modes over radio. Generally new modes can be tested in the amateur radio service, although national regulations may require disclosure of a new mode to permit radio licensing authorities to monitor the transmissions. Encryption, for example, is not generally permitted in the Amateur Radio service except for the special purpose of satellite vehicle control uplinks. The following is a partial list of the modes of communication used, where the mode includes both modulation types and operating protocols.

#### Morse code

[Morse code](Morse%20code.md) is called the original digital mode. Radio telegraphy, designed for machine-to-machine communication is the direct on / off keying of a continuous wave carrier by Morse code symbols, often called amplitude-shift keying or ASK, may be considered to be an *[amplitude modulated](Amplitude%20modulation.md)* mode of communications, and is rightfully considered the first digital data mode. Although more than 140 years old, bandwidth-efficient Morse code, originally developed by Samuel Morse and Alfred Vail in the 1840s, uses techniques that were not fully understood until much later under the modern terms of *source coding* or *data compression*.

Alfred Vail intuitively understood efficient code design: The bandwidth-efficiency of Morse code arises because its encodings are variable length, and Vail assigned the shortest encodings to the most-used symbols, and the longest encodings to the least-used symbols. It was not until one hundred years later that Shannon's modern information theory (1948) described Vail's coding technique for Morse code, giving it a firm footing in a mathematically based theory. Shannon's information theory resulted in similarly efficient data encoding technologies which use bandwidth like Morse code, such as the modern Huffman, Arithmetic, and Lempel-Ziv codes.

Although commercial telegraphy ended in the late 20th century, Morse code remains in use by [amateur radio operators](Amateur%20radio%20operator.md). Operators may either key the code manually using a telegraph key and decode by ear, or they may use computers to send and receive the code.

- [Continuous wave](Continuous%20wave.md) (CW)
- Modulated continuous wave (MCW) is most often used by [repeaters](Amateur%20radio%20repeater.md) for identification.
- [Frequency-shift keying](Frequency-shift%20keying.md) (FSK) dots and dashes are transmitted as different frequency continuous waves, for easier reception in noisy conditions.

#### Analog voice

Decades after the advent of digital amplitude-shift keying (ASK) of radio carriers by Morse symbols, radio technology evolved several methods of analog modulating radio carriers such as: amplitude, frequency and phase modulation by analog waveforms. The first such analog modulating waveforms applied to radio carriers were human voice signals picked up by microphone sensors and applied to the carrier waveforms. The resulting analog voice modes are known today as:

- [Amplitude modulation](Amplitude%20modulation.md) (AM)
- Double-sideband suppressed carrier (DSB-SC)
- Independent sideband (ISB)
- [Single sideband](Single-sideband%20modulation.md) (SSB)
- Compatible sideband transmission, also called amplitude modulation equivalent (AME)
- [Frequency modulation](Frequency%20modulation.md) (FM)
- Phase modulation (PM)

#### Digital voice

Digital voice modes encode speech into a data stream before transmitting it.

- APCO P25 - Found in repurposed public safety equipment from multiple vendors. Uses IMBE or AMBE CODEC over [FSK](Frequency-shift%20keying.md).
- [D-STAR](D-STAR.md) - Open specification with proprietary vocoder system available from [Icom](Icom%20Incorporated.md), Kenwood, and FlexRadio Systems. Uses AMBE over GMSK with VoIP capabilities.
- DMR - Found in both commercial and public safety equipment from multiple vendors. Uses AMBE codec over a [FSK](Frequency-shift%20keying.md) modulation variant with TDMA.
- [NXDN](NXDN.md): Used primarily in commercial 2-way (particularly railroads). Equipment is available from multiple manufacturers. NXDN uses FDMA with bandwidths of 6.25 kHz common.
- System Fusion - Open specification with proprietary vocoder system available from [Yaesu](Yaesu%20%28brand%29.md). Uses AMBE voice codec with [4FSK](Frequency-shift%20keying.md) modulation. In Japan, known as *WIRES*.
- FreeDV - Narrow bandwidth, open source digital voice mode. Uses Codec 2 with differential or coherent PSK modulation, as well as the new experimental high-fidelity Radio Autoencoder (RADE) based on the Framewise Autoregressive GAN (FARGAN) ML vocoder.
- [M17](M17%20%28amateur%20radio%29.md) - Another open source digital voice mode based on Codec 2. Uses [4FSK](Frequency-shift%20keying.md). Utilizes punctured convolutional coding and quadratic permutation polynomials for error control and bit stream re-ordering.

#### Image

Image modes consist of sending either video or still images.

- Amateur television, also known as Fast Scan television (ATV)
- [Slow-scan television](Slow-scan%20television.md) (SSTV)
- Facsimile

#### Text and data

Most amateur digital modes are transmitted by inserting audio into the microphone input of a radio and using an analog scheme, such as [amplitude modulation](Amplitude%20modulation.md) (AM), [frequency modulation](Frequency%20modulation.md) (FM), or [single-sideband modulation](Single-sideband%20modulation.md) (SSB).

- Amateur teleprinting over radio (AMTOR)
- [D-STAR (Digital Data)](D-STAR.md) a high speed (128 kbit/s), data-only mode.
- Hellschreiber, also referred to as either *Feld-Hell*, or *Hell* a facsimile-based teleprinter
- Discrete multi-tone modulation modes such as Multi Tone 63 (MT63)
- Multiple frequency-shift keying (MFSK) modes such as

 - [FSK441, JT6M, JT65, and FT8](WSJT%20%28amateur%20radio%20software%29.md)
 - Olivia MFSK
 - JS8
- [Packet radio](Packet%20radio.md) (AX25)

 - Amateur Packet Radio Network (AMPRNet)
 - [Automatic Packet Reporting System](Automatic%20Packet%20Reporting%20System.md) (APRS)
- PACTOR (AMTOR + packet radio)
- Phase-shift keying:

 - 31-baud binary phase shift keying: [PSK31](PSK31.md)
 - 31-baud quadrature phase shift keying: QPSK31
 - 63-baud binary phase shift keying: PSK63
 - 63-baud quadrature phase shift keying: QPSK63
- [Frequency-shift keying](Frequency-shift%20keying.md):

 - [Radioteletype](Radioteletype.md) (RTTY) Frequency-shift keying

#### Other modes

- [Spread spectrum](Spread%20spectrum.md), which may be analog or digital in nature, is the spreading of a signal over a wide bandwidth.
- High-speed multimedia radio, networking using 802.11 protocols.

### Activities sometimes called 'modes'

Certain procedural activities in amateur radio are also commonly referred to as 'modes', even though no one specific modulation scheme is used.

- AllStarLink (ASL) connects amateurs and [repeaters](Amateur%20radio%20repeater.md) via the internet using the Asterisk (PBX) IAX VOIP Protocol.
- Automatic link establishment (ALE) is a method of automatically finding a sustainable communications channel on [HF](High%20frequency.md).
- Automatically Controlled Digital Stations (ACDS)
- Earth-Moon-Earth (EME) uses the Moon to communicate over long distances.
- [EchoLink](EchoLink.md) connects amateurs and amateur stations via the internet.
- [Internet Radio Linking Project](Internet%20Radio%20Linking%20Project.md) (IRLP) connects [repeaters](Amateur%20radio%20repeater.md) via the internet.
- [Satellite](Amateur%20radio%20satellite.md) (OSCAR - Orbiting Satellite Carrying Amateur Radio)
- [Low transmitter power](QRP%20operation.md) (QRP)
- [Prosigns for Morse code](Prosigns%20for%20Morse%20code.md)

---

*Source: Wikipedia, List of amateur radio modes (https://en.wikipedia.org/wiki/List_of_amateur_radio_modes), by Wikipedia contributors, CC BY-SA 4.0.*
