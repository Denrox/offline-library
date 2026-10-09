# Adequate lightning protection for sloped dipole or G5RV?

*Tags: antenna, equipment-protection, lightning · score 3*

## Question

Has anyone had experience, or knows from first principles, whether installing a G5RV or dipole BELOW a "lightning-rod" in such a manner would serve as a means of discouraging direct lightning strikes onto your dipole:


A "lightning rod" is some distance above the highest point of the G5RV, and has a ground wire that avoids coming near to the dipole.


Such that the "lightning rod" is connected to a ground wire which goes directly to its own ground-rod which has been attached to its own dedicated ground-spike.


With some hope that lightning, should it strike above your QTH, would hit the "rod" above the G5RV and most of the current would travel down the ground wire.


The lightning rod is about 5 feet above the dipole, and is supported from below by fiberglass pole.


There are no other antenna towers or tall metal objects within 100 feet of the above.


The antenna wire and antenna coax do not come within 4 feet of the ground wire, the air gap is intended to discourage lightning jumping from the lightning rod to the antenna. The ground wire is installed with a sloping section to avoid coming near to the G5RV or dipole.

Is the above a reasonable thing? Is it worth doing? Assume that the G5RV or dipole has a lightning arrestor attached to its coax feed line in the usual manner, and that this "lightning rod" is a secondary protective feature.

Here's a sample scenario for the sake of criticism/critique:

## Accepted answer (score 3, by Phil Frost - W8II)

I suspect this scheme will do little or nothing to decrease the chance of damage to your equipment in the case of a lighting strike.

For the sake of argument, let's just presume that it does work as you expect: lighting always strikes the rod, which has a dedicated conductor to a dedicated ground rod, and all of that is sufficiently isolated from everything else that no arcing occurs. Your situation is something like this:

We've made a bunch of assumptions but you still have a problem. Lighting happens when the charge imbalance between Earth and a cloud becomes so great that the voltage difference is enough to ionize the air and establish a conductive channel. Electric charge then travels over this channel to equalize the charge imbalance. That electric charge doesn't just need to get to the ground: it needs to spread out over the whole Earth. If it didn't, then there would be a spot on the ground where the lighting struck that would have a severe excess or lack of charged particles. It's like dumping a huge bucket into a pool: the water spreads out over the entire pool to minimize the gravitational potential of the water.

Now, Earth is anything but a great electrical conductor. That's why we need radials for ground plane antennas if we don't want them to be lossy. The impedance of the Earth between your connections to ground is represented by R2, R3, and R4.

Now, you have many kiloamperes of current flowing through an Earth that is a little bit resistive. Do you see the problem? Do you think most of that electric charge will go through R3, or your radio?

So, one important aspect of effective lighting protection: have exactly *one* ground. You can have multiple ground rods, but you should tie them together with a low impedance path, but any equipment you want to protect should have exactly *one* connection to this system of grounds. Remember to consider non-obvious paths through your electrical outlet, feedline, Ethernet cable, etc.

Also, those assumptions we made are probably not good ones. Having a lighting rod up high reduces, but does not eliminate the odds of a strike on things below it, and it's very likely lighting will arc to anything and everything even many feet away from your lighting rod system.

I suggest you check out [How can I protect equipment against a lightning strike?](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md) for other important aspects of effective lightning protection.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2027/adequate-lightning-protection-for-sloped-dipole-or-g5rv, by Warren  VA7WPX, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
