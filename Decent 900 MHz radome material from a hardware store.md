# Decent 900 MHz radome material from a hardware store

*Tags: antenna, antenna-construction, mesh-network · score 4*

## Question

I'm working on some outdoor Meshtastic nodes, and am considering materials for a radome to enclose the antenna, transceiver/host, and (possibly) battery all in one tube. The most important considerations are:

- Commonly available at any hardware store (PVC, PEX, LDPE, etc.)
- Works outdoor (UV, waterproof)
- Reasonably cheap (doesn't have to be the *cheapest*, but not Gore-Tex either)

For the 900 MHz band, what material would have the least effect on the signal and still meet these other requirements? I understand PVC may not be the best radome material in general, but how does it stack up against the other commonly available pipe?

## Accepted answer (score 6, by tomnexus)

At 900 MHz the radome losses will be quite small, whatever you choose.

Mechanical considerations will be much more important - price, availability of fittings and boxes, strength, glue, etc.

For the antenna part, if it's going to be in a pipe of some kind that sticks up, try to use the thinnest wall pipe you can find, and keep the antenna away from the plastic. The plastic will detune the antenna. This is not a problem if you're designing and tuning it yourself, but if you're using an off-the-shelf antenna it won't work properly in a thick plastic radome, taped to a sheet of glass, etc. In this regard, common plastics (PVC, ABS, etc, Er of 2.1) are better than things made mostly of glass (fishing pole, pultruded pipe, Er of 4). Carbon fibre (arrow shafts, tent poles) is right out!  
You can evaluate the *loss* of the material by putting a piece in the microwave oven for 10 seconds, if it gets warm then it's lossy. PP is best, ABS OK, PVC and Nylon worse, but the actual loss is very small at 900 MHz.

Choose something nice and rigid, PEX might be too flexible. It should be glueable. You should probably paint any common plastic building material you install in direct sunlight. Make sure it's completely waterproof at the top, but be sure to leave a drain hole at the bottom, for condensation. Completely waterproofing an enclosure is not a good idea, and nearly impossible if there are cables.

Finally, if you're building a few and you want them to look neat,look at ready-made waterproof ABS boxes from the usual mail-order suppliers. I've been pleased to find smallish boxes for just a dollar or two, quite good quality with a soft o-ring sealing gasket, brass inserts, screw mounting holes etc. Clear lids even. At the hardware store everything is built to meet all sorts of plumbing / electrical standards, you'll be lucky to pay under \$20 for what you're describing, while a 6x6x3" waterproof box with absolutely no certification might cost \$10, shipped.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22906/decent-900-mhz-radome-material-from-a-hardware-store, by Brad, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
