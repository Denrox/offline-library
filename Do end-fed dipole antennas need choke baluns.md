# Do end-fed dipole antennas need choke baluns?

*Tags: balun, end-fed-antenna, choke-balun · score 7*

## Question

I have a couple of end-fed wire antennas I bought that came with matching baluns. One has a 9:1 unun, and I'm not sure about the other one. In addition to those, should I also put a choke balun on the coax before the matching one?

## Answer (score 4, by Glenn W9IQ)

End fed antennas have become quite popular in recent years, primarily due to their convenient installation conditions. Many people subjectively report good results from the antenna. But how the antenna works is not often well understood.

The end fed antenna often utilizes an unun at the feedpoint of the antenna. This is done because the feedpoint impedance of an end fed half wave wire is in the 5,000 ohm range. The unun, which is typically nothing more than an autotransformer, attempts to convert the relatively high impedance of the antenna to the lower impedance of the coax. In reality, the unun does a far from ideal conversion of a simple transformer but rather contributes to a non-linear complex impedance transformation.

The other anomaly of an end fed antenna is that there is only one apparent connection to the antenna. The coax and transmitter, on the other hand, require that current flows in equal and opposite directions. While the unun contributes somewhat to this requirement, in most installations the balancing current actually flows on the outside of the coax shield. Due to the skin effect of RF, this is a completely distinct current from what is flowing on the inside of the shield of the coax. This is sometimes called the third wire of the coax. Thus the coax often forms part of the radiating antenna. Normally we try to avoid this condition but without any other form of counterpoise, it is nearly a requirement to make this type of antenna work reasonably well.

Placing a choking balun at the feedpoint of the antenna may be counterproductive for many end fed antenna arrangements. On the other hand, it is not desirable to allow the current that is flowing on the outside of the coax to enter the shack since this can lead to RFI while transmitting. Often a good compromise is to place a choking balun on the coax just before it enters the shack.

Once you have your antenna in place and have experimented with the choking balun near the shack, you could try an additional choking balun at the antenna feedpoint between the coax and the unun. Be prepared though to see a rise in SWR but potentially a helpful noise level reduction. You will need to judge based on your circumstances if this additional choking balun is helpful or not.

## Answer (score 3, by JSH)

I cannot speak to the off-center type dipole feeds that use the 1:9 (impedance) transformers, but for the truly end-fed dipoles fed with something like a 1:49 impedance ratio, the answer is, it depends.

I performed some simulations of an end-fed dipole system with an autotransformer and an additional wire representing the currents along the feed line. I did so with the wire open ended and with a couple 1/4 wave radials to represent both ungrounded and grounded situations. In the article I look at SWR, Return Loss and antenna gain in the axis of only the antenna radiator. All tell the same story, but gain gets the nod to view for this answer...

Key points include:

- Feedline lengths up to near 1/4 wave do not cause much trouble for either case. This jives well with the many reports of successful portable operations using EFHW antennas with very short feed lines.
- Whenever the feedline presents a high impedance to the antenna feed, current is drawn from the primary radiator resulting in perturbed performance and lower gain.

So to answer your question if the feedline is under 1/4 wave in length, there appears to be no reason for a current choke. However, if you have lengths 1/4 wave or longer, it may be time to add one... but where?

If my simulations are correct, placing the high impedance of the choke 1/4 wave back should provide protection to the system for any length of feedline past the choke since the choke always forces a low impedance (1/4 wave transformer) at the feed point that is very dissimilar to the high impedance feedpoint. This odd phenomena is reverse of the case of a center-fed dipole or 1/4 wave monopole.

This is what simulations and a growing set of measured data suggests.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9533/do-end-fed-dipole-antennas-need-choke-baluns, by Pablo Fernandez, Glenn W9IQ, JSH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
