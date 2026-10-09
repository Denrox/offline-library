# Why do we have to hand wind toroids?

*Tags: diy · score 10*

## Question

Many, if not most, ham radio kits (transceivers, tuners, ununs, baluns) require the builder to hand wind and tap their own toroids. (example)

This is a considerable area of stress for newbie builders and a failure point for their builds.

I can’t think of another component that builders have to essentially make themselves. We don’t wind our own (non-RF) transformers and inductors, for example.

Even the bitX folks have a small army of Indian women who are handwinding their toroids for their kits.

Why do we have to hand wind our own toroids? Is there something specific to ham toroids that makes them unamenable to mass production? Did they used to be mass produced? Is the market too small because we’re the only folks still using tapped toroids?

## Accepted answer (score 9, by Marcus Müller)

Some things are best answered in Song. I don't want to encourage you, but you might hum along to the tune of *Eye Of The Tiger*:

It's the wind of the donut  
It's the thrill of the built  
Rising up to the challenge of our fingers  
And the last known capac'tor puffs its smoke in the night  
and he's watching us all with the eeeeeye of the winder

No, seriously, kits are generally bought because you *want* to build something. And self-wound coils are actually possible – how cool is being the manufacturer of your own discrete components?

On a less enthusiastic note, no, there's no reason to wind your own low-power 3.3 µH inductors as done in the kit you linked to. (You can buy these, for like, cheap, even for significant currents).

Now, only problem being that your component reality is that aside from your inductance, you get capacitive effects between windings – so, you either get RF inductors that are wound with that in mind, or you get power inductors that can handle high currents at lower frequencies (where these parasitic effects play little role, and other, higher-µ, core materials still work well).

High inductance needs either a lot of core material, or higher-µ material, but higher-µ material usually is pretty lossy (and hence leads to lower inductivity and lower Q for the resulting inductor) at high frequencies.

That's really all not impossible to buy, but bear in mind that you're right, low-volume components are more expensive – buying a bunch of toroid cores, on the other hand, is cheap, since they are used for all kind of inductivities.

Also, discrete coils are, technically, typically the passive component type with the *worst* tolerance ranges. So, any circuit that involves an inductivity is thus designed to deal with a large range of values that are "around the nominal value, but not quite the nominal value"; tolerances of 10 or even 20% aren't unusual for power inductors, for example.

So, if anything, that's the component you want to let people build themselves, and then work around its inaccuracies.

Let us take a look at the larger 8 µH self-wound inductor in that kit:

QRPGuys Website says it's rated for 10W. It's pretty certain that the largest wave impedance in this system is 50Ω and the lowest around let's say 20Ω, so let's consider the current flowing through a 20Ω system as the worst-case sustained current:

$$\begin{align} P &= U\cdot I\\ &= (I\cdot R) \cdot I\\ &= I^2 \cdot R\\ \implies I &= \sqrt{\frac PR}\\ &=\sqrt{\frac{10\,\text{W}}{20\,\text{Ω}}}\\ &=\sqrt{\frac12}\sqrt{\frac{\text{VA}}{\frac{\text{V}}{\text{A}} }}\\ &=\frac1{\sqrt2}\sqrt{\text{A}^2}\\ &\approx 0.7A \end{align}$$

So, let's be careful engineers and overdimension by a factor of 2, so look for 8 µH that guarantees a current of 1.4 A. That inductor's only used for matching at 40 m, i.e. needs to work at 7.5 MHz. Mouser gives me 20 results and the cheapest is around 55¢ + VAT. Note that I didn't search for exactly 8 µH, but for +- 10% of that, because, oh well, nothing is ever perfect in this system, and using 7.5 µH certainly hurts less than not accounting for inductivity loss of a TR68-2 toroid at frequencies above 10 MHz...

## Answer (score 14, by Glenn W9IQ)

I suspect the primary reason that the kit supplier does not ship the kit with prewound toroids is that there is insufficient volume to make it economical to have them commercially wound.

A second possibility is that the kit supplier views winding toroids as a desirable part of the kit building experience.

A third possibility is that the kit supplier is simply trying to keep the cost of the kit as low as possible since prewound toroids would be more expensive.

A fourth possibility is that the kit supplier is a small, home based business that is not sophisticated enough, or has no desire, to develop a supply chain that can provide prewound toroids.

There are machines that wind toroids but their cost is generally out of reach for the hobbyist. Here is an example from spwindustrial.com:

A few years ago I built a solid state, 7 band, linear amplifier. Halfway through winding all the toroids for the bandpass filters, I nearly bought such a machine!

There is also a maker movement to create homemade toroid winding machines such as this one from http://www.instructables.com/id/Simple-Toroidal-Coil-Winder/:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10506/why-do-we-have-to-hand-wind-toroids, by RoboKaren, Marcus Müller, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
