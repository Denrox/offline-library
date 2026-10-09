# Better explanation for beyond-line-of-sight VHF signal reach than "lower curvature to radio waves"

*Tags: propagation, vhf · score 10*

## Question

I am currently studying for the Technician Exam and have come across an answer to a question I think is ridiculous. The question is:

Why do VHF/UHF signals usually travel somewhat farther than visual line-of-sight distance between two stations?

The given "correct" answer is,

Because the Earth seems less curved to radio waves than to light.

Come on, there are much better answers than that and one does not even have to go into the duality of particles and waves. My question is, asking a ham expert, what would be a better answer to this question?

## Answer (score 8, by Marcus Müller)

Please accept Phil's answer. It's the sanest one.

Now, however to answer:

what would be a better answer to this question?

Why do VHF/UHF signals usually travel somewhat farther than visual line-of-sight distance between two stations?

Because they are not the same as light; first of all, they aren't blocked by things like a thin cotton sheet.

I hear me muttering to myself:

Ok, you know exactly how that question was meant; don't be an arse:

Why can VHF/UHF waves be detected when no straight line through an RF-transparent medium connects emitter and receiver?

Because beam optics don't apply here.

Remember that the assumption that light forms perfectly straight beams is actually wrong; it just looks that way because the wavelength of visible light, which is an electromagnetic wave just like radio waves, is in the nanometers, and hence, most effects that we can observe in lights are well-modeled with a model of light following a straight beam.

However, that's just a justifiable simplification under the assumption that

1. all structures interacting with the wave are way, way larger than the wavelength
2. the medium (air, for example) through which the wave travels is homogenous, and works the same no matter in which direction you travel through it
3. the sensitivity with which we look at light phenomena is low enough for us to ignore the effects that can't be explained by the model (this applies to any model of the world, by the way)

## Large-scale-ness (Assumption 1)

To illustrate 1.: Maybe you've done slit experiments with light: Make a really, really narrow slit and place it between a source of light and a screen. You'll see that light really doesn't need a straight path to travel. Also, you'd ideally be able to observe interference effects on the screen, ie. not only light in places that should be dark, but also regular patterns of brightness fluctuating.

However, you need a *really* narrow slit to make this work visibly well (or even better, a lot of identical slits in equal distance, to make the effect stronger).

Same applies to radio waves and the earth: Say your UHF signal has a wavelength in the order of "single-digit meters". The earth has a radius of 6370 km. It's "huge enough" compared to the wavelength that radio waves, just like light, wouldn't "reach beyond the horizon", **iff* there was no atmosphere around earth.

## Homogenous, anisotropic Medium (Assumption 2)

Now here's the thing: if the earth is really large-scale compared to UHF waves, the optical propagation model would work, and we shouldn't be able to receive things from a place to which a straight line goes through the earth.

However, the atmosphere doesn't play along here, at all:

On the lower end, it's limited by earth, or actually, globally, more often by seawater, which is at least partially a pretty well-reflecting surface for radio waves. On the upper end, we get the ionosphere, and troposphere and whatsitcalledsphere; basically, you get a refraction that "bends" the beam towards the earth just enough to make it "cling" to earth's surface a little more.

(I've writtne an advanced high-school physics level explanation for that [here](Communications%20Ground%20wave%20propagation.md).)

So, what we see happen for microwave radio is similar to what happens in a (graded index multimode) optical fiber; the fiber doesn't have to run in a straight line, but a light beam can still pass relatively unhindered through it, by the simple fortune of always being refracted (and reflected) back towards the core of the fiber when it comes closer to the edge.

That doesn't make the fiber (earth) any less curved; it's just that macroscopically, the beam follows the curvature. The fact that the curvature isn't "eradicated" by this refractive model can pretty simply be verified by realizing that light still has to travel a distance longer (and hence, for a time measurably longer) than the straight connection between the points.

So, yes, I'd consider that answer wrong.

## Sensitivity too low to detect the difference to the simpler model (assumption 3)

While our eyes are tremendous instruments that can be continuously and smoothly adjusted to different lightning situation, their instantaneous *dynamic range* (the ratio of the weakest detectable to the strongest detectable light power) is limited: Numbers differ depending on who examined what, but it's fair to assume doesn't exceed the order of magnitude of 1:1,000,000 (or 60 dB).

With radio receivers, and transmitters, we can be a lot more sensitive by something that light waves don't allow us (because the waves aren't coherent):

We can take an arbitrarily long observation and boil it down to a number. (We call the increase in sensitivity *processing gain*. I find that name very fitting.)

You won't be able to see a lighthouse's atmospherically refracted light at all if the ambient light outshone it, even if you stood right next to it – but with radio receivers, we can suppress the effect of ambient and receiver noise. You can do something like:

