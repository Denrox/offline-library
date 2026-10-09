# NXDN

**NXDN** stands for **Next Generation Digital Narrowband**, and is an open standard for public land mobile radio systems; that is, systems of [two-way radios](Two-way%20radio.md) ([transceivers](Transceiver.md)) for bidirectional person-to-person voice communication. It was developed jointly by [Icom Incorporated](Icom%20Incorporated.md) and [Kenwood Corporation](Kenwood%20Corporation.md) as an advanced digital system using [FSK](Frequency-shift%20keying.md) modulation that supports encrypted transmission and data as well as voice transmission. Like other land mobile systems, NXDN systems use the [VHF](Very%20high%20frequency.md) and UHF frequency bands. It is also used as a niche mode in [amateur radio](Amateur%20radio.md).

NXDN is implemented by Icom in their IDAS system  and by Kenwood as NEXEDGE; both Kenwood and Icom now offer dual-standard equipment which supports the European dPMR standard.

### Applications

The NXDN protocol and the communications products in which it is used are intended for commercial [Private Land Mobile Radio](Land%20mobile%20radio%20system.md) (PLMR)  and public safety communications systems. The technology satisfies the U.S. Federal Communications Commission (FCC) mandate requiring all communications systems covered by Part 90 regulations to use narrowband technology by January 1, 2013. Part 90 regulations specify a bandwidth of 12.5 kHz, but the FCC “strongly urges licensees to consider migrating directly to 6.25 kHz technology rather than first adopting 12.5 kHz technology and later migrating to 6.25 kHz technology.” The FCC “will expeditiously establish a schedule for transition to 6.25 kHz narrowband technology.”

### Technical characteristics

NXDN uses Frequency-Division Multiple Access (FDMA) technology in which different communication streams are separated by frequency and run concurrently. Time-Division Multiple Access (TDMA) systems combine the communications streams into a single stream in which information from the different streams is transmitted in interleaved time allocations or "slots." Code-Division Multiple Access (CDMA) systems allow many users to share a common spectrum allocation by using [spread-spectrum](Spread%20spectrum.md) techniques.

The basic NXDN channel is digital and can be either 12.5 kHz or 6.25 kHz wide. 6.25 kHz dual-channel systems can be configured to fit within a 12.5 kHz channel. This effectively doubles the spectrum efficiency compared to an analog [FM](Frequency%20modulation.md) system occupying a 12.5 kHz channel. The architecture of NXDN is such that two NXDN channels, within a 12.5 kHz channel for example, can be allocated as voice/voice, voice/data, or data/data. As of 2012, this capability cannot be implemented in commercially available hardware on simplex or "talkaround" frequencies, but only through repeaters.

Systems that use NXDN also support mixed analog FM and digital NXDN equipment, including direct radio-to-radio communications. This allows system owners to migrate to a narrowband, digital system without replacing the entire system at once. NXDN equipment is currently FCC type-accepted for use on VHF (137-174 MHz) and UHF (406-512 MHz) bands.

Data is transmitted using 4-level [frequency-shift keying](Frequency-shift%20keying.md) (FSK) modulation. NXDN uses the AMBE+2 vocoder (codec) for digital audio. This combination provides better weak-signal voice quality than for analog FM. For an equivalent transmitter power, NXDN is represented as having a wider range and slightly better multi-path characteristics than analog FM in typical RF environments, specifically at the 12 dB SINAD threshold. The transmission bit rate is 4,800 bit/s.

The following FCC emission designators apply to NXDN transmissions:

- 8K30F1E 12.5 kHz single channel digital voice
- 8K30F1D 12.5 kHz single channel digital data
- 8K30F1W 12.5 kHz single channel digital voice and data
- 4K00F1E 6.25 kHz single channel digital voice
- 4K00F1D 6.25 kHz single channel digital data
- 4K00F1W 6.25 kHz single channel digital voice and data
- 4K00F2D 6.25 kHz single channel analog CW ID

### Application functions

The NXDN protocol provides support for the following functions. Implementation of the functions and the user-level interfaces by which they are accessed and used may vary by manufacturer.

- Encryption:

 - "Scramble encryption": A pseudorandom binary sequence created by combining an exclusive-or bitwise operation on the audio or data stream and a linear-feedback shift register with a feedback polynomial of $$x^{15} + x + 1$$, which has a 32,767-bit repeat period, yielding 32,767 possible encryption keys except all zero. This level of encryption offers absolutely no protection and there is software that allows you to find the key instantly.
 - DES Encryption: 64-bit block encryption cipher operating in OFB mode using a 56-bit key expressed in 64 bits with parity bits. This level of encryption helps protect against casual attackers but not against a company.
 - AES Encryption: 128-bit block encryption cipher operating in OFB mode using a 256-bit key. This last level of encryption provides complete security.
- Paging & status reporting: radio-to-radio and dispatch-to-radio
- User aliases: 65,535 different group IDs and user IDs
- Man-down and emergency call
- Remote radio management functions: stun/kill/revive and monitor
- Over-the-air programming
- Over-the-air alias
- Interface to third-party applications for: paging to radio, GPS location, taxi data terminals, in-building tracking

### Audio quality

In all lossy compression schemes, trade-offs are made in voice reproduction quality in return for minimizing the raw bit rate of the transmission. This leads to artifacts and compromises of frequency response in reproduced speech. Encoders and other compression schemes that are highly optimized for speech are often unsuitable for non-speech audio, such as music or [frequency-shift keyed](Frequency-shift%20keying.md) data. Using an inappropriate encoder usually results in the creation of distortion and artifacts in the reproduced audio.

The audio reproduction quality of IDAS and NEXEDGE communications systems is dependent on the performance of the AMBE+2 voice codec used by NXDN. The AMBE family of vocoders has been subjected to comparative testing and found to be adequate for its intended uses, primarily mobile and aeronautical radio. The AMBE+2 vocoder has also been selected for use in the Motorola MOTOTRBO radio family as well as [DMR](Digital%20mobile%20radio.md) systems, and [Project 25](Project%2025.md) (P25) mobile radio system. The following reports and papers are descriptions of laboratory-environment evaluations of AMBE+2 and other speech vocoders.

Compromises in audio quality are inherent in the use of any codebook-based speech coder, particularly when used in conditions of high background noise. Incremental improvements are being made in the algorithms, which may lead to differences in performance even while the basic method remains unchanged. In the US, the Department of Commerce Public Safety Communications Research laboratory regularly reports on progress in this field. While their work specifically pertains to Project 25 radios, it is directly applicable to any system using similar multi-band excitation coders.

### NXDN Forum

The NXDN Forum was formed in order to promote the NXDN protocol in North and South America. The forum's members are:

- CML Microcircuits
- Freedom Communication Technology
- Hytera Communications
- [Icom Incorporated](Icom%20Incorporated.md)
- InterTalk Critical Information Systems
- [Kenwood Corporation](Kenwood%20Corporation.md)
- Ritron, Inc.
- Trident Micro Systems which was bought by Motorola Solutions in December 2014.
- Remota Tecnologia em Comunicação

---

*Source: Wikipedia, NXDN (https://en.wikipedia.org/wiki/NXDN), by Wikipedia contributors, CC BY-SA 4.0.*
