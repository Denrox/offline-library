# Why does Free space have the highest loss compared to other losses like atmospheric loss, feeder loss etc?

*Tags: satellites · score 4*

## Question

In a communication Satellite system, there are losses that occur when the signal is received at the antenna and then passed through a communication link to the output stage which could be the receiver. Among these losses free space seems to be the highest loss that can happen why ?

## Accepted answer (score 12, by tomnexus)

Free space loss is the power lost because it *doesn't reach the receiving antenna*.

An example using an analogy is your eye, looking at the light from a light bulb.

If you stand 10 metres away from a light bulb, and your pupil has a diameter of 2 mm, then you can see that only a tiny fraction of the power radiated from the light bulb actually enters your eye. The rest of the power is lost.

The formula is simply the ratio of the areas: $${Pout\over{Pin}} = {\pi0.001^2\over{4\pi10^2}} = 2.5\times10^{-9} = -86\text{ dB}$$ Where the numerator is the area of your pupil, and the denominator is the area of a 10 m sphere.

Antennas have a capture area too, based on their gain and the wavelength, or for dish antennas, it's usually easier to consider the whole aperture of the antenna, and then some efficiency factor.

The transmit antenna also has gain - this can be compared to focussing of the light. You know that a distant light bulb looks much brighter if it has a reflector - compare how much brighter a car headlight looks (55 watts, focussed forwards) to a naked porch light.

For satellite communications, picture the transmitter high up there looking at nearly half of the earth. Even if its transmitter power is concentrated just on earth, not wasting any power to space, only a very small fraction of the transmitted power will be intercepted by your little dish antenna!

Other losses, as you say, are quite small - just a dB here and there for cable and things.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17283/why-does-free-space-have-the-highest-loss-compared-to-other-losses-like-atmosp, by Signal, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
