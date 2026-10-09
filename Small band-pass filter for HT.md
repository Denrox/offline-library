# Small band-pass filter for HT?

*Tags: baofeng, filter · score 6*

## Question

I'd like to add a band-pass filter to my Baofeng UV-82 to make it comply with the spurious emissions requirements. Ideally it would be a rigid device with SMA or BNC connectors that would fit between the radio and the antenna.

I'm open to building my own, but it would have to be a foolproof design because I don't have the test equipment to verify it. Buying one is also an option as long as the price is reasonable.

You can see how bad the emissions are in this video that I found: https://youtu.be/mLjc3-gSU-M?t=6m14s When transmitting on 145 MHz, there are strong signals from 35 MHz up to 1.025 GHz.

What can you recommend? (Besides the obvious "buy a better radio" suggestion. I don't have the budget for that.)

## Accepted answer (score 4, by Phil Frost - W8II)

If you want cheap, building your own is not difficult. Here's a simple low pass pi filter:

The values of the components should be such that they have a reactance of 50 ohms at the cutoff frequency, which should be just a little above the top of the 2-meter band, if that's your objective.

For better attenuation you can cascade two of these together. Since you'll end up in one section with two capacitors in parallel, you can replace this with a single capacitor of half the capacitance for an equivalent circuit.

Since the output power of the HT probably isn't more than 5W, you won't need unusually high-voltage capacitors. You want to keep the leads as short as possible to minimize stray inductance. I'd use large chip capacitors. At 2 meters you can probably get sufficient inductance out of air-cored coils you wind yourself from enameled wire over a pen or something for a form. Align them with their axes at right angles to minimize coupling between them.

Perhaps build it in a small cast-aluminium box or copper pipe (suggestion from comments), put a couple SMA connectors on it, and you should be golden.

## Answer (score 4, by Mike Waters)

[This was from comments by @MarcusMüller and myself. I've moved them to this answer.]

Don't underestimate the filtering effects of an antenna. It's most important how the spurs "close" to your intended frequency are – the rest will be attenuated by the antenna (do try to at least theoretically estimate the attenuation, though!). Antennas can actually be made resonant for only a small bandwidth – maybe that's actually key to a solution here, because it's anyway likely that you'd want to use an antenna that's not a full-sized monopole :)

A recent ARRL review of a Baofeng handheld did it the way the it was done in the video the OP found --with similar results-- which was a bad example that perhaps the video's creator copied. The way to do this test would be to transmit with the stock antenna, and pick up the signal using a broadband antenna (such as a Discone) out in the open and at least a a couple of wavelengths away, and feed the received signal into his spectrum analyzer.

This is not to say that the Baofeng is a marvel of technical engineering excellence. ;-) *Any transmitter should be able to use a broadband antenna --like a discone-- without transmitting those spurs, and it appears that this one cannot do that.*

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9765/small-band-pass-filter-for-ht, by mrog, Phil Frost - W8II, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
