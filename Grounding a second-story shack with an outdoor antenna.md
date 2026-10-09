# Grounding a second-story shack with an outdoor antenna

*Tags: grounding · score 12*

## Question

My shack is on a second story, really far away from the house ground. To run a ground from my equipment to the outside/ground is a run of at least 60-75 feet. The antenna is at least 100 feet away as well.

How do I ground this system? I cannot reach the house ground. I can ground the antenna at its base; can I run a ground from the shack to the outside to a rod? Do I tie all my equipment to one point and bring this ground wire to the outside? What wire should I use?

## Answer (score 8, by Phil Frost - W8II)

How do I ground this system?

Don't. You can't, anyway. Whatever connection you make will be long enough that it will be more of an antenna than a ground. But don't worry, you don't really need a ground anyway.

Why would you need a ground? One reason is lightning protection, but that's probably not what you hand in mind, and it's more complicated than running some wires to some dirt. You should [read more about it in a separate question](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md).

The other reason is to give common-mode currents some place to go. Due to the law of charge conservation, any common-mode current must be accompanied an opposite current somewhere else in the universe, and usually that thing is the Earth. By grounding the feedline somewhere, you short out these currents.

But it's really better if you just have no common-mode currents in the first place. Anywhere there's common-mode current on your feedline, it's radiating. And by reciprocity, that means it's also receiving. In effect, it's part of the antenna, and usually that's not what you expect.

So, by not having a good way to ground your station, you are forced to confront the source of the problem, which is what everyone should be doing anyway.

Put [baluns on your antennas if they need them](Using%20a%20balun%20with%20a%20resonant%20dipole.md). With a properly current-balanced antenna, you won't have any significant common-mode currents due to your transmissions, so you won't have any problems with RF in the shack.

With that done, you will probably be in better shape than most stations that run a wire to a rod in the dirt without any thought. For further reading, I suggest W8JI's article on station grounding.

## Answer (score 5, by user4148)

The misconception about grounding is widespread. In the real world outside of hobbies, grounding is an art depending on each situation and location.

I have no grounds running down my 3rd floor condo, but I do have solid point-to-point grounding systems for two consoles of radio and computer gear.

Do not depend on your house power wiring grounding pin/points as they are often loosely connected, corroded or simply not on the same common grounding points.

Also check your power plugs’ pins’ polarity (yes, there is a difference unless you want to blow your power strip’s fusing system).

I run grounding straps to a common grounding node: a length of metal braided wire and a terminal block cheaply purchased from a hardware store. That has done the trick up to power levels of 600-1.2 kW.

Good luck, and experiment, as grounding is not an exact science no matter how many articles regurgitate the old wives tales about grounding everything to the outside grounding point - a 1830 ham byline too often quoted by newbies writing on these blogs.

## Answer (score 4, by Cecil - W5DXP)

Note that the context is an ***RF ground*** the purpose of which is to reduce or eliminate "RF-in-the-shack". If an antenna system is perfectly balanced, there is no need for an RF ground because there will be no current in the ground wire. Moral: Avoid unbalanced antenna systems (OCFs and EFs) if one's shack is on the second story. (Please note that a vertical with radials has balanced voltages AND currents if the feedpoint impedance of the antenna and the feedpoint impedance of the radials are equal, i.e. "balanced" can have two different meanings.)

"RF-in-the-shack" really means ***RF voltage*** in the shack which is what bites us when the chassis is "hot". We can have high RF current in the shack and not even realize it. The purpose of a 1/4WL wire connected to the transmitter chassis is to move the voltage maximum point from the transmitter chassis out to the end of the 1/4WL of wire. There is just as much RF energy in the shack as before but we have forced it into the magnetic field (current) on the transmitter chassis rather than existing in the electric field (voltage). But that 1/4WL of wire will radiate just like 1/4WL of a 1/2WL dipole antenna (and may be physically too close to the operator). The energy in the forward and reflected waves on that 1/4WL wire does NOT cancel. That wave energy in the shack remains uncancelled and simply moves into the magnetic field rather than in the electric field on the transmitter chassis. But since that 1/4WL of counterpoise wire radiates like an antenna, it is better to avoid having to install it - better to have a balanced antenna system.

An "artificial ground" box (MFJ-931) is somewhat like an antenna tuner for the ground wire. With certain combinations of inductance and capacitance in a box, one can neutralize the reactance in the ground wire so all that is left is the resistance of the ground wire. Note that this is the RF resistance, not the DC resistance. If one has an artificial ground box and the wire to ground is 1/4WL, neutralizing the reactance will not help as the RF resistance is sky high. If a ground wire is run from the second story to earth ground, it needs to be a multiple of 1/2WL but like the 1/4WL counterpoise, it will radiate just like an antenna element. Better to have a balanced antenna system.

Note: This posting does not address lightning protection or safety grounding.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3523/grounding-a-second-story-shack-with-an-outdoor-antenna, by Jay, Phil Frost - W8II, user4148, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
