# Why isn't twisted pair used for feedlines?

*Tags: coaxial-cable, feed-line, balun, transmission-line · score 12*

## Question

My son was asking about some Ethernet cable (Cat 5 unshielded twisted pair), and since he recently passed his Technician exam and we both have "radio stuff" on our minds, I tried to make the analogy between coax transmission lines and the balanced pairs in the wire. I understand they both are used as RF transmission lines, essentially.

This got me thinking: why don't we use twisted pair for antenna feedlines?

As question T9B03 on the FCC exam covers:

Why is coaxial cable used more often than any other feedline for amateur radio antenna systems?

The correct answer being "It is easy to use and requires few special installation considerations" and **not** that "It has less loss than any other type of feedline" — the latter advantage going to balanced line, which is low-loss but does require special considerations particularly to avoid coupling to nearby metallic objects.

Would twisted pair offer something of best of both worlds? Could it provide lower loss than coax, and still without "special installation considerations"? (Looks like Category 5 cable specifically has a 100ohm characteristic impedance, but that seems easily enough dealt with since you'd need a unbalanced-to-balanced transformer off of most ham equipment anyway, right?)

## Accepted answer (score 9, by Marcus Müller)

Balanced lines (of which twisted pair is a special type) really have an upper frequency limit; you can't use them to transport 1 GHz (well, you can, but the smallest variation in direction or distance would have catastrophic effects, and the conductor distance would get *pretty small*).

This can be seen in technical practice: 100 Mbit/s Ethernet (Fast Ethernet) and 1 Gigabit/s ethernet both work with twisted pair, their baudrate being 125 MBaud – and hence, most of their signal energy is contained below ~250 MHz.

For higher-rate digital busses, twisted pair, as nice and cheap it is, doesn't do well enough anymore (see the attenuation of roughly 36 dB at 250 MHz sent over 100 m of twisted pair; you're losing literally 99.975% of energy in the cable) – the typical "cheap" (as in: 16€/m) direct attach copper for the next faster 10GE (10GBase-CR) uses Twinax - which is exactly that, a balanced line within a shielded, well-specified dielectric (same goes for SATA 6b/s, where this picture is from):

That way, up to 3.125 Gigabaud are possible. So yeah, for digital baseband, balanced line is used up to the multiples of GHz, but it's not cheaper than coax – in fact, it's the noise immunity considerations of differential signaling that led to the usage of twinax instead of simple coax. For an antenna, simple coax would have the same effect.

On the other hand, whenever you see a PCB transport RF signals, you'll find something like a microstrip line, a buried microstrip line, or a pair of differential lines – there you are, balanced lines again. On PCB, this gets easier (and necessary, as there's no chance to build true coax on a PCB), because the dielectric (the PCB substrate) is so mechanically and electrically reliable, and powers typically are limited.

For higher frequencies, losses due to radiation simply take the upper hand in free-swinging balanced line – and coax, with its losses in the dielectric, becomes the better line. If you go for the really high frequencies, or rather the really high powers, you typically drop the (inner) conductor altogether – and use a wave guide.

## Answer (score 5, by Phil Frost - W8II)

Twisted-pair is just a special case of a balanced (untwisted) feedline. The twisting reduces crosstalk between the multiple pairs in the cable assembly but doesn't otherwise change the fundamental operation of the transmission line.

Category 5 UTP in particular probably isn't frequently used because it can not handle much power. I suppose in a low power or receive application it could work. The most commonly available category 5 cable is not UV resistant, and so is not appropriate in an exposed outdoor installation.

Disassemble a cat 5 cable carefully, and you'll notice each pair is twisted at a different rate. Twisting the pairs at different rates "mixes up" the interactions due to the pairs being bundled together, and over many twists these randomized interactions between pairs tend to average out and cancel.

For a single antenna application, this is of little relevance. Perhaps in an antenna array where minimizing crosstalk is important (a phased array, for example) some benefit from the twisted pairs in cat 5 could be realized, but coax would be even better. Ladder line is sometimes installed twisted, but this is to keep it from fluttering in the wind, not for any particular electrical benefit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6445/why-isn-t-twisted-pair-used-for-feedlines, by natevw - AF7TB, Marcus Müller, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
