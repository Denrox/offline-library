# Software-defined radio

**Software-defined radio** (**SDR**) is a radio communication system where components that conventionally have been implemented in analog hardware (e.g. mixers, filters, amplifiers, modulators, demodulators, detectors, etc.) are instead implemented by means of software on a computer or embedded system.

A basic SDR system may consist of a computer equipped with a sound card, or other analog-to-digital converter, preceded by some form of RF front end. Significant amounts of signal processing are handed over to the general-purpose processor, rather than being done in special-purpose hardware (electronic circuits). Such a design produces a radio which can receive and transmit widely different radio protocols (sometimes referred to as waveforms) based solely on the software used.

Software radios have significant utility for the military and cell phone services, both of which must serve a wide variety of changing radio protocols in real time. In the long term, software-defined radios are expected by proponents like the Wireless Innovation Forum to become the dominant technology in radio communications. SDRs, along with software defined antennas are the enablers of cognitive radio.

### Operating principles

A [superheterodyne receiver](Superheterodyne%20receiver.md) uses a variable-frequency oscillator (VFO), a mixer, and a filter to tune the desired signal to a common intermediate frequency (IF) or baseband. Typically in SDR this signal is then sampled by the analog-to-digital converter. However, in some applications it is not necessary to tune the signal to an intermediate frequency and the radio-frequency signal is directly sampled by the analog-to-digital converter (after amplification).

Real analog-to-digital converters lack the dynamic range to pick up sub-microvolt, nanowatt-power radio signals produced by an antenna. Therefore, a low-noise amplifier must precede the conversion step and this device introduces its own problems. For example, if spurious signals are present (which is typical), these compete with the desired signals within the amplifier's dynamic range. They may introduce distortion in the desired signals, or may block them completely. The standard solution is to put band-pass filters between the antenna and the amplifier, but these reduce the radio's flexibility. Real software radios often have two or three analog channel filters with different bandwidths that are switched in and out.

The flexibility of SDR allows for dynamic spectrum usage, alleviating the need to statically assign the scarce spectral resources to a single fixed service.

### Military usage

#### United States

The Joint Tactical Radio System (JTRS) was a program of the US military to produce radios that provide flexible and interoperable communications. Examples of radio terminals that require support include hand-held, vehicular, airborne and dismounted radios, as well as base-stations (fixed and maritime).

This goal is achieved through the use of SDR systems based on an internationally endorsed open Software Communications Architecture (SCA). This standard uses CORBA on POSIX operating systems to coordinate various software modules.

The program is providing a new approach to meet additional soldier communications needs through software programmable radio technology. All functionality and expandability is built upon the SCA.

The SCA, despite its military origin, is under evaluation by commercial radio vendors for applicability in their domains. The adoption of general-purpose SDR frameworks outside of military, intelligence, experimental and amateur uses, however, is inherently hampered by the fact that civilian users can more easily settle with a fixed architecture, optimized for a specific function, and as such more economical in mass market applications. Still, software defined radio's inherent flexibility can yield substantial benefits in the longer run, once the fixed costs of implementing it have gone down enough to overtake the cost of iterated redesign of purpose built systems. This then explains the increasing commercial interest in the technology.

SCA-based infrastructure software and rapid development tools for SDR education and research are provided by the Open Source SCA Implementation – Embedded (OSSIE) project. The Wireless Innovation Forum funded the SCA Reference Implementation project, an open source implementation of the SCA specification. (SCARI) can be downloaded for free.

### Amateur and home use

A typical [amateur](Amateur%20radio.md) software radio uses a direct conversion receiver. Unlike direct conversion receivers of the more distant past, the mixer technologies used are based on the quadrature sampling detector and the quadrature sampling exciter.

The receiver performance of this line of SDRs is directly related to the dynamic range of the analog-to-digital converters (ADCs) utilized. Radio frequency signals are down converted to the audio frequency band, which is sampled by a high performance audio frequency ADC. First generation SDRs used a 44 kHz PC sound card to provide ADC functionality. The newer software defined radios use embedded high performance ADCs that provide higher dynamic range and are more resistant to noise and RF interference.

