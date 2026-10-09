# Are there any Alternatives to Packet Radio for sending digital data?

*Tags: packet, linux · score 5*

## Question

Recently, I asked a question about using an Arduino to send packet radio. I noticed that the top record speed for packet radio is 1 megabit/second, on a modified radio. Someone mention on stack overflow that the normal speed is around 120 kilobits/second! So is there an alternative to packet radio for sending digital bits over ham?

## Answer (score 4, by Edwin van Mierlo)

In absence of a clear indication of what Amateur Radio band is being targeted here, an answer for the 13 cm band:

You can use 802.11g/OFDM with a 20MHz bandwidth on 2400-2450 MHz Amateur band. You could even modify existing/consumer Wifi equipment to do so.

**This would give you a (theoretical) 54 Mbits/sec throughput.**

Obviously you need to check that you are licensed to do so, and I would advise you to check the bandplans as well.

There are 3 regions with different bandplans, here

From the 3 regions only Region-2 details the following footnote:

Broadband applications can be used in 2410 – 2450 MHz with the maximum CW of 22 MHz. The broadband applications should not cause interference on satellites communications

*) *I believe the bandplan contains a typo. I seriously believe that where "CW" is mentioned in this footnote, it should read "BW" indicating Bandwidth.*

Region-1 bandplan does not list such footnote, and Region-3 does not list anything above 1300 MHz. If you are located in those regions I would advise to consult with your regulatory body.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10549/are-there-any-alternatives-to-packet-radio-for-sending-digital-data, by itisyeetimetoday, Edwin van Mierlo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
