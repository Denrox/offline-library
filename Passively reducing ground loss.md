# Passively reducing ground loss?

*Tags: antenna-theory, wire-antenna, antenna-system, earth · score 7*

## Question

Would a disconnected wire or conductive mat below a low height antenna reduce ground losses?

A tuned length of wire under a wire antenna might be suitable for NVIS gain. But would a bunch of space blankets or unconnected random length wires or mesh (gopher wire) on or slightly above the ground help reduce ground loss of a low dipole or a vertical with far too few counterpose radials? (e.g. maybe one).

## Answer (score 4, by Mike Waters)

It is well-established that a wire reflector --on or just above the ground-- directly under a dipole can do just that.

I don't have a reference, but at a field day that I was present at years ago, a ham on 75m did that. Afterwards, as W8JI (who also was present) said, "He was just 'killing people'", meaning that his QSO count immediately went way up. His reflector was directly under his center-fed dipole. IIRC, it was laying directly on the ground. Although the spacing between the wire and the dipole was not optimum, it certainly seemed to work.

It was good and conductive soil, in NW Ohio near the Maumee River where Route 235 ends at a SW-NE road parallel with it. 200 years ago, that was part of the Great Black Swamp. Later, ditches were dug and tiles laid to drain it into the river, which turned all of Lucas and Wood county into fertile farmland. Still, adding that wire helped his signal.

Perhaps the band conditions improved at the same time, and the wire had little or nothing to do with it. But I've heard of too many similar experiences to discount that.

As for a vertical as you describe, I'm leaving that for someone else to answer.  See this answer by R. Fry, which seems to disprove my anecdotal statements.

## Answer (score 2, by Richard Fry)

Below is the result of a NEC4.2 comparison of a 75m, center-fed dipole at 10m elevation above 15 mS/m Earth, with and without a reflector on the surface of the earth directly under it.

The gain improvement **with** the reflector is about 0.03 dB.

As for adding a single wire on the surface of the earth or buried several inches below the surface to improve the performance of a vertical monopole -- its effect on antenna system radiation performance would be close to negligible, also.

That single conductor, no matter how long it is, will be ineffective in collecting and re-radiating the r-f currents flowing on and just below the surface of the earth within a circle of 1/2WL radius from the base of a radiating monopole.

## Answer (score 2, by tomnexus)

Random long wires - probably will help. Especially if they're aligned with the dipole above them.

Space blankets might not have a thick enough metal layer to be effective at HF, (though I know reflective window film is as good as wire mesh at 900 MHz).

Most importantly, things < ${1\over2}\lambda$, not connected together, will make no difference, the fields will go right through them. There is no easy way of connecting space blankets to each other. Perhaps with a substantial overlap and some sandbags on that.

Finally, note that adding metal under an antenna, as it makes it more efficient, will also push its pattern up. Better for NVIS and worse for long distances. So depending on your ground conditions, dipole height and band, you might see a loss of performance on some paths.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14585/passively-reducing-ground-loss, by hotpaw2, Mike Waters, Richard Fry, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
