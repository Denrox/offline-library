# Why are loopstick ferrite antennas commonly wound with Litz wire?

*Tags: antenna-theory, loop-antenna, ferrite, inductor · score 5*

## Question

What is the advantage of using Litz wire to wind ferrite (loopstick) antennas? How much of an advantage in what characteristic does this type of wire provide? (over generic single strand enameled or insulated wire). How do different types of Litz wire (number of strands, etc.) effect this difference?

Would there be any advantage to using Litz wire to improve any characteristics of wound toroidal cores as commonly used when building RF filters and transformers in radio kits?

## Answer (score 7, by Mike Waters)

The advantage of Litz wire —lower loss than solid wire— is realized below about 1 MHz. It is of little use above 160 meters.

From https://en.m.wikipedia.org/wiki/Litz_wire

Litz wire is a particular type of multistrand wire or cable used in electronics to carry alternating current (AC) at radio frequencies. The wire is designed to reduce the skin effect and proximity effect losses in conductors used **at frequencies up to about 1 MHz**.

It consists of many thin wire strands, individually insulated and twisted or woven together, following one of several carefully prescribed patterns often involving several levels (groups of twisted wires are twisted together, etc.). The result of these winding patterns is to equalize the proportion of the overall length over which each strand is at the outside of the conductor.

This has the effect of distributing the current equally among the wire strands, reducing the resistance. Litz wire is used in high Q inductors for radio transmitters and receivers operating at low frequencies, induction heating equipment and switching power supplies.

Hams *are* using it to advantage for multi-turn **air core** receiving loops on the 2200 and 630 meter bands.

Because of Skin Effect, on low frequencies Litz wire is much more efficient than solid wire. *As long as all the strands are soldered together at both ends of the coil! Unsoldered strands of Litz wire in a coil are extremely lossy.*

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18571/why-are-loopstick-ferrite-antennas-commonly-wound-with-litz-wire, by hotpaw2, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