A fast PC performs the digital signal processing (DSP) operations using software specific for the radio hardware. Several software radio implementations use the open source SDR library DttSP.

The SDR software performs all of the demodulation, filtering (both radio frequency and audio frequency), and signal enhancement (equalization and binaural presentation). Uses include every common amateur modulation: [morse code](Morse%20code.md), [single-sideband modulation](Single-sideband%20modulation.md), [frequency modulation](Frequency%20modulation.md), [amplitude modulation](Amplitude%20modulation.md), and a variety of digital modes such as [radioteletype](Radioteletype.md), [slow-scan television](Slow-scan%20television.md), and [packet radio](Packet%20radio.md). Amateurs also experiment with new modulation methods: for instance, the DREAM open-source project decodes the COFDM technique used by Digital Radio Mondiale.

There is a broad range of hardware for radio amateurs and home use. There are professional-grade transceivers, e.g. the Zeus ZS-1 or FlexRadio, home-built transceivers, e.g. PicAStar or the SoftRock SDR kit, and starter or professional receivers, e.g. the FiFi SDR for shortwave, or the Quadrus coherent multi-channel SDR receiver for short wave or VHF/UHF in direct digital mode of operation.

#### RTL-SDR

RTL-SDR is a type of low-cost software-defined radio receiver named after the Realtek RTL2832U demodulator chip on which it is based, which supports USB output. Originally designed for DVB-T reception, the chip was found in 2010 to output raw radio signal data. With drivers developed by the Osmocom project, these devices were repurposed as general-purpose SDR receivers. Early DVB-T USB sticks often sold for under US$10, while models purpose-built as SDR receivers with improved shielding and frequency stability sold for about US$30 as of 2025.

RTL-SDR devices typically include a Rafael Micro R820T, R820T2, or R860 tuner chip, and can receive frequencies from approximately 24 to 1766 MHz with a bandwidth of up to 3.2 MHz. They are used for applications including FM and digital radio reception, aircraft data reception (ADS-B, ACARS), [trunked radio](Radio%20scanner.md) decoding, weather satellite reception (GOES, Meteor-M), radiosonde tracking, and basic radio astronomy.

#### HPSDR

The HPSDR (High Performance Software Defined Radio) project uses a 16-bit 135 MSPS analog-to-digital converter that provides performance over the range 0 to 55 MHz comparable to that of a conventional analogue HF radio. The receiver will also operate in the VHF and UHF range using either mixer image or alias responses. Interface to a PC is provided by a USB 2.0 interface, although Ethernet could be used as well. The project is modular and comprises a backplane onto which other boards plug in. This allows experimentation with new techniques and devices without the need to replace the entire set of boards. An exciter provides 1/2 W of RF over the same range or into the VHF and UHF range using image or alias outputs.

#### WebSDR

WebSDR is a project initiated by Pieter-Tjerk de Boer providing access via an internet browser to multiple SDR receivers worldwide covering the complete shortwave spectrum. De Boer has analyzed Chirp Transmitter signals using the coupled system of receivers..

#### KiwiSDR

KiwiSDR is also a via-browser SDR like WebSDR. Unlike WebSDR, the frequency is limited to 3 Hz to 30 MHz (ELF to [HF](High%20frequency.md))

OpenWebRX, an open-source software project, provides access to VHF and UHF spectrum as well.

### Other applications

On account of its increasing accessibility, with lower cost hardware, more software tools and documentation, the applications of SDR have expanded past their primary and historic use cases. SDR is now being used in areas such as wildlife tracking, radio astronomy, medical imaging research, and art.

---

*Source: Wikipedia, Software-defined radio (https://en.wikipedia.org/wiki/Software-defined_radio), by Wikipedia contributors, CC BY-SA 4.0.*
