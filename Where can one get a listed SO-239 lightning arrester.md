# Where can one get a "listed" SO-239 lightning arrester?

*Tags: antenna-system, grounding, lightning, equipment-protection, pl259-so239-connector · score 6*

## Question

According to this summary of NEC requirements for radio antenna grounding (from 2014, but hopefully still somewhat accurate):

https://www.mikeholt.com/files/PDF/Radio_and_Television_2014NEC.pdf

It says "Antenna lead-in surge protectors must be listed". As far as I can tell, there are no "listed" SO-239 lightning arresters available on the market.

I even contacted Alpha Delta to ask if theirs were listed, and they said they used to be, but no longer are because their customers did not require it, and the certification was expensive. I looked at other brands online, and none claim to be listed.

*In order to be compliant with NEC requirements, where can an amateur radio operator get listed SO-239 lightning arresters?* Thanks.

## Accepted answer (score 6, by Phil Frost - W8II)

The NEC defines "listed" as:

Listed. Equipment, materials, or services included in a list published by an organization that is acceptable to the authority having jurisdiction and concerned with evaluation of products or services, that maintains periodic inspection of production of listed equipment or materials or periodic evaluation of services, and whose listing states that either the equipment, material, or services meets identified standards or has been tested and found suitable for a specified purpose.

[source]

So, it's up to the authority having jurisdiction (AHJ, often your city or county) to decide what organization's lists are acceptable. Certainly manufacturers like Alpha Delta and Polyphaser test their own products. There's no way to know for sure if your AHJ finds this "acceptable" without calling them. But if a major manufacturer like Polyphaser doesn't offer many products listed by a nationally recognized testing laboratory, that's a pretty good indication there aren't many jurisdictions requiring that level of testing.

## Answer (score 4, by Kevin Reid AG6YO)

If the problem is only that “SO-239 connectors” and “listed” can't be found together but *can* be found separately, then you should consider using a different connector — SO-239/PL-259/“UHF” is an old design that remains in use by amateurs, but doesn't have much of a market outside that. Notably, the N connector is the same physical size (even using the same thread!), has less of an impedance discontinuity, and is more weather-resistant due to having a gasket between the connectors.

Adapters are readily available, as are cables with N on one end and PL-259 on the other, and in some cases it's even feasible to modify equipment to replace a SO-239 with a N connector while using the same chassis holes for the connector flange so the modification is completely nondestructive.

I haven't checked whether listed N lightning arresters are available, but my point in more generality is: if there is listed equipment with *any* connector (of suitable impedance and power rating) then you can adapt to it; SO-239 is not mandatory even if your equipment uses SO-239.

If you can't find listed lightning arresters of any form, then it seems that you and, arguably, your AHJ have a bigger problem.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18856/where-can-one-get-a-listed-so-239-lightning-arrester, by User5754448, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
