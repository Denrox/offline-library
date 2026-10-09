# Debugging SM0VPO's spiral loop antenna build

*Tags: balun, impedance-matching, loop-antenna, magnetic-loop · score 4*

## Question

I had built SM0VPO's spiral loop antenna. And here it is.

Recently I got myself a NanoVNA to see how finnicky it is to be tuned with that poor man's tuning cap. I brought it from 12 MHz into the 14 MHz 20 m band range by cutting off the extra wire to reduce the capacitance at the end.

But it is still not ideal. Here is the NanoVNA measurements:

I can't get the SWR under the 1.67:1 and essentially the impedance is 80Ω instead of 50Ω.

I also note that this antenna is pretty bad at receiving. I have no comparison to anything better at this point as it's really constraining inside an apartment where I'm still stuck, but I don't trust this baby.

I know that a spiral loop may not be the ideal antenna, but this has got a bit of fame because it is such an easy thing to build from scratch, so I wanted to give it the best chance.

**Questions:**

How can I improve the matching to get 50Ω impedance / 1.0:1 SWR?

From the Extra exam I just took, I remember you could put a length of 75Ω coax in series on the feed point to adapt 50Ω to 100Ω.

I also remember the stub match. Especially the very simple technique to just run a parallel open piece of coax from the feed point. But I guess that can only work at precisely one frequency and cannot be tuned, even a little bit. Given that mag-loops in general are such low bandwidth antennas, tuning ability is essential.

There seems to be excess capacitive reactance, what can I do to counteract it and not just reduce the (already bad?) efficiency of the antenna even more? I mean, I could perhaps insert a coil at the feed point, but I was hoping perhaps I could tweak something else?

I twisted and pushed and shoved the wire around to see if I can make an impact, and also moved to different locations, away from that lamp thing, away from the wall, etc. to no decisive avail.

Could I tweak this 1:1 Ruthroff balun, as there is apparently tweak-ability? Mine is according to the instructions done with 7 turns.

## Answer (score 3)

When tuning can be achieved then the only variables you have to optimize is the coupling and the compensation of the feed loop inductance (because k < 1). Just modify the area of the feed loop by bending the wires to a smaller or a larger area. You will end-up close to 50 Ohm. But resonance of the loop does not exactly correspond with lowest impedance. See below.

Second, not very critical and not essential, but just a recommendation: the tuning of the uncoupled part of the feed loop inductance. That can be done with series capacitance between the inner coax and the connection with the feed loop. Value probably 500 pF film or low-loss RF capacitor (estimation, based on experience with this type of loops).

Finally: the feed loop is already floating. The transformers adds only to the losses. There is no need to insert that transformer.

For reception the loop is OK and not that critical w.r.t. losses. For transmitter use I schould go for lower loss copper or alumin material and a variable capacitor made from copper PCB-material and teflon or nylon dielectricum (cutting board, more than 2 mm thickness, white material without color pigment).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18010/debugging-sm0vpo-s-spiral-loop-antenna-build, by Gunther Schadow. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
