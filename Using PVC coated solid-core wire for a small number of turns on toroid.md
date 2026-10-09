# Using PVC coated solid-core wire for a small number of turns on toroid

*Tags: balun, ferrite, inductor · score 3*

## Question

I'm researching making my own 49:1 unun using an appropriate mix ferrite toroid and some reasonable gauge solid-core wire. (This is for an experimental HF end-fed antenna, though this detail probably isn't relevant.)

I know it is tradition to use solderable coated "magnet" wire for this, and there are a fair amount of pixels spilled over how thin the coating ought to be. But, as far as I can tell, the thickness of the coating is to reduce the spacing when making high-turn, closely spaced wire toroids. In this application there is a tension between having thin coatings so you can really pack the turns tightly, but not so thin that it breaks and allows shorts.

Since I'm looking at something like 9-11 (I'd have to look at my notes again, but it can't be more than 11 [duh -- it's 7 turns if I'm making a 49:1 Z-ratio unun]) looser turns of lower gauge wire spaced more or less evenly over a larger ferrite toroid, spacing just isn't a concern.

Are there specific observed problems using plain old PVC (or silicone rubber, for that matter) coated hookup wire for this purpose, given that I'm not making 100s of turns closely spaced? My search-fu did not come up with anything, here or on the greater unwashed internet.

One potential issue I considered was that the thicker "dialectric" might lead to pronounced unwanted capacitance, but I'm not seeing how such loose spacing would be affected in this manner; that air-gap is already acting as a dialectric. But maybe I'm making a better capacitor by introducing a layer of non-air dialectric?

Similarly, I don't see capacitance across the wire and ferrite mixture being an issue, but I cheerfully admit that (like many hams) my understanding of the physics of inductors is probably lacking. I suppose the closer the wire is to the ferrite core, the better it will act as an inductor. But many 49:1 unun designs already call for wrapping the toroid in what is essentially dialectric tape before winding the wire on them. So that doesn't seem like a valid argument against PVC hookup wire.

I even considered that wire coatings can affect the velocity factor of the conductor, but I'm not sure how that would even come into play in this application. I'm ignoring this, probably out of sheer ignorance.

Can I just use plain old hookup wire for my unun, or do I need to spring for (so-called) magnet wire?

### Postscript

*Of course, the moment I post a SE question my searches the next day show countless examples of people using PVC coated hookup wire for similar designs without any comment. Many such project pages compare and contrast almost identical ununs as mine, some with coated wire, some without. I think we can accept the "go for it" answer below as more or less canonical, but if I learn how to measure and test these things I might come back and put those details in an answer.*

## Accepted answer (score 1, by webmarc)

You should be fine with the hookup wire for all the reasons you note.

Another item to take into consideration is the additional distance of the wire from the toroid, but for this application it strikes me as a de minimus concern.

Best practice, of course, is to measure the characteristics of what you build, and I imagine your measurements will show that you're well within tolerances of what you are intending to build.

All of this is a long winded way of saying: **go for it!**

After you build it, would love if you would come back and update your question with any actual results that you've measured :-)

Happy hamming!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20977/using-pvc-coated-solid-core-wire-for-a-small-number-of-turns-on-toroid, by webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
