# How many frequency channels are there in a frequency band?

*Tags: frequency, bandwidth · score 4*

## Question

I've often heard people saying that 4G uses the 1800 MHz band but precisely what all frequencies does it work upon? Does it mean that is just uses one frequency i.e. 1800 MHz, well in that case wouldn't there be interference among signals carrying different data.

1. What is the difference between a frequency band and frequency channel?
2. Why don't we directly use frequency ranges to tell what a particular technology operates upon instead of telling what band it uses. For example, why do we say that 4G uses 1800 MHz band instead of saying it uses frequencies between X MHz and Y MHz. Wouldn't it be easier to understand?

## Accepted answer (score 2, by rclocher3)

A frequency band represents a range of frequencies, which are usually defined by law or regulation. For instance, the 1800 MHz GSM band ranges from 1710.2 MHz to 1879.8 MHz, according to Wikipedia. Bands are wide enough to contain many signals without interference (universally, as far as I know). Because the frequency bands for a particular service are generally widely-spaced, it's usually quite clear what you mean by the usual shorthand definition of a band, if you're looking at a table showing the frequency ranges for the various bands for a particular service. Yes, it would be more clear to say "the 1710.2 to 1879.8 MHz band", but "the 1800 MHz band" rolls off the tongue much more easily. In amateur radio practice, the shorthand name for a band usually refers to its approximate wavelength in meters rather than the frequency, for historical reasons; for instance, the "20m band" in the US ranges from 14 – 14.350 MHz.

A channel is also a frequency range, which is usually defined by law, regulation, or general practice. However a channel is usually much narrower than a band, because a channel is typically only wide enough for a single signal. The intent of dividing a band into channels is to prevent interference. Sometimes channels are given numbers, but not always. Not all services are channelized; the amateur radio service generally uses unnumbered channels for VHF and UHF FM, according to state-wide (US) or nation-wide band plans, and the 60m band is channelized in the US because it is shared with federal government users, but other bands are usually not channelized. In other words, operators using other ham bands can generally select any frequency inside the band, as long as the entire bandwidth of the signal is within the band allowed by law. (Activity inside a ham band is often segregated by frequency according to voluntary "gentlemen's agreements" to reduce interference.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6839/how-many-frequency-channels-are-there-in-a-frequency-band, by Shivam Aggarwal, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
