# Antenna RX vs. TX

*Tags: antenna, antenna-theory · score 10*

## Question

If I only want to receive radio signals and not transmit, are there any differences in the way I design the antenna I need to use, or is it the same either way? I was going to pick up a Realtek RTL2832U and use it as an SDR, but it has an antenna that I would like to improve. (Approx range: 25MHz-1700MHz)

## Accepted answer (score 8, by Kevin Reid AG6YO)

Most of the issues are already covered in this previous answer by Phil Frost to “[Is there a simple, DIY, antenna suitable for HF receive only?](Is%20there%20a%20simple%2C%20DIY%2C%20antenna%20suitable%20for%20HF%20receive%20only.md)”:

Receive antennas are the easiest thing ever. You just need two things:

1. something that conducts electricity
2. another thing that conducts electricity

… Don't worry about tuning, or impedance matching. This also will increase the fraction of the energy received by your antenna coupled to the receiver, but again, once you have enough to overcome the receiver's noise, more is of absolutely no help.

…

If you really must worry about something, worry about getting your antenna away from noise sources. …

As covered there, most characteristics of the antenna don't matter if you are not transmitting.

However, if you are interested in the VHF/UHF (rather than HF) frequencies which those receivers cover, there are a couple more concerns.

1.

Polarization matters, because it is not randomized by the ionosphere. You will want your antenna to be vertically or horizontally polarized depending on what signals you want to receive. In the amateur radio bands, most VHF/UHF signals are vertically polarized.

2.

Location matters. At these frequencies signals are much closer to propagating like light — you want a clear path from the transmitter to your antenna, if possible. For strong transmitters like FM broadcast stations and amateur repeaters, this is less of an issue.

3.

Finally — this is equally applicable to HF but more practical at higher frequencies — if you are seeking to receive weak signals, it is helpful to have a *directional* antenna pointed at the source. The most common amateur uses for directional antennas at VHF are satellite communications and direction-finding.

So, get a piece of wire of roughly the right length for the band you think you'll be most interested in (again: doesn't matter much), mount it vertically as high in the air as you feel like arranging, hook it up to the center contact of your receiver's antenna port, and there you go. Or if you want to buy something premade, buy a “scanner” antenna, because those are intended for receive-only use and wide bandwidth.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1567/antenna-rx-vs-tx, by Jason Petrilla, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
