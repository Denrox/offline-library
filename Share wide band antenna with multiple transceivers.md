# Share wide band antenna with multiple transceivers

*Tags: antenna, transceiver, antenna-system, electronics, transmitter · score 5*

## Question

I'm trying to incorporate several transceivers on my board design; I need

- WiFi (2.4 GHz)
- SatCom (~1.6 GHz)
- RF (~900 MHz) and
- GNSS (~1.5 GHz).

I need to combine them into one antenna. I found a wide band antenna that can handle the 700 MHz to 5 GHz frequencies, but I'm not sure how to combine or mix the signals for transmission.

I'm presuming that I won't need to worry about it for receiving - but what's the proper way to accomplish this combining?

## Accepted answer (score 7, by Marcus Müller)

A wideband antenna is not what you're looking for – you really don't care about anything *between* 900 and 1500 MHz, or between 1600 and 2400 MHz.

Wideband antennas are inherently hard to make, and even harder, even impossible, to make uniformly good across their whole range.

What you much likely will rather want is a *multi-band* antenna. For example, I'd assume that you can get 2400 + 900 MHz antennas commercially, as that is, due to ISM bands, a rather common combination.

Something feels off about your presumption that you'll build a GNSS *transceiver*; you definitely want a receiver, but I doubt you'll send data to a GNSS satellite ;)

So, honestly, what small multi-band devices like smart phones do is having separate PIFA antenna for the completely separate GPS receiver (that luckily fall far above the 800/900 MHz GSM frequencies and far below UMTS at 1800 MHz), and then typically have some combined multi-band antenna for the rest, which is integrated into the mechanical design of the device.

Simple multi-band antennas I've seen look like connected dipoles for different wavelengths – but not really, the "branches" tend to be slightly offset (not periodically offset like in logper wideband antennas) and not quite exactly as long as they should be. My best guess is that someone started with an antenna that is just multiple dipoles for these frequencies connected to the same feedline, and then just simulated that, got the frequency response, and started randomly change lengths and positions until things worked out.

## Answer (score 8, by Glenn W9IQ)

The basic concept is to use RF bandpass filters for each frequency range. This is frequently done by hams for VHF and UHF applications. The common term for a grouping of these filters is diplexer, triplexer, or quadplexer as appropriate. Sometimes the term "duplexer" is used although this creates confusion with a different device that is typically much more expensive and used for repeater implimentations. Here is one example of a triplexer for the frequencies used by ham radio operators.

The nice thing about these type of bandpass filters is that they work for transmit as well as receive. During receive, each received frequency range is routed to the correct receiver with minimal loss. This is advantageous compared to simple splitters or combiners that divide the receive power among all of the radio ports equally thereby effectively reducing the receive range of each radio.

It is unlikely that you will find an off the shelf version of a quadplexer for your indicated frequencies. You can design and build such devices but in order to properly tune them, you will require some test equipment such as a spectrum analyzer with a tracking generator or a wide band vector network analyzer. If you have access to some of this type of equipment, please indicate so and I will update my answer with more specific design guidance. In the end, you may find that it is easier and less expensive to simply use separate antennas.

I would be concerned about an antenna that claims a 700 MHz to 5 GHz bandwidth as this suggests the antenna may not be very efficient. You may wish to update your question with a link to the antenna you are considering.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12575/share-wide-band-antenna-with-multiple-transceivers, by Jedi Engineer, Marcus Müller, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