Let the transmitter transmit a $\cos(2\pi 200\,\text{MHz} t)$ for 1 ms, then a $-\cos(2\pi 200\,\text{MHz} t)$ (i.e. a 180° phase shifted, or inverted, version of the same carrier), and repeat that pattern for an hour (that's 3,600,000 ms).

If our receiver knows that pattern, it could take all signals from the odd-numbered milliseconds, record them and add them up. Do the same for all the even-numbered milliseconds, but in a separate accumulator.

Now you get two different "sum-recordings", each with 1,800,000 summed up cosine segments, one with all the +cos, the other with all the -cos.

If the two bins don't look like cosines at all, then you pretty certainly only noise with no cosines "hidden" in it.

If the one bin, however, looks like a cosine, and the other like a minus-cosine, then you can say with high certainty that you received the transmitter's signal. The same-phase cosines just added up constructively – you made a cosine with amplitude of 1.8 million out of a cosine with amplitude 1. The noise can't add up as much; the math is relatively easy here: If we say a cosine with amplitude 1 has power $P$, then a cosine with an amplitude of $A\cdot 1$ has power of $A^2 \cdot P$, i.e. you see a power increase in the sum signal of $1\,800\,000^2$. Uncorrelated noise's power adds up – so the power increase of the noise is "only" $A$, not $A^2$; hence, the signal-power-to-noise-power ration (SNR) of the sum is $\frac{A^2}{A}=A$ times better than that of the original single observation.

That's a pretty crass thing – and it's the reason modes like WSPR or things like GPS work so robustly – your GPS receiver might work with a 4-bit ADC, that means the weakest-to-strongest instantaneously discriminatable signal rate, i.e. the dynamic range is just 16, even ignoring that one bit should actually be the sign of the received signal. GPS signals are usually significantly below noise floor – i.e., they have a negative SNR (in dB). Still, GPS works well! GPS receivers know the pattern in the signal sent by the satellites, and they add it up over a long time, which lifts the signal out of noise.

This all is just to illustrate that we have it much easier, because it's just such a standard thing to do, to detect sub-ambient RF signals than light signals; hence, it's easier to notice that things don't work like in the nice and simple optical (beam) model.

## Answer

Because we're breaking the assumptions necessary for modelling electromagnetic waves as beams, we can't make any statements based on a beam-based model.

Especially, emitted energy does reach beyond the horizon due to *wave* (as opposed to ray) propagation effects such as refraction, diffraction and reflection.

## Answer (score 7, by Phil Frost - W8II)

The full question, and possible answers:

T3 C11  
Why do VHF and UHF radio signals usually travel somewhat farther than the visual line of sight distance between two stations?

A. Radio signals move somewhat faster than the speed of light  
B. Radio waves are not blocked by dust particles  
C. The Earth seems less curved to radio waves than to light  
D. Radio waves are blocked by dust particles

Of these, *C* is the only answer that makes any kind of sense. Arguably, one could take issue with the phrasing of the answer, because radio waves have no consciousness, and so nothing can "seem" anything to them. However, atmospheric refraction does bend the relatively low frequencies (compared to visible light) of VHF and UHF to a greater extent, and it's in human nature to transform our observations into impossible reference frames to more intuitively reason about the world. If your eyes could see in RF you would indeed see farther which means the Earth is effectively less curved, so even if it's an impossible scenario, it holds up to simple intuition and reason.

Trying to simplify a complex interaction of atmospheric conditions and electrodynamics into a single sentence question and answer in simple language is bound to generate some degree of disagreement about the single "best" sentence that captures the situation, and going to require some reasonable assumptions to be made. The best we can hope is that one of the four proposed answers is obviously correct, while the other three are obviously wrong, and by that standard, this question seems fine to me.

## Answer (score 5, by Rich Morgan - KF9F)

From Electronics Notes, a British page.

Line of sight radio communications

It might be thought that most radio communications links at VHF and above follow a line of sight path. This is not strictly true and it is found that even under normal conditions radio signals are able to travel or propagate over distances that are greater than the line of sight.

The reason for the increase in distance travelled by the radio signals is that they are refracted by small changes that exist in the Earth's atmosphere close to the ground. It is found that the refractive index of the air close to the ground is very slightly higher than that higher up. As a result the radio signals are bent towards the area of higher refractive index, which is closer to the ground. It thereby extends the range of the radio signals.

The refractive index of the atmosphere varies according to a variety of factors. Temperature, atmospheric pressure and water vapour pressure all influence the value. Even small changes in these variables can make a significant difference because radio signals can be refracted over whole of the signal path and this may extend for many kilometres.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12866/better-explanation-for-beyond-line-of-sight-vhf-signal-reach-than-lower-curvat, by Dave G, Marcus Müller, Phil Frost - W8II, Rich Morgan - KF9F. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
