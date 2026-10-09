# Antenna polarization when dealing with satellite communications

*Tags: antenna, satellites, polarization · score 3*

## Question

It's easy to understand, conceptually anyway, the difference between a horizontally polarized antenna and a vertically polarized one, when referenced to ground. However, when they are pointed nearly straight up at a satellite that reference is effectively lost. Yet communications with satellites require different polarizations. How does that work?

## Accepted answer (score 9, by Glenn W9IQ)

Satellite engineers tend to use circular polarization for two reasons:

1.

When a linearly polarized signal travels through the atmosphere there are anomalies, such as Faraday rotation, that alter the polarization of the EM wave.

2.

The geographic reference of the satellite polarization changes for a non-stationary satellite as it traverses its path above the earth-bound point of observation.

Either of these conditions can introduce significant antenna system losses when linear polarization is involved.

A circularly polarized EM (electro-magnetic) wave refers to a wave that rotates between horizontal and vertically polarization and all planes in between. The rotation cycle repeats once per wavelength. When viewing the wave in the direction of travel, a clockwise rotation is considered right hand circular (RHC) polarization while a counter (anti) clockwise rotation is considered left hand circular (LHC) polarization.

Amateurs often use cross polarized linear yagi antennas for circularly polarized satellite communications. Technically these produce an elliptical polarization. With a simple control of the phasing network, a near RHC or LHC polarization can be achieved.

The loss between antennas of mismatched polarization, when one involves circular polarization and the other is linear, is typically limited to 3 dB. This is contrasted to the loss between a worst case horizontal and vertical polarization that can incur a >20 dB loss (in theory, an infinite loss). There is a similar high loss when a RHC polarized antenna is used with a LHC polarized signal and vice versa.

[EDIT]

If you are interested in this topic, there is a very nice article on antenna polarization experiments by first year MIT engineering student, 18 year old Adeline Hillier AA7HH, in the January 2019 issue of QST. It is great to see this type of interest and enthusiasm from an aspiring electrical engineer.

## Answer (score 3, by Marcus Müller)

However, when they are pointed nearly straight up at a satellite that reference is effectively lost

Satellite communications typically uses *circular* polarizations instead of *linear* (horizontal/vertical) for that exact reason; that's why when you open e.g. sat-TV feedhorns, you'll often find "snail"-shaped structures inside.

With clockwise and counterclockwise, you don't need absolute orientation; what's important is the same "rotational direction", if you will.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12414/antenna-polarization-when-dealing-with-satellite-communications, by mike65535, Glenn W9IQ, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
