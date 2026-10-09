# Why is gain used?

*Tags: antenna, gain · score 6*

## Question

It always confused me why 100 watts out of your transmitter could radiate 200 watts coming from a high-gain antenna.

Why is the term gain used instead of directionality?

## Answer (score 10, by hotpaw2)

The directional antenna doesn't actually radiate 200 Watts, it just focuses the actual mere 100 Watts so that along some optimal directional axis, a receiver would see same power as if an imaginary 200 watt transmitter using an imaginary isotropic antenna were instead the source.

Which makes it easier to categorize the radiated power from that "high gain" antenna in that optimal direction using just one number, instead of 2 or more.

An additional 100 Watts isn't created, more like taken away from other less optimal directions in the antenna's radiation pattern.

## Answer (score 9, by Phil Frost - W8II)

I'm going to assume you mean directivity, not directionality. Then:

Why is the term gain used instead of [directivity]?

These are two related but different things.

Gain measures the ratio of input electrical power to output electromagnetic radiation (or the reverse, for receiving). It is a spherical function, that is: an antenna has gain defined for any direction, azimuth and elevation. When we discussing just "gain" as a single number and not a function, it's usually understood that we mean *maximum* gain: the gain of the antenna in the direction of peak sensitivity.

From the law of conservation of energy, a passive antenna (one without any amplifier or other source of energy) can't have an *average* gain greater than 1. The only way it can radiate more energy in one direction is to radiate less energy in another direction. The total power output remains the same.

Directivity is a measure of the extent to which an antenna does this. If the gains are normalized such that the peak gain is 1, then directivity is 1 divided by the average gain over all directions. An isotropic antenna, one that radiates equally in all directions, has a directivity of 1.

It's possible to have a high directivity, low gain antenna. Simply build a very lossy, very directional antenna. This antenna might have a peak gain of -10dBi. The average gain might be -60dBi. That is, it receives and transmits much better in one direction, and thus has a high directivity, but even in that direction it's very poor. In practice we might actually call this device a dummy load or a heater.

To build a high gain, low directivity antenna you must have an amplifier. An amplifier with a low directivity antenna could be considered a high gain, low directivity system.

Assuming that we can point our antennas appropriately, then peak gain is a useful number for the calculation of a [link budget](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md). We might then care about directivity if we consider all energy received from unintended directions as "noise": then maximizing directivity will minimize noise. Conveniently, if we can make a passive antenna more directional without also making it less efficient, then we maximize both peak gain and directivity.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1631/why-is-gain-used, by Skyler 440, hotpaw2, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
