# Yaesu FT-817

The **Yaesu FT-817** is one of the smallest MF/HF/VHF/UHF multimode general-coverage [amateur radio](Amateur%20radio.md) [transceivers](Transceiver.md). The set is built by the Japanese Vertex Standard Corporation and is sold under the [Yaesu](Yaesu%20%28brand%29.md) brand. With internal battery pack, on board keyer, all mode/all band capability and flexible antenna, the set is particularly well suited for portable use. The FT-817 is based on a similar circuit architecture as Yaesu's FT-857 and FT-897, so it is a compromise transceiver, and incorporates its features to its low price ($670 at its 2001 release).

The upgraded **FT-817(N)D** was launched in 2004. The difference between the two models is the addition of 60 meter band coverage in five fixed channels (USA model only), other display lighting options, modifications in the RF stage, the included FNB-85 battery pack, and NC-72B charger.

The FT-817 is a [QRP](QRP%20operation.md) transceiver.

The FT-817(N)D is no longer in production, and was replaced by the FT-818 (also now discontinued), which improves on the previous model with an increase of RF output from 5 to 6 watts, higher capacity battery and the inclusion of a TCXO for better frequency stability, though those three changes can be made to an FT817ND. In December 2022, Yaesu announced they were also discontinuing production of the FT-818.

### Technical description

#### CAT interface

A serial port with a wide range of commands is provided.

#### Circuit description

The following circuit description is an extract from the service manual.

RX signals may be input via a front [BNC connector](BNC%20connector.md) or a rear [UHF SO-239 connector](UHF%20connector.md) (Yaesu calls it a type "M" connector) using a relay on the PA unit. The selection has to be made per band ([HF](High%20frequency.md), 6, 2 m or 70 cm) using menu selection. The BNC connector is the antenna connector chosen when the relay is bypassed.

A 70cm signal path goes through a high-pass filter network, through the RF directional coupler/power detector (not on rx) to a low-pass filter to a PIN-diode. In rx mode, these are turned off. The rx signal then passes through a DAN235U; this is a dual diode, and when in UHF rx mode, the appropriate diode is turned on, passing the 70 cm signal through, and the signal then leaves the PA board. On the MAIN circuit board the 70 cm rx signal enters a DAP236U. This dual diode get its current from the PA unit, and when 70 cm rx mode is active, one of the diodes is turned on. Rx signal goes through a device consisting of two back-to-back diodes providing protection for the receiver's front end. The output of the preamplifier is sent to a helical resonator filter. The output of the filtered and amplified 70 cm path is passed through and coupled into the receive mixer. For 70 cm receive, PIN diode bias is provided to the PA unit, through the MAIN unit, and then through an RF-decoupler network, a parallel-output shift register.

A 2m signal goes to a relay and then the signals are diplexed, with 2m and < going to a low-pass filter. The signal gets diplexed again using a high-pass filter, separating out the 2 m signal from the HF-6 meter signal path. The rx signal passes through the VHF directional coupler/power detector (not used in rx) to a low-pass filter and then passes by two PIN diodes (both HSU277). These diodes and related components form T/R isolation switches that operate similarly to that of the 70 cm front end. Rx signal passes through the half which is not used for 70 cm, then to the RX RF output, and is then passed to the MAIN unit. Here the signal enters and then passes through a transformer, along with a varactor and related components, and forms an electrically-tuned filter/matching network, the 2 meter preamplifier. The output of the preamplifier goes through two electronically tuned transistors. Finally, the output goes through to the rx mixer. For 2 m rx, the PIN diode bias is provided by the PA unit to 2 m preamplifier.

Aircraft band Rx path (108-154 MHz) is the same as that of the 2 m path on the PA unit. On the MAIN unit, it goes through the same part as the 2 m signal, but it then goes through the diode portion that was not used for 2 m into an electronically tuned bandpass filter. The output passes through the rx mixer. The PIN diode bias is provided by the PA unit and flows through the primary transistor. On the output, current is provided and goes through the secondary transistor. Both current paths are completed using the aircraft band rx preamplifier.

WFM broadcast band rx path (76-108 MHz) is identical to the 2 m path on the PA unit. On the MAIN unit it passes through the same portion as the 2 m signal, then through a HSC277 diode. This signal then goes into pin 10 of a Sony CXA1611 FM receiver IC. The IC has a front end, mixer, IF and demodulation and provides received audio. In order to suppress local oscillator leakage and provide a slight amount of image rejection, a varactor and a coil provide one stage of tracking bandpass filtering. Typical for single-chip receivers, the dynamic range of this receiver is poor. When using a large antenna, expect overload/intermod problems.

