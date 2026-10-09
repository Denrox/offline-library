# How does a mag mount antenna achieve a ground plane?

*Tags: antenna, mobile, theory, antenna-theory · score 19*

## Question

I've been thinking for some time about magnet mount mobile antennas and wondering how they establish their ground plane. Consider that many mag mount antennas have some kind of protective coating on the magnet. Consider also that most cars have a coat of paint between the mag mount and the sheet metal. Both of these should result in some level of electrical isolation between the antenna feed shield and the sheet metal.

I guess what I'm simply not clear on is how a mag mount antenna's ground plane is connected electrically. Or is this accomplished through inductance?

## Accepted answer (score 27, by WPrecht)

There's *always* a ground. Whether it's what you intend it to be or not is another issue...

A mag-mount antenna is grounded through capacitive coupling between that magnet and the metal it's stuck to. At VHF/UHF frequencies, this effect is adequate for good results which explains the popularity of these mounts. Some folks advocate adding a wire instead of relying on the coupling effect, but in most cases, this has little or no effect.

At HF frequencies, it's a different story. The capacitive effect is not enough and thorough grounding of the vehicle is usually indicated. There are several good guides out on the internet, I suggest starting with K0BG's excellent site on the ins and outs of mobile amateur radio oeprating.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/754/how-does-a-mag-mount-antenna-achieve-a-ground-plane, by Peter KB1AVL, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
