# 3D Printed yagi antenna

*Tags: antenna, diy, yagi, microwave · score 4*

## Question

I'm trying to produce a Yagi antenna for the 2.45 GHz band using a 3D dual extruder printer. The idea is to print the antenna elements using a metal filament and encasing it all in plastic.

The antenna needs to be highly directional, with 8 elements or more. Will it work?

Another option is to print the antenna plastic casing and then insert the metal rods through openings created during the printing process.

Any thoughts? Thanks

## Accepted answer (score 2, by hobbs - KC2G)

Not likely. To the best of my knowledge, any "metal filament" that's printable with a home 3D printer is PLA with 10%-50% of metal powder. This is good enough to make prints that look and feel metallic, but it's *not* enough for good electrical conductivity. Most likely it won't work as an antenna at all; definitely it won't have positive gain in any direction.

The idea with putting rods into a 3D-printed form is more hopeful. The low-dielectric-loss plastics you would *really* want to use for antennas (PTFE or polystyrene) aren't very practical to print with; PLA and ABS are very printable, but electrically they're much worse. But you might be able to get away with it if you take care to decrease the plastic coverage as much as possible.

## Answer (score 4, by tomnexus)

Some general hints from my experience:

1. Use wires not printed metal. You could stop the print for a while to drop in the wires, then finish it, or push them in later. For sanity's sake, design your yagi to use identical directors, and make or buy a wire cutting machine to produce lots of wires of the same length.

1.

Plastic will have an effect on tuning - the wires will need to be 10% to 20% shorter than the simulation design, and you will have to experiment to find out how much. Element spacing is not affected much, and what effect there is will be taken up by the length trimming that you do.

2.

Because you need to trim and measure many many times, you will need to print a "tuning model" antenna that can be opened and shut easily. It's nearly impossible to tune an antenna when the parts you need to adjust are sealed inside. Make sure the tuning model is representative of the plastic density of the final model.

3.

Water is a problem on tuned antennas like yagis, droplets on the elements will detune them. But if you have the elements embedded in slightly porous 3D-printed plastic, then the antenna will be completely useless if it gets wet. Printing a thin boom and letting the elements stick out will reduce the effect, but test it if it matters to you!

4.

Feed design - for 2.4 GHz, this would usually a small PCB connected to the coax, possibly with the reflector built in. See [this answer](How%20does%20a%20folded%20balun%20work.md) for some PCB design ideas for the feed:  
  
( the elements are a bit truncated )

This is an ABS plastic yagi we used to make. Elements were 1.2 mm tinned steel wire. It could be tuned over 1.4 to 2.6 GHz by adjusting the length of the directors. The feed and director were on a credit-card sized PCB at the back. Two identical housing halves were glued together.  
  
Gain was about 12 dBi, I think the plastic cost us 2 or 3 dB in losses, it was quite thick around the elements.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18474/3d-printed-yagi-antenna, by PHOLAN, hobbs - KC2G, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
