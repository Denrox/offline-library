# Satelite dish modified for Wi-Fi (Signal Elevation Question)

*Tags: antenna, antenna-theory · score 4*

## Question

I am doing a project where I will be re-purposing an old TV satellite dish as a directional Wi-Fi antenna. The dish is circular in shape, not oval. The dish has an arm coming from the bottom that makes a 90 degree angle with the dish. I will be adding a second arm to the end of the dish's arm that will allow me to mount an SMA antenna connected with RG-59 cable precisely where it will utilize the dish's geometry. **I need to figure out the proper position of the antenna on the dish.** I want the dish to receive signal directionally where there is a zero signal elevation angle. From my previous understanding, dishes receive their signal from space where there is an angle of elevation from the transmitter and the receiver part of the dish.

I created a diagram that illustrates my plan with dimensions and calculations. **I need some verification with my diagram and suggestions on how to maximize the reception strength.**

I think that the antennae should be placed somewhere along line C in the diagram but I want to be sure before I start modifying the dish.

EDIT: I've calculated the focal point on the dish to be approximately 320 mm.

PS:I just realized that the 75 ohm impedance of the RG-59 cable is not optimal for the Wi-Fi adapter. I only need about 6 inches of cable so I will try it with and without the jumper cable and compare signal levels.

## Accepted answer (score 2, by Glenn W9IQ)

Unfortunately, your drawing is not correct.

To find the focal point of a symmetric parabola, measure the diameter of the open rim of the dish, call this D. Measure the depth of the dish at its center, call this c.

Calculate the focal point distance from the bottom of the dish as:

$$ f = \frac{D^2}{16c} $$

Note that the focal point is in the center of the dish, it is not offset as in your drawing. So your receive antenna will slightly shadow aperture of the dish.

Due to the physical aperture of your receive antenna, you may need to adjust it in or out from the focal point in order to fully illuminate the dipole or other element.

If the dish is an asymmetric parabola, the focal point will be offset from the center in order to avoid blocking the aperture. This is the type of parabola that nearly all modern home satellite dishes use. They are identified by an LNA support arm that extends from the bottom of the dish and the dish apparent elevation angle appears to be lower than the satellite capture elevation.

In the case of an asymmetric dish, the existing LNA arm should be used as a starting point to find the appropriate focal point for the dipole or other antenna element since the focal point is largely frequency independent.

## Answer (score 4, by always_learning)

You can experimentally 'ball park' the location of the focus, visually, several ways, by using sunlight.

