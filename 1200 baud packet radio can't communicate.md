# 1200 baud packet radio can't communicate

*Tags: diy, modes, packet · score 6*

## Question

I'm toying with a simple 1200 baud packet radio I built. I'm attempting for it to be compatible with APRS, which uses the Bell 202 signaling, 1200Hz for mark and 2200Hz for space, which I assume map to 0 and 1 respectively.

However it's not communicating with the commercial TNC I'm using or testing.

I've tried mapping 1 to space and 0 to mark as well, but that doesn't work either.

## Accepted answer (score 7, by Rocketmagnet)

If you're used to dealing with protocols between chips, like UART, SPI and I2C, then APRS will feel quite strange. Whereas if you've been involved with CAN, Ethernet, USB at the low level, then APRS will seem quite familiar.

It's not as simple as 1200Hz means 0, and 2200Hz means 1. There are two things which make it different, firstly bit-stuffing, and secondly NRZI encoding.

**Bit-Stuffing**

For reasons that will become clear in a moment, you're not allowed to transmit more than 5 1s in a row. If you want to transmit more than five 1s in a row, you'll have to stuff extra 0s to break up the string of 1s.

**NRZI**

Non-Return to Zero inverted is an alternative way to encode a bit stream. Surprisingly, it's the change from one frequency to the next which encodes 0 and 1. Between each 1/1200th of a second, if the frequency changes, that's a 0, and if it doesn't change, that's a 1.

Take your original bit stream. Imagine turning all the 0s into edges, and all the 1s into not-edges, like this:

Then join up the edges, like this:

The receiver uses the frequency changes to synchronise itself to the incoming bit stream. It needs to do this fairly often to make sure it stays synchronised. This is the reason that a long string of 1s isn't allowed. A long string of 1s means a long time without any frequency changes.

For more information on implementing APRS, there's a good set of blog posts on Hugo's Projects which goes into detail about all of the implementation issues.

## Answer (score 5, by Adam Davis)

While 1200 baud packet radio uses AFSK with 1200 and 2200 tones, they don't correspond with digital 1's and 0's directly. It employs NRZI encoding as well as bit stuffing. Non-return to zero inverted (NRZI) means that a 0 is encoded as a change in tone, and a 1 is encoded as no change in tone. This depends on having an accurate clock on both ends. But even with a decent clock, a long string of unbroken 1's will end up providing no changes in tone, and after awhile the clocks will drift apart, and the receiver may think it's on the 50th 1 in a row, while the transmitter is on the 49th 1 in a row, because the tone is never changing.

For that reason if there are five 1's in a row, a 0 is inserted at the end of the fifth 1. This forces a tone change, so that the receiver can match its clock with the sender at least every 5 time periods based on the tone change. The receiver, upon seeing a tone change after 5 time periods of no tone change, discards the tone change (the digital 0), realigns the clock, and continues to decode the bitstream.

There is one time you might see 6 1's in a row, but that is a special flag on the AX.25 protocol, so it's not technically part of the 1200 baud system. It's common in packet radio, though, so it should be kept in mind.

I found this, and more, at "1200 Baud Packet Radio Details" by N1VG.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1006/1200-baud-packet-radio-can-t-communicate, by Adam Davis, Rocketmagnet. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
