# Designing a helical antenna for a dish

*Tags: antenna, antenna-theory, microwave, reflector · score 5*

## Question

I'm interested in a dish antenna with an axial mode helical feed for receiving video. My target frequency is about 1280 MHz or the 1.2/1.3GHz range.

I've been able to figure out helical basics, like circumference equals wavelength, more turns is more gain, spacing is 1/4 wavelength, etc.

However, when designing the antenna as a feed for a dish, I can't figure out optimal parameters for the design of the feed to maximize performance (directionality.)

My best guess would be to have the angle of the outside edge of the dish from the focal point equal the *half power beam width* of the helical (fancy words I learned here.)

**So basically my question is how many turns to put in a helical given dimensions of a parabolic reflector. Are there any tried and tested rules for something like this?**

The best example I can find of this online is here, but I can't figure out how the OP decided on the number of turns.

## Accepted answer (score 9, by hobbs - KC2G)

I haven't built one of these myself, but one of the best resources I know of for the theory is antenna-theory. The second page mostly discusses gain. There it talks about optimizing the distance between the feed antenna and the dish, given a fixed pattern for the feed antenna, but basically the same thing applies to narrowing or widening the pattern of the feed antenna for a fixed distance.

There isn't a lot of worked out math there, but it discusses what the tradeoff is. The more obvious component is "spillover loss" — any part of the feed antenna pattern that doesn't hit the dish is wasted power on transmit (and a source of noise on receive), so you want to minimize that. The slightly less obvious component is "taper loss" — the dish is most efficient when you're using *all* of it. If you concentrate 99% of your pattern within half of the diameter of the dish, you might as well just use a dish half as big (with accordingly lower gain).

We can work backwards from this graph which shows the efficiency of different values of the angular size of the dish given a pattern that's shaped like $\cos^{n} \theta$, for different values of *n*. The trick is to figure out what half-power beamwidths those *n*s correspond to, which is a simple matter of solving $\cos^{n} \theta = 0.5$, or $\theta = \arccos \sqrt[n]{0.5}$. This works out to

$$ \begin{align} n = 2 && \theta_{HP} = 45^\circ && \theta_{maxEff} = 67^\circ\\ n = 4 && \theta_{HP} = 32.76^\circ && \theta_{maxEff} = 52^\circ \\ n = 6 && \theta_{HP} = 27^\circ && \theta_{maxEff} = 45^\circ \\ n = 8 && \theta_{HP} = 23.5^\circ && \theta_{maxEff} = 40^\circ \end{align} $$

where $\theta_{HP}$ is really a half-power *half*-beamwidth, and $\theta_{maxEff}$ is me eyeballing the peak efficiency values off of that graph.

This indicates that your guess was not terrible, but it loses a little too much power off the edges of the dish. The ideal seems to a half-power beamwidth between 55% of the angular diameter of the dish (for feeds fairly far from the dish) to two-thirds the angular diameter of the dish (for feeds fairly close). Having it be 100% of the dish diameter is 1-2 dB worse.

## Answer (score 2, by Ray Maxfield)

The information on Dish illumination is Correct. That is... the Angle of the waves from the Dish to the Feed Antenna ( helical ) at the Widest (rim) point. Using an off-center point feed makes it Vary Hard to design. the next thing is the Focal Point. this is the Exact Point the Waves are Concentrated at, to set the Helical at. It is like taking a magnifying Glass and finding the Focus point to Burn something. I would look for a UHF /VHF handbook, and find Satellite communications, and Parabolic Dish design information. ray

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16520/designing-a-helical-antenna-for-a-dish, by Gabe, hobbs - KC2G, Ray Maxfield. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
