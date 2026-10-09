# How do I extend broken coaxial cable?

*Tags: diy, connectors, coaxial-cable · score 8*

## Question

I have a piece of 75 ohm coaxial cable of unknown type (outer diameter is around 7 mm) which has developed a breakage in the center conductor (which is stranded). This cable is an adapter cable which connects my RG-6 type coaxial cable to my RTL-SDR card.

As far as I understand, the best way to solve the issue would be to simply replace the cable with another cable of higher quality. Unfortunately, this solution is not applicable to me, since the ends of the cable are attached to connectors of types which I can't easily obtain. The card end uses MCX connector and the RG-6 end uses a type of Belling-Lee connector suited for work with thin coaxial cables.

Second idea that came to me and which I used with success with some other coaxial cables is to cut out the middle, damaged, section and leave short pieces of cable near the connectors I can't replace. After that, connect easily obtainable connectors to the healthy ends of the cable and mate the new connectors or use another coaxial cable in the middle.

SMA and RP-SMA connectors come to my mind here, but the problem is that they are 50 ohm connectors in general. I also don't have the tools to install them and this one-off repair doesn't justify obtaining such tools.

Another idea that I like the least but am currently most likely going to go with would be to directly connect the two healthy ends of the cable. Solder together the inner conductors, cover the joint with heatshink tube, then carefully solder together outer braided conductors and cover them in heatshrink tube as well. Problem here is that I don't like the reliability of the resulting work. A variation of this theme would be to solder the healthy ends of the existing cable to a new piece of a different, but similar, coaxial cable. The effect of this is that I'd have more room to work with.

Finally the worst solution I see right now would be to replace the connector on the card which uses the damaged coaxial cable with an SMA connector. The problem with this is that SMA connectors are in general 50 ohm connectors and this is a 75 ohm system.

So my question is basically how do I repair this cable? Which of the options I could work with is the least bad and are there any better ideas I didn't think of?

## Accepted answer (score 4, by WPrecht)

A complete replacement will be the most reliable solution. Barring that, replacement of one end if the resulting size is acceptable. I would rate a manual repair dead last. Soldered joints are rigid and even if the repair holds, it will place stress on adjacent sections of coax.

These connectors and in fact, complete cables with MCX on one end and a Belling-Lee connector on the other are available, inexpensively, on eBay. One UK shop lists them all: http://stores.ebay.com/RFShopUK. They cost from about 2.00USD for the ends to about 10.00USD for the whole cable.

## Answer (score 3, by The Lightning Stalker)

Cut off a little extra and save some dielectric material. Then strip the outer sheath off and bend back the braid and carefully flip it inside out like a sock back over the sheath. Then cut back the exposed dielectric and core a little. This is so the braids can overlap.

Now strip the dielectric off the core and solder the 2 core ends together with about 1/8" (5mm) of overlap for strength. Make sure it's a nice shiny joint with the right amount of solder so it doesn't ball up. Liquid flux and a clean iron tip really help. Then clean flux residue with some IPA.

Remember that dielectric material you saved? Cut a piece the length of the exposed core in your joint and slit it lengthwise with a razor like a hot dog bun. Take this and slip it over the core so it's covering as though the dielectric was continuous through the whole joint with as little exposed core as possible. Keep it all as short is you feel comfortable with.

The last step is to flip the braid back over the soldered core and your dielectric hot dog. The two ends of braid should slightly overlap and stay close against the dielectric. If there was foil under the braid wrap some around as well as it is in the rest of the coax. Keep in mind we are trying to recreate the conditions of the coax as closely as possible using pieces of itself. Then very carefully solder the braid all the way around using as little heat as possible. It is very easy to melt the dielectric and ruin the splice. This isn't the case so much with Teflon but other types can be difficult or impossible to solder without melting it. That is why industry only uses crimp connections on foam core. If you're using a soldering iron without temperature control, you should unplug it and let it cool, then plug it back in and quickly solder it up before it gets too hot. Heat shrink or tape over this and it should be a near perfect splice.

This old trick has been used many times to join sections of coax without using connectors.

## Answer (score 2, by HarveyB)

I would opt for the "solder and shrink" and just go on with it. Like you I worried about this problem and decided to do some "basic research" while I had access to proper instruments. What I found was that the use of "dirty patches", "wrong impedance connectors" and even unshielded joints (twisting the shield braid into a single conductor) made no measurable difference in signal. **Note to all who are about to flame me**: If you disagree, TRY IT before you judge! Do the tests yourself and post the results!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/936/how-do-i-extend-broken-coaxial-cable, by AndrejaKo, WPrecht, The Lightning Stalker, HarveyB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
