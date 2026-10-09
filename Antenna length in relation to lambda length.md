# Antenna length in relation to lambda length

*Tags: antenna, antenna-theory, jargon · score 6*

## Question

I'm pretty new with antenna stuff. I'm not sure how to understand antenna length in relation to lambda with dipole antennas.

If a simple dipole antenna is lambda/4, has it a total length of lambda/2 (every pole lambda/4 long) or a total length of lambda/4?

## Accepted answer (score 6, by Kevin Reid AG6YO)

Terminology can be ambiguous here; there is no universal standard for how to describe antennas. That said, here are some heuristics:


If someone says, e.g., “a 20-meter dipole”, they mean an antenna which is *for the 20-meter band*, i.e. almost 10 meters long from end to end (because a full-size dipole has an electrical length of λ/2).


If someone says the *length* of a dipole antenna is some particular value, then they mean the length from one end to the other — the physical space taken up by the antenna — which will be λ/2.

In the US, if they specify a length in *feet*, then they're almost certainly referring to the physical length. I don't know if there are any clues like this in other countries.


As far as I know, no one ever uses the λ/4 value in discussing dipole antennas, unless they're giving instructions for cutting the wires to the proper length.

## Answer (score 3, by adengle)

Also, don't get confused if you see actual, physical antenna lengths shorter than theoretical wavelengths/lambdas.

Because the dipole legs are made of real-world components in complex situations, "velocity factor" comes into play which will tweak the numbers slightly.

Many guides give you nice numbers to make the math easier, but almost always advise that these are starting lengths, almost always longer than needed, so you will trim the antenna to best resonance.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5681/antenna-length-in-relation-to-lambda-length, by leAthlon, Kevin Reid AG6YO, adengle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
