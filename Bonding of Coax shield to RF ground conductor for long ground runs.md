# Bonding of Coax shield to RF ground conductor for long ground runs?

*Tags: grounding · score 4*

## Question

My shack is on the second floor of my home, and I run a single operator, 2 radio contest setup. The two coax runs pass through the wall and drop down to an antenna switch approximately 15 feet from the radios.

The ground system consists of multiple copper ground rods driven in over a fairly wide area, bonded together with 4awg bare copper wire, and the ground then travels up the exterior of the house to the shack via a 1" wide copper braid, also about 15 feet long in total.

The coax shields are grounded to the same ground stakes that the antenna switch is grounded to, and there are polyphaser lightning arrestors located at the ground stakes.

K9YC and W8JI both recommend installing common mode chokes as close to the radio as possible, and connected to a low impedance ground line to prevent high power common mode signals from efficiently coupling to nearby electronics. I intend to do so using 1:1 common mode chokes right at the radio coax connector, bonded to the ground line, but neither mention bonding feed line runs together.

I'm trying to determine if there would be any advantage or disadvantage to bonding the shields of both coax runs and the ground line together at the bulkhead panel. On the one hand, this would reduce overall impedance of the ground connection, but on the other, it may provide a route that common mode current appearing on one conductor could bleed over on to the other conductors.

I will likely also include common mode suppression within the antenna switch itself, so the line should be fairly well isolated on both ends.

Should I use the bulkhead connectors and bond the lines together at the pass through plate (some 6 feet from the radios and 10 feet from earth), or use grommets to protect the coax as it passes through the hole in the aluminum panel, and bond the coax shield to the ground line only at the radio chassis and the antenna switch?

## Accepted answer (score 4, by Phil Frost - W8II)

Bond it all together. At both ends, if you can. Effective lighting protection isn't really just about providing a path to ground, though that's part of it. More importantly, [lightning protection](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md) is about having "ground" at just one point so "ground over here" can't be 200V different from "ground over there". This is what you get, for example, when your radio is plugged into a normal AC outlet which goes to the ground at the electrical panel (ground #1), while also being plugged into the antenna (ground #2).

The more effectively you bond all the grounds together, the less potential difference can develop between them, providing better protection. The lightning protector is just there to temporarily ground thing which can not be grounded (like the coax center conductor) in the case of a strike.

Bonding the grounds together isn't going to make common mode issues any worse, and if anything will make them better. In fact common mode currents will flow over all your cables whether you connect them or not: that they run parallel means they are inductively and capacitively coupled and so the RF current will "jump" across them even if they aren't connected at DC. This is why for example common mode currents always end up on the outside of coax, even if you try to drive the current on the center.

And if your common-mode currents are due to something like driving a vertical without a sufficient ground plane, then those common mode currents want to get to ground to match the current in the vertical. Providing a lower impedance path to ground will thus improve things.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6574/bonding-of-coax-shield-to-rf-ground-conductor-for-long-ground-runs, by Hamsterdave, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
