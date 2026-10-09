# What are some equivalents of a BF199 transistor?

*Tags: receiver, electronics, fm · score 4*

## Question

I'm planning to build an FM radio receiver using the instructions on http://www.instructables.com/id/Build-your-own-Crude-FM-Radio/

The schematic uses a BF199 transistor which is marked "obsolete" by some component suppliers. What would be a current and widely available equivalent?

I tried to search at my preferred shop, https://www.rs-online.com using the following properties:

- Si NPN RF Transistor
- Vcb max 40V
- hFE min 38
- ft 1100 MHz
- Pc 350 mW

And did not find anything suitable.

The original data sheet is here: https://www.mouser.com/ds/2/308/BF199-1118776.pdf

## Accepted answer (score 3, by Phil Frost - W8II)

This is not a terribly critical application, and there are many transistors that would work. If you have some NPN transistors on hand, try those. It may work anyway, with some reduction in gain. If you'd like to buy new transistors, I'd look for something with a high gain bandwidth product.

## Answer (score 2, by Mike Waters)

**A 2N5109 will work just fine**.

Datasheet here.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10015/what-are-some-equivalents-of-a-bf199-transistor, by Alexander Churanov, Phil Frost - W8II, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
