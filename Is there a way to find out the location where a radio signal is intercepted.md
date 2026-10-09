# Is there a way to find out the location where a radio signal is intercepted?

*Tags: receiver, direction-finding · score 4*

## Question

I am a software engineer and a noob to radio.

Is there a way to find out the location where a radio signal is intercepted? That is, the location where somebody is eavesdropping on my wireless communication.

I don't believe this can be done if the receiver is not transmitting back, but I would like some expert advice.

## Accepted answer (score 7, by Katrina Petkovic)

Yes. Detecting a receiver is VERY VERY VERY hard to do. Since it is only an absorber rather than transmitter of RF energy, it requires a signal strength meter to detect a dip in RF energy. It requires a very directional antenna, and circuitry to detect subtle changes in the signal. This is compounded by the fact that the receiver has a high-gain amplifier inside, so it "steals" very little RF energy. I would stake my bets that one would have better luck if there were a local oscillator inside. Personally, I'll stick to detecting transmitters. AM radios may be easier to detect than FM radios because of the local oscillator.

## Answer (score 8, by Kevin Reid AG6YO)

It is possible *in principle* to detect a receiver.

1.

Almost all designs of receivers have a *local oscillator* (LO), which oscillates at the same frequency as the carrier frequency of the signal it is receiving, or at some close offset to it. The signal from the LO can leak back out the antenna. However, in a well-designed receiver this leakage is minimized and will always be immensely weaker than the signal from a transmitter.

2.

A receiving antenna collects radio waves — electromagnetic energy. It therefore casts a shadow: if the receiver is between you and the transmitter, the signal will be weaker than if the receiver wasn't present. However, this effect will most likely be very much smaller than the effects of other large objects in the area that are not even radio devices (buildings, metal objects, landscape, etc.).

These effects are very small and unlikely to be usable for good location purposes, or even to tell whether there's a receiver at all. Even using equipment designed for the purpose, locating a radio that is *transmitting* is tricky and requires readings taken at multiple locations, experience interpreting them, and guesswork; it will be essentially impossible for the orders-of-magnitude-weaker effects I've described above.

If you're talking about unlicensed digital communication systems like WiFi and Bluetooth, an additional complication will be other devices unrelated to yours actively using the same channel frequencies.

Finally, a hypothetical eavesdropper can be farther away than you might think: use of a directional antenna accurately pointed at the transmitter increases the received signal power, allowing it to be received from much farther away. Never believe any claims about how some wireless signal has a *maximum* range; it always depends on antennas and environmental conditions. (For a popular computer-security story on this, look up the “Bluetooth sniper rifle”.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2160/is-there-a-way-to-find-out-the-location-where-a-radio-signal-is-intercepted, by Suneesh, Katrina Petkovic, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
