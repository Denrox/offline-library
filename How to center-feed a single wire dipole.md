# How to center-feed a single wire dipole?

*Tags: dipole · score 5*

## Question

I have heard that it is possible to feed single wire like a dipole from the center-point without actually making two separate wires.

How would I do this, what impedance would I expect to see, and what matching technique should I use to keep it at 50 ohms.

I would expect a very low impedance because of a DC short, with wires right next to each other but I know that changes with RF.

## Accepted answer (score 2, by Phil Frost - W8II)

There are several ways to do this, but given your previous question, we can reasonably assume that:

1. your wires won't be resonant at your desired frequency
2. you desire operation on a number of bands anyway
3. even if your wires *were* resonant, there are several nearby parallel wires that are going to alter the impedance from a theoretical dipole
4. you aren't going to dig up your patio to install a counterpoise, nor do you have much more space to install a new antenna or extend the existing wires

Given all of this, I think your easiest solution would be to pick one of those wires, and place another wire closer and parallel to it, shorting it on the ends. This makes a folded dipole, which does have a center feed, but which does not require that you cut the existing wire.

The unbroken conductor is your existing wire; the parallel wire with the feedpoint is a wire you add. Keep them roughly parallel with some non-conductive spacers.

Inherent in a folded dipole is an impedance step-up, since only some of the current flows in the half with the feed. If you make the wire you add smaller, then you get a greater impedance step-up. If you make the wire you add equal in diameter, then you get a 4:1 step-up. For "fat" wire you could use just the shield of some cheap coax. Flat braided wire could work also.

I'd run this, via ladder-line, to a tuner. This will allow you load up your wires on just about any band and get reasonable performance. Ladder line works better than coax in this application since it has much lower loss and is cheaper, and the SWR on the transmission line could be pretty high.

Another option would be a delta match. Simply take your ladder line feed and cut it down the middle for some length. Then attach the two ends at some points centered on the wire:

*image source*

You can think of this working as an autotransformer, with the dipole being a single-turn, straight inductor. By adjusting the connection points you can get different feed impedances. This was, back in the day, a very popular way to feed a half-wave dipole with 600-ohm ladder line. Find the best arrangement by experimentation.

Another option, since you seem to have multiple parallel wires: connect the ends of some of them together, making a loop. Leave a gap in one of the wires you add for the feedpoint. Or, feed it with a delta, as above.

Or, don't make a loop. Just connect one end, forming a "U". Now you can make a center-fed, bent dipole.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1914/how-to-center-feed-a-single-wire-dipole, by Skyler 440, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
