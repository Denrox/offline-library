# Metal panels in 4nec2

*Tags: antenna-system, antenna-modeling · score 5*

## Question

I have a number of immovable metal roofs that are near my antennas. I'm wanting to model how these affect my antenna performance.

Is there a way I can put a metal plane into my models on 4nec2?

## Answer (score 3, by tomnexus)

NEC2 can model metal structures, using a grid of wires. There's no card for a metal sheet, you need to construct it out of segments. I've done this many many times to model aircraft, buildings, vehicles, ships. But I've never used 4nec2.

4nec2 seems to be able to do the meshing for you. It says "Geometry builder to create cylindric, patch, plane, box, helix and parabola shaped structures using auto-segmentation and/or equal-area rules."

The equal-area rule recommends a segment radius that makes the total area of the wire mesh, the same as the area of the metal sheet it replaces. (I forget if it's one side or both sides of the sheet, it doesn't matter too much, and 4nec2 will do it for you anyway. The mesh grid will be about $\lambda/10$ as usual, so it uses a lot of segments.

I don't find many examples of meshed structures in 4nec2, but see slide 34 of this presentation for one. The last page of this presentation gives an example of the *geometry builder* being used to model a parabolic dish.

The more complex problem is exactly what to build. You don't say whether this is HF or VHF/UHF, the approach will be very different in these two cases.

If you have a 2 m vertically polarised antenna high up but near a large metal sheet, you could model that sheet as a wire grid, and simulate the whole thing in free space.

If you have an HF Inverted-V, Vertical or Yagi, then apart from the antenna itself, you should also:

- Include a Somerfeld-Norton ground in the simulation, using suitable ground parameters ([here's a list of soil types](DIY%20Short%20Vertical%20Wire%20Loaded%20Antenna%20Using%2020%20Ohm%20Resister%20to%20Widen%20Q.md))
- build your metal roof structure, though it can be quite sparse at these frequencies.
- *connect your roof to the ground with some vertical wires* because most buildings are at least somewhat conductive, with lightning conductors, internal wiring and downspouts etc. You can also put the edge of a meshed grid wall touching the ground, just make sure there are no segments lying on the ground.
- NEC2 tells you in the output file which segments were properly connected to the ground, so you can confirm that you got what you wanted.
- 4nec2 may be able to grid a box for you directly, this would be a good choice for a nearby building. A 20 x 20 x 10 metre box, at 15 MHz, will only take up a few hundred segments.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22433/metal-panels-in-4nec2, by David Findlay, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
