# Phased Array Pattern

*Tags: phased-array, radiation-pattern · score 9*

## Question

I'm working on a passively scanned phased array radar project, as a concept and hopefully design.

One of the things that bugs me is that antenna patterning used. The vast majority of radar arrays I've seen employ a hex grid pattern, with a small minority using an orthogonal grid.

What would be the benefits of using a hex grid like this:

As opposed to a square orthogonal grid like this:

## Answer (score 4, by SDsolar)

The hex grids can fit more transmitter/receivers into the same space, resulting in greater power output per square meter.

But more importantly, the one you pictured also has independent transceivers so they are individually field-replaceable.

The computer that runs it all does diagnostics on startup and can flag the bad ones so they can be fixed right away without having to have access to the back of the array. That is key.

No disassembly required - just pull out the bad one(s) from the front and slide in a new one, right on the flightline. No need to pull it into a shop.

Just one bad TRX can cause unwanted sidelobes which can defeat the LPI (low probability of intercept) property of those arrays.

Addressing what you said about passively: All I can mention is that the old phased arrays used switched delay lines in order to generate the pattern. But they were very limited in the switching speed, and could not transmit during the switching.

The unit you pictured can probably track more than two dozen targets "at once" - of course it is scanning, but it is so fast it seems to be simultaneous.

Good luck with your project. I am sure you are learning a lot.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5786/phased-array-pattern, by Oliver, SDsolar. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
