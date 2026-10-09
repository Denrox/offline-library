# Why do we talk about common mode current from an antenna, but not from a transmitter?

*Tags: antenna-system, feed-line, theory · score 3*

## Question

There's a lot of information available about how to block common mode current originating at the antenna end of a coax cable. But, I haven't seen any reference to common mode current originating at the transmitter. If common mode current is on the outside of the cable's shield (as many people describe it), and both the inside and outside of the cable braid are connected to the same wire in the radio (which they are), and the feed line is the right length to be an effective radiator (which could happen), wouldn't the shielding be radiating like crazy? That doesn't seem to happen in real life, so I feel like I'm missing a crucial piece of information here. What's stopping common mode current from originating at the transmitter?

## Accepted answer (score 6, by tomnexus)

The short answer is that it can't.  
A shielded transmitter, connected to an ideal piece of coax, does not generate common mode currents.

The inner and the outer of the cable look connected (and for Direct Current they are), but high frequency currents really cannot pass through the thick metal, they are confined to the inside or the outside.  
Real coax can leak, but in practice it's very little.

**Here are some examples.**

First - a simple coaxial cable connecting a transmitter to a dummy load. See how the Inside and the Outside of the coax never meet - they really are separate worlds. No RF current can reach the outside of the coax. There are no common-mode currents.

Second, a shielded transmitter feeding a length of coax, connected to a balanced antenna without a balun, which creates the unbalanced currents.

**Balanced lines**

I should mention that it is not only coax that can be used to generate balanced currents, it's just the example you asked about.  
If the transmitter drives a balanced line with equal and opposite voltages, say with a transformer, there will be no unbalanced voltage, and no common-mode current. Ethernet cables are like this (CAT5 etc, before they were shielded). There is very little radiation from the pair, even though it is carrying significant RF power, because the transformer that feeds it has a high common-mode impedance, and the other end is an identical circuit, not an antenna.

**Generating common-mode currents on purpose**

It is possible to generate common mode currents at the transmitter, but generally we take pains to avoid doing that. Here is an example where it is desirable - I have a bluetooth-receiver-FM-transmitter gadget in my car, which works best if there's a USB cable plugged in. It uses the USB cable *in common mode* as the antenna. Separately, inside the shielding, the USB D+ and D-, and 5V and 0V, are available as differential signals to the phone. The same is done in phones that have FM radio receivers, using the headphone cords.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16227/why-do-we-talk-about-common-mode-current-from-an-antenna-but-not-from-a-transm, by mrog, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
