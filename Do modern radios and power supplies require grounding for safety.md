# Do modern radios and power supplies require grounding for safety?

*Tags: grounding, safety · score 5*

## Question

Do modern radios require grounding to be used safely? All I am concerned about is not getting electrocuted when I attempt to use the radio. I'm not concerned with RFI or Lightning safety at this point in time.

The power supply apparently has a ground connection as well, even though it uses a standard AC 3rd prong ground power cable. Is this one different or required as well?

## Accepted answer (score 3, by gmlux)

The OP states clearly that the only interest is safety. That is how I answer the question.

In most countries there is a category of equipment that is double insulated. If your radio is connected to a double insulated supply then it should be considered safe from an electrical safety perspective. There is little possibility of a live cable internally touching a chassis which is connected to equipment that you are touching. There is therefore little possibility of electrocution.

In the circumstances that you talk about with the help of the picture, the power supply is grounded through the mains power feed. The power supply can be considered safe because if a live wire comes adrift for example inside the power supply and touches the chassis, the protection circuit , often a fuse, should blow, avoiding any risk of electrocution.

Consider the case where your radio is connected to that power supply and the negative rail is connected to the power supply ground internally. The equipment would be safe. Because like in the previous case, if a live wire comes adrift and contacts the chassis the protective fuse will blow. Negligible possibility of electrocution.

Consider another case, where this time the negative rail is not connected to the power supply ground the chassis of the radio will not be grounded. This is still safe since there is no high voltage made available to the radio that may contact the casing of the radio. In any case, if a live wire comes adrift and touches the chassis, the fuse will blow.

For completeness, the question might therefore be asked - why are there grounds lugs on the power supply and the radio? This is a wholly different area but please note that in some countries with some kinds of premises wiring it can actually be unsafe to connect this lug, or any part of any antenna, to an external ground such as a ground rod outside. But this is outside the scope of your question as are all RF noise and lightning concerns.

## Answer (score 2, by David Hoelzer)

I'm going to say "Yes," but refer you to the ARRL for a discussion that you might review to make your own decision.

Safety is potentially a factor, but a bigger concern is that the electrical ground for your house isn't ideal to use to ground your entire radio and antenna system. Doing so can lead to difficult to diagnose noise issues.

Certainly, the radio will be electrically grounded to the house ground too, but the secondary ground serves to ground the radio chassis and antenna to a common ground. Most of the hams that I know hammer a ground stake into the ground nearby their shack and use that to create a separate ground for everything radio related.

In the event of a lightning strike on your antenna, assuming you don't have a lightning arrestor, if you are using the house ground all of the energy still passes into the house (albeit, the ground), while the separate ground stake should almost certainly be a much shorter path.

## Answer (score 2, by Andrew)

If a radio is powered by 13.8V DC and it doesn't have vacuum tubes in it then it doesn't require a ground for safety. The ground in a radio is only required for safety when there are voltages in the radio that are dangerous, such as the mains supply or plate voltage of a valve, so that if something with high voltage accidentally touches the metal case inside for example, the high voltage will short out to ground and blow the fuse, instead of allowing a high voltage to be present on the case which is dangerous.

A power supply for a radio absolutely must have a ground for this reason if it's powered from the high voltage mains supply.

Note that the requirement for grounding has changed over the years.

An old timer ham radio operator will insist that everything MUST be grounded or you will DIE, this is because years ago most ham radio equipment contained valves with high voltage plate supplies which operated at low frequencies which required large antennas. Valve equipment should be grounded for safety and vertical antennas for low frequencies need a good ground to operate properly.

Today, most ham equipment is transistorized, and those radios which don't have a mains supply in them don't need a ground for safety, and higher frequency beam antennas and loaded vertical antennas with a coil at the base for example don't need a ground at all to operate properly.

Hope that all makes sense !

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18813/do-modern-radios-and-power-supplies-require-grounding-for-safety, by Nick H, gmlux, David Hoelzer, Andrew. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
