# Antenna size for wideband

*Tags: antenna, frequency · score 10*

## Question

I just bought a SDR dongle that comes with an antenna. The dongle is for DVB-T.

The antenna is very small but the specs say that the dongle can go 30Mhz to 850Mhz.

From my knowledge of antenna physical size should be 1/4 the size of the wavelength.

How can the small antenna scan from 30Mhz to 850Mhz? i thought the size of the antenna would have to be different to accommodate that wide of a frequencies. Unless there is a design of antenna i do not know about and i can not find the answer anywhere on the internet.

## Accepted answer (score 8, by Kevin Reid AG6YO)

An antenna of the wrong size is just an antenna that is not *resonant* at the particular frequency — meaning that each cycle of the radio wave *captured by and conducted in the antenna* does not perfectly match phase with the preceding cycle, since that only happens at the specific length.

(Incidentally, the length of 1/4 wavelength is appropriate for a *ground plane* antenna, which you don't exactly have unless you have a ground plane. (Those antennas usually have a magnetic base — stick it on the biggest flat metal object you have handy for better performance.) Other designs of antennas have other required lengths.)

When the antenna is not resonant, it will be *less efficient* at transferring energy from electromagnetic radiation to the feed point (connection to the cable to the dongle), or vice versa. The effect of this for reception is that you will see *slightly* stronger signals close to the resonant frequency of the antenna, and weaker signals elsewhere, but the antenna will still work.

This can be to your benefit — the antenna is acting as a (not very sharp) filter, and filtering out frequencies you *don't* want to receive gets you less noise in the signal you *do* want. So, if there is a particular frequency range you are interested in more than others, or which typically has weak signals whereas other bands have strong signals not needing any help, then you can improve the situation by using an antenna of the right length for about that frequency (either cut and built to that length, or using a telescoping element).

The place where the resonant frequency really starts to matter is when you are *transmitting*, because that's where the inefficiency starts to hurt. When receiving, [it doesn't matter how efficient the antenna is as long as the signal is strong *enough* that the ambient noise floor received by the antenna exceeds the receiver's inherent noise floor](Can%20I%20improve%20reception%20with%20a%20more%20sensitive%20antenna%20preamplifier%20better%20feedline.md). On the other hand, when transmitting, the inefficiency is wasted energy and decreased range. A sufficient mismatch will damage equipment (usually the transmitter's amplifier first) due to heating or excess voltage.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4994/antenna-size-for-wideband, by Martin Naughton, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
