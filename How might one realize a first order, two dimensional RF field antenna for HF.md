# How might one realize a first order, two dimensional RF field antenna for HF?

*Tags: antenna, software-defined-radio, phased-array · score 9*

## Question

I just coined the term "field antenna". It is by analogy to the lightfield camera or the soundfield microphone. Essentially, it is an antenna that captures not only the strength of an RF field, but also the *direction* of it.

Of course, these antennas already exist in forms, such as phased arrays used for radar, or four-square antennas popular on the lower bands. However, I have a somewhat different use case in mind: I want it to work at HF, for receive only, and I don't want to implement the phasing with a fixed network (or maybe a few switched networks) as in the four-square antenna. Instead, I want to perform the phasing in software.

One possible application: listening to radio in stereo, with the sound heard corresponding to the direction from which the signal was received, a "wetware rotator" of sorts.

Now, the usual way to doing this processing is to decompose the signal into circular harmonics. These are like spherical harmonics, but in two dimensions (circles) instead of 3 (spheres). For the sake of simplicity I'm stopping at the first harmonic (first-order), so I will have, perhaps after some processing, three signals:

1. an omnidirectional signal (0-th order)
2. a figure-of-eight pattern aimed East-West
3. a similar figure-of-eight, but aimed North-South

Described mathematically, I'm looking for the responses in azimuth defined by:

$$ \frac{1}{\sqrt{2\pi}}, \frac{\cos \theta}{\sqrt{\pi}}, \frac{\sin \theta}{\sqrt{\pi}} $$

or described graphically:

Now here's the question: how might one realize such an antenna? Remember the antennas need not actually have these responses: they might have other responses from which these responses can be calculated.

## Answer (score 5, by WPrecht)

OK, this is an interesting one.

At first blush you could achieve this with two tuned magnetic loops at right angles to each other (visualize an egg-beater) and a 1/2 wave vertical for the omnidirectional part.

Of course, someone has thought of this crossed loop arrangement before, in 1907 Bellini and Tosi invented the Bellini-Tosi Goniometer:

A coil is rotated inside an electrical field fed from the N-S and E-W antenna signal components such finding the angle of maximum signal. The antenna can be either be a circular array of 1/4 wave verticals or a Crossed-Loop Antenna:

Systems based on this principal were the basis of the first radio navigation systems for aircraft until replaced by radar following WWII.

Back to the original question though, I think the loops would have to be tuned fairly precisely and high-Q loops are rather narrow in bandwidth so you'll have to pick your operating frequencies with care. But I don't see any obvious reason why it couldn't be done.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1145/how-might-one-realize-a-first-order-two-dimensional-rf-field-antenna-for-hf, by Phil Frost - W8II, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
