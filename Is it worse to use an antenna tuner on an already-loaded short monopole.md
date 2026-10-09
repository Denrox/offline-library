# Is it worse to use an antenna tuner on an already-loaded short monopole?

*Tags: antenna-theory, impedance-matching, antenna-tuner · score 3*

## Question

If I had a good transmatch and wanted to use a spare CB antenna on the amateur HF bands, would I be better off bypassing its tuning coil completely?

One ham pastime is using an antenna tuner to match a random conductor (house gutters, bedsprings, chain link fence, a head of lettuce…) and use it as a makeshift antenna on ± any band.

But in the case of a too-short monopole element that's been baseloaded to make it resonant at a lower than natural frequency — does that make it even narrower bandwidth and harder to retune than the original whip? Or will the antenna's coil simply work in concert with the capacitors and inductors in my tuner to force a match just as well as without the coil?

Does it make much a difference if I'm trying to electrically re-tune/re-match a loaded antenna designed for 11-meter on a close (10/12-meter) versus completely random (say 75-meter) band?

## Answer (score 3, by hobbs - KC2G)

There's a large amount of "it depends". There's nothing inherently bad about having both loading at the antenna and a tuner in the shack.

The antenna coil *probably* makes the antenna a better match for the coax, and therefore reduces coax loss related to high SWR, but that's not guaranteed, especially if you're far from the design band. The antenna impedance could be something far-out and you can't be sure unless you measure it. (Also, what seems to be a base loading coil might actually be an autotransformer!)

The antenna coil *might* make the impedance seen at the shack end of the feedline one that your tuner can deal with more easily / more efficiently, but it might *not*, too, because every feedline is an impedance transformer, and depending on the length of the coax, you might get unlucky.

Even if the impedance works out in your favor, the coil in a mobile antenna might be a fairly low-Q (lossy) one, and the tuner loss plus the mismatch loss in the cable from letting the tuner do all the work might be lower than the coil loss in the antenna. Or it might be the opposite.

The results depend on the antenna design, the coax quality, the coax length, the tuner build, and the frequency you're using — every case is different! You'll have to measure and experiment. Or just use the thing, you'll probably get out in any case.

## Answer (score 2, by Richard Hum)

The loading coil would help by reducing the amount of inductance required from your tuner. If you were to remove it, the tuner would have to make up for that missing inductance by adding more of it's own, and potentially run out of inductance to give.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20772/is-it-worse-to-use-an-antenna-tuner-on-an-already-loaded-short-monopole, by natevw - AF7TB, hobbs - KC2G, Richard Hum. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
