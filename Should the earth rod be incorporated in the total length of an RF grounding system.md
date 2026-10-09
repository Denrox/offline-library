# Should the earth rod be incorporated in the total length of an RF grounding system?

*Tags: grounding · score 3*

## Question

I have installed a grounding system just outside my radio shack and was careful to avoid a quarter wavelength or multiples thereof (for single band use), or anything in total length that is close to this. However, I then thought to myself, what if I have created a quarter wavelength by not including the six foot copper earth rod? What are people's thoughts on this please?

## Answer (score 4, by Phil Frost - W8II)

The reason to avoid multiple of a quarter-wavelength is that by virtue of the length this will transform the low impedance at the ground rod into a high impedance. This implies you are expecting this ground connection to carry significant RF current when you transmit.

Such antenna system designs are not usually good ones, for a couple reasons.

Firstly, soil is not a great conductor. Any antenna system with significant current in the soil will experience significant resistive loss. Antenna efficiency will suffer.

Secondly, if your desk must be grounded that implies high RF current at the desk. That presents a higher risk of RF burns if you're operating at higher power. It also means your desk and everything around it is part of the *receiving* antenna, which will be profoundly horrible for performance since nearly every modern desk is surrounded by digital noise sources.

In the early days of radio it was common practice to ground the transmitter, and for the antenna to be just a wire coming out of the transmitter. This is effectively what we could call a "vertical" or a monopole today, but with the transmitter right at the feedpoint, and no radials.

But in the decades since, we've developed convenient and inexpensive coax feedlines, and RF engineering is much better understood. Station designs that require a low-impedance ground as part of the deliberate RF path might still have a valid application in temporary, low-power stations where the ease of setup is more important than efficiency and the risk of RF burns is non-existent. But for any semi-permanent station, it's time this design is relegated to history books.

Instead of trying to make your ground system a particular length so it can have a low impedance for common-mode current, strive to eliminate the common-mode current at the source. This means [if you are using a dipole with a coax feed, use a balun](Using%20a%20balun%20with%20a%20resonant%20dipole.md). If you are using a vertical, install radials. If you are using some other kind of antenna which has just one terminal at the feedpoint, don't use that kind of antenna.

[Measure the common-mode current](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md) on the feedline and/or your ground connection to guide your efforts.

There are still reasons to ground your equipment, such as to avoid electrocution if a live mains wire comes in contact with a chassis through some fault, or for [lightning protection](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md). But these applications don't require a low-impedance ground at your specific transmitting frequency, so there are no particular lengths to avoid.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17536/should-the-earth-rod-be-incorporated-in-the-total-length-of-an-rf-grounding-sy, by Francis Archibald, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
