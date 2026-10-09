# Why do today's transceivers use LC filters rather than crystal filters?

*Tags: equipment-design, filter · score 13*

## Question

Going through a number of schematics for today's receivers (Elecraft KX3, for example) I note that most use LC circuits for filtering. The wikipedia article for Crystal Filters suggests, however, that crystal filters are used in high quality receivers:

A crystal filter is very often found in the intermediate frequency (IF) stages of high-quality radio receivers. Cheaper sets may use ceramic filters ... or tuned LC circuits.

What are the disadvantages of crystal filters that make LC filters more popular for amateur radio transceivers?

## Answer (score 7, by makomk)

As Phil Genera says, the KX3 uses a different type of receiver that requires a different kind of filter. A traditional superheterodyne receiver, which is what you'd find in most older radios, uses a mixer to convert the desired signal to a fixed IF of say 10.7MHz and then uses a very narrow bandpass filter at that frequency to select only that signal. Crystal filters are particularly well suited here because they're extremely narrow, stable bandpass filters - far narrower and more stable than can be achieved with LC bandpass filters. Ceramic filters are very similar but cheaper, less narrow, and less stable.

The KX3 doesn't work like that. It's a quadrature direct conversion receiver - instead of converting the signal to IF, it converts it to a pair of I and Q signals at around audio frequencies, and then uses a pair of lowpass filters to filter out all the other frequencies, which can easily be implemented as standard LC filters. (Though looking at the schematic, those aren't the only filters - there's also some active filtering in the following amplifier stages. See the capacitors in the op-amp feedback loops? Those turn the amplifiers into additional low-pass filters. This is a very common and effective way of filtering audio-frequency signals.)

There is also a subsequent software filtering stage that's far sharper and more adjustable than the hardware filters, but this isn't specific to direct conversion designs - there are modern ham transceivers out there that use traditional superheterodyne receivers with a standard IF filter, followed by adjustable software filters.

So you might ask, [why use such a high intermediate frequency](How%20is%20the%20IF%20for%20a%20superhet%20selected.md) if it makes constructing filters harder? Image rejection. The mixer doesn't just convert our desired frequency to the IF, it also does the same with an image frequency exactly twice the IF away from the frequency we want. Since we can't make tunable RF filters that are anywhere near as narrow as our fixed-frequency IF filter, we have to make the IF high enough that we can stop the image frequency reaching the mixer using a relatively wide input filter. Using separate I and Q signals makes it possible to distinguish signals at the desired and image frequencies and makes direct conversion practical, but only if all the stages after the IQ conversion are done in software rather than hardware.

## Answer (score 4, by Gert-Jan Dam)

The KX3 receiver is a software defined radio SDR. The IF filters are made in the software. Since software IF filters are steeper than crystal filters the crystal filters are not necessary anymore. Another advantage is that SDR IF filter width is continuous adjustable. But band filters and audio filters are still LC filters like in the past. That has not changed. The IF of the KX3 is at audio frequencies. It is not really direct conversion but it is similar. These audio frequencies are fed to usually a soundcard and then the computer does the IF filtering demodulation etc. The KX3 is the first software defined radio that does not require a external computer. It’s a great radio. I ‘m never gonna sell it.

More info: http://en.wikipedia.org/wiki/Software-defined_radio

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1367/why-do-today-s-transceivers-use-lc-filters-rather-than-crystal-filters, by Adam Davis, makomk, Gert-Jan Dam. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
