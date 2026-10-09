# Is it possible to have 2 FM transmitters on the same frequency?

*Tags: repeater, repeater-coverage · score 6*

## Question

Has there been any success in transmitting two simultaneous FM signals? I am assuming if the phase is correct, and the signals are identical, it would be possible.

That would be really nice if newer repeaters could find a way to broadcast two signals on the same frequency from two different locations, giving extended coverage without sacrificing more coordinated frequencies. RX is already solved with voting receivers, but I haven't heard much on the TX end.

## Answer (score 4, by Dave Tweed N3AOA)

Yes, it's very possible, and in fact, it's quite commonly done in commercial FM broadcasting, in order to provide full coverage for major metropolitan areas.

The key to making it work is to make sure that the *modulation* (not the carrier) of two transmitters is time-aligned in the "overlap" region where the signal levels are approximately equal (e.g., within 6 dB). Outside this region, an FM receiver will "capture" one transmitter or the other, but inside this region, it will randomly jump from one to the other. But as long as the modulation is time-aligned, the output of the detector is essentially the same regardless.

That isn't to say that there aren't many compromises in such a system. Given the variabilities of terrain, etc., it's impossible to get optimal time alignment in all of the overlap regions. Considerable effort goes into modeling the placement of the transmitters (and to some extent, adjusting their power levels) in order to position the less-well-optimized regions away from high-traffic areas.

In the distant past (1990s), I worked for a company that sold networking equipment to commercial radio stations, and I designed the part that implemented the required timing control.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4972/is-it-possible-to-have-2-fm-transmitters-on-the-same-frequency, by Skyler 440, Dave Tweed N3AOA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
