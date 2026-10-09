# Is it possible for an amateur to transmit ATSC?

*Tags: digital-modes, modes, atv · score 6*

## Question

Amateur television has long used the NTSC (analog) television standards to transmit video and audio. Several years ago, the digital broadcast television transition made higher-quality television signals possible. Can amateurs acquire and use digital television (ATSC or DVB) transmission equipment?

## Accepted answer (score 7, by K7AAY)

FCC Regulations, Title 97.307(f)(8) says yes, you can transmit with ATSC modulation in the US, BUT you can't use frequencies which match US ATSC channels. You would need to find a receiver (maybe PC controlled?) flexible enough to listen to amateur frequencies.

As to DVB-T or DVD-S, well, they'll work with about 2MHz of bandwidth instead of the 6MHz slice required for ATSC. Again, a flexible receiver is called for.

## Answer (score 2, by Geremia)

Software defined radios (SDRs) that can transmit can certainly do this. In the GNUradio software, for example, there are blocks for receiving and transmitting ATSC; cf. this blog post for how to receive and decode ATSC with a SDR.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/808/is-it-possible-for-an-amateur-to-transmit-atsc, by JC Hulce, K7AAY, Geremia. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
