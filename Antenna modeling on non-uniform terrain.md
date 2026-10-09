# Antenna modeling on non-uniform terrain

*Tags: antenna, antenna-theory, hf, antenna-modeling · score 9*

## Question

I'm interested in modeling the radiation pattern of wire antennas for hf before I invest the resources necessary to erect the antenna. I'm familiar with tools such as 4nec2, but from what I can tell the ground is modeled as being flat.

However, at my house, the terrain is sloped at roughly 25 degrees. My intuition says that this will affect the radiation angles of radiation. How can I model antennas to include local terrain? Would a useful representation be rotating the antenna 25 degrees to account for the terrain? Does it really matter?

## Accepted answer (score 3, by Phil Frost - W8II)

Would a useful representation be rotating the antenna 25 degrees to account for the terrain?

I'd think so, as long as you also then rotate all the results 25 degrees in the opposite direction. I can't think of anything that actually wouldn't rotate with the ground (gravity, geomagnetic field, ...) that would have any significant effects.

Does it really matter?

No doubt the 25 degree slant will significantly affect many antenna designs. Not only will you have a hard time transmitting through a mountain, but the [ground will form an image antenna](What%20causes%20ground%20losses%20in%20a%20HF%20antenna%20system.md) as if it were a mirror, creating a phased array. Turning the mirror 25 degrees will make a big difference.

Of course, probably there's nothing you can do about it. Maybe you will feel better not knowing.

Besides, there are plenty of other things that can make a big difference. Modeling results can be very wrong if they don't include everything near the antenna: the tower, the feedline, your gutters, trees, etc. Ground conductivity can change with weather. Then, the ionosphere swirls around and messes the whole thing up. So, from a practical standpoint, modeling can only solve some of the problems involved with making a good antenna.

My personal approach would not bother with modeling. I have a trapped vertical that wasn't too expensive and covers enough bands that one of them is always open. If you have the space, a couple of parallel-fed simple dipoles would probably work as well for less cost. I put in plenty of radials to keep the ground losses low, and tuned it carefully. The idea is to focus on radiating, and not where I'm radiating. I wouldn't win any DX contests, but I have no difficulty making an international contact any day.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/477/antenna-modeling-on-non-uniform-terrain, by W5VO, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
