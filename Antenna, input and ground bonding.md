# Antenna, input and ground bonding

*Tags: antenna, grounding · score 4*

## Question

I'm new to this and am in need of guidance. I am mounting a multi-band antenna on a 50 foot tall 1 1/4" galvanized mast. I plan to drive a ground rod at the base of the antenna and bond the mast to it. I also plan to ground the RG-8/U at the top of the mast and at the bottom of the mast. The mast/ground rod is on the opposite end of the house (probably 50' of wire needed) from the electric service entrance and ground.

My questions are:

1.

What size wire is recommended to bond the antenna ground to the electric service ground?

2.

When I ground the RG-8/U nearest the entrance to the house, can I ground it to ground wire running in item #1, or do I run the ground to one of the ground rods?

3.

The ground bus that I install in the shack should be bonded to which ground rod, and should use what size wire?

Any help would be very much appreciated.

Ray KK4WPB

## Answer (score 5, by Phil Frost - W8II)

What size wire is recommended to bond the antenna ground to the electric service ground?

I'd recommend (and electrical code may require) 6 AWG solid wire, both for electrical and mechanical reasons. If the cost is acceptable, flat copper strap is even better since it has lower inductance.

Make the connections with brazing or welding if possible. Every milliohm matters when lightning currents are involved. And mechanical connections have a way of failing. I use Harris Stay-Silv 15 with a MAPP gas torch. Cadweld is another option.

When I ground the RG-8/U nearest the entrance to the house, can I ground it to ground wire running in item #1, or do I run the ground to one of the ground rods?

To get [proper surge protection for your equipment](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md), everything must be grounded at a single point. Typically this is achieved by mounting a copper or aluminium sheet or bulkhead where the feedlines enter the building. Attached to this sheet are the lightning protection devices (gas discharge tubes, MOVs, etc), and then strap runs straight down from this panel into the ground system below.

The ground bus that I install in the shack should be bonded to which ground rod, and should use what size wire?

I wouldn't bother with RF grounding at the desk unless you have a single-wire feeder or [poorly designed antenna system](Using%20a%20balun%20with%20a%20resonant%20dipole.md). Without common-mode currents at the desk there's no reason for the ground. And the coax shields connecting all the equipment are already grounding the chassis. And unless your operating desk is very close to the entrance panel you can't make a low impedance RF ground anyway.

Here's my station ground almost completed as an example. This is where the feedlines enter the house: the desk is 15 feet away on the other side of the room. All the cables from the desk run to this bulkhead.

On the bulkhead are two gas tube surge arresters for feedlines (from Polyphaser), at electrical outlet with integrated MOV (Lutron), and a TVS diode protection device for the ethernet cable (Ubiquiti).

The braid will go to the ground rod just outside. That ground rod is connected with buried solid uninsulated 6 AWG wire to the electrical service entrance 40 feet away, with another rod every 10 feet along the way.

Not pictured is a larger 30 kA MOV in the main breaker panel on the other side of the house.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9526/antenna-input-and-ground-bonding, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
