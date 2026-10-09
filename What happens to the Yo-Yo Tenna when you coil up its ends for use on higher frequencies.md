# What happens to the "Yo-Yo Tenna" when you coil up its ends for use on higher frequencies?

*Tags: antenna, antenna-theory, dipole, inductor · score 6*

## Question

I have gathered what is basically a Yo-Yo Tenna using some Camco laundry reels and a spool of cheap speaker wire split in half (pretty much exact duplicate of this build as it turns out). I've got a bit of equipment to measure the amount of noise the antenna absorbs to help tune it up, but I'm wondering more from a theoretical/antenna-design standpoint: what happens RF-wise as I roll the reels up?

That is, the idea of these antennas is simply a "wind up" dipole: two lengths of wire that can each be coiled up. Not only does this make the antenna nicely portable, but as the description of the Yo-Yo Vee claims:

Simply adjust bands or SWR by winding/unwinding the reels!

I've seen this to be true with my own setup too, I can unwind way less than the 100ft of each leg and get a higher frequency resonance. But what happens with the wound ends of the wire? Won't they form something of an inductor hanging out at each end? How would that inductance be expected to affect the efficiency and radiation pattern of the resulting antenna?

## Accepted answer (score 5, by Kevin Reid AG6YO)

I'm not certain of this answer, but this is my approximate understanding:

Yes, the coiled-up ends form inductors at the ends of the antenna. But the ends of the antenna are the part of it where (almost) no current flows, only voltage builds up! Therefore no current flows through the inductor, and so the inductance has no effect.

And if you're wondering why the extra length of wire doesn't still result in a “long” antenna due to the propagation time through it — well, the *mutual inductance between the turns of the coil* acts to couple the signal into all turns simultaneously, rather than it passing through the full length of the wire, so the signal enters the coil and immediately has effectively hit the end of the wire.

(But I think those are just two descriptions of the same thing, not two separate issues.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5557/what-happens-to-the-yo-yo-tenna-when-you-coil-up-its-ends-for-use-on-higher-fr, by natevw - AF7TB, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
