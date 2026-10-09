# Ferrite beads on a wire antenna?

*Tags: antenna-construction, wire-antenna · score 4*

## Question

Will putting a ferrite bead or beads near (but not at) the end(s) of a wire antenna electrically lengthen or shorten it? (lower or raise its resonant frequency)?

## Answer (score 4, by Phil Frost - W8II)

Lengthen. The bead increases the inductance, similarly to a loading coil. Near the ends the current is low, so the effect is diminished compared to the same coil near the feedpoint.

I wouldn't recommend it for a transmitting antenna. Ferrites have significant loss, and may saturate. Non-linear components are definitely not something you want in a transmitting antenna.

## Answer (score 2, by user103218)

Actually, the answer is "it depends".  
Polydoroff did some work on this in the 60's and documented it in his book: https://books.google.com/books/about/High_frequency_Magnetic_Materials.html?id=GC4jAAAAMAAJ

I'd quote the relevant part but my copy isn't with me at the moment. He showed significant shortening of the antenna with the ferrites he tested. He used ferrites of very low permeability, something like 8 or 10 if I remember correctly.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11847/ferrite-beads-on-a-wire-antenna, by hotpaw2, Phil Frost - W8II, user103218. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
