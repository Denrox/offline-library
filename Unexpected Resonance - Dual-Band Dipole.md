# Unexpected Resonance - Dual-Band Dipole

*Tags: antenna, antenna-construction, impedance · score 3*

## Question

I tried to make a dual-band (2m/70cm) dipole this morning by following the instructions on this page: http://www.amateurradio.bz/2m-70cm_vertical_dipole_antenna.html, with the rather major significant exception of placing the antenna's elements in a groove I routed out of a 2x4 and I'm using bare #10 copper wire instead of stainless steel.

I plugged a VNA into it and the antenna's lowest SWR was ~1.09 at ~124MHz. I tried it in a couple different environments and orientations and made sure there wasn't anything conductive right near the antenna (other than the wood, which I'm expecting to reduce the effective velocity factor of the wire.

Since I have no shortage of #10 wire, I started trimming the ends in 1/2" increments. I got the lowest SWR to 1.04 at 148MHz... but only while horizontal! Orienting the antenna vertically causes the lowest SWR point to jump to 1.52 at 153MHz.

What's happening here? Why was the tuning so far off? Is it the wood? Is it the copper wire? Why does orientation affect the tuning so much? I know I've got a lot of variables here, but is there one that is obviously the most important difference?

## Accepted answer (score 1, by William)

It was the wood!

It may *also* be the fact that I'm using copper wire instead of stainless steel rod, but I can't test that as I don't have access to any stainless.

Further experimentation this evening show much more predictable results. While I thought the 2x4 would be relatively transparent to RF, simply being near the 2x4 seems to cause the whole system to seem electrically much longer than it is, thus making the antenna very difficult to tune.

At first, I thought that it was conducting RF to the wood because the wire was bare, but I cut new elements just now out of my solid-core #10 THHN, this time leaving the THHN on everywhere except where the bolts contact the wire and had basically the same results. Bending the wire away from the wood such that the tips of the dipole (where voltage is highest?) caused the match to jump from 118MHz to 137MHz.

My best guess here is that the lumber is not fully dried and whatever water left in it is causing it to be a (poor) conductor, causing some capacitative coupling. I'd still love for anybody with more experience to chime in though, as I'm just guessing and am pretty new to making antennas.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7223/unexpected-resonance-dual-band-dipole, by William. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
