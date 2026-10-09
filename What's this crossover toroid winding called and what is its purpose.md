# What's this "crossover" toroid winding called and what is its purpose?

*Tags: physics, toroid, transformer · score 9*

## Question

I am winding an EFHW matchbox and many of the designs I've found (including the diagram provided with the kit I bought) include a sort of "twist" when winding them:

(Image taken from this post and similar can be seen here and here and here.)

My understanding is that the section where the two green turns go with the initial red turns is called a "bifilar" winding and some recommend twisting the two wires together for that part — its own topic that I can research a bit more on my own.

But what is the trick where the red winding crosses across the middle and then continues winding? Does it have a name? Does it count as a turn — or a "negative turn"? (In the diagram I have linked there are drawn 8+7 turns labeled as 2x7…but I suspect this is just a mistake.)

Why would the toroids be wound this way in two groups instead of just a simple total number of windings spread evenly around? When is this technique useful?

## Accepted answer (score 5, by tomnexus)

This is a magnetic flux transformer, not a transmission line transformer. It works by flux coupling just like a mains power transformer. So the bifilar part isn't too special, nothing like a transmission line transformer.

In a regular flux transformer, the position of the winding doesn't really matter, only the number of turns. At RF though there is the concern about capacitance.

First concern is the inter-turn capacitance, which might make the coil resonant and stop working as a transformer. The best you can do is keep the number of turns small, and spread them out evenly. Of course fewer turns means more flux, so there's a trade-off.

The second concern is about the capacitance from one end of the winding to the other. A 64:1 transformer will have a very high impedance at the high voltage end, and any capacitance to the ground end of the winding will tend to load the high impedance end. This transformer might transform to an impractical 3200 ohms, but quite likely the capacitance from live to ground will be less than that.

So if you follow the wire, the reverse winding only reverses direction on the core, it keeps going the same way through and out, so it keeps developing more voltage at each turn. The reverse winding is a neat trick to keep the windings spread out, keep them going in the same direction, and keep the high voltage, high impedance end of the transformer far away from the ground.

I don't know it's name, but I'm sure it will have one.

Recommended reading: Jerry Sevik - Transmission Line Transformers

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5619/what-s-this-crossover-toroid-winding-called-and-what-is-its-purpose, by natevw - AF7TB, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
