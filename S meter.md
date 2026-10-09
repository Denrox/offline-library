# S meter

An **S meter** (signal strength meter) is an indicator often provided on communications receivers, such as [amateur radio](Amateur%20radio.md) or shortwave broadcast receivers. The scale markings are derived from a system of reporting signal strength from S1 to S9 as part of the [R-S-T system](R-S-T%20system.md). The term **S unit** refers to the amount of signal strength required to move an S meter indication from one marking to the next.

### Technical description

Analogue S meters are actually sensitive microammeters, with a full scale deflection of 50 to 100 μA. In AM receivers, the S meter can be connected to the main detector or use a separate detector at the final IF stage. This is the preferred method for [CW](Continuous%20wave.md) and SSB receivers. Another approach in the days of electronic tubes (valves) was to connect the S meter to the screen grid circuit of the final IF amplifier tube. A third option is to connect the S meter to the AGC line through a suitable level conversion circuit.

In FM receivers, the S meter circuit must be connected to the IF chain before any limiter stages. Some specialized integrated circuits for FM reception like CA3089 and CA3189 provide a DC signal to drive a 100 μA S meter.

### IARU Region 1 Technical Recommendation R.1

In the 1930s, it was already agreed that S9 corresponds to 50 μV at the input terminal of the receiver, but this was not a measure of the power received as the input impedance of receivers was not standardized.

The International Amateur Radio Union (IARU) Region 1 agreed on a technical recommendation for S Meter calibration for [HF](High%20frequency.md) and [VHF](Very%20high%20frequency.md)/[UHF](Ultra%20high%20frequency.md) transceivers in 1981.

IARU Region 1 Technical Recommendation R.1 defines S9 for the HF bands to be a receiver input power of -73 [dBm](DBm.md). This is a level of 50 microvolts at the receiver's antenna input **assuming** the input impedance of the receiver is 50 ohms.

For VHF bands the recommendation defines S9 to be a receiver input power of -93 [dBm](DBm.md). This is the equivalent of 5 microvolts in 50 ohms.

The recommendation defines that a difference of one S-unit corresponds to a difference of 6 [decibel](Decibel.md) (dB), equivalent to a voltage ratio of two, or power ratio of four.

Signals stronger than S9 are given with an additional dB rating, thus "S9 + 20dB", or, verbally, "20 decibels over S9", or simply "20 over 9" (or even the simpler "20 over").

### Examples

A weak signal with signal strength of S2 corresponds to received power of -115 [dBm](DBm.md) or 0.40 microvolts RMS in 50 ohms on HF.

A strong signal with signal strength of S8 corresponds to received power of -79 [dBm](DBm.md) or 25 microvolts RMS in 50 ohms on HF.

Some signal generators are calibrated in dB above 1uV and have an output in emf. For example to set an HF receiver's S-reading to S9 set the signal generator output to 34 dB above 1uV

- S-reading   HF      Signal Generator emf
- μV (rms, Relative to 50Ω)   dBm   dB above 1uV
- S9+10 dB   160.0   -63   44
- S9   50.2   -73   34
- S8   25.1   -79   28
- S7   12.6   -85   22
- S6   6.3   -91   16
- S5   3.2   -97   10
- S4   1.6   -103   4
- S3   0.8   -109   -2
- S2   0.4   -115   -8
- S1   0.2   -121   -14

### Accuracy

Most S meters on traditional analog receivers are not calibrated and in practice can only provide a relative measure of signal strength, based on the receiver's AGC voltage. Some S meters on traditional analog receivers are calibrated to read S9 for an input of -73 [dBm](DBm.md) but do not provide the correct 6 dB per S unit correspondence.

Often the correlation between a radio listener's qualitative impression of signal strength and the actual strength of the received signal on an analog receiver is poor, because the receiver's AGC holds the audio output fairly constant despite changes in input signal strength.

[Software-defined radios](Software-defined%20radio.md) (SDRs) acquire and process signals differently, and determine S-readings by direct measurement of RF signal amplitude. Consequently, many SDR systems with bit depths of 14-bits or more are accurately calibrated from one end of the S scale to the other right out of the box. In cases where this is not so, a few minutes with a signal generator to set the reference level are all that is required. Low bit depth SDRs such as an 8-bit design can be somewhat accurate, but as they distinguish much coarser differences in input levels, precision at the low end of the S scale will suffer.

Even with a high quality SDR, it is worth keeping in mind that the S meter is measuring the strength of the signal at the 50 ohm input of the receiver, *not* at the antenna. For example, if the radio's input is 50 ohms, but the antenna's impedance is significantly higher, power transfer from the antenna into the radio will suffer, and signal levels will be lower than if they were fed to an input with a matching high impedance. Many antennas vary in impedance over various frequency ranges, particularly in the case of wideband designs. What is useful to know is that the relative signal strengths at any one frequency will remain meaningful, even if they are not from one frequency to another.

---

*Source: Wikipedia, S meter (https://en.wikipedia.org/wiki/S_meter), by Wikipedia contributors, CC BY-SA 4.0.*
