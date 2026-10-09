# Can a Yaesu FT-7900R be physically connected to both KPC-9612+ ports?

*Tags: packet, yaesu · score 6*

## Question

The Yaesu FT-7900R has a single data port (mini DIN 6-pin) for 1200 and 9600 bps TNCs. Page 10 of the manual states:

In accordance with industry standards, the signal levels, impedances, and bandwidths are significantly different on 9600 bps as opposed to 1200 bps. If your TNC does not provide multiple lines to accommodate such optimization, you may still be able to utilize your TNC, if it is designed for multiple-radio use, by connecting the TNC “Radio 1” port to the 1200 bps lines on the FT-7900R, and the “Radio 2” port to the 9600 bps lines.

Is it possible to follow these directions with a KPC-9612+?

## Accepted answer (score 2, by oh7lzb)

**RX audio:** The FT-7900R has separate audio outputs for RX audio on the DIN connector for 1200 and 9600, so those can be simply wired to the two separate KPC-9612+ ports.

**PTT:** The PTT line has a little voltage provided by the radio, and the TNC's PTT pin grounds that pin to transmit. You can directly wire both TNC port PTTs to the radio, and it'll transmit when either of the TNC ports ground the pin.

**TX audio:** The correct method would be to provide some mixing circuit to mix the audio signal outputs of the TNC. Some audio level loss is OK, since you can compensate by adjusting the output level of the TNC up, so a passive circuit is good. The most important thing is that the mixing may not affect the frequency response, since it's quite important for good 9600 bit/s operation. Simply wiring both the 9600 and 1200 bit/s audio outputs of the TNC together might work, or it might not, depending on the type of the outputs on the TNC. A simple resistor mixer might work better.

It's probably obvious, but you'll have to make sure the two TNC ports don't transmit at the same time - the transmit audio, mixed 1200/9600 data, would not make any sense.

This is a community wiki, so if someone has better details on the TX audio connection, please edit it in.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/527/can-a-yaesu-ft-7900r-be-physically-connected-to-both-kpc-9612-ports, by Jacob, oh7lzb. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
