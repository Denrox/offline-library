# What are some ways to ground a transmitter+antenna in an enclosed attic?

*Tags: grounding, antenna-system · score 9*

## Question

If I want to minimize "RF in the shack" and lightning hazard, what some good ways to ground a transmitter and indoor antenna in a top floor room or attic with no exterior access? (say a multi-story wood-framed building with large non-opening glass windows)

## Answer (score 8, by Phil Frost - W8II)

Your solution to "RF in the shack" should be proper antenna design first, and grounding second. See [Using a balun with a resonant dipole](Using%20a%20balun%20with%20a%20resonant%20dipole.md) (or any other antenna, really). If you take care to address common-mode currents, you won't need a ground.

Regarding lightning protection, you might just forget about it. If lightning has struck your indoor antenna, it's already struck your house. You have bigger problems. You can try to provide a path for that energy to ground, but keep in mind: it's a lot of energy, so you need a big conductor. You don't have exterior access, so that means going through the floor. If you don't mind a couple pieces of 6" copper strap running straight through the living room you might accomplish something worthwhile. Otherwise, I'd suggest insurance.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1227/what-are-some-ways-to-ground-a-transmitter-antenna-in-an-enclosed-attic, by hotpaw2, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
