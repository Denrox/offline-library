# When is RF grounding necessary, and when is it not?

*Tags: grounding, installation · score 14*

## Question

I've seen many installations, particularly at field day and also in second-floor installations, where RF grounding is ignored entirely. What are the drawbacks to this and when is it absolutely essential to have RF grounding?

## Accepted answer (score 4, by K7PEH)

I think there might be confusion between RF ground, counterpoise, and electrical safety grounding. I am going to restrict my answer to RF ground (but, the word counterpoise is often used for the same thing).

In a perfectly balanced antenna, such as a Dipole at its resonant frequency, there is no need for an RF ground since no current would flow to the RF ground (like I said, in a perfect balanced antenna).

In a perfectly unbalanced antenna, such as a 1/4-wave vertical, an RF ground (aka counterpoise) is absolutely necessary to "complete" the antenna and make it whole. As they say, the ground image of your quarter wave antenna is the "other half" of the antenna and current will flow in this ground.

This is why a quarter wave antenna needs some sort of RF ground counterpoise made of conductors to make this current flow less lossy. Just relying on the ground itself results in a very lossy other half of your vertical and thus definitely not as efficient. In general, the more you can make the ground a good conductor (more radials, etc.) then the more efficient your antenna will be.

Given these two extremes, the need for an RF ground depends on all kinds of situations where the actual individual antenna geometry, height above ground, other nearby conductors, and so on come into play.

If your dipole antenna is not balanced for example, then common-mode current will flow down your feed line and radiate or enter into your shack and cause other problems. Making sure that your equipment is well grounded may help eliminate some of this RFI but it is best to eliminate the common-mode currents using an RF choke at the antenna feed point.

In summary, for good balanced antennas such as dipoles, Yagis, and similar geometries, RF grounding should not be necessary. If you have an unbalanced antenna like a vertical or a single long-wire antenna, or an inverted-L, or similar then a ground plane (RF ground) is required for efficient operating.

## Answer (score 4, by Andrew Beals)

Two drawbacks to ignoring your grounding:

1. You will have a poor(er) signal.
2. ***You*** could become the ground and experience an RF burn first-hand.

That said, VHF antennas are often not grounded - handhelds and VHF radios in cars, for example.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/34/when-is-rf-grounding-necessary-and-when-is-it-not, by Bill - K5WL, K7PEH, Andrew Beals. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
