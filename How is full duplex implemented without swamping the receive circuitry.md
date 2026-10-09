# How is full duplex implemented without swamping the receive circuitry?

*Tags: software-defined-radio, transceiver · score 8*

## Question

I've seen a few references to full duplex SDR radios, and I'm wondering how can one transmit and receive at the same time without overwhelming the receiver, and without heavy filtering such as the cavity filters used in repeaters.

## Answer (score 3, by Adam Davis)

One method to achieve this is to invert, attenuate, and delay the transmitted signal and feed it back into the receiver. This will cancel out most of the power of the transmission, so the input end of the receiver isn't swamped by the RF from the transmitter.

http://sing.stanford.edu/fullduplex/

This will have to be actively managed, but the report suggests that it works for ultrawide bandwidth signals.

## Answer (score 3, by natevw - AF7TB)

The bladeRF is one such SDR radio that supports full duplex, i.e. simultaneous signal transmit and receive.

The short answer is that in its case, as I suspect in many other cases with a "raw" SDR unit, they could **not** be used "out of the box" for full-duplex *communications*. I.e. the receive circuity **will** be swamped unless the user takes their own care to prevent this.

If you take a look at this forum thread, Cavity Duplexer needed? you will find the first reply says basically:

- the bladeRF isn't a great choice in situations where one would typically use a cavity duplexer, e.g. repeater
- "using separate RX and TX antennas is entirely doable, especially if the antennas are in each other's nulls and they're operating far enough apart frequency-wise … Filters are, as always, a good investment, but they don't need to be anywhere near as sharp as a cavity" — i.e. you could sort of use it anyway, but you're relying on external arrangements for preventing receiver desense/overload

Likewise in the case of the Flex radio systems you mention in your question. For example in Is the 6500 a true 'full duplex' radio you find answers such as:

- "appears to me the answer is yes... If you have sufficient isolation between your RX and TX antennas"
- " I am not sure it will be possible with the 6500. With the 6700 you have the two SCUs and a compliment of BPFs for both of them."
- "The radio hardware has some capabilities that you would consider full duplex. There are limits to what can or that you would want to do and we have not yet spent any time looking into this. For the immediate future, we are muting receivers when transmitting…"

So again, it's clear that there is no silver bullet inside either the bladeRF or the Flex radio SDRs which handles the tight filtering needed when transmitting near a receiver. The 6700 model radio mentioned in comparison to the Flex unit would possibly be able to serve as a *cross-band* repeater with its separate band pass filters, but not within the same band if the TX signal has any significant level of amplification.

However, this is not to say that having an SDR with full-duplex capability is worthless — especially if you were to use it as test equipment rather than a transceiver. A vector network analyzer like the VNWA3 for example is quite similar to a full-duplex SDR, architecturally speaking. With the right software and perhaps an external bridge or similar, I would think something like the bladeRF could be useful for measuring filters and much much more.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1042/how-is-full-duplex-implemented-without-swamping-the-receive-circuitry, by Adam Davis, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
