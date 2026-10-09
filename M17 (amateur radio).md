# M17 (amateur radio)

**M17** is a digital voice and data protocol specification developed by Wojciech Kaczmarski ([amateur radio call sign](Call%20sign.md) SP5WWP) with contributions from the amateur radio community. M17 is primarily designed for voice communications on the [VHF](Very%20high%20frequency.md) [amateur radio](Amateur%20radio.md) bands, and above. The project received grants from the Amateur Radio Digital Communications in 2021 and 2022. The protocol has been integrated into several hardware and software projects, including commercial handheld radios.

### Technical characteristics

M17 uses Frequency-Division Multiple Access (FDMA) technology in which different communication streams are separated by frequency and run concurrently. It utilizes 4,800 symbols per second, 4-level [frequency-shift keying](Frequency-shift%20keying.md) (4FSK) with a root Nyquist filter applied to the symbol-mapped bitstream. Radio channels are 9 kHz wide, with channel spacing of 12.5 kHz. The gross data rate is 9,600 bits per second, with the actual data transfer at 3,200. The transmission, called *stream*, is divided into 40-millisecond long *frames*, each prepended with a 16-bit long synchronization word. A group of 6 frames form a *superframe* and is needed to decode the link information data. The protocol allows for low-speed data transfer (along with voice), e.g. GNSS position data. The mode has been successfully transmitted through EchoStar XXI and QO-100 geostationary satellites. M17 transmissions have also been tested using the OPS-SAT experimental satellite platform.

### Voice encoding

M17 uses Codec 2, a low bitrate voice codec developed by David Rowe VK5DGR et al. Codec 2 was selected as the voice codec due to its open licensing and suitability for low-bitrate digital voice applications. It is based on linear predictive coding with mixed-harmonic sinusoidal excitation. The M17 protocol supports both 3200 (full-rate) and 1600 bits per second (half-rate) modes.

### Error control

Three methods are used for error control: binary Golay code, punctured convolutional code and bit interleaving. Additionally, exclusive OR operation is performed between data bits and a predefined decorrelating pseudorandom stream before transmission. This ensures that there are as many symbol transitions in the baseband as possible. A 16-bit cyclic redundancy check (CRC) code is used for data integrity assurance.

### Application functions

The M17 protocol is designed for use in amateur radio communications.

- Callsign encoding: a 48-bit field holding up to 9 alphanumeric characters allows stations to be identified directly by callsign, eliminating the need for a centralized user-ID registration system.
- Two modes of operation: stream mode for continuous voice or data transmission, and packet mode for discrete data transfer.

 - Stream mode offers one 3200bps net bitrate channel (encoded speech or data) or two 1600bps channels (encoded speech alongside data).
 - Packet mode supports text messaging, [APRS](Automatic%20Packet%20Reporting%20System.md), [AX.25](AX.25.md), 6LoWPAN, [Winlink](Winlink.md), and raw binary data transfer.
- Slow-speed side channel for short and repeated data transfers, e.g. GNSS position data or telemetry.
- Network operation via reflectors and IP links, allowing repeaters and private access points (*hotspots*) to interconnect and route voice calls and data streams between distant stations.

#### Security features

- Bit scrambler encryption: a pseudorandom binary sequence created by combining an exclusive-or bitwise operation on the audio or data stream and a linear-feedback shift register using one of 3 feedback polynomials with 255, 65,535 and 16,777,215-bit repeat periods.
- AES encryption: symmetric, 128-bit block cipher operating in CTR mode with user-selectable 128, 192 or 256-bit keys.
- Digital signature authentication using ECDSA: a rolling digest is accumulated over the transmitted stream and signed by the sender using the *secp256r1* curve. The signature is transmitted in additional frames at the end of the transmission and can be verified by receivers using the sender public key. This provides stream authentication independently of whether encryption is used.

### Hardware support

With a small hardware modification, TYT MD-380, MD-390 and MD-UV380 handheld transceivers can be flashed with a custom, free, open source firmware to enable M17 support.

In July 2024, a US-based company Connect Systems, Inc. released the CS7000-M17, being the first commercial off-the-shelf handheld transceiver with native M17 support.

### Bridging with other modes

Links between M17 and other digital voice modes and Internet linked networks exist, with several networks providing M17 access. Modes bridged include [DMR](Digital%20mobile%20radio.md), [P25](Project%2025.md), System Fusion, [D-STAR](D-STAR.md), [NXDN](NXDN.md), AllStarLink, [EchoLink](EchoLink.md) and [IRLP](Internet%20Radio%20Linking%20Project.md).

### Comparison with other standards

- M17  Digital Mobile Radio (DMR)  D-STAR  System Fusion (YSF)
- Specification type  Open  Open  Partially open  Closed (proprietary)
- Developer  Amateur radio community (decentralized)  European Telecommunications Standards Institute (ETSI)  Japan Amateur Radio League (JARL), [ICOM Inc.](Icom%20Incorporated.md), [Kenwood Corporation](Kenwood%20Corporation.md), and others  [Yaesu](Yaesu%20%28brand%29.md)
- Modulation  4FSK  4FSK  GMSK  4FSK
- Channel (medium) access  FDMA  FDMA (Tier I), 2-slot TDMA (Tier II/III)  FDMA  FDMA
- Voice codec  Codec 2 (open-source)  AMBE+2 (proprietary)  AMBE (proprietary)  AMBE+2 (proprietary)
- Arbitrary data transfer support  Full  Limited (text messaging, geolocation)  Limited (text messaging, geolocation, images)  Limited (text messaging, geolocation, images)
- Extensibility  Full, through specification extensions  Fixed, defined by the specification  Fixed, defined by the specification  Fixed, defined by the specification

### M17 over IP

Access nodes and repeaters can be linked using *reflectors*. Over 130 M17 reflectors exist worldwide (June 2026).

### Governance and licensing

The protocol's specification is released under GNU General Public License, with reference implementations released as open-source software. Development is coordinated publicly, with protocol documentation, reference code, and discussion available to the amateur radio community.

### Applications and projects with M17 support

- OpenRTX - free and open-source firmware for ham radios
- DroidStar - digital voice client for Android
- SDR++ - multiplatform, open-source software defined radio receiver
- SDRangel - multiplatform, open-source software defined radio receiver/transmitter
- OpenWebRX - web-based software defined radio receiver
- mrefd - M17 reflector
- rpitx - general radio frequency transmitter for Raspberry Pi
- dsd-fme - digital speech decoder
- mvoice - voice client and graphical repeater application (Raspberry and Linux)
- mspot - hotspot software

---

*Source: Wikipedia, M17 (amateur radio) (https://en.wikipedia.org/wiki/M17_%28amateur_radio%29), by Wikipedia contributors, CC BY-SA 4.0.*
