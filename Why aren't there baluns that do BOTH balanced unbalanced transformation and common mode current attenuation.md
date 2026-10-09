# Why aren't there baluns that do BOTH balanced/unbalanced transformation and common mode current attenuation?

*Tags: balun · score 7*

## Question

I have read myself blue, about baluns. Especially 1:1 ones.

Some claim they're only there to balance the unbalanced signal, and that's what's in the name also, but I find several that claims that the main thing at the point of a balun is common mode current attenuation.

And from where I stand I agree with both, because both are logical.

So, when I Google around for baluns I find recipes for ones that do one or the other, never any that do both. Why?

## Accepted answer (score 6, by Hamsterdave)

There are. I suspect you're confusing a couple of different things when it comes to balance.

Common mode current is current which appears to flow on both conductors in the feed line with the same polarity and magnitude. If you put RF in to an ideal coax and from an ideal source, the current on the center conductor is precisely equal in magnitude and opposite in phase to the current flowing on the *inside* of the coax shield. No current should flow on the exterior of the coax shield at all, and the fields of the current on the two conductors on the inside of the coax cancel, resulting in zero radiation.

Any current that does flow on the exterior of the coax shield has no opposing current, as there's no closely coupled conductor for it to induce that opposite current on as there is for the center conductor and the inside of the shield. There is no counteracting field to cancel it, so it can radiate freely. In the case of a received signal and an ungrounded radio, you can imagine that this unopposed signal would cause the entire radio to "float" at the common mode voltage, essentially the signal would enter the receiver through the ground plane of the radio's circuits. This makes it very difficult to filter once it reaches the radio.

In the case of a transmitted signal, the exterior of the coax shield appears to be a radiating element or a ground radial, depending on the exact nature of the installation. This is most often the cause of "RF in the shack". The exterior of the coax is radiating in very close proximity to sensitive electronics.

Common mode on balanced line is just the same. It is some voltage that appears to travel on both conductors equally, not opposite in phase as it should be, and the same problems arise.

Common mode can arise either because of a difference in magnitude between the two conductors in a feed line, or difference in phase between the two. Let's consider an example:

If you have a symmetrical dipole with perfect balance, fed with ladder line, we know that the voltage on one feed line conductor will be precisely equal in magnitude and opposite in phase to the other. If we were to measure voltage on a single conductor relative to ground at an arbitrary instant in time and point on the ladder line and saw a potential of +100 volts, we would expect to check the spot on the other conductor at the same point in time and place on the ladder line and see -100 volts. Measured relative to each other, the voltage would be 200 volts peak to peak.

Now let's pass our ladder line by a big chunk of grounded metal, but let's say that one of the ladder line conductors was much closer to that metal than the other. More power would be coupled out of the conductor that came closer to the metal than the one that was further away. If we measured voltage at some point between the radio and that grounded metal, perhaps now we would see only +75 volts relative to ground on the one that came close to the metal, and still -100 volts on the conductor that was further away. We now have a common mode voltage of -25 volts between the conductors. The field of the wire with lower voltage doesn't have a strong enough field to cancel the entire field from the other conductor, so there is now "excess" field, the feed line can radiate, and if the radio is not well grounded, it will appear to float at -25 volts. This is how RF burns from microphones happen.

Ok, so now we've got a good picture of common mode and what it is. What do baluns do about it?

There are two basic forms of balun, and it is important not to confuse them: Chokes, and transformers.

Transformers are less common. They work through magnetic coupling and generally have **isolated windings**. This means there are separate primary and secondary windings, and no direct path for DC between the two. Any transfer of current between them is via coupling, usually through a core of some kind. Transformers are good for very high efficiency impedance transformation because the cores are very low loss at the frequency you're using, and they're usually designed to resonate at a given frequency. When the differential mode and common mode current meet in the primary, they are essentially added together, resulting in a wave that is once again "clean" and balanced, but with the magnitude of the wave altered by the constructive and destructive interference of the two signals being combined. This is what is meant when it is said that balance is "forced".

When properly designed and installed, **they do provide common mode suppression**, but at a price. They are generally narrow banded, working best on only a couple of bands. Outside of their resonant window, there is substantial reactance that will make them inefficient and cause SWR issues. They also tend to be more expensive, as the low loss core material is more expensive to make, and it must be physically large because it will carry 100% of the total current between the windings.

You can make them wide banded, but only by sacrificing the common mode suppression, as you won't have isolated windings. These are often called "ununs" though that's a terrible term IMO because it implies that it still does...something...with regards to choking or the like. They are, in fact, only impedance transformers (Put a good choke on your EARCHI at the feed point with no radials and it won't tune at all).

The second kind of balun, a choke, is much more common and provides both balance and excellent common mode attenuation over a wide frequency range. The trade off is efficiency.

Choke baluns work by inducing the current of both conductors on to a single core at the same time. We know that the current is equal and opposite ideally, so if they are wrapped around a toroid side by side, in the same direction, the field they induce on the toroid will also be equal and opposite. This means it will cancel and there will be no net magnetic field in the core. This means that if the system is perfectly balanced, zero current will flow in the toroid.

When the system is unbalanced, the field of one conductor "wins", and induces some current on the toroid. This current then has to travel through the toroid between the two conductors. If we use very lossy core material, this current will be turned to heat and disappear from the feed line. Since that induced field is equal to the difference in field strength between the two windings, the signal will once again be balanced when it leaves the balun, though at a loss equal to the ratio of common mode current to differntial mode.

The problem with chokes is that heat. If the system is badly unbalanced, considerable heat can be generated by the toroid, and because they aren't particularly efficient shapes or materials for radiating that heat, it can accumulate to a problematic level with only 15 or 20 watts of common mode loss in a large toroid. You can get around this by using several toroids and fewer turns around them, spreading the power dissipation between several toroids, but this gets big, heavy, and potentially pretty expensive.

By using a combination of series and parallel 1:1 chokes, you can accomplish impedance transformation efficiently (assuming reasonable balance in the first place). The fact that they are non-resonant and actually utilize loss rather than avoiding it to the greatest degree possible makes them very wide banded.

**TL;DR** There is no effective difference between attaining balance and eliminating common mode, but there are two different ways to accomplish balance that are easily described as "transformers" and "chokes".

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6473/why-aren-t-there-baluns-that-do-both-balanced-unbalanced-transformation-and-co, by Hans Neve, Hamsterdave. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
