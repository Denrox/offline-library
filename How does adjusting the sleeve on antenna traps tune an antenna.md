# How does adjusting the sleeve on antenna traps tune an antenna?

*Tags: antenna, antenna-theory · score 3*

## Question

Take for example, the Hustler 4BTV. It has traps formed by an inductor, covered by a sleeve that's connected at the lower end, and the upper end is covered by a non-conductive cap:

The tuning instructions for this antenna advise the installer to move the sleeve up or down relative to the coil it covers, rather than adjusting the length of the intermediate elements. What's the electrical explanation for why this effects a change in resonant frequency?

## Accepted answer (score 6, by Phil Frost - W8II)

The trap is an LC parallel circuit:

At some frequency, the inductive and capacitive reactances are equal, and the trap looks like a very high impedance. No significant current can flow through this impedance, and the rest of the antenna is effectively disconnected.

When the sleeve is adjusted up, more of it overlaps the top section of the trap, increasing the capacitance. Now the trap isn't precisely resonant, and starts to look more like a series capacitor. This electrically lengthens the antenna, effectively making the rest of the antenna a capacitive hat, making it resonate at a lower frequency.

Adjusting the sleeve down has the opposite effect: it reduces capacitance and now the trap looks more like a series inductor. This is not like a loading coil: adding series inductance at the *top* electrically shortens the antenna, making it resonate at a higher frequency. This is not something you ordinarily see since people usually want to make a small antenna work as a bigger one, not the other way around.

With these kinds of adjustments, you can get a very large change in resonant frequency without moving the trap very far, but it's not without disadvantages. Since current is no longer flowing in a quarter-wave section, it won't behave like a quarter-wave antenna. The feedpoint impedance and radiation pattern will be different. There are most likely higher losses as well, since currents are flowing through more metal, increasing resistive losses. The magnitude of these problems is proportional to the distance from resonance the trap has been adjusted.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1863/how-does-adjusting-the-sleeve-on-antenna-traps-tune-an-antenna, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
