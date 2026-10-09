# What do the three-letter modulation codes (emission designators) stand for?

*Tags: jargon · score 12*

## Question

I've seen these weird three-letter modulation codes like J3E, A3F, A1A, F3E and so on. Someone even wrote 2K40J3E or 12K5F3E. What do these codes stand for?

## Accepted answer (score 16, by user)

The emission type specifier is made up of several fields, which are defined as follows.

First comes an (optional) specifier of the necessary radio bandwidth. This is four characters, mixed letters and numbers, with one of H (Hz), K (kHz), M (MHz) or G (GHz) where the decimal point would be. For example, 400H specifies a bandwidth of 400 Hz, 2K40 specifies 2.40 kHz, 25K0 specifies 25.0 kHz and 6M00 specifies 6.00 MHz. This is the bandwidth used by the signal on the air, not the modulation bandwidth. For example, narrow-band FM modulated with a 3 kHz signal would be 12K5 because it needs 12.5 kHz of bandwidth on the air.

This is followed by three characters which specify, in turn, the modulation type, the nature of the modulating signal, and the type of information carried.

**Modulation type**

- A = amplitude modulation, two sidebands, full carrier
- B = amplitude modulation, independent sidebands
- C = amplitude modulation, vestigial sideband
- D = amplitude and angle modulation of carrier
- F = angle-modulated, straight frequency modulation
- G = angle-modulated, phase modulation
- H = amplitude modulation, single sideband, full carrier
- J = amplitude modulation, single sideband, suppressed carrier
- K = pulse, amplitude modulation
- L = pulse, width modulation
- M = pulse, with phase or position modulation
- N = No modulation at all
- P = pulse, no modulation
- Q = pulse, with carrier angle-modulated during pulse
- R = amplitude modulation, single sideband, reduced or controlled carrier
- W = pulse, two or more modulation modes used
- X = all other cases

**Nature of the modulating signal**

- 0 = No modulating signal
- 1 = Digital modulating signal, on/off or quantified with no further modulation
- 2 = Digital modulating signal with modulation
- 3 = A single analog channel
- 7 = Two or more digital channels
- 8 = Two or more analog channels
- 9 = Composite modulating signal, one or more analog channels plus one or more digital channels
- X = all other cases

**Type of information carried by the modulating signal**

- A = aural telegraphy, for people (generally Morse code)
- B = telegraphy for machine copying (generally RTTY or high-speed Morse code)
- C = analog fax
- D = data, telemetry, telecommand
- E = telephony, voice or sound
- F = video or television
- N = no information carried
- W = a combination of the above
- X = all other cases

This can be followed by two more characters giving details, which normally are not used for amateur radio purposes.

**Examples**

*J3E*

- amplitude modulation, single sideband, suppressed carrier
- a single analog channel
- telephony, voice or sound

*Also known as single-sideband transmissions or SSB,* generally in amateur applications with voice modulation. 2K40J3E is J3E with a 2.40 kHz radio signal bandwidth.

*A3F*

- amplitude modulation, two sidebands, full carrier
- a single analog channel
- video or television

*A1A*

- amplitude modulation, two sidebands, full carrier
- digital modulating signal, on/off or quantified with no further modulation
- aural telegraphy, for people

*Also known as Morse code* and informally CW. Actual CW (pure carrier) is N0N.

*F3E*

- angle-modulated, straight frequency modulation
- a single analog channel
- telephony, voice or sound

*Also known as frequency modulation or FM,* generally in amateur applications with voice modulation. 12K5F3E is F3E with a 12.5 kHz radio signal bandwidth.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/369/what-do-the-three-letter-modulation-codes-emission-designators-stand-for, by user. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
