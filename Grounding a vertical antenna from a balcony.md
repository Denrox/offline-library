# Grounding a vertical antenna from a balcony

*Tags: antenna, antenna-theory, coaxial-cable, vertical-antenna, grounding · score 6*

## Question

I have a multiband vertical antenna mounted onto the railings of my balcony apartment high up on the 6th floor of an apartment building. The antenna is not grounded. This antenna comes without radials.

I can see at the side of my building, a ground wire coming down from the roof of the building from other antennas from the roof to ground. Would it make sense if I attached the outer coax of my feeder to this ground wire, for better antenna performance.

Feel free to correct me and tell me if this is a nonsense idea and why. I am still learning here:) Thanks

## Answer (score 5, by Andrew)

Engineer999.

While it might seem like a good idea to connect your antenna to the building ground wire, my experience has been that for those vertical antennas which are designed to operate without radials it makes little or no difference what the ground is connected to.

You also should consider that if you are in a multi-tenanted building where you aren't the owner, there may be legal reasons not to connect to that wire, it may be there for lightning protection for example.

Also, how it's wired into the building grounding system is unknown and you may run into problems with grounding currents which can cause damage to electronic equipment.

For example, imagine this : your mains supply ground is connected to an earth at one point in the building and that ground wire is connected to a different earth somewhere else. If you connect your antenna to the ground wire, then the ground of the radio and the ground of the power supply for the radio will be different, and if there is a voltage difference between the two grounds, which is a distinct possibility, then there will be AC current flowing in your equipment, the result can be burnt out ground tracks in the radio or the radio power supply.

One other side effect may be the increased risk of RFI interference to your neighbors' TVs and radios when you transmit, because the building ground wire will become part of your antenna system.

My suggestion is that it's a bad idea.

Hope that helps !

## Answer (score 3, by webmarc)

It may be great, it may not... that's definitely an empirical question due to the many factors:

- how much of the xmit current on the ground leg will be parallel and next to your vertical? this could cause destructive interference and make the antenna pattern more directional.
- are there other currents on the ground that will make their way into your antenna system as RFI?
- prob more.

If this is primarily for 10/20m, you might first experiment with dropping a simple 1/4 wave wire attached to the coax shield at the feed point to create a place for the "ground leg" of your RF current to operate. I would expect to find an improvement in SWR as well as both xmit and receive capability.

I should add: since the goal is to provide a low impedance path for the shield current, it can really be any multiple of 1/4 wave... so if 20m is your lowest frequency, cut to that wavelength which is 2/4 waves at 10m and still good.

There are some GREAT Q&A here on the topic of grounding, I've learned a ton by perusing.

**Especially relevant**, [this answer to a closely related question](Can%20I%20use%20electrical%20ground%20earth%20as%20my%20RF%20ground.md). In part, Phil notes:

"RF ground" usually means "something that is at the same potential as the soil". This is important because if you have a wire (such as your feedline, for example) which is not at ground potential, then there exists a non-zero electromagnetic field between that wire and the soil. That means the feedline is radiating/receiving, which is usually undesirable.

It's worth checking out the [entire answer](Can%20I%20use%20electrical%20ground%20earth%20as%20my%20RF%20ground.md).

**Unrelated**: if you haven't already installed an RF choke on the feedline at the feed point, you should consider doing so to keep RF off your coax and keep it going thru your antenna. Likewise, you should consider another RF choke on the feed line at the receiver to keep any environmental RFI that enters your feed line out of your receiver. I've found this to be very helpful in some of the dense living situations I've encountered :-)

## Answer (score 2, by Aleksander Alekseev - R2AUK)

Would it make sense if I attached the outer coax of my feeder to this ground wire, for better antenna performance.

Probably not, at least because you will gather the noise from the entire building.

I had a similar antenna (OPEK HVT-400B) for some time. What it actually needs, as a vertical, are radials, more is better. I had space for two radials 5 meters long each (they can be folded if there is not enough space). This worked OK, I could use the antenna on 20m and 40m. Although after I learned a little more about antennas I realized that 10 meters of the RG-58 coax were probably working as a radial for 40m, HI HI. To prevent this from happening you need a balun at the feed point of the antenna.

You also need a static bleeder to protect the transceiver from static electricity. I used 90 turns of 0.9 mm insulated solid copper wire on a ferrite rod with μ = 400, which gave 313.7 uH, between the shield and inner conductor of the coax for several years now. This arrangement works flawlessly.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18709/grounding-a-vertical-antenna-from-a-balcony, by Engineer999, Andrew, webmarc, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
