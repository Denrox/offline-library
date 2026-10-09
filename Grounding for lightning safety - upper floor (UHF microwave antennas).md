# Grounding for lightning safety - upper floor (UHF/microwave antennas)

*Tags: antenna, uhf, grounding, lightning · score 3*

## Question

I have some UHF, microwave antennas and an antenna rotator on a roof mounted mast. The "radio room" is in the second floor just below the antennas. Also the service entrance for building electricity comes up the outer wall and **enters the building in the second floor** near the cables for the roof mounted antennas. The location of the service entrance is quite different from most descriptions I find on the web, which makes me a bit confused about how to best connect things for best protection.

I do not want to propagate the coaxial cables for UHF and microwave all the way down to ground to protect them before propagating them up again because of cable loss. My thinking was that I should add a single point ground panel on the outside wall on the second floor, connect the mast and all antenna and rotator cables through it and ground the panel with a wide copper conductor all the way to ground. At ground level I connect it to a new grid of ground rods + the electricity safety ground rod. Since the service entrance for building electricity is very close to where the ground panel on the second floor will be, I was thinking to bind the ground wires together also at this point. This means there will be two ground conductors going on that outer wall quite close to each other all the way to ground - one thick new one, and the existing one from the electricity provider. They are connected to each other in both ends.

Are there any problems associated with having two down conductors for grounding close to each other - vertically like 7 meters? Should I ensure a maximum/minimum distance between the two? Is it correct to connect them together also in the top? I am mainly thinking in terms of lightning safety + and also not screw up the building electrical safety.

I hope someone with more experience can answer these questions.

## Accepted answer (score 4, by Phil Frost - W8II)

Your two ground conductors must be connected at both ends.

They must be connected at the bottom because that's where the ground is and they aren't ground conductors if they aren't connected there.

And they must be connected at the top because if they are not, you don't have a single point ground. Without a single point ground the potentials between the two ground conductors will be different, and the lightning protection will not be effective.

I would route them as closely together as possible. The idea is to minimize the area of the loop they create. A larger loop area means higher inductance, meaning more induced voltage due to changing magnetic fields, and higher voltages with changing current.

Remember the goal of a lightning protection scheme is to divert as much as possible of the strike current away from the protected equipment, and to ensure everything within the protected equipment stays at about the same voltage. If you haven't already, see [How can I protect equipment against a lightning strike?](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16650/grounding-for-lightning-safety-upper-floor-uhf-microwave-antennas, by rubund, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
