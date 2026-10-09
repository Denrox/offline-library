# When a dipole antenna is fed via coax, what powers the ground-side of the dipole?

*Tags: antenna, dipole, coaxial-cable, feed-line, physics · score 5*

## Question

I've been trying to understand how dipole antennas work, and I believe I understand the basics when they're fed via a balanced feed line. In fact, every dipole physics YouTube video and web page I can find explains how they work with a balanced feed line as the example.

But how do they work with an unbalanced feed line, such as coax? In that case, the shield of the coax is connected to one half of the dipole. What's driving that half of the dipole?

This is a closely related question: Coax fed dipole: shield goes to one side, yet is grounded via chassis line to Earth

However, it never fully explains what's driving that grounded half of the dipole.

The best I've managed to surmise, is that perhaps the center conductor of the coax somehow affects the inner diameter of the shield of the coax in an equal and opposite manner, and THAT force is what drives the 2nd half of the dipole. But I'm not sure, and no one seems to discuss this directly in any resource I can find.

The other option I've considered is that perhaps the driven half of the dipole is influencing the non-driven half, due to its proximity to the EM field. In that case, the coax wouldn't really play a role other than giving the current somewhere to flow when that half of the antenna is influenced (but that seems wrong since that half should radiate that energy...).

So put simply: in a dipole antenna driven by coax feedline, what's powering the half of the dipole that's connected to ground? Where does that current come from?

Thank you!

## Answer (score 4, by Kevin Reid AG6YO)

But how do they work with an unbalanced feed line, such as coax? In that case, the shield of the coax is connected to one half of the dipole. What's driving that half of the dipole?

**The current in the shield is.** In the center conductor, current flows one direction, and in the shield, equal and opposite current flows. *This part* of the situation is exactly the same as if there was a balanced feed line.

Remember basic electric circuit principles: **current flows in loops.** This is still true in RF, except that sometimes the loops extend out into air (by radiation). Your feed line is a two-wire circuit, and so the current through the coax in one direction must equal the current through the coax in the other direction — *unless* there is “common-mode current”, in which case the feed line radiates and a portion of the return current loop is through other conductors connected by some path to the transmitter's ground. (But that situation can be analyzed as a *superposition* of the 'regular' current and the common-mode current.)

You may be thinking: "But the shield is grounded!" That doesn't stop current from flowing in it; it only affects the *voltage* of (the grounded point(s) on) the shield. Just like our ordinary circuit grounds, that we say are more-or-less "0 volts": there are return currents flowing in the "ground" conductor. Suppose my "transmitter" is a battery instead: I can attach the negative terminal to the coax shield (and optionally to the earth), and the positive terminal to the center conductor, and put some DC load in place of the antenna, and I'm transferring power through the cable. **This works the same whether you're looking at DC or RF;** the only thing RF adds is the complication of ensuring that the RF won't radiate away except for where we want it to (the antenna).

## Answer (score 2, by Phil Frost - W8II)

Good question! Properly operating, the coax shield is at ground potential. But a dipole needs both sides driven, ideally with voltages symmetrical around ground potential. So how can this work?

The first thing to realize is while the coax shield is at ground potential, it does not have zero current. Rather, the shield is at ground potential because it has equal in magnitude but opposite in direction currents to the center conductor. These opposite currents are associated with electromagnetic fields which cancel, resulting in no electromagnetic fields outside the shield. In other words, the shield is at ground potential if and only if there is zero common-mode current in the coax.

So what's required is something that will allow this shield current to pass through to the dipole, while allowing the potential at the shield and at the shield-fed side of the dipole to be different. So there must be something in the circuit across which this voltage can appear.

[That's the balun's job](Using%20a%20balun%20with%20a%20resonant%20dipole.md).

## Answer (score 2, by hotpaw2)

There is no "ground side" of an antenna or feed line at radio frequencies.

A wire of any dimension longer than a fraction of a wavelength in an RF field can have very different voltages at one end than at the other end (or somewhere in the middle). Thus, it's nearly impossible to absolutely "ground" the entire length of any wire or feed line of finite dimension, if any RF signal or RF field is present. And if there’s a voltage differential and the impedance is finite, then current will flow along that path.

Furthermore, an antenna in free space only cares about the voltage potential difference between the 2 sides of a feed point. Both can be positive, both can be negative, one or the other can be grounded (with respect to Earth). But as long as there is a changing potential difference between the two, charge can flow, and accelerating charges can radiate RF waves.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18369/when-a-dipole-antenna-is-fed-via-coax-what-powers-the-ground-side-of-the-dipol, by Asker2093022, Kevin Reid AG6YO, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
