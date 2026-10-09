# Does mounting a ground plane antenna upside down change the takeoff angle?

*Tags: antenna, vertical-antenna, antenna-modeling · score 8*

## Question

A typical gain pattern for a quarter wave ground plane antenna is:

[Image from a similar question and see watermark.](What%20is%20the%20effect%20of%20using%20different%20number%20of%20radials%20with%20ground%20plane%20antenna.md)

For a situation where the signals of interest are below the antenna in elevation (e.g. antenna on a hill/mountain), would mounting the antenna upside down make any difference?

A naive response would be that the antenna's pattern would be unaffected except to be rotated 180 degrees, i.e.:

An [answer to a similar question](What%20is%20the%20effect%20of%20using%20different%20number%20of%20radials%20with%20ground%20plane%20antenna.md) seems to imply that the radials on a ground plane antenna don't have as much to do with the pattern as the actual **earth**. My trials at modeling this with EZNEC resulted in no change based on the antenna's orientation, but I don't trust myself.

Also, looking at just the plots would lead you to believe that there is zero chance of receiving a signal from below the antenna's elevations. Which also is hard to believe.

Searching the internet resulted in many variations of "Try it." or "It worked for me back in ...". I'm looking for more specific reasoning.

And in case it matters much for this answer, I am mainly considering the 2m range of frequencies. Also for consideration, height above ground can be assumed to be in the 5 meter range.

Simplified configuration for clarity:

## Accepted answer (score 3, by JSH)

An elevated "ground-plane" antenna with tuned radials has, by itself, a pattern much like a dipole doughnut shape (freespace is what I'm talking about at the moment). Unfortunately we must mount the antenna and feed it with a feedline. This introduces one or more additional conductors below the radials that demonstrably (via simulation and measurement) draw/induce some power from the radials and flow energy below the antenna. See figure 5 of this article. This seems to cause the slight uptilt you most often see in ground-plane antenna documentation. The 3 dB beamwidth in the vertical E-plane is still quite enormous with energy both above and below the level of the antenna.

Some purists do mount these things upside down on a tower side bracket when the antenna site is much much higher than the surrounding users of the radio system. Indeed "beam downtilt" in collinear phased array systems is a serious attribute to study for some radio system circumstances... especially for the shorter wavelengths. Trigonometry helps answer when to consider this approach as I cover here.

That said, the vertical beamwidth of the typical quarter-wave monopole antenna is so big, mounting it upside down is probably not going to make any difference for most circumstances.

## Answer (score 4, by rclocher3)

If you were to flip the antenna upside-down, ideally with no part of the antenna touching the ground, then your antenna radiation pattern wouldn't change all that much, as you've discovered on EZNEC. Two things have changed compared to a 'normal' ground-mounted vertical: you've elevated the radials, and you've flipped the antenna.

(The following explanation may displease physicists as being overly simplified, but I think it's useful for the average ham. This is ham.stackexchange.com, not physics.stackexchange.com.)

By elevating the radials you've changed the way that the antenna works. Instead of a 1/4 λ monopole mirrored by the ground that you've made highly conductive with your radials, you now have a dipole. Half of your dipole is the vertical conductor, which creates vertically-polarized radiation. The elevated radials, which should be tuned to be 1/4 λ long, work to counter-balance the vertical part of the antenna. (Some people use the word 'counterpoise' for elevated verticals, but that word has been overly used and abused so much that the late L.B. Cebik, W4RNL, argued that the word should be retired.) Verticals with elevated radials work very well, but because the verticals must be tuned, they are essentially single-band antennas (plus odd harmonics).

So you've flipped the antenna. The pattern of the signal is very similar to a 'normal' ground-mounted vertical because the pattern is the result of a vertically-polarized signal radiated close to the earth and not in free space. Flipping the antenna but not flipping the earth just doesn't do much to change the pattern.

There is no particular reason to flip the antenna just because the antenna is on a mountaintop. Vertically-polarized antennas on mountaintops are common but I've yet to see a flipped one, ha ha. Antenna modeling is almost always done over an idealized flat earth, but experience shows that the signal from a mountaintop antenna makes it down into the valley. There is a program called HFTA or HF Terrain Analysis by Dean Straw N6BV, which comes with the ARRL Antenna Book, that can be used to model propagation over actual terrain that isn't perfectly flat, but the software only works with horizontally-polarized antennas.

## Answer (score 4, by Marcus Müller)

To answer this very graphically:

Flipping the diagram geometrically **can't** work:

What you've actually build is kind of a waveguide, consisting of two grounded planes below (earth) and above (virtual earth spanned by radials) your antenna; in this rotation-symmetrical setup, the H-field only exists in horizontal direction, and the E-field between the two planes will only exist vertically.

In other words: if we assume the virtual ground plane to be a perfect circle, then this looks like a lot of dipoles standing tightly next to each other between that plane's edge and the ground, being fed with exactly the same signal. Since this, for symmetry reasons, won't have any horizontal gain, the only gain we can have is vertical; but there's no vertical group factor in a group of horizontally shifted dipoles, so this will really just have the radiation pattern of a half-length dipole.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6325/does-mounting-a-ground-plane-antenna-upside-down-change-the-takeoff-angle, by hazzey, JSH, rclocher3, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
