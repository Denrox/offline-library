# AX.25 to Kenwood $PKWDWPL sentence

*Tags: digital-modes, aprs · score 4*

## Question

In my vehicle, I have a Byonics TinyTrac4 paired with an AvMap G6. I also have a Kenwood TM-D710 that I'm currently using for voice. I live in a region of the US where both 2m APRS and 70cm High Speed APRS are in common use, and am interested in using BOTH radios, one on each band, to feed the G6. I MIGHT be able to get away with an off-the-shelf NMEA0183 multiplexer, assuming they don't drop sentences they don't recognize, and they are a bit out of my budget.

Instead, I would like to use a Raspberry Pi, paired with some good NMEA multiplexing software.

Additionally, I do a lot of off-roading, and I like the idea of being able to digipeat across the bands as well, ensuring that 1) I'm heard in an emergency, regardless of what they are running, and 2) everyone else can see each other as well.

This is where things get a bit fuzzy:  
To implement this functionality, I need to act as a digipeater, and I THINK that in turn requires the TNCs to be in KISS mode.

Fine, I can put the TNC in kiss mode, use APRSDigi (Or something similar) to run as a digipeater... But how to generate an NMEA Kenwood Sentence stream from there?

If I understand my problem correctly, I am looking for an APRS digipeater that generates an NMEA output...

Or I'm looking for an AX.25 to NMEA converter of some kind.

Or... Maybe I'm missing an obviously easy solution...

## Answer (score 3, by oh7lzb)

You're right, to make a properly working digipeater, you'll need to put both of the radios/TNCs in KISS mode, and use aprsdigi (or, my favourite, aprx), as a digipeater. But I don't think they can output both KISS and NMEA at the same time.

For NMEA, you'll then need some other software to receive APRS packets, decode them and output NMEA. That's not very difficult to do, but I don't think such application exists right now.

I'd use the Linux AX.25 kernel tools to interface the KISS TNCs, so that you could run existing digipeater software, unmodified, just to do the digipeating, and at the same time run another program which also listens to traffic on the same TNCs and does the NMEA encoding.

To implement the conversion program I'd personally just take the Ham::APRS::FAP perl parser (same APRS packet parser as used by aprs.fi), which can decode raw KISS / AX.25 frames, attach it to the raw packet socket to receive packets, and then write the new code necessary to generate NMEA.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/297/ax-25-to-kenwood-pkwdwpl-sentence, by KD7KUJ, oh7lzb. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
