# How to splice RG-174 coax?

*Tags: hf, coaxial-cable, repair · score 3*

## Question

I'm pretty good at repairing broken regular coax, but I recently had an RG-174 cut and it's too small for me to solder the center wire and keep the braid away from it. What's a good way to do this? Edits for clarity: this is for a feedline to an antenna, using for HF signals, so the repair method is important in keeping a clean signal.

## Answer (score 2, by tomnexus)

At HF there are almost no limits on how bad your splice can be, as long as:

- there's no short circuit
- braid is connected to braid and inner to inner

You could even use a "chocolate block" connector :)  
* photo from Tudor Barker, cropped

But to do a neat job:

1. At each cut end, strip about 25 mm (1") of the outer sheath, and then about 7 mm (1/4") of the inner.
2. open the braid out and lay it back on the jacket
3. lay the inners overlapping and solder quickly and carefully. RG174 inner melts quickly, the trick is not to bend or force it until it sets again.
4. insulate them with a 25 mm piece of electrical tape. (or more if you're < 200 MHz, less chance of a short circuit)
5. fold the braids back, they will also overlap
6. wind a bit of thin wire gently around the braid to keep it snug against the inner (but not so tight that it'll sink through the insulation
7. solder the braids together carefully. Use a cool iron. Don't fully wet the joint - the RG174 insulation will melt and run out the ends! Just gently wet the bits of the braid where they meet, and tack the wrapping wire to the braid in a few places. The idea is to get just enough mechanical strength, not a solid tube of solder.
8. insulate the whole thing with tape, or heatshrink if you remembered to put it on first...

I'm comfortable splicing coax like this up to 1.5 GHz for GPS without unreasonable loss. Of course it won't be a first class measurement cable, but for radio transmission a tiny, short impedance mismatch won't hurt. At HF the whole joint is 1/1000 of a wavelength, it will be fine no matter how ugly it is.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14486/how-to-splice-rg-174-coax, by scook, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
