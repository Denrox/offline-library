# Is is possible to operate D-Star from a software-defined radio?

*Tags: modes, software-defined-radio, digital-voice, d-star · score 14*

## Question

What is preventing a software-defined radio from transmitting the D-Star protocol?

## Accepted answer (score 17, by Sterling N0SSC)

Nothing is preventing an SDR from transmitting the D-STAR protocol, other than the need to implement it as such. It is open, and currently I know that Digital Signal Decoder (DSD) can actually decode some data and textual frames.

What prohibits transmission of D-STAR Digital **Voice** is the codec used to encode the voice - it's AMBE2000, which is patented and proprietary. A license for one of these is in the ballpark of $100,000, allowing only large businesses to use it. Icom, having already developed P25 hardware using the AMBE codec, is the only one to do so thus far, aside from the DVDongle (though I don't know how they can afford to use it). The reason why AMBE was chosen was because it was the only low-bitrate RF speech codec available at the time.

Now, if codec2 can be implemented over D-STAR (or its own protocol, like FreeDV), it would be completely open. This is certainly a future development.

## Answer (score 6, by Phil Frost - W8II)

Nothing. In fact, the UDR56k is an SDR and transmits D-STAR.

If you want D-STAR digital voice, you do need to purchase an add-on card which contains an ASIC from DVSI implementing the propritary AMBE codec, or pay a substantial (but undisclosed publicly) licensing fee. One can safely assume that any licensing agreement would forbid any free proliferation of the implementation.

The DVDongle contains the same ASIC, visible here as the large IC on the right, with "AMBE-2000" printed on it:

The middle IC is at Atmel microcontroller, and the IC on the left looks like an FTDI USB interface. There's not much else to it.

## Answer (score 2, by k7ve)

The DV3000 from NW Digital Radio provides the AMBE Vocoder. One person has modified Digital Speech Decoder (DSD) to use it instead of reverse engineered library, it is also supported by other solutions such as G4KLX's DummyRepeater. An AMBEServer, (Raspberry Pi + DV3000) on your LAN would provide Vocoding to a SDR if the proper protocol and modulation components were available.

The UDRX-440 is a band limited SDR which will provide GMSK modulation and use the DV3000 internally to provide D-STAR Digital Voice.

http://nwdigitalradio.com/category/dv3000

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/809/is-is-possible-to-operate-d-star-from-a-software-defined-radio, by Paul V, Sterling N0SSC, Phil Frost - W8II, k7ve. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
