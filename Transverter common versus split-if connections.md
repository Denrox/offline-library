# Transverter common versus split-if connections

*Tags: vhf, transverter · score 3*

## Question

I have a radio (Flex-1500) that has low level transverter outputs. They can be configured as either a common or split-if.

I also have a DEMI transverter that can easily be wired up for common or split-if.

Are there any advantages or disadvantages in using one configuration versus the other?

## Answer (score 2, by Martin Ewing AA6E)

Both systems work. One problem with the common connection is that, if you screw up your transmit switching somehow, there is the potential to send your transceiver's Tx output into the transverter's Rx output, and that might fry something. (But probably not if the levels are really low.)

There's probably also an extra relay in the circuit that could slow down T/R switching a little.

On the other hand with the common setup, you only need one coax cable.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2412/transverter-common-versus-split-if-connections, by James, Martin Ewing AA6E. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
