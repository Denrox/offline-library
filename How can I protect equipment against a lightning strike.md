# How can I protect equipment against a lightning strike?

*Tags: safety, weather, equipment-protection, lightning · score 25*

## Question

A lot of aerials (almost by design) would be rather good attractors of lightning. What steps do I need to take in the field to keep my gear safe against a lightning strike?

I'm presuming the obvious already here (such as not operating in a storm), but are there any additional steps I should take?

## Accepted answer (score 21, by Phil Frost - W8II)

There's a lot that can be said about lightning protection, but it usually boils down to doing *all* of these things:

1. make good, low impedance connections to Earth
2. bond all Earth connections together with a low impedance path
3. have only a *single* point of entry to protected equipment

A real problem when discussing lightning protection is that people will consider only some of these things, and the result is sometimes worse than doing nothing.

#### make good, low impedance connections to Earth

Just about everyone understands this one. You want long rods in the ground, at least 8 feet. Multiple rods, if you can, about as far apart as they are deep. Lightning currents from a big direct strike can be in excess of 100,000 amperes, so you need *fat* conductors so they aren't vaporized by the current. Lighting is also an extremely fast pulse, which means it contains a lot of high-frequency energy, and you should think about it like RF current. Wide strapping is better than round conductors (skin effect) and you should make the path of your conductor as straight and short as possible to minimize resistance and inductance.

#### bond all Earth connections together with a low impedance path

This one is frequently neglected. The current from a strike is so huge that it won't simply all go into the closest grounding rod can find. The Earth itself isn't a low impedance conductor, so even when lightning strikes a point in an empty field, significant voltage gradients can be observed significant distances away from the strike point.

W8JI has a great example of this, where a tree was struck, and some 20 feet away, arced back out of the ground to travel through a Beverage antenna.

Consequently, if you have multiple connections to Earth, or even things *close* to Earth, lightning currents *will* find a way to those points, even if that means flowing through your station equipment, arcing across water pipes, HVAC ducting, or even through wood or concrete in your home, which aren't great insulators. Bonding all the grounds together with heavy wire gives the current an intentional place to go.

Most building and fire codes *require* that all grounds are bonded with very heavy wire or strap, for this reason.

#### have only a *single* point of entry to protected equipment

Perhaps the most neglected point of all. If there are multiple points of entry, that means lightning current can enter at one point, and exit at another. As discussed in the previous point, lightning currents are so huge that they make significant voltage gradients almost everywhere, including between the two points of entry to your station. Where there are voltage gradients, there are currents, and where there are currents, things break.

A very common situation in amateur stations is to have a grounding rod at the mast or tower, where the feedline enters the shack, or both. W8JI provides a great diagram of a **poor** grounding system:

(I highly recommend reading through the rest of W8JI's lightning and grounding information. Lots of diagrams, pictures, and good advice. On this topic: Ground systems, House ground layouts, and Second floor grounding.)

When lightning strikes the power lines, some of this current will go to ground through the additional ground(s) at the tower or shack entrance. After passing through your equipment and frying it, of course. Strikes on the tower cause the same problem, in the other direction. This is a situation where a naïve attempt at protection has made things worse, virtually *guaranteeing* equipment damage when a strike occurs. Even a nearby strike might introduce enough of a voltage between the grounds to cook your equipment.

Worse, in some setups, disconnecting the feedline leaves this extra ground (B) still connected, violating the popular "wisdom" that disconnecting the feedline in a storm protects your equipment!

So what can you do?

#### the ideal approach

Ground the base of your tower or mast with a large field of radials and a lot of ground rods, spaced over a wide area, bonded together with wide copper strap. Bond the shields of all coax feedlines to this. Should lightning strike the mast, this will provide a low impedance ground to take a big share of the current. It may also be useful to reduce ground losses if you want to use the mast as a radiator.

Inspect the ground where your electrical, CATV, and phone service enter the building and ensure it's in good shape and a sufficiently low impedance. Remember lightning can strike the utility lines, too. Again, you want this to be a low impedance ground so it takes a good part of the strike current, diminishing the load on the other components.

Surround your entire house in wide copper strap, with a hefty ground rod every eight feet or so. The copper strap effectively puts all the ground rods in parallel, lowering the ground impedance. The ring around the house also acts as a sort of 2-dimensional Faraday cage, reducing the electric potential difference between any two points on the ground within the ring.

Bond tower and house ground systems together with wide copper strap, so that any current caused by a voltage between them favors that strap over your feedlines. Make sure any utility grounds (electric, telco, etc) are also part of this system of grounds. This is often required by fire codes because it reduces the chances of an electrical arc between these two ground systems, which might be especially likely if there's a good conductor that goes most of the way but not quite all the way between the grounds, for example a disconnected feedline.

*Every* cable that enters your shack, including the mains wiring, any control lines up the tower for rotators and such, ethernet cables for a home network, *everything*, enters the shack through a big, fat copper plate that's connected with a wide, short, straight connection to the ground running around the house. Each of these cables go through protection devices such as gas discharge tubes or MOVs. Conductors that should be grounded (feedline shields, AC safety ground, etc) are bolted directly to the grounding panel. By making such a single point of entry, you ensure all the protected equipment stays at the same electric potential.

With a setup like this, you can confidently leave your feedlines connected in a storm, and survive direct strikes to the antennas. In fact, your house is probably *less* likely to be damaged by lighting than ordinary residential construction. A direct strike may cause some damage to exterior components, burning insulation or melting thin-gauge wires, but equipment inside is quite safe.

#### more modest approach

Most people will not want to invest the time or money to install a protection scheme that extensive. If you don't have a tall tower, or you live in an area where lightning is not frequent, it may be difficult to justify such expenditures.

In this case, it's better to think about what you *shouldn't* do. Don't create an extra ground. It's better to address [common-mode currents](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md) with [baluns](Using%20a%20balun%20with%20a%20resonant%20dipole.md) and proper antenna design. If you must have a ground (such as a vertical installed at ground level), then consider the ground part of the antenna, not the station, and be sure to disconnect it in storm conditions.

## Answer (score 6, by Kenneth Larsen)

QST magazine printed a comprehensive three part article in 2002 addressing lighting: *Lightning Protection for the Amateur Radio Station*. They are republished by the ARRL.

- QST June 2002, pp. 56-59
- QST July 2002, pp. 48-52
- QST August 2002, pp. 53-55

The *surest* way to protect your radio gear is to disconnect it from power, from the antenna, from your computer and even from ground. And even that is no guarantee -- a while back I had an **enormous** bolt of lightning strike my backyard. I had three transceivers; one rig was still connected to my computer and both the computer and rig were smoldering. The other two rigs were also fried despite being disconnected from power and antenna. My presumption is that the electromagnetic field from the lightning was powerful enough to destroy components in the rigs.

It's a hassle, but disconnect your rigs from power, antenna and computer.

## Answer (score 5, by Joseph)

Many companies make lightning surge protectors. the install in the coax to your radio and divert the strike to ground.

***NOTE:*** THERE IS NO SURE WAY TO PROTECT YOUR RADIO EXCEPT DISCONNECTING IT FROM POWER AND THE ANTENNA.

Search for polyphaser, they are well respected, MFJ also makes some lower cost options..

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/51/how-can-i-protect-equipment-against-a-lightning-strike, by berry120, Phil Frost - W8II, Kenneth Larsen, Joseph. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
