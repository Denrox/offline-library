# Using inner conductor of a coax feedline as an antenna

*Tags: antenna-theory, wire-antenna, coaxial-cable · score 3*

## Question

Can I use the inside conductor of coax to radiate RF energy?

My in-laws have some sort of attic antenna installed many years ago for broadcast reception, which I would love to temporarily co-opt for MW/HF reception, and/or QRP transmission on 40 meters. I'm assuming the antenna itself is designed for the VHF/UHF television bands, but there's a tantalizing amount of feedline leading up to it — at least relative to the weather conditions outside to operate a proper antenna.

If I'd like to use the feedline as an antenna, does it make much difference if I connect to the outer shield versus the inner conductor? Seems intuitively that the outer shield should work just fine as a long wire. But will the center conductor also serve just as well? In this case, does the outer "shield" still serve as such, or would it just sort of re-radiate the signal like a director element might? I am assuming there is no earth grounding on the far end of the coax, that it simply is connected to a VHF/UHF antenna in the attic.

I guess my question boils down to: if the outer braid of a coax is *not* grounded, does it still shield the inner conductor? Trying to answer this question myself, I can see it going both ways:

- yes, the shield always works as a Faraday cage around the wannabe "antenna" inside it
- no, when the center conductor near a section of braid has a lot of electrons it will repel the electrons on the inside of the shield so they migrate to the outside of the shield and then cause radiation from there

Bonus: what happens if I short the inner and outer conductors and then feed *that* as an antenna?

## Accepted answer (score 3, by Phil Frost - W8II)

if the outer braid of a coax is not grounded, does it still shield the inner conductor?

No.

Can I use the inside conductor of coax to radiate RF energy?

You can, but you might as well use the shield.

what happens if I short the inner and outer conductors and then feed that as an antenna?

Basically the same thing. The currents end up on the shield.

The purpose of the shield, in ordinary operation, is to assure that there are no electromagnetic fields outside the cable. All the energy being transferred in coax, in ordinary operation, exists in an electromagnetic field exclusively between the center conductor and the shield.

This works because usually the shield is grounded. If you wanted to launch a voltage step down a coax transmission line, you'd connect a voltage source to the shield and the center conductor:

At the instant the button (SW1) is pressed, the voltage source (V1) will pump electric charge into the center conductor and out of the shield. It will pump however much charge is necessary to maintain a difference in electric potential of 1V.

Since the voltage source can neither create nor destroy electric charge, the charge removed from the shield must exactly equal the charge put into the center conductor. *Current* is amount of charge moved per second, so this means the center conductor and shield have *equal but opposite currents*. The shield current, and the center conductor current each have an associated magnetic field. But because they are equal but opposite, for any position outside the cable, they cancel. (The same is true for the electric field).

If you wanted to connect the voltage source to just the center conductor, you are left with the question of where the other end of the voltage source connects. Probably you will use Earth. So you end up with this:

At the instant you press the switch, V1 begins pumping charge out of Earth, and into the center conductor. The current on the center conductor is now positive and increasing. That current is accompanied with a concentric magnetic field which is growing, and that growing concentric magnetic field will reach the shield.

When it does, eddy currents will be induced in the shield. These eddy currents will cancel the current in the center conductor and reinforce the current on the shield, especially on the outer surface of the shield. This is known as skin effect.

This only happens at the instant the switch is pressed. Eventually V1 moves enough charge to make its 1V difference and reaches a steady state. There are still currents and magnetic fields, but they aren't changing. Without a changing magnetic field, there are no eddy currents, so there's no skin effect so the current can flow on the center conductor. So, skin effect is relevant only for AC or RF currents.

So for radio applications, the current ends up on the shield anyway, and you end up making a field between Earth and the "shield", which isn't really shielding anything. Maybe if you want to use the feedline as an antenna this is good for you.

That's the theoretical explanation. There are also some practical concerns.

This feedline probably connects to some television receiver's enclosure, which is probably in turn connected to the safety ground on the electrical cord, which is in turn connected to a grounding rod at your electrical meter. So you will end up with this:

You can still make an antenna out of this: it's called a shunt fed antenna. But it's not how your typical long-wire antenna is set up.

Also, your home's wiring is directly connected to just about every noise source in your home. You may find that it does not make a very quiet antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5605/using-inner-conductor-of-a-coax-feedline-as-an-antenna, by natevw - AF7TB, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
