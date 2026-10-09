# How to achieve highest Q-factor in inductors for 6-160m amateur bands?

*Tags: filter, ferrite, toroid · score 6*

## Question

When building filters for ham bands (direct sampling SDR frontend) - it is common to build filters using 2,6,10,12 material toroids. Are there any recent developments that offer lower losses / higher-Q in amateur bands? (6-160m)

Are there any other tricks to increase Q? For example, I guess for 160m band it is possible to wind coils with litz wire. Any other similar high-Q tricks, especially ones suitable for 20/30m bands?

If no better core materials are available, is there anything could be done with the wire itself? It is clear that it must be single layer. But beyond that - maximize diameter of the wire or there must be some air gaps left? Flatten wire in the inner part of the coil? What is maximum frequency where Litz wire can still help in increasing Q?

## Accepted answer (score 2, by Ryuji AB1WX)

Among the toroidal core materials for preselector filter uses, 2, 6, 10, and 17 materials are still the best options. You can achieve higher Q with large diameter air-wound inductors for some inductance ranges, but they will be physically larger and you'll also have to take care to avoid magnetic field coupling.

The original poster's intention is to build receiver preselector filters for HF/6m ham bands. Such filters have relatively low loaded Q's (the Q of the filter circuit). The inductors should have 10x or greater unloaded Q (component's Q) to achieve the filter performance as designed and avoid large insertion loss. For low bands up to 40m or 30m, some insertion loss may not matter, as those bands have high external noise levels that often benefit from attenuation. Component Q greater than 20x of filter Q will have diminishing returns in terms of the performance of the implemented filter. Please note that there are different Q's, one for the circuit (loaded Q) and another for individual components (unloaded Q). Using an inductor of higher Q does not necessarily make the filter sharper.

In short, for typical HF to 6m preselector filters, careful design and construction with toroids of 2, 6, 10, or 17 material would suffice. I would consider 2 for 160 and 80, 6 for 60 through 20 or 15m, and 10 or 17 for 12m and up for small core sizes like T25, T27, T30, and maybe T37. But if the OP wants to build something unusually sharp, inductors of higher Q may be needed, but such a filter will also likely require close attention in other aspects.

## Answer (score 4, by Aleksander Alekseev - R2AUK)

To my knowledge there were no recent discovers in the area of ferrite materials. Mix 6 is pretty much as good as you will get when it comes to building low-pass / band-pass filters for HF bands. I believe one of the reasons may be that even if you invent something better it will not present a valuable product for the market. Current low-pass and band-pass filters are good enough.

Lower losses and higher Q can be obtained with quartz crystals though. A Q of 100 000 is quite common and sometimes you can get crystals with Q of 150 000 and more. Quartz crystals are commonly used for building narrow band IF filters. For instance it's not difficult to build an band-pass filter with 2-3 kHz bandwidth and insertion losses of 1-2 dB. Also there are filters available from many manufacturers for common IF frequencies if you don't want to build one.

## Answer (score 3, by Jimbo47)

You mentioned litz wire. Using this can reduce ohmic losses in the wire due to skin effect and proximity effect. I have read they can be useful up to 8 MHz. BUT! Problem is that the needed wires get smaller as the frequency increases (the individual wire needs to be smaller than the skin depth) and nobody seems to make litz wire cables with wire smaller then about 48 awg. This is good to about 2.8 MHz. So it could be of benefit to a 160 Meter filter. Jim KA6TPR

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21549/how-to-achieve-highest-q-factor-in-inductors-for-6-160m-amateur-bands, by BarsMonster - R2AYN, Ryuji AB1WX, Aleksander Alekseev - R2AUK, Jimbo47. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
