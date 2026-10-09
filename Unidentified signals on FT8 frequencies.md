# Unidentified signals on FT8 frequencies

*Tags: digital-modes, signal-identification, ft8 · score 5*

## Question

When I work in FT8 mode I often see signals like these:

I couldn't identify these signals using SigiWiki nor managed I to decode them using WSJT-X. Though these signals seem to use 15 second frames. They don't seem to be a noise created by stations that use too much power.

Does it look like any amateur radio digital mode to you?

## Accepted answer (score 5, by hobbs - KC2G)

The fact that they align properly to the FT8 15-second period, and have 8 tones (the same as FT8) is a sign that these may be distorted FT8 signals, caused by AF harmonics in the transmitter or the receiver. The one on the right, being about 100Hz wide, is a second harmonic, and the one on the left, being about 150Hz wide, may be a third harmonic.

But before you go looking for the offending signal at 1/2 or 1/3 of the audio frequency, remember that when the "Split" option in wsjtx is set to "Rig" or "Fake It", the software will adjust the TX VFO in order to put the transmit audio somewhere between 1500 and 2000 Hz. e.g. if you're on 14.074.000 and you put your transmit cursor on 235Hz, wsjtx will actually tune the rig to 14.072.500 and send it audio at 1735Hz; if you put your transmit cursor on 2560Hz, wsjtx will tune the rig to 14.075.000 and send it audio at 1560Hz. If the distortion is being caused by the transmitter, therefore, the subharmonic will probably *not* appear on the waterfall at 1/2 or 1/3 of the frequency of the harmonic product.

Even with this offsetting, a third harmonic anywhere to the left of 3000Hz on the waterfall is hard to explain, but it may be caused by frequency aliasing in the receive path. Perhaps someone else has a more complete explanation.

## Answer (score 3, by Glenn W9IQ)

Both marked signals follow an 8 tone MFSK pattern. The one on the left is about 125 hertz wide while the one on the right is about 100 hertz wide.

The signal on the left appears to follow the waterfall that would be expected from an Olivia 8/125 (8 tones with 125 hertz bandwidth) signal although this is not a common Olivia mode. Olivia is a free typing, teletype like mode, so the 15 second sequence wouldn't apply.

I cannot offer any suggestions for the 100 hertz wide signal on the right of the waterfall.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12976/unidentified-signals-on-ft8-frequencies, by Aleksander Alekseev - R2AUK, hobbs - KC2G, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
