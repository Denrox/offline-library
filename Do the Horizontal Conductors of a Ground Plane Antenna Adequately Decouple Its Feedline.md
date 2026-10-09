# Do the Horizontal Conductors of a Ground Plane Antenna Adequately Decouple Its Feedline?

*Tags: coaxial-cable, feed-line, radiation-pattern, radial · score 3*

## Question

A NEC4.2 analysis of this configuration may reveal an unexpected truth about this...

## Answer (score 3, by Richard Fry)

Below is a NEC4.2 comparison of the v-plane patterns of a 1/4-wave ground plane antenna mounted 5m above level Earth and using 4 x 1/4-wave, horizontal radials, with / without a coax transmission line having the OD of the shield "grounded" to the Earth.

Two observations:


The 4 x 1/4-wave horizontal conductors do not effectively decouple the transmission line from currents flowing along the vertical conductor of the ground plane, and


The net, peak radiation pattern gain of the ground plane antenna is reduced by about 1.8 dB for these conditions, due to the effects of the radiation from the OD of the outer conductor of that transmission line.

Added below are my comments and a graphic in response to the comment of hotpaw2:

The feedpoints for the GP as modeled attach the center conductor of the coax feedline to the base of the vertical conductor, and the feedline shield to the common-point of the four radials. The vertical conductor is one pole of the antenna system; the radials are the other.

If the radials are attached to the base of the vertical conductor and then driven together by the center conductor of the coax feedline, that would force all of the r-f current flowing on the ID of the shield to migrate to the OD of the shield at the top of the feedline, and produce radiation from its outer surface.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16422/do-the-horizontal-conductors-of-a-ground-plane-antenna-adequately-decouple-its, by Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
