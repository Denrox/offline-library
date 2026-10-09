# Requirements for 9600 baud

*Tags: digital-modes · score 5*

## Question

I want to setup a TCP/IP link between my friends house 7km away from me on 70cm.

1200 Baud is a bit slow, and we are looking into something with a faster data rate.

I know normal audio does not work for 9600 baud packet. What are the requirements?

I have a bunch of Motorola Radius SM50 UHF wideband commercial radio's and I am wondering if they would work? They have direct discriminator out on the back.

## Answer (score 3, by user3486184)

In fact, it appears 9600 baud will work on narrowband FM. Here is a description from Amsat of a 9600 baud packet modem which used a bandwidth of 4800 Hz and its board.

According to the Amsat article, the design is used in many devices including:

- PacComm Inc: NB-96
- Kantronics: DE-9600
- MFJ: MFJ-9600
- Tasco: TMB-965
- Symek: TNC2-H

(These were from 1988 when the article was written; here are some slightly more modern instructions.)

Packet is AX.25, which Linux routes natively. Here's an AX.25 howto.

## Answer (score 2, by Duston)

In addition to what user3486184 said and the direct discriminator on the back, you'll need direct access to the modulator too. A good way to test whether it all works is to fire up a sound card packet program. Once you can make reliable connections with that (that's your Network Layer 2) you can move up the stack to TCP/IP.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5145/requirements-for-9600-baud, by Skyler 440, user3486184, Duston. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
