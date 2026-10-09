# TV strong station has no signal when coax is connected

*Tags: antenna, uhf, antenna-system · score 5*

## Question

Right, not directly ham radio related, but this puzzles my ham brain. I have several TVs connected to a distribution amp connected to an outside antenna. All but one work fine, and the one won't pull in the strong stations, but does fine with the weaker ones. If I unscrew the F so that only the center conductor touches, it gets the strong stations as well. I've been trying to come up with an explanation, but have failed so far. I tried disconnecting all the other TVs (thinking it's a ground loop or something) with no success. What would cause that and how would I fix it?

## Accepted answer (score 3, by Duston)

Problem resolved. I put a splitter in before the amp and put the problem TV on one output and the input of the amp on the other. Now all TVs have all the appropriate channels. I could probably have accomplished the same with an attenuator on the TV itself, but I don't have one so I went with the no-cost solution.

## Answer (score 5, by Kevin Reid AG6YO)

I'm not at all sure about the exact situation, but I predict that you will find that the cable between the distribution amplifier and this particular TV set is damaged.

In general, when you omit the shield connection to a coaxial cable, it starts operating more like an unshielded single wire — a monopole antenna, if the other end is disconnected. For example, if you have a piece of coaxial cable that is not connected on either end, and connect it to a receiver (using a F, RCA, or "UHF" connector, or other type with a protruding center pin), it will function as an antenna until the shield makes contact and then it will be silent.

If your cable works better without the shield connection, that strongly suggests that there is damage which means that it cannot function as a proper coaxial cable but can function as "a piece of wire", and the TV signal works in that case because of some combination of direct capacitive coupling and antenna behavior.

## Answer (score 5, by AG5CI)

You may be overloading the front end of the "faulty" TV, creating adjacent channel interference or some other kind of distortion. The loss you introduce by only loosely coupling the receiver may be bringing down the signal level to a point where it is no longer impairing the receiver. The fact that a distribution amp is inline with your television probably plays a role in your problem.

I used to work for a company that supplied tuners for digital televisions and I have worked personally with TV manufacturers in Japan, Korea, China, and the U.S. I can tell you that there is huge variation in the quality of DTV front ends. The performance standards that TV sets need to meet in the U.S. are minimal.

There is a standard for receiver performance called A/74, but compliance is not mandatory for TV sets. Compliance was mandatory for the so-called "coupon" converter boxes, but testing at my company's lab identified major manufacturers who weren't complying, including LG and a company that manufactures for Walmart. We met with the FCC, several Congressmen, and a Senator to raise the issue. Everyone was polite, but no one did anything - even though tax-payer dollars were subsidizing non-compliant boxes. So if that was the industry response to a standard that *was* mandatory, you can imagine the response to one that isn't.

Even if the set meets or exceeds all ATSC performance standards, it still is no guarantee that there wouldn't be a problem. It's possible that all of the sets meet A/74, but the problem set doesn't have as much margin. There is a really good overview of interference mechanisms at work for ATSC here. The author (Charlie Rhodes), who is very well respected in the industry, makes the case that even if standards are adhered to, they may not be adequate.

Some distribution amps have a variable gain setting. If you have it set to the max (or even if not), you might try backing the gain down a little and seeing if that improves the situation without losing the signal on your other sets.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9611/tv-strong-station-has-no-signal-when-coax-is-connected, by Duston, Kevin Reid AG6YO, AG5CI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
