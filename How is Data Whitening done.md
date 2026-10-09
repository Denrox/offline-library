# How is Data Whitening done?

*Tags: encoding, whitening · score 5*

## Question

Is it safe to define that Data Whitening is always X-ORing a payload with a pheudorandom sequence known to both receiver and transmitter?

In more detail, lets assume the following case. I have the exact pseudorandom string that is used for Data Whitening of a SX-1234 transceiver (a random transceiver). Lets also assume that I have captured the **already whitened payload** received by another SX-1234 transceiver. Provided SX-1234 does not perform any other encoding steps other than data whitening, if I simply X-OR my received payload with the pseudorandom string, will I get back the originally transmitted data?

If not, what other methods are there for data whitening other than simple X-ORing.

## Accepted answer (score 4, by Marcus Müller)

Is it safe to define that Data Whitening is always X-ORing a payload with a pheudorandom sequence known to both receiver and transmitter?

No, but that's a very common way of doing it. However, you can scramble and whiten a sequence by pushing it through an appropriate Linear Feedback Shift Register, and I'd assume that this is even more commonly applied in practice.

I have the exact pseudorandom string that is used for Data Whitening of a SX-1234 transceiver (a random transceiver)

That is a rather uncommon case. As said above, I'd assume most systems do NOT just XOR with a fixed sequence, but scramble the data itself.

And even for systems where the data is XOR'ed with a pseudorandom sequence, I'd assume that for whitening reasons, you'd want that sequence to be long. Such sequences aren't stored, but again, generated using things like linear feedback shift registers, or other algebraic approaches. Such a sequence can easily become *very* long.

So, unless SX-1234 is a very old standard, it's questionable that you "captured" the whole sequence. Maybe you mean you've got the generator for the same sequence? Then you "only" have to sync up to your data stream.

It's very hard to estimate the current state in that sequence from a short observation (that's a requirement for good pseudorandom generators, and it's often very desirable, again, for autocorrelation/whitening reasons). So your syncing can, often, only be approached by a brute force trial of all possible shift – a usually impractical approach.

Provided SX-1234 does not perform any other encoding steps other than data whitening, if I simply X-OR my received payload with the pseudorandom string, will I get back the originally transmitted data?

No. If SX-1234 is prudent enough to whiten the data, then it'll certainly also employ channel coding (and that can be, if you don't know anything about the channel code, pretty much encryption). Oh, and let's not forget interleaving, which, especially for systems that transmit long streams of data, is employed to convert burst errors into sporadic errors (which the channel code can much easier correct).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9716/how-is-data-whitening-done, by Denis, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
