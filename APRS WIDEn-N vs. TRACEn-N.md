# APRS: WIDEn-N vs. TRACEn-N

*Tags: digital-modes, aprs, packet · score 6*

## Question

The suggested APRS digipeater path is WIDE1-1,WIDE2-1 for the most use cases. According to the specs, this ensures two retransmissions by fill-in / regular digipeaters around the sender, without the digipeaters adding their own callsign to the path.

The TRACEn-N path, as opposed to that, is intended to let digipeaters insert their callsign when forwarding. However, despite the use of WIDEn-N, I see one or multiple digipeaters in the path of most packets.

**Are there still valid use cases for TRACEn-N? Will a TRACEn-N packet have the same coverage as a WIDEn-N one?**

## Accepted answer (score 6, by oh7lzb)

Actually, current specifications encourage or require digipeaters to add their callsigns to the WIDEn-N path, since including callsigns greatly helps in finding and fixing all sorts of network issues (look for "traceable" in the page). WIDE1-1 is often replaced by the callsign of a dumb digipeater, WIDE2-1 is usually prepended by the callsign of a digipeater.

**TRACEn-N is often useful for diagnostics.** Many areas still have obsolete digipeaters in use, which don't add their own callsigns to the WIDEn-N path, and those digipeaters often do add their callsign to TRACEn-N paths. So someone might want to sometimes temporarily use TRACEn-N to see which digipeaters are retransmitting your packets. If all digipeaters in your area have already been upgraded to make WIDEn-N traceable, it should not make much difference at all.

Unless there is a digipeater which completely ignores TRACEn-N packets in your area (would be surprising), it should get the **same coverage**.

Prepending a few digipeater callsigns in the packet path does not have a significant practical effect on transmission time/size, since each callsign-SSID pair is only 7 bytes long (56 bits - 6 bytes for callsign, plus one byte for SSID as an integer), which at 1200 bits/s takes 46.7 ms to send. Kenwood TH-D72 has a default **txdelay** setting of 300 milliseconds, which at 1200 bits per second already attributes to 360 bits of "waste" in the beginning of each transmission. Other radios and trackers have similar and sometimes longer default settings for txdelay - even up to 500 ms. And then there's the actual packet contents, which often are very long with uncompressed coordinates and verbose comment texts.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/395/aprs-widen-n-vs-tracen-n, by Georg DO1GL, oh7lzb. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
