# Why is 9 kHz the lowest frequency for spectrum analyzers?

*Tags: frequency, spectrum-analyzer · score 9*

## Question

I researched a number of spectrum analyzers and it seems that the lowest frequency that these operate at is 9 kHz.

Why is the lowest frequency supported by spectrum analyzers 9 kHz?

## Accepted answer (score 13, by tomnexus)

Spectrum analysers are often *specified* down to 9 kHz because this is the lowest frequency of conducted or radiated emissions that is specified in the Electromagnetic Compatibility (EMC) standards.

These standards apply to most electronic devices. They regulate both the strength and frequency of *intentional emissions* like WiFi, but also the *unintentional emissions*, electronic noise radiated from all electronics, for example LED lightbulbs. Because unintentional emissions can happen at all frequencies, there is a limit line that specifies the maximum field strength that may be radiated, over a range of frequencies.

The standards all start with something like this:

**Radiated emission limits; general requirements**.  
... the emissions from an intentional radiator shall not exceed the field strength levels specified in the following table

Several of the standards go down to 9 kHz, this is what drives the spectrum analyser design.

- FCC "Part 15" regulations for *intentional radiators* start at 9 kHz (summary)
- CISPR-11 and CISPR-22 specify radiated emissions from 9 kHz.  
They're not free but you will find good summaries around the web, here's one.
- MIL-STD-461 (freely available) specifies Radiated Emissions from 10 kHz to 18 GHz, (and conducted emissions from under 100 Hz!)

You will find that the spectrum analyser works below 9 kHz, often all the way down to DC, but it may not meet its specifications there.

There is good coordination between test equipment and regulatory standards. It goes in the expected direction, that equipment is designed to test things to the standard, but it also seems to go the other way, that the equipment manufacturers sometimes sit on the committees and drive the standards in their favour.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20614/why-is-9-khz-the-lowest-frequency-for-spectrum-analyzers, by kittygirl, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
