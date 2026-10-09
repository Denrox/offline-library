# Grounding a chimney mounted antenna

*Tags: grounding, lightning · score 3*

## Question

I'm installing a new antenna mast to hold one or more antennas. The new mast will be strapped on to a chimney near the center of my house. Coax will run down the mast, across the roof, down the side, and enter the house within inches of ground level.

A collection of several ground rods spaced several feet apart (and tied together) is already installed near where the coax enters the house, with one rod being less than a foot from the entry point. The coax will run through a lightning arrester (specifically https://www.dxengineering.com/parts/DMN-SP3000W) at the ground rods.

Since the mast itself will have no ground connection (except what a brick chimney provides), the coax should be the most likely path to ground. Is the lightning arrester sufficient for lightning/static discharge, or should I run a separate grounding wire from the mast down to the ground?

If it's relevant, station ground will come to a single point in the shack and then be a thick copper cable wire back out to the same ground rod system.

## Accepted answer (score 4, by tomnexus)

You should definitely ground the antenna to your earth system with a heavy conductor. The coax alone will not cope well with the lightning current. By carrying a share of the current, the earth wire also reduce the voltage transferred to the coaxial cable inner conductor, and hence the load on the lightning protection device.

Better would be a metal cable tray, continuously bonded, carrying the coax and earth cable, and connected to the antenna and earth system.

Grounding your shack at a single point sounds good. The lightning protection device is great.

Note that the LPD does only two things - it provides a solid ground point for the coax shield, and it prevents large differential voltage in the coax. It doesn't scare away lightning, and only makes a difference if it's part of a well designed grounding system.

Remember that *all* cables entering the shack must be protected - coax you have taken care of, what about power? It should also go through a lightning arrestor at the single earth point. Otherwise a strike on a nearby utility pole could lift the mains up by a few thousand volts, which will travel through your shack to get to your nice earth.

## Answer (score 2, by W2ASC)

One definitive answer comes from the National Electric Code Section 810, which requires that both the coax ***and*** the mast itself be grounded. However, in my experience, the vast majority of people do not bother.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14710/grounding-a-chimney-mounted-antenna, by Adam KC0DAD, tomnexus, W2ASC. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
