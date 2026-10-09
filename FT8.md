# FT8

**FT8** (short for Franke–Taylor design, 8-FSK modulation) is a [frequency shift keying](Frequency-shift%20keying.md) digital [mode of radio communication](List%20of%20amateur%20radio%20modes.md) used by [amateur radio](Amateur%20radio.md) operators worldwide. It was released on June 29, 2017, by its creators Joe Taylor, K1JT and Steve Franke, K9AN, as part of the [WSJT](WSJT%20%28amateur%20radio%20software%29.md) software package.

FT8 was adopted quickly, becoming the most widely used digital mode reported by automatic spotting networks such as PSK Reporter within two years.

### Introduction

FT8 is a popular form of digital weak signal communication used primarily by amateur radio operators to communicate on amateur radio bands with a majority of traffic occurring on the [HF](High%20frequency.md) amateur bands. The mode offers operators the ability to communicate despite unfavorable conditions such as those seen during low solar activity, high RF noise, or with [low transmitter power](QRP%20operation.md). With advances in signal processing technology, software can decode FT8 signals with a signal-to-noise ratio as low as −20 dB in a 2500 Hz bandwidth, which is significantly lower than conventional [CW](Continuous%20wave.md) or SSB transmissions.

### Operation

FT8 involves 77-bit message blocks transmitted in regular 15-second periods, consisting of 12.64 seconds of transmission time and 2.36 seconds of decode time, giving a digital data rate of 6.09 bits/sec. Source encoding gives an effective message throughput equivalent to about 5 words per minute. The required signal-to-noise ratio in a 2500 Hz bandwidth is −21 dB, so the corresponding *E**b*/*N*0 is 10 log10(2500/6.09) = 26.1 dB greater, or −21 dB + 26.1 = 5.1 dB.

Although FT8 transmissions occur within fixed time windows, the software can cope with discrepancies between sending and receiving systems of up to a second or two. Provided that they are manually set to the correct time every so often (for example, by using WWV or other time standard broadcasters), conventional computer real-time clocks are usually adequate. However, most FT8 users take advantage of online time servers using NTP or time signals from the GPS to achieve and maintain better time accuracy, automatically.

Forward error correction helps achieve reliable communication despite common RF issues such as fading and interference, and weak/noisy signals due to marginal propagation paths, low power operation, and inefficient antennas (e.g., in restricted and overcrowded urban locations). If anticipated messages are missed or not acknowledged, the software can re-send them in the next time slot.

Each 77-bit message can carry up to 13 text characters. A compact encoding method allows standard FT8 exchanges, such as callsigns, signal reports, and grid locators, to fit efficiently within that limit. The protocol uses hashing to handle long or unusual callsigns, but these can still lead to occasional decoding errors or collisions that produce false or corrupted callsigns. Such errors are rare but can be mistaken for genuine or exotic stations, sometimes causing brief confusion or excitement among operators.

There are multiple uses for FT8 including contesting, testing antennas, and for scientific research.

### Applications in amateur radio

In amateur radio, FT8 is a mainstream digital modulation mode. It operates on a 15-second cycle, usually completing a QSO in about 90 seconds. It’s commonly used for short-wave QSOs, DX, and long-distance contacts.

Most amateur radio hobbyists monitor FT8 frequencies on the HF bands. During meteor scatter or [sporadic-E](Sporadic%20E%20propagation.md) propagation, VHF or UHF FT8 signals can sometimes be received from over 1000 km away.

To avoid interference and maintain reliable operation, hams have designated specific FT8 frequencies in each amateur band. Common short-wave frequencies include 7.074 MHz (40 m), 14.074 MHz (20 m), 21.074 MHz (15 m), and 28.074 MHz (10 m).

#### Format and requirements

FT8 communication requires strict time accuracy. Each transmission must begin exactly at 00, 15, 30, 45, or 60 seconds. If the station clock is not properly synchronized, messages will likely fail to decode.

FT8 has 6 stages, usually like this.

- The format of the FT8 contact in different stages
- Tick   Format   Example
- 00tick(6th message)   CQ <Callsign TX> <QTH TX>   CQ BH8GIS OM20
- 15tick(1st message)   <Callsign TX> <Callsign RX> <QTH RX>   BH8GIS JA3KWJ PM85
- 30tick(2nd message)   <Callsign RX> <Callsign TX> <QSA>   JA3KWJ BH8GIS -2
- 45tick(3rd message)   <Callsign TX> <Callsign RX> <R-QSA>   BH8GIS JA3KWJ R-12
- 60tick(4th message)   <Callsign RX> <Callsign TX> RR73   JA3KWJ BH8GIS RR73
- 75tick(5th message)   <Callsign TX> <Callsign RX> 73   BH8GIS JA3KWJ 73

---

*Source: Wikipedia, FT8 (https://en.wikipedia.org/wiki/FT8), by Wikipedia contributors, CC BY-SA 4.0.*
