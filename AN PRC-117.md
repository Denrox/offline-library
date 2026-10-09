# AN/PRC-117

The **AN/PRC-117** is a family of portable, tactical VHF/UHF/L-band [software-defined](Software-defined%20radio.md) voice and data communications [combat-net radio](Combat-net%20radio.md), originally manufactured by Harris Corporation (now [L3Harris](L3Harris.md)). The AN/PRC-117 series is notable for its software communications architecture (SCA), allowing for quick upgrades and adaptability to evolving mission requirements. It is widely used by US military and allied forces.

In accordance with the Joint Electronics Type Designation System (JETDS), the "*AN/PRC-117*" designation represents the 117th design of an Army-Navy electronic device for portable two-way communications radio. The JETDS system also now is used to name all Department of Defense and some NATO electronic systems.

### Features

Fully compliant with the Joint Tactical Radio System (JTRS) standard, the radio supports multiband and multimission operations across a wide frequency range. The AN/PRC-117G variant is 30% smaller and 35% lighter than the previous models, enhancing portability for dismounted operations. It features Type-1 and NINE Suite B encryption, enabling secure interoperability with US, NATO, and coalition partners. Its removable Keypad Display Unit (KDU) facilitates operation while the radio is stowed, effective for on-the-move communication.

The AN/PRC-117 may also be deployed in a vehicle-mounted configuration under the AN/VRC-103 designation, with mounting systems and integrated communication cases supporting multi-transceiver setups. The radios are engineered to endure battlefield environmental conditions including shock, vibration, and water immersion. The radio is Mobile User Objective System (MUOS) ready for beyond line-of-sight (BLOS) satellite communications (SATCOM), and the AN/PRC-117F(C)-HQ includes ground-to-air capabilities with Have Quick I/II support. Multiple power options (AC, DC, and battery) provide operational flexibility.

### Variants

The PRC-117 has been released in several different versions, most notably:

- **AN/PRC-117A** was a portable VHF transceiver radio.
- **AN/PRC-117B** was a VHF-low band [FM](Frequency%20modulation.md) full band [frequency-hopping spread spectrum](Frequency-hopping%20spread%20spectrum.md) radio operating from 30–89.975 MHz (9.99–3.33 m).
- **AN/PRC-117D MANPACK** added VHF-high band and UHF frequency coverage and [AM](Amplitude%20modulation.md) and contained integrated [communications security](Communications%20security.md) (COMSEC) abilities using TSEC/KY-57, as well as Single Channel Ground and Airborne Radio System ([SINCGARS](SINCGARS.md)) interoperability. It operated in three bands including VHF-low 30–89.975 MHz (9.99–3.33 m), VHF-high 116–174 MHz (2.58–1.72 m) and UHF 225–420 MHz (1.33–0.71 m). It had data transfer rates up to 16 kbps.
- **AN/PRC-117F Falcon II MBMMR** (Multiband Multimission Manpack Radio), also referred to as AN/PRC-117F-MP. This radio operates in the 30–512 MHz (9.99–0.59 m) frequency range, and is provided without an internal GPS. Optionally an external commercial GPS can be connected, or a GPS selective availability anti-spoofing module (SAASM) such as the Precision Lightweight GPS Receiver (PLGR) or the Defense Advanced GPS Receiver (DAGR).
- **AN/PRC-117G Falcon III MNMR** (Multiband Networking Manpack Radio), also referred to as AN/PRC-117G-MP. This radio, provided with internal SAASM GPS, operates from 30–2,000 MHz (9.99–0.15 m). Optionally an external commercial GPS can be connected).

F and G version radios are NSA certified for the transmission of voice and data traffic up to Top Secret level communications.

### Users

The PRC-117F/G radios are used extensively by the United States Department of Defense including United States Navy Seabee and EOD teams, and embedded in the Navy's remote mine hunting systems. It is also used by the United States Air Force, Army, Marine Corps, Coast Guard, and USSOCOM.

Besides US forces, the radio is used by the British Army, Canadian Armed Forces, Croatian Army, German Armed Forces. Norwegian Armed Forces, Royal Air Force, Royal Danish Army, Royal Netherlands Army, and the Spanish Air and Space Force.