One example -- some have temporarily attached (double-sided tape?) about a dozen one inch square mirrors in the dish, or reflective tape, from rim to center, and along say four radial lines from the center (if by the clock, at 12, 3, 6, 9 o'clock). Then put a small white card where you think your antenna should be positioned, and aim the dish at the sun, and note where the bright square reflections (or two lines from the reflective tape) converge on the card as you shift the card around the imagined focus. MacGyver probably would have used the reflective tape, and some gum, and a paper clip. Also note what happens to those bright indicators as you correct your aiming at the sun. The point is that there is a visual method available to you that can get you very close for the RF trials.

A link from Twitter of someone using this method.

Of course the sun needs to be shining on the dish to do this.

**CAUTION!!**

When doing any sort of experiment that focuses light, particularly sunlight, the heating, or damage, or burning of body tissue or other materials, is possible! Even a dozen one inch *ideal reflective* square mirrors focused on one single square inch spot is now 12x the solar radiation of any sort of radiation that can be reflected by those mirrors, that would normally be on only one square inch! Similarly, when testing or focusing or aligning any sort of RF link that uses a parabolic dish antenna, exercise proper RF safety practices, and do not allow anyone to be in front of a focused microwave (wifi) transmitting antenna system or open waveguide, particularly the head and eyes! There are body parts that are naturally resonant to certain microwave frequencies and may suffer more damage due to that resonance, particularly in the head. Experimenting with any sort of parabolic reflecting dish requires a functional knowledge of at least minimal safety considerations, for others as well as oneself, and property. Understand the radiation frequencies and potential power levels involved!

If using reflective tape, be very careful to lay down the tape exactly on two 'diameters' that are 90 degrees to one another, and pass through the center of the dish. If you are not sure if this is a prime focus dish, try some additional pieces of tape and experiment with the position of the card, until they all in some way intersect at one point, which is what a parabolic reflector is ultimately supposed to do. Two bright bars centered on your target focus point 'card' might not mean what you think it means. Ultimately, the key to this is where the brightest portion of the reflected line(s) intersect on the card. If it is a prime focus dish, then if you are careful to have the tape(s) pass through the center of the dish, the result will be more helpful, but again, what matters is where the brightest portions of the reflection lines intersect or converge, as crisply as possible. (Remember, if you use wider tape, very reflective, and more pieces of it, you will be focusing that much more sunlight energy to the focus point, and it becomes damgerous as a burn hazard during your visual focusing efforts! Mind the caution earlier in this posting!). Think of the example of using a magnifying glass to focus the sun to a pinpoint, to burn a piece of dry wood. One moves the glass closer and further away to find that focus distance where the *dot* of the sun is smallest (and hottest). If the glass is way too close or far, it may still show a big white spot *the size of the glass itself*. That is what the reflection lines alone are like, ie, they may not yet be focused on your target card, even though they may produce intersecting lines on the test focus card or surface, so you must move the card closer and farther away to get the intersection point strong, bright, minimal in its brighter 'size' compared to the rest of the lines that will appear. If your dish is an offset dish, it is a little trickier. Again, you don't just want to see all the lines from many pieces of tape 'intersecting'. You also want to find the brightest intersection point by moving the card closer and then farther away. Let each of those extra pieces of tape be 'rim to rim', even if they don't span through the center of the dish. If they project a curved line on your 'card', at least one point of the line should touch the other reflective tape produced lines on the card. And again, the more tape strips you use, the more dangerous it may become if using sunlight. A secondary benefit of this method, when done safely, is, it can be fun. I'm pretty sure it will work on an offset dish.

Mount your test focus 'card' on the same structure on which you intend to mount the antenna module, ideally one that is adjustable. This will help your results be more stable (no jitters from shaking or shifting hands), and will let your hands be free to tweak the dish aiming at the sun. Have fun.

If you find that best spot of strongest convergence on your card, and you find your dish's rim is not anywhere near perpendicular to the position of the sun, then you may indeed have an offset dish, instead of prime focus.

One might think that this could be done at night, more safely, with a bright spotlight instead of the sun. If the dish is a prime focus dish, then the problem... can you guess... is that your focus card will be blocking much of the light source. The sun, even though it appears almost like a point source of light in the sky, is many times larger than the earth, and your dish, which means that much solar radiation is coming into that tiny (relatively speaking) dish area, straight into it, beyond the edges of the focusing card. Don't let the tiny dot of the sun in the sky skew your physics understanding. Whereas with a bright flashlight, the rays of light from it are coming into the dish at an angle, at best *straight* from the outer rim of the flashlight's outer edge of its own parabolic reflective. So aligning the focal point with the light from a nearby flashlight, at night, or in a dark room, will not give the same results.

Your final adjusting should of course be done with the RF signal itself. Be aware of, and respect the laws governing wifi antenna system output in your region, usually well thought out, by smart people, for good reasons. If you are running a linux system, there are many ways to check your signal quality and strength with commandline based utilities. Try an internet search, with your favorite search site, of this

terminal based wifi signal strength utility

Something like this can give you a continuously updated overview:

```
watch -n 1 cat /proc/net/wireless

```

That was taken from this link.

There are plenty of other links as well. Of course, always be mindful of any security risks of your software sources, and the software itself. I am not your source for a professional review of such security issues. Personally, I have used the wavemon utility, which you may likely need to install first, (it does what its name says) on any current raspberry pi system (Stretch or Buster on Pi2 through Pi4B).

**Very important:**

Once you have found your focus visually, and RF'ally, remove the reflective tape, just in case you are coincidentally aiming at the sun one day. Don't want to overheat your antenna module, whatever you finally decide that module to be.

And, first test, in a very small area, maybe on the back of the dish, a weak solvent that is sufficient to remove any residue from the reflective tape, without removing the paint on the dish. Maybe 70% iso propyl alchohol will be enough without removing paint, but I can't predict what is painted on your dish, or what solvent will be ideal. Maybe the tape will peel off without leaving any residue at all, or, maybe it will peel the paint off. What you don't want is a final result of a shiney aluminum 'light mirror', unless you want to cook hotdogs with it. If you need to touchup some areas, maybe a light gray spray paint will do it, as long as it isn't formulated with the military's secret stealth RF absorbing materials, which would be, needless to say, counter productive, in perhaps more ways than one.

**Final:**

I am sure I have left out many details. This wasn't intended to be a comprehensive wiki, but only a pointing out of another method, visual, to determine a dish's focus point.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7817/satelite-dish-modified-for-wi-fi-signal-elevation-question, by Jake Psimos, Glenn W9IQ, always_learning. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
