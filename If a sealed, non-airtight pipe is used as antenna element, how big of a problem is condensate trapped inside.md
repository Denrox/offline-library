# If a sealed, non-airtight pipe is used as antenna element, how big of a problem is condensate trapped inside?

*Tags: antenna-construction · score 3*

## Question

I'm building a vertical antenna. The lowest portion of its element consists of 3/4" type M copper pipe, with end caps that will be soldered on and 3/8-24 screws poking through at both ends (so the bottom can screw into a 3/8-24 mobile mount, and the top can attach to Hustler mobile resonators like the RM-30 and RM-40).

So far, so good... mechanically and electrically, it's decent (I wouldn't want to depend upon a single 3/8-24 screw to secure the entire lever force of an 8-10 foot antenna, but I'll have a second strap a few inches higher to secure it against swaying and lever force, so the lower screw's main purpose is to provide electrical contact with the RF signal, support its vertical weight, and keep it from drifting horizontally). However...

I'm a Floridian, and I know from years of hard firsthand experience that any outdoor cavity that isn't airtight *inevitably* ends up with water trapped inside. Why? Humid air gets inside, condenses when it eventually gets "cold"(-ish), and the same seal that keeps rainwater out eventually drowns the very circuit it's naively meant to protect.

Is this an actual problem with antenna elements that have non-airtight cavities inside? Or is trapped water inside a hollow antenna element not actually a problem (because RF runs along the surface, or condensate is deionized & basically an insulator, etc)?

If it IS a problem, how big of a hole do I need to put at the bottom for water to drain out, keeping in mind that the copper end caps aren't very thick to begin with, and any hole I drill is going to have a negative impact on what little structural strength it *has*.

Putting the various dimensions into perspective, 3/4" type M copper pipe has an inside dimension of .8125". A 3/8" screw is 0.375". That means a perfectly-centered screw hole has at most .21875" of copper between the center hole and inside surface of the pipe.


A 2mm hole is approximately .08" wide (2mm x 1 inch/25.4mm), or approximately 1/3 of the area. Probably ok, though, if it's drilled near the edge of the area.


At 0.25", 1/4" hole would literally be wider than the distance between the 3/8" screw and pipe wall. A 1/4" hole would HAVE to be drilled through the side, instead (i.e., perpendicular to the 3/8-24 screw... through the 3/4" pipe itself and side of the end cap).

## Accepted answer (score 2, by user10489)

Trapped vapor inside the element isn't a problem.

The problem is that with repeated heating and cooling cycles, a sealed cavity will develop pinhole leaks. If you don't make your own hole, it will form somewhere random. If it is on a top surface, then when the cavity heats, air escapes, and when it cools, it will suck in vapor, which will then condense and drop to the bottom, and this repeats until the cavity is mostly water.

If instead you make the hole on the bottom, then when the cavity heats, it will push out any condensed liquid, so hopefully it doesn't get a chance to accumulate.

If this was coax rather than an antenna element, ideally, the unsealed end would be in an air conditioned (humidity depleted) environment so that when it cooled, it would suck in drier air.

The hole doesn't have to be very large. Just large enough that if it clogs, it will still be weaker than any other pinhole and liquid can still be pushed out of it during the heating cycle. Clearing it periodically could help.

## Answer (score 3, by Brian K1LI)

Welcome to ham SE. I recommend that you add a weep hole to the bottom of your trap. If structurally possible, a second weep hole might allow at least a small amount of air circulation in the cavity. Just as important is to periodically inspect the weep hole to be sure it's open. If you make a second weep hole, periodically blowing pressurized air into one weep hole will help to drive water vapor out the other weep hole.

I have rebuilt numerous units of a particular aluminum multiband trapped yagi antenna that begs the question you asked. My local environment experiences extremes of weather from +35$^o$C to -40$^o$C, heavy rain/snow/ice, high humidity and sometimes drought conditions.

I have always left open the small weep hole that the manufacturer drilled into the trap body and ensured the hole faced the ground when the antenna was mounted. I have never had a problem with this approach; I removed, inspected and sold one of the antennas after 9 years. Some users of this antenna have complained that insects enter the trap through the weep hole and either wreak havoc or plug the weep hole. Installing find-mesh screen kept out the bugs but the small mesh retained moisture, defeating the purpose of the weep hole.

A nearby friend, who shares a penchant for the same antenna, decided to seal the traps with layers of conformable rubber tape and adhesive "goop." He experienced trap failures within two years owing to moisture that bypassed his sealing regimen and created a layer of corrosion that was sufficiently conductive to arc over.

## Answer (score 2, by Andrew)

Despite the intuitive feeling that water somehow might make a metal tube more conductive or something, for an antenna made from hollow mostly sealed tubular metal, regardless of which metal the tube is made from, water inside the tube will in fact make zero difference to the way the antenna performs in an RF sense electrically for receive or transmit.

This is due to a phenomenon call Skin Effect, where RF current mostly always only travels on the outer surface of a conductor. For example when used for transmitting, RF applied at the base of your vertical antenna will only flow on the outside of the tube. Signals received from the atmosphere also will only flow on the outside of the tube.

In both case there will be extremely little or no RF current flowing inside the tube, and so the water doesn't do anything,

Of course there are mechanical considerations. Water adds weight at the rate of 1 kg per litre ! Added weight might result in bent or broken elements. Also, water inside a tube might cause corrosion or rust depending on the metal used.

And of course if you live in a cold area, frozen water which expands might cause a sealed tube to distort or burst, or the ends you soldered on might pop off.

In contrast, an additional consideration is that a tube filled with water might make less noise in the wind, but generally it's probably a bad idea for water to be present inside the elements of an antenna.

My suggestion is to use metal that doesn't rust much ie copper or aluminium and try and leave the ends open and not make the antenna elements sealed, or in your case at least leave the bottom end open, then water can't fill it up. If you do this, RF current still mostly flows on the outside of the tube.

If you must have ends on your elements, for mounting reasons or if it just makes you feel better, to drain any water which accumulates, you could drill a small hole about 2 mm in diameter right at the bottom of the element if it's vertically positioned. If the hole is at one of the ends, then it won't make much difference to the strength of the element. The hole will make zero difference to how antenna works electrically, but if the hole freezes over then you no longer have a hole and the antenna element will be sealed again.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18088/if-a-sealed-non-airtight-pipe-is-used-as-antenna-element-how-big-of-a-problem-, by Bitbang3r, user10489, Brian K1LI, Andrew. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
