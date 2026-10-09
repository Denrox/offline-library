# Grounding VHF base station antenna

*Tags: grounding · score 10*

## Question

I'd like to install an outdoor dual band VHF/UHF base station antenna, a simple pole antenna like the Comet GP-1.

I live in an area where lightning is rare, but not unheard of. Should I drive ground rods into the ground for antenna/RF grounding? The antenna itself has several small ground radials, so I'm assuming that a good ground will aid performance, but don't know if using the existing building ground is "good enough".

I live in a multi-unit building which may complicate this since my understanding is that any antenna ground system should be bonded to the building ground to prevent differing ground potentials (and the bonding should be via a dedicated ground wire directly to the building ground, not through a ground conductor in the building wiring), however my building ground rod is in a separate structure. The service entrance is in a closet in the back of a garage structure, then it goes under a sidewalk and my front yard and then into a service panel in my kitchen in the middle of the house (either under or through the cement slab). There's no apparent grounding electrode for the living unit, and even if there was, there's no easy way to run a ground wire from the antenna to it since I'd either have to go around a neighbor's unit or over the roof to reach it. It is possible that the service panel is grounded to the slab rebar or to a ground electrode that's not visible.

My housing complex looks something like the diagram below (though there are more housing units than what I've drawn), where I'm in unit 2 and would mount the antenna outside a room on the back side of the unit, while the service entrance comes in from the garage on the other side, The "V" shows the location of the service panel inside the unit:

Since I'll be using it with a 12VDC mobile transceiver, I could conceivably keep the tranceiver isolated from ground, leaving the antenna & transceiver ground completely separate from the building ground, but that seems quite unsafe if there is a difference in ground potential between the back yard and front yard.

What is the best practice for grounding this antenna?

## Accepted answer (score 10, by Phil Frost - W8II)

Should I drive ground rods into the ground for antenna/RF grounding?

*Probably not*. What you are likely to accomplish is this: (diagram from W8JI)

If the lightning hits the antenna, have the same problem in the other direction. The important thing to realize is that the current from a lightning strike is so huge that it will go through *all* the grounds, and if one of those paths is through your equipment, expect something to be broken.

You might even be making things worse by adding a ground (*B*) to your station. Now your radio is part of the safety ground for your house's electrical system, *even if you disconnect the feedline (A)*. Don't do that!

Grounding the antenna won't improve its performance. The important thing is to eliminate [common-mode currents](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md) in your antenna system, perhaps [with a balun](Using%20a%20balun%20with%20a%20resonant%20dipole.md). Once you've done that, there won't be any need to ground the antenna for performance.

A proper lightning protection scheme requires that you take *all* cables entering your station, including the feedline, AC mains, ethernet, telephone, and anything else, and passing them through a common ground point which is bonded *really well* with the Earth (read: multiple ground rods, wide, short copper strap). With only one ground connection, there's no path *through* your equipment, only *around* it.

This is costly and time consuming, and given your specific situation (relatively small VHF antenna on what I assume isn't an especially large tower, in a region with rare lightning) it may be difficult to justify the expense and effort.

If you don't add more grounds (such as *B* in the diagram above), then you can be reasonably protected by [disconnecting the feedline](How%20to%20keep%20a%20disconnected%20coaxial%20connector%20weatherproof.md). Your station at least won't be any more vulnerable than any other device you leaved plugged into mains, like your TV.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1535/grounding-vhf-base-station-antenna, by Johnny, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
