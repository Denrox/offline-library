# What is this matching technique called?

*Tags: antenna, impedance-matching · score 3*

## Question

I've had this suggested to match 50 ohm coax to a lower feedpoint impedance, like a vertical, especially mobile shortened verticals. What's it called?

(CircuitLab has no symbol for an inductor with a tap, but you get the idea)

## Accepted answer (score 0, by HarveyB)

This is commonly called a "Tapped Loading Coil", and combines the functions of loading coil and RESONANT transformer. Typically used with a shortened vertical antenna, the impedance of the coil is selected to cause the antenna to be resonant on the desired frequency. The position of the tap is then adjusted to match the impedance of the transmitter to the resonant antenna circuit.

## Answer (score 2, by Ryuji AB1WX)

The real tragedy here is that the schematic tells a lie—boldly, unapologetically. That missing dot to show the tap connection? Irrelevant. The real story is in those two inductors. They aren’t supposed to be coupled, because if they were, the whole contraption would just crank up impedance like some overeager do-gooder and utterly fail to match a short vertical monopole. You pointed that out already, bless you.

Now, someone might chime in, "Hey, that antenna’s just one inductor with a tap, isn’t it?" Sure, but it’s more of a pragmatic hack than a theoretical marvel. It works because air-core inductors barely couple. Try the same stunt with a ferrite or carbonyl iron dust core, and you’ll be left holding the smoking ruins of your dreams.

The kicker? If the schematic were honestly drawn—two separate inductors like it should be—nobody would even ask the question. They’d look at it, nod, and say, "Ah, an L-match," and then go back to their coffee, problem solved.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1856/what-is-this-matching-technique-called, by Phil Frost - W8II, HarveyB, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
