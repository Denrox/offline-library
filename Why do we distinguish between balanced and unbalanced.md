# Why do we distinguish between balanced and unbalanced?

*Tags: antenna-theory, antenna-system, balun, choke-balun · score 6*

## Question

I hear all the time, "you need a balun between your balanced dipole and unbalanced coax to stop the common-mode current" when it seems the proper advice is "you need something to stop common-mode current (full stop)." Sure, attaching a balanced system (e.g. dipole) to an unbalanced system (e.g. coax) is a frequent source of common-mode current. But, [this answer](Using%20a%20balun%20with%20a%20resonant%20dipole.md) points out that even with a so called "balanced" antenna connected to a balanced feedline, the antenna often isn't really balanced, so some sort of common mode choke is a good idea no matter what.

So, if the same advice applies either way, *why do we make such a big distinction between balanced and unbalanced?* My assumption is that it's one of a couple things:

- Misconception: A lot of people may not realize a common-mode choke is recommended anyway.
- Old knowledge: This is sort of a special case of misconception. Maybe in the past, we didn't think of common-mode suppression as a generally recommended thing, and only later did it become common knowledge that this is a good thing even in balanced systems. Meanwhile, outdated information persists.
- Other reasons to differentiate: Even though common-mode suppression is a good idea regardless of balanced vs. unbalanced, there may be other ways we *do* treat them differently, or other reasons to distinguish between them.

My suspicion is the first one is true to some degree, but that the third case is the main reason.

To further muddy the waters, I'm seeing the word "balanced" used in two seemingly different ways. One is in the sense above where, for example, we have a "balanced" dipole that's actually unbalanced because one side is close to a hunk of metal, causing it to present an unbalanced impedance at the feed point. The other way I've seen it used is to represent a system where the two conductors have equal and opposite voltages relative to ground, versus unbalanced where one of the conductors is grounded. Are these two uses of the word actually the same thing? If so, how?

## Accepted answer (score 5, by Phil Frost - W8II)

There are balanced feedlines (twin-lead), and balanced antennas (dipoles), and similar things all described as "balanced". In this sense, balance means the two halves of the thing have equal impedance relative to *ground*. Here, *ground* does not mean whatever is called ground on the schematic. Rather, it means "the environment".

Consider twin-lead for example. If the [spacing between the conductors is small relative to wavelength](Why%20must%20twin-lead%20conductor%20spacing%20be%20small%20to%20avoid%20radiation.md), we can say they are effectively in the same space. And the wires have the same geometry. Since they're both the same (for frequencies low enough that this is a valid approximation), of course they are going to have the same impedance to the environment. Meaning, if an electromagnetic wave from a distant transmitter reaches the feedline, each half of the twin-lead will be affected equally.

This same property means if we drive the twin-lead with each half having an equal but opposite current, each individual half will have surrounding it an equal but opposite electromagnetic field. But these equal but opposite fields cancel, and thus the feedline does not radiate. It's this property that allows a feedline to move electromagnetic energy from one end to the other without much loss, or carry a signal from an antenna to a receiver without picking up noise from everything around the feedline.

For this reason, in discussion of feedlines, and the antennas and radios to which they are connected, you may encounter discussion of *current balance*. This just means equal but opposite currents, also known as differential mode current.

Coax is not a balanced feedline, which can be seen by considering how it would pick up an electromagnetic wave from a distant transmitter, for example. The wave will interact with the shield just like a fat wire, effectively an antenna. But the center conductor, being screened from the environment by the shield, isn't affected at all. The two parts of coax do not have equal impedance to ground, thus it is not balanced.

But coax does require *balanced current*. Only if the currents on the shield and center conductor are equal but opposite will the coax act as a feedline. Otherwise, it will radiate, or pick up noise.

It's for this reason the common-mode choke is so ubiquitous. Regardless of whether the feedline or antenna attached to it is balanced or unbalanced, differential mode current (AKA, balanced current) through it sees a low impedance, whereas common mode current (the remainder) sees a high impedance.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10173/why-do-we-distinguish-between-balanced-and-unbalanced, by Dominick Pastore, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