After relay the signal is diplexed via a low-pass filter. At this point, 2 m, aircraft and WFM are diplexed. The signal passes through a low-pass filter, continues through the RF directional coupler/power detector (not used in rx), through low-pass filters selected by relays as appropriate for current rx frequency. The combination of low- and high-pass filters provides broadband bandpass filtering to the rx front end. For 6 m, the high-pass filter includes a preamplifier (always used on 6 m rx and not affected by the IPO menu setting). The appropriate high-pass filter output is selected with a PIN diode with logic levels. The output from the PIN diodes are routed to the MAIN unit. Here the rx signal is applied to dual PIN diode modules (type DAP236U). One path routes the signal directly between the two modules and the other path passes the signal through a 10 db pad - the pad that is switched in as a menu item. The output is then passed through a simple low-pass filter to another DAP236U. One of the outputs is applied to a preamplifier, and the other is applied to a diode, bypassing the preamplifier. The output of the diode is applied to an IF trap. The purpose of this is to prevent 68.33 MHz energy from the antenna from getting into the 1st IF. The HF receive signal is routed to the receive mixer.

#### Technical specifications

- RX freq coverage: 100 kHz-30 MHz, 50 MHz-54 MHz, 76 MHz-108 MHz (WFM), 108 MHz-154 MHz, 420 MHz-450 MHz
- TX freq coverage: 160 - 6 meters, 2 meters, 70 centimeters (amateur bands only), 5.1675 MHz Alaskan emergency frequency (USA model only), 5 fixed channels (USA model FT-817ND only) 5.332 MHz, 5.348 MHz, 5.368 MHz, 5.373 MHz, 5.405 MHz
- Power consumption: 13.8 V DC @ transmit 2A, @ receive 450mA
- Operating voltage range: within 8 -16V (AA alkaline batteries: 12V; nicad battery: 9,6V)
- Tuning steps: 100 Hz AM, FM, WFM; 10 Hz SSB, CW switchable
- Dimensions 13.5 x 4 x 16.8 cm
- Weight appx. 1.2 kg with alkaline batteries and flex antenna
- Emission: CW, SSB, AM, FM, digital mode
- Power output: 5W (SSB, CW, FM), 1.5W (AM, carrier) @ 13.8V
- Carrier suppression: better than -40 dB below rated output
- Unwanted sideband suppression: better than -60 dB below peak output
- Spurious: better than – 40 dB below peak output
- Distortion: better than -31 dB below peak output
- Transmitter freq response: 350 – 2700 Hz (-6 dB)
- Stability: ±0.3 ppm/1 hour @25 °C, after warmup
- Ant output impedance: 50 ohms unbalanced (front BNC connector, rear UHF (SO-239) connector)
- Microphone output impedance: 200-10k ohms (nominal: 600 ohms)
- Receive sensitivity: 100 kHz – 29.999 MHz continuous better than 0.7 microV for S/N 10 dB
- Image rejection: HF/50 MHz: 70 dB, 144/430 MHz: 60 dB
- IF rejection: -60 dB (all freq)
- Selectivity: -6 dB 2.2 kHz, -60 dB 4.5 kHz
- Audio output: 1 W @ 10% THD, 8 ohms

### Accessories

- Shoulder strap
- Carrying case, soft vinyl
- YHA-63 flex [whip antenna](Whip%20antenna.md) for 50/144/430 MHz
- FBA-28 battery case for AA batteries
- E-DC-6 DC cable
- MH-31A8J hand mic
- FNB 72 and 85 internal NiCd/NiMH 9.8V battery packs 1000/1400mAh
- NC-72B battery pack charger
- TCXO stability unit
- DTMF mic
- Cat interface and packet cable
- ATAS 25 portable manually tuned antenna

#### Suitable antenna tuners

- MAT-TUNER MAT-10 automatic [antenna tuner](Antenna%20tuner.md)
- LDG Z817 automatic antenna tuner
- [Elecraft](Elecraft.md) T1 miniature automatic antenna tuner
- Emtech ZM-2 small, lightweight manual Z-match tuner for balanced and unbalanced feedlines

### Known weaknesses

The 2SK2975 FETs in the final stage are VERY sensitive and can easily be destroyed by high SWR, overheating, overvoltage, or voltage peaks. In the ND model, Yaesu (Vertex) replaced the FETs with RD07MVS1 FETs, but the problem may still exist. The RF stage may remain sensitive to damage.

The internal battery should be removed if the radio is to be stored for an extended period. In the non-ND model, a failing battery can cause the finals to oscillate which destroys the FETs. This was corrected with the ND model though it is still recommended that the internal battery be removed for extended storage to prevent this issue as well as to ensure that there is no possibility of battery leakage which can destroy internal components of the radio.

---

*Source: Wikipedia, Yaesu FT-817 (https://en.wikipedia.org/wiki/Yaesu_FT-817), by Wikipedia contributors, CC BY-SA 4.0.*
