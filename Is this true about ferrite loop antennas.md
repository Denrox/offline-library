# Is this true about ferrite loop antennas?

*Tags: antenna, ferrite, loop · score 3*

## Question

There is an article on wikipedia about loop antennas.

It shows like an AM radio's antenna with the ferrite rod and says this:

This greater conductance channels thousands of times more magnetic power through the rod, and hence through the loop, allowing the physically small antenna to have a larger effective area.

Now if I imagine the coil without the ferrite but I multiply the area by 1000, that will be a huge area, how can it be 1000 times more power?

If I place another radio next to it, will it literally zap half the power from the other radio?

## Accepted answer (score 4, by Phil Frost - W8II)

Now if I imagine the coil without the ferrite but I multiply the area by 1000, that will be a huge area, how can it be 1000 times more power?

Because, as the article says, the magnetic permeability of the ferrite rod is much higher than that of air, and thus it concentrates the magnetic flux from a large area around the antenna.  
[Ferrite Antennas for A.M. Broadcast Receivers, Laurent and Carvalho, 1962]

This has the same effect as making the loop physically bigger (neglecting losses in the ferrite, which aren't large at AM broadcast frequencies).

If I place another radio next to it, will it literally zap half the power from the other radio?

I don't know what "literally zap" means, but yes, any antenna can absorb electromagnetic energy from the space around it, making that energy unavailable for other receivers. It does require that the antenna be terminated in a load that will convert the electromagnetic energy to another form, such as a resistor converts electrical energy to heat.

If you were to optimize for this energy capture, perhaps putting this antenna very close to the transmitting antenna with the objective of capturing *all* the transmitted power such that nothing else can receive it, you will have made a transformer.

## Answer (score 2, by hotpaw2)

Nearby antenna elements do affect each other. Consider a Yagi-Uda. Pointed in the "wrong" direction, the director and reflector elements will reduce the EM power that the driven element receives from the impinging RF field.

However, a parasitic loop can often increase the power to a nearby small radio antenna, rather than steal (or "zap") power.

The magnetic field concentration caused by a multi-turn loop inductance, whether with a ferrite core or not, concentrates the EM field lines not only inside the loops of the coil, but in the total virtual aperture area or volume nearby. All nearby EM field lines (in the entire neighborhood) will be distorted towards the loop inductor and/or volume of higher relative permeability.

There are inductor coil antenna products that take advantage of this. You merely put a tuned passive loop antenna near your small receiver's internal antenna to increase the received signal level. Here's an example of one by Kaito, a "Tunable Passive AM Radio Loop Antenna", but there are other vendors of similar products: https://www.amazon.com/gp/product/B001KC579Q/

If you are wondering where the "added" power comes from, consider it stolen, not from nearby receive antennas, but from the transmitter's antenna, due to more efficient inductive coupling between the two stations. All the EM field lines will be pulled closer, not just the ones near the receive antenna ferrite core.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18827/is-this-true-about-ferrite-loop-antennas, by pgibbons, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
