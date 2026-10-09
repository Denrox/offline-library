# How high an SWR can the USRP 2901 (B210) handle?

*Tags: software-defined-radio, antenna-system, impedance-matching, usrp · score 3*

## Question

I connected a USRP 2901 (B210) to an amplifier I designed. The USRP seems to shutdown every time I try to transmit. I guess I messed up with the input impedance matching on the amplifier. Is it the impedance mismatch that is causing the USRP to shutdown? If so, how high a mismatch can it handle?

## Accepted answer (score 2, by Marcus Müller)

The B210 / NI-USRP 2901 has no problems with an open end condition or a short: You can't damage the transmitter with its own power. There's no significant PA on that board. So, it can handle any mismatch.

Also, shutting down (whatever that means) isn't a reaction anyone included in the hard- or software in reaction to an impedance mismatch.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10355/how-high-an-swr-can-the-usrp-2901-b210-handle, by user11096, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
