# Slot antenna for 2 meter mobile

*Tags: antenna, diy, mobile, 2m-band · score 4*

## Question

My primary vehicle is a Smart car, with a roof that's a piece of plastic(100% moon roof). Not the most awesome of cars to use for grounds. I'm building a bumper mounted antenna tower, EMT with some square tube. Earlier today I stumbled across an article on 2 meter slot antennas cut in to satellite dishes. Literature is repetitive either directed towards that subject or TV and UHF broadcasting. I like the idea of a Dipole analogue that doesn't look like an antenna... Currently the 1/2 wave whip makes it look MORE like a cheap RC toy...

This isn't a basic theory question, more of a practical application...

So the questions are:

Would a Slot antenna cut into a piece of 1.5 inch wide, 1/8 inch thick bar stock work? Minimal expense and I can get it almost anywhere.

Would that be better than just cutting the slot into the bars? I can't find out if that's very directional, I assume I'd cut it in the top and use weep holes, cheapest option.

Any better Ideas?

## Answer (score 3, by Edwin van Mierlo)

So you don't want a whip, as it makes the Smart Car look like a "RC Toy" (although some in the hobby, me at least, will disagree, afterall antennas on cars are fantastic)

And you don't want to hinder and doors/trunk/whatever opening, as you use the vehicle for certain purposes... (fair enough)

And you cannot use any mag-mount, as the vehicle is largely plastic, which also means you don't have a "ground plane" or whatever name you want to give it. (Technically the metal horizontal parts of a vehicle will act as a capacitor to earth when properly bonded. But some think the car itself is the ground plane)

You are thinking of a "slot antenna" but just to realize that a "slot" in the "slot antenna" is the same size as a 1/2 wave dipole, the "slot antenna", besides that it will be directional (not good for mobile use) will be quite large... which you do not want (the "RC toy" effect again)... as well as difficult to mount. If you have already a problem with 1/2 wave whip, then the slot will be even bigger.

Furthermore, it will be doubtful if you can actually use a slot antenna for VHF, as these are mostly designed for much higher frequencies.

If you don't mind doing a bit of DIY: you can get antenna's for the 87-108 MHz which you can stick to a windscreen (front or back), example:

You will have take out any active/passive components, and tune it for 2m. But it will not obstruct doors, it will not have a visual impact.

Efficiency and how this works is hard to say. I have not done this (yet).

To answer your specific questions:

Would a Slot antenna cut into a piece of 1.5 inch wide, 1/8 inch thick bar stock work? Minimal expense and I can get it almost anywhere.

That is not how a slot antenna works, please look up some designs online. Examples:

- http://www.eetrend.com/files-eetrend/antena-part8.pdf
- http://www.qsl.net/n1bwt/ch7_part1.pdf
- *there are many more*

You will quickly find that your approach is too simplistic to produce a working model.

Would that be better than just cutting the slot into the bars? I can't find out if that's very directional, I assume I'd cut it in the top and use weep holes, cheapest option.

As per previous answer, the design is much more complex. (and) Yes, a slot antenna is a directional antenna which is not suitable for mobile use.

## Answer (score 2, by webmarc)

Check out this video from AG6IF who built a 2m slot antenna out of an old parabolic dish. His application was for home mounting a stealthy antenna, but the interesting notion there is that the slot is curved. His video shows a chart from an analyzer as well.

This indicates to me that it's worth trying your idea too.

Hope this is helpful!

## Answer (score 2, by Juan Jimenez)

I mounted a Diamond antenna on my 451 for 2 meter/70 cm on the front bumper using the (painted) tow eyehook. The Diamond antenna doesn't need a ground but in this case the metal bumper provides it.

The mount itself is a piece of steel blowtorched into 90-degree submission, with a 5/8" hole for the double-ended SO-239 and 11/16th for the tow bolt. I added two 5/8" washers and a 3/4" x 2" galvanized steel segment as spacers. Everything is painted with black acrylic spray paint. I still have to wrap the connectors with electric tape to keep out moisture.

The RG-8/X coax was run from the cabin through the grommet behind the instrument panel (use a knife to cut one of the four nipples) into the front compartment and out the bottom grill. You don't even need a wire chaser, just push it through from either the front or inside the cabin.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9882/slot-antenna-for-2-meter-mobile, by Omagasohe, Edwin van Mierlo, webmarc, Juan Jimenez. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
