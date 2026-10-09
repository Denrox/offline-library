# Ideal Doublet Size 160-10 Meters

*Tags: antenna-system, antenna-tuner · score 3*

## Question

Is there considered an ideal / optimum length for a doublet for use on 160-10 meters when fed with open-wire feedline and a balanced tuner in the shack?

## Answer (score 5, by Phil Frost - W8II)

A single antenna that functions over such a wide band will necessarily be less than ideal. Compromises must be made to achieve such wideband performance.

The antenna will have to be at least big enough for the lowest band, so anything significantly than 259 feet will be quite difficult to get working on 160 meters.

Then, you especially want to avoid any length where the antenna is an even multiple of half-wavelengths: it's at these lengths that SWR is at a maximum and you'll probably be unable to match the antenna.

You could plot or calculate these points for every band and pick a length to avoid them, but you will likely find this fails to take into account confounding variables:

- rotation of the feedpoint impedance by the mismatched feedline
- height above ground
- surroundings
- feedline position and common-mode suppression
- straightness (or lack thereof) of the antenna
- capabilities and efficiency of your tuner

You could try modelling your antenna and feedline, and adjusting the length by trial and error. Or you could simply build it and find a good length empirically.

Keep in mind, changing the length by a few inches will be very significant for the higher frequencies, but relatively insignificant for the lower frequencies. So in picking your initial length, getting a reasonable match on the lower bands will be most critical. From there taking it a few inches longer or shorter you can find something that works for the higher bands while keeping the lower bands good enough.

## Answer (score 2, by Mike Waters)

Make yourself a multiband antenna **with many doublets in parallel**, fed with just one feedline.

A fan dipole is very likely a much better choice of multiband antenna for you, for both (1) easy impedance matching *and* (2) similar patterns on each band. You can make one with many doublets in parallel, spaced apart and fed with just one feedline.

You won't need open wire line. Contrary to popular myth, LMR-400 (or inexpensive, low-loss 75Ω CATV coax) *will actually have significantly less loss than even the best parallel conductor line available*, which Phil Frost nicely explained here (somewhere) a few years ago. For paralleled λ/2 dipoles like this, coax just has lower loss than ladder line.

I assume you asked your question based on commonly available tuners which incorporate a ferrite core balun for feeding balanced line. That type is really difficult (if not impossible) to match a single dipole on all of those bands, since the impedance and complex reactance varies so widely for each band. However, if you are determined to use a ladder-line-fed 160m doublet: with the right type of tuner and low-loss open-wire line, you can match a center-fed dipole on any band. But you may have to build a custom balanced tuner yourself (as I did years ago using old junk parts).

However, a custom balanced tuner will not change the radiation patterns of your 160m doublet. The higher you go in frequency, the more lobes and nulls you'll have. (That can actually be a good thing, but it depends on where you want to work.)

## Answer (score 2, by Brian K1LI)

While studying this question enroute to writing an article on "A Slightly Off-Center-Fed Diople" in *QST* for September 2019, I learned that connecting the feedline to the antenna at a current node will essentially prevent the antenna from taking power at that frequency. Center-fed dipoles experience current nodes when the feedpoint is any even multiple of the frequency on which the length equates to an electrical half-wave. Since you ask for coverage from the 160 meter band and up, here's an 200$\Omega$ SWR plot of a 266-ft long center-fed dipole in free space:

Note the SWR dips near odd multiples of the half-wave resonant frequency.

Simply moving the feedpoint to 45% from either end doubles the number of SWR dips, indicating more opportunities for successfully coupling energy from the line into the antenna:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15687/ideal-doublet-size-160-10-meters, by W4QA, Phil Frost - W8II, Mike Waters, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