In 2004, the radio was incoporated into an over-the-horizon SATCOM improved dual command and control (C) console system. The console was deployed to aviation units in Afghanistan and Iraq in 2005 where line-of-sight (LOS) communication was difficult. It was recognized by the US Army as a "Top 10 Invention" in 2005 where winning entries were selected based on impact to Army capabilities.

### Operating specifications (AN/PRC-117G)

Source: AN/PRC-117G Datasheet

#### General

- Frequency range: 30–2,000 MHz (9.99–0.15 m)

 - Narrowband: VHF 30–225 MHz (9.99–1.33 m), UHF 225–512 MHz (1.332–0.586 m)
 - Wideband: UHF/L-band 225–2,000 MHz (1.33–0.15 m)
 - SATCOM: Transmitting 292–318 MHz (1.03–0.94 m), Receiving 243–270 MHz (1.23–1.11 m)
 - MUOS: Uplink 300–320 MHz (1.00–0.94 m), Downlink 360–380 MHz (0.83–0.79 m)
- Presets: 99 (110 including DAMA)
- Channel spacing/bandwidth:

 - Narrowband: 8.33, 12.5 and 25 kHz
 - Wideband: 500 kHz, 1.2, 2.5 and 5 MHz
 - SATCOM: 5 and 25 kHz
- Frequency deviation: 5, 6.5 and 8 kHz
- Frequency stability: +/- 0.5 ppm
- Tuning resolution: 10 Hz

#### Transmitter

- Output power: Narrowband 10 W, Wideband 20 W peak/5 W average, SATCOM 20 W
- Harmonic suppression: >50 dBc
- Transmission modes: [AM](Amplitude%20modulation.md), [FM](Frequency%20modulation.md), amplitude-shift keying (ASK), [frequency-shift keying](Frequency-shift%20keying.md) (FSK), phase shift keying (PSK), continuous phase modulation (CPM), gaussian minimum-shift keying (GMSK)

#### Receiver

- Sensitivity for 10 [dB](Decibel.md) signal-to-noise and distortion ratio (SINAD):

 - LOS FM: 30–152 MHz (9.99–1.97 m); –118 [dBm](DBm.md)
 - LOS AM: 90–512 MHz (3.331–0.586 m); –110 dBm
 - TACSAT: –120 dBm
- Adjacent Channel Rejection >40 dB

#### Waveforms

- Narrowband: AM/FM, VHF/UHF LOS, SINCGARS, Have Quick I/II, SATURN (optional), [APCO P25](Project%2025.md) (optional), P25 OTAR (optional)
- Wideband: Soldier Radio Waveform (SRW), ANW2C, ROVER III L-band receive (optional)
- UHF SATCOM:

 - MIL-STD-188

 - −181B; Advanced Narrowband Digital Voice Terminal (ANDVT) dedicated 56 kbit/s data channel
 - −181C, −183B; Interoperability standard for access and multiple-access to 5-kHz And 25-kHz UHF satellite communications channels
 - −182A, −183A Demand Assigned Multiple Access (DAMA)
 - High performance waveform (HPW)/IP
 - MUOS (optional)

#### Interoperability

- The AN/PRC-117 interoperates with other radios including AN/PRC-77, AN/PRC-113, AN/PRC-119A/B/G, [AN/PRC-148](AN%20PRC-148.md), [AN/PRC-152](AN%20PRC-152.md), AN/PSC-5 and other versions of the AN/PRC-117.
- Crypto Modes KY-57, ANDVT/KYV-5, KG-84C, FASCINATOR
- Fill devices: AN/CYZ-10 DTD, AN/PYQ-10 SKL (Supports DS-101, DS-102 and Mode 2/3)

### Physical characteristics

- Physical dimensions: 3.7 × 7.4 × 8.8 inches (9.4 × 18.8 × 22.4 cm) with or without battery
- Volume: 155 in (2,540 cm) without battery; 235 in (3,850 cm) with battery
- Weight: 8.2 lb (3.7 kg) without batteries; 12 lb (5.4 kg) with batteries
- Operating temperature: −40 to 158 °F (−40 to 70 °C)
- Immersion in water: 1 meter
- Finish: CARC green
- Power: BA-5590/U, BA-5390/U, BB-2590/U, BB-590/U or BB-390/U batteries

---

*Source: Wikipedia, AN/PRC-117 (https://en.wikipedia.org/wiki/AN/PRC-117), by Wikipedia contributors, CC BY-SA 4.0.*
