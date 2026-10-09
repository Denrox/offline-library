# Are "end-fed" antennas really more multi-band than dipoles?

*Tags: antenna, wire-antenna, impedance-matching · score 7*

## Question

Several "end fed" antenna kits (including the ARRL's for example) include wording suggesting that they are useful as multi-band antennas.

But does feeding a wire antenna highly off-center with a transformer/balun/unun actually allow it to radiate efficiently on more HF bands than a dipole of the same length and height (and wire diameter, etc.) fed at its center?

Or is this mostly an illusion of a wider bandwidth on multiple bands, created due to the VSWR being reduced by transformer core and wire losses in the balun/unun and/or feedline and/or tuner, and/or added common-mode off-center feedline radiation that varies with the band in use?

## Answer (score 7, by EdvinW)

**End fed antennas do work on more bands than centre fed dipoles.**

The reason is that end fed antennas are resonant on all harmonics, while normal dipoles only resonate on every other harmonic.

To see why it matters where you feed the antenna, first consider an antenna element, sitting in free space without any feed point, and consider how it could resonate electrically. I will go on about it for a while, but it will lead to an explanation at the end.

Since the ends are not connected to anything, no current can run there, but there can be electric potential, i.e. voltage.

**At the fundamental frequency**, the potentials at the ends will oscillate between plus and minus the amplitude. Current will flow back and forth but, because of the isolated ends I noted above, it will be stronger in the middle.

If you, at any given time $t$, would draw a graph of the current along the segment, you would find it would look like a segment of a sine wave with zeros at the ends and a maximum or minimum in the middle. The amplitude would vary depending on the time as $\sin(fx + p)$, where $f$ is some constant depending on the frequency and $p$ is the phase. The point is the bend in the graph would move up and down, like a skip rope. This is a standing wave.

If you instead draw a graph of the potential along the segment, you will find that it is also a standing wave shaped like a sine wave, but that it instead has maxima and minima at the ends. At the fundamental frequency, the potential would only have opposite extreme points at the ends, one + and one -, and a 0 at the middle. There are physics reasons why the ends should be extreme points for the potential in a simple (ideal) antenna.

**At the harmonics above the fundamental**, most of what I laid out in the previous two paragraphs still holds true: The graphs of current and potential are shaped like (shifted) sine waves, and, at the ends, the current is always zero and the potential is at an extreme.

**At the first harmonic above the fundamental**, the current thus has two extreme points, one minimum and one maximum, and the potential has three, two at the ends with the same sign and one in the middle of the opposite sign. The graph of the current will look like a skip rope spun quicker to produce two lobes and a stationary centre.

**At the second harmonic above the fundamental**, there are three extreme points for the current, at ¹/₆, ¹/₂ and ⁵/₆ times the element length, and four extreme points for the potential at 0, ¹/₃, ²/₃ and 1 times the element length.

And so on: the number of extreme points increase by 1 each time you go to the next harmonic.

**Now, consider how you might feed your antenna to make it resonate at one of its harmonics.First, say you want to feed it at its centre**. If you look at the examples above, you see that there are two different things going on in the middle. Either the current is maximised and potential constantly 0, as in the fundamental and the second harmonic above the fundamental, or current is 0 but potential is varying! This means that the method you use to produce the fundamental resonating frequency, pushing current back and forth, will only work on every other harmonic! As for the first harmonic, no current flows through the centre, so no amount of current pushing will get it going.

**Second, let's instead say you feed your antenna at the end**. No matter which harmonic you want to use, you simply need to make the potential vary as much as possible (within reasonable limits, of course) while keeping the current low. The ununs used for endfeds accomplish this by acting as transformers to ramp up the voltage from your feed line, while the coils stop the alternating current from getting through too easily. This means you can use the same type of feeding to produce any of the harmonics!

Because of end effects and some other details where the real world isn't as simple as we'd like, you might have to tweak the antenna somewhat to get the resonating frequencies precisely on the ham bands. (Edit: Also, the higher you go, the harder it is to get resonant harmonics. If you play a string instrument, you will recognise this phenomenon; the high harmonics of say a guitar tend to be more dampened and sound a bit duller than the lower ones. Getting the antenna to work on two bands is easy, and at least up four bands is common. See also @hobbs-KC2G 's answer for a more practical consideration!)

**With an end fed antenna 20 m long, you could thus use it on the bands 40 m, 20 m, 15 m and 10 m.** (some fine tuning is required to get it good in all the bands)

**A traditional centre fed dipole for 40 m** (also consisting of 20 m of wire) **can only be used on the 40 m and 15 m bands**, with the same degree of fine-tuning. To get more bands, you need to add traps or use more complicated antenna models.

## Answer (score 7, by hobbs - KC2G)

It's mostly real.

To a first approximation, a center-fed dipole will have a reasonable impedance on bands where it is an *odd* multiple of a half wavelength (the fundamental, third harmonic, fifth harmonic, etc.) while the end-fed has a reasonable (for an end-fed) impedance on bands where it's *any* multiple of a half-wavelength (*all* the harmonics of its design length).

The only real 3:1 relationship on bands where we're likely to use wire antennas is 40m and 15m, which is a common pairing. 10m and 30m look like they're 3:1 when written that way, but the third harmonic of 30m (10.1MHz) is well above the top of 10m (28-29.7MHz). 160m and 60m are another close call, but not really practical.

But when you include second and fourth harmonics, lots of things open up, because lots of ham bands are roughly second harmonics of other ham bands. In particular, it's possible to cut an EFHW for 40m and have it behave reasonably well on 40m+20m+15m+10m. Just 20m+10m is a fine portable combination, and 80m+40m works if you have the space and you prefer the lower part of 80.

End-fed transformers do tend to be a bit lossy, and you can definitely see that the SWR curve is getting shallower by the fourth harmonic, but it's not terribly bad, and in my opinion these are fine portable antennas.

That said, I have seen some store-bought end-feds with big sealed transformer boxes that are sold as "All band" 160m-6m or 80m-6m. They have SWR curves that wiggle around all kinds of ways but never seem to go over 5:1. Antennas like that are definitely just deliberately lossy to offer "a good match on all bands".

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20742/are-end-fed-antennas-really-more-multi-band-than-dipoles, by hotpaw2, EdvinW, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
