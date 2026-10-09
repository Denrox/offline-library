# Why is this requirement in 60m in the US?

*Tags: united-states, fcc · score 10*

## Question

According to the FCC, if you are using an antenna other than a dipole, in 60 meters, you must keep a record of the transmission and gain of the antenna.

I don't remember seeing any other requirement of log keeping. Why does this one exist? What's the story behind it?

## Accepted answer (score 7, by Mike Waters)

Some decades ago, the FCC used to require that US amateurs log *every single QSO.* And those logging requirements could be somewhat complex, especially for third-party traffic with other countries.

It's the law because **those 5 channels are shared with other licensed commercial services**. If we interfere with those, then the FCC might pay us a personal visit and see what our ERP is *and what it might have been with our 'previous' 60m antenna* (indicated, of course, by our log).

Here are the 60m rules.

Amateurs may transmit with an effective radiated power of 100 W or less, relative to a half-wave dipole. If you’re using a commercial directional antenna, FCC Rules require you to keep a copy of the manufacturer’s gain specifications in your station records. If you built the directional antenna yourself, you must calculate the gain and keep the results in your station records.

When using a directional antenna, you must take your antenna gain into account when setting your RF output power. For example, if your antenna offers 3 dB gain, your maximum legal output power on 60 meters should be no more than 50 W (50 W plus 3 dB gain equals 100 W Effective Radiated Power).

It's intended to make sure that the ERP does not exceed those limits.

From http://www.arrl.org/60-meter-faq#:

**How can I be sure I don't exceed the power limit?** The FCC said hams may run 100 W effective radiated power (ERP) on the five 60-meter channels. The new rules say, "For the purpose of computing ERP, the transmitter PEP (peak envelope power) will be multiplied by the antenna gain relative to a dipole or the equivalent calculation in decibels. A half-wave dipole antenna will be presumed to have a gain of 0 dBd." This means if you use a half-wave dipole (about 87 feet 3 inches for the "middle" channel according to the formula), set your transmitter's output power for 100 W PEP (many transceivers' meters can be set to indicate peaks), and you should be in compliance. The FCC asks licensees using antennas other than half-wave dipoles to "maintain in their station records either manufacturer data on the antenna gain or calculations of the antenna gain." This is a new record-keeping requirement for amateurs. The "best" antenna configurations are those with a proven track record on the lower bands, keeping in mind that using a loop or an array of some kind will require you to "do the math" to ensure you are not radiating more than 100 W ERP in any direction. For the math you must reduce your power by the number of decibels your antenna gain exceeds 0 dBd (0 dB relative to a half-wave dipole). Conversely, you can increase your transmitter power if your antenna exhibits loss compared to a dipole. Be prepared to document these situations in your station records.

*More information from the Federal Register*

## Answer (score 3, by rclocher3)

On most bands, US Amateur Extra-class hams are allowed to transmit 1.5 kW because hams are the primary users of the band. On 60m, US hams are secondary users of the band, and government agencies are the primary users. The idea for the 60m band came from negotiations between governments at the 2012 and 2015 ITU World Radiocommunication Conferences, according to Wikipedia. The US government presumably wanted to keep hams from interfering with existing users of the band, so we hams were allowed only low power, channelized operation on five frequencies only, and upper sideband as the only phone mode. (For single-sideband operation, hams [traditionally use lower sideband on frequencies lower than 10 MHz](Why%20do%20we%20use%20LSB%20below%2010%20MHz%20and%20USB%20above%2010%20MHz%20when%20operating%20SSB%20HF.md), but government users use upper sideband exclusively.)

According to the ARRL, "Our expanded privileges on 60 meters were the result of collaboration between the FCC and the NTIA – the National Telecommunications and Information Administration, the agency that manages and coordinates telecommunications activities among US government departments, the primary users of the band."

The ARRL page goes on to mention that the NTIA expressed concern about possible interference from digital modes, and requested that US amateurs limit digital operating to PSK31 and PACTOR III only.

@MikeWaters answer explains the reasons behind the logging requirement quite well: so that the FCC will be able to estimate a station's Effective Radiated Power when investigating possible ham interference with other (government) users of the 60m band.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9376/why-is-this-requirement-in-60m-in-the-us, by Pablo Fernandez, Mike Waters, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
