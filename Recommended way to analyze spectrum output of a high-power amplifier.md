# Recommended way to analyze spectrum output of a high-power amplifier?

*Tags: amplifier, measurement, equipment-protection · score 5*

## Question

I have a small collection of "software defined RF lab" equipment, notably a HackRF and a VNWA3. I am almost done building a 35W HF amplifier and once I've done some other testing, would like to look at the spectrum of the final output as a whole.

The most natural tool for this job would be a spectrum analyzer, of course, but any of my SDR receivers and/or the VNA should be able to handily gather spectrum data as well. The trouble is: all of my equipment is rated for input in the ballpark of 0dBm, i.e. milliwatts or less. It looks like even a "real" spectrum analyzer like the entry-level Rigol DSA815-TG has input rated around +20 dBm (100 milliwatts).

In preparation for another project where I want to diagnose a ~5W signal, I bought a handful of SMA attenuators. The larger dB-drop ones have heat sinks and are rated at 5W — so I should be able to connect my "device under test" for this other project directly to my equipment through the attenuators.

But how would one go about measuring the spectrum of a 35W signal? Or 1500W and beyond for that matter! I could be mistaken, but I get the impression that that inline attenuators are NOT a common method past a certain power level.

How are high-power signals typically measured in a professional RF lab setting? How might I go about characterizing my signals with more typical amateur operator equipment? Say, between my amp and a dummy load and an SDR, what's a good way to connect/couple them so that I can get a known — or at least "known-to-be-safe" — signal level into some spectrum analysis software?

## Accepted answer (score 6, by Dave Tweed N3AOA)

Professional-level dummy loads generally have a "sampling" port that provides a reduced level signal for analysis. You should be able to create something similar.

## Answer (score 3, by K7PEH)

As answers already posted show, there are a variety of solutions to this problem. But, a very simple one is an old timer ham radio operator's "trick". Popular back in the late 1950s and 1960s as "the only way" to hook up an oscilloscope (which also usually had low power input needs) to a high power amplifier was to use a regular PL-259 coaxial connector. You snip off the center conductor pin from the male plug (it doesn't hurt too much if you do it fast) and then hook up to the output of your amplifier. You do not screw the PL-259 all the way in but fiddle with it to get just the right signal pickup to drive your measuring device. It capacitively couples with the source. Works quite nicely but I do admit to never having done it with power as low as 35 watts. Usually I have had 1000 to 1500 watt amplifiers feeding my oscilloscope.

## Answer (score 2, by Phil Frost - W8II)

As Dave Tweed says, professionals have equipment for exactly this. But since you are asking I bet you don't have that equipment.

If you just want something on the cheap, transmit into a dummy load at full power and put the receiver nearby. There's enough "accidental" coupling you can probably hear the transmitter even without an antenna.

The trouble with this is it's not calibrated or reproducible at all, which is important in a professional context. However if you just need to see a spectrum, and you don't need to make accurate quantitative measurements, it's probably good enough.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6185/recommended-way-to-analyze-spectrum-output-of-a-high-power-amplifier, by natevw - AF7TB, Dave Tweed N3AOA, K7PEH, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
