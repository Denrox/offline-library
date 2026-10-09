# What is the difference between channel & frequency & band in RF?

*Tags: frequency, jargon · score 12*

## Question

I am reading about wireless networks basics. I found three terms I cannot find exact definition for: channel, frequency band, frequency.

Can anyone give exact definitions for them?

## Answer (score 18, by Kevin Reid AG6YO)

If you don't know what a **frequency** is, you need to read up on waves-in-general and radio waves. But the other two terms can be defined in terms of frequency; frequencies are the “natural” thing and everything else are things people invented on top of that.

A **frequency band**, or **band**, is a range of frequencies with a specific least frequency and greatest frequency. Generally bands are used to describe some relevant range:

- A radio is capable of operating within some band of frequencies; outside that band its performance will not meet specification or it will be incapable of tuning there.
- The legal limits on transmissions are defined in terms of many bands; when people say "the 2.4 GHz band" they mean the ISM band that extends from 2.400 GHz to 2.500 GHz, which is purely a legal definition and has no technical significance other than that devices may be internally restricted to operate in those bounds.
- When a signal is actually transmitted, we can talk about the band of that signal, that is, the range of frequencies which have significant/useful signal power on them. This usage is where the terms "in-band" and "out-of-band" come from. (The *bandwidth* of a signal is the size of the band, the lowest frequency subtracted from the highest frequency.)

**Channel** has two different meanings:


Usage of a band can be **channelized**, which means that the radios which transmit on it do not pick frequencies arbitrarily but stick to a certain step size (e.g. 10 KHz for CB radio, so frequencies like 27.105, 27.115, 27.125 MHz). This makes it easier for a receiver to match a transmitter, and allows more efficient use overall as there are no wasted narrow gaps between signals. If you want to see a spectacular example of precise channelization, take a look at broadcast FM radio: stations with added HD Radio digital signals transmit right up to the limits of their channel.


In communications theory, the **channel** is the medium that carries the signal. This is a different kind of word than the others because it's an abstraction that is not about frequency, but it is like the above in that to look at an RF channel you ignore everything outside of the frequency range that defines the channel. Within that range, you care about the effects on the signal — loss, noise, multipath, fading, etc. — and those effects are frequency-dependent on a larger scale and possibly even within the channel.

## Answer (score 4)

A channel is a generally accepted stopping point - somewhere that we know other people or devices will be listening. For example, in the United States, amateurs get access to 5 distinct channels on the 5 MHz band. Or your WiFi router uses several channels, but most of those channels overlap.

A frequency band is a range of frequencies. They're usually referred to by the wavelength (e.g. 40 meters is the band from 7000 KHz to 7300 KHz).

A frequency is the reference point for tuning your transceiver. Depending on how you're communicating, you'll be using far more than that single frequency, but when people mention a frequency, that's what they're referring to - where you should set your transceiver.

## Answer (score 2, by Scott Earle)

For regulatory purposes, a frequency is usually used to refer to a carrier frequency, which has a specific meaning related to the mode of transmission (for example, in an SSB transmitter the carrier frequency is in theory never actually transmitted, but in a morse code CW transmitter it is the only frequency ever transmitted).

A frequency band is a range of frequencies with a lower and upper limit. If the regulations state that you must only transmit signals within a specified band, then you must make sure that your transmitted signals never go outside that range of frequencies - again, very easy to determine when transmitting CW, not so easy with SSB, AM or FM (requires knowledge of the bandwidth of the transmitted signal on each side of the carrier).

A 'channel' is an agreed-upon set of specific frequencies with additional information included in the agreement. For example, in the amateur 2m and 70cm bands, a portion of the band is 'channelised' and set aside for repeaters. These repeaters use specific spot frequencies for both their inputs and outputs, and have certain other requirements regarding mode (FM), deviation (for example, max. 3kHz) and other requirements for CTCSS tones and the like.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5547/what-is-the-difference-between-channel-frequency-band-in-rf, by ashok, Kevin Reid AG6YO, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
