# Long range HF polarization

*Tags: hf, propagation, polarization · score 3*

## Question

Is it possible to polarize HF signal (20-30m) at long range (thousands of km)?

*It was commented in my over questions that polarization is not feasible at long range. However in this article is specifically mentioned long range HF polarization: https://www.electronics-notes.com/articles/antennas-propagation/antenna-theory/polarisation-polarization.php*

## Accepted answer (score 5, by user10489)

It is useful to use polarization of HF signals, but not for the same reasons you'd do that with a VHF signal, and the effects are radically different for groundwave vs. skywave propagation.

Groundwave propagation is generally considered the same as line of sight, but this isn't strictly true, as line of sight is free space propagation, where groundwave propagation is ... near the ground. As such, conductivity of the ground affects it and some refraction occurs towards the ground, extending the range of propagation on a curved surface. Horizontally polarized signals are refracted differently than vertically polarized signals, allowing vertically polarized signals to travel slightly further. (Also, the amount of refraction is larger for longer wavelengths, and different polarizations have to deal with different types of noise.)

Skywave propagation occurs when a signal bounces (really, refracts) from the ionosphere. Part of the refraction process can cause the linear polarized signal (both H and V) to be split into two circular polarized signals, clockwise and counterclockwise (faraday rotation). These signals may have variations in their propagation such that when received, they may be somewhat out of phase with each other. A linear polarized receive antenna will mix the two signals. Under certain conditions, after mixing, constructive and destructive interference effects will cause the mixed signal to fade and become stronger in a periodic fashion (selective fading). A circular polarized antenna can be used to try to receive only one of the two signals and reduce selective fading.

So, for a groundwave signal (hundreds of miles), picking your (linear) polarization may help.

For skywave propagation (more than 400 miles), the transmitted polarization will be randomized (as the path length changes), but a circular polarized receive antenna may help. In this case, transmitted polarization can't be controlled, but received (circular) polarization can be taken advantage of.

The understanding of polarization effects on groundwave propagation has been well understood for a long time, but complete understanding of the causes and effects of polarization on skywave propagation by the amateur radio community is relatively recent, and a lot of literature predates this and just says you can't polarize skywave, which while mostly true, is not the whole story. (Constructing an HF circular polarized antenna is left as an exercise for the reader.)

Edit: Here is a 1967 paper that goes into detail on this topic. https://apps.dtic.mil/dtic/tr/fulltext/u2/663707.pdf Polarization of Ionospherically Propagated Waves, M. R. Epstein. October 1967. Technical Report No. 143, Office of Naval Research Contract Nonr-225(64)

Page 6-7 describes how the signal is split into LCP and RCP signals.

## Answer (score 6, by Phil Frost - W8II)

All radio signals are polarized. You can't *not* polarize an HF signal.

The problem with HF is often we're considering skywave propagation, which involves reflections off the ionosphere and ground. Every reflection has the potential to alter the polarization. Furthermore, there are usually many possible paths from transmitter to receiver, involving reflections at different angles and different atmospheric heights. All theses paths happen simultaneously, and they may interfere with each other constructively or destructively.

As such, it's not feasible to predict what the polarization will be at the receiver. And worse yet, the ionosphere consists of gasses moving all the time, so the conditions are changing every second. So at any given time, there is an optimal polarization for the receiving antenna, but:

1. it's not feasible to predict what it will be, and
2. every few seconds the polarization may change.

Consequently, if you can pick only one polarization, it doesn't really matter what you pick. Sometimes it will be the right one, and sometimes it will be the wrong one, and one must simply deal with the consequent variable fading of the signal.

Alternatively, it's possible to set up two antennas with orthogonal polarization, and then dynamically pick the best one in the moment. This is called polarization diversity. While this is common practice in all kinds of modern communication (cell phones, WiFi, military communications) it's not so common for amateurs. LZ1AQ has some nice demonstrations.

## Answer (score 5, by rclocher3)

From the Wikipedia article on HF: "Long-distance (skywave) receiving antennas can generally be oriented either vertically or horizontally since refraction through the ionosphere usually scrambles signal polarization, and signals are received directly from the sky to the antenna."

Every RF signal radiated by an antenna is polarized. I believe you meant to ask if an antenna receiving a long-range HF signal can take advantage of the polarization of the incoming signal. If that's what you meant to ask, then the answer is generally no, because typically long-range HF signals arrive randomly polarized, because they are "sky wave" signals that have been bounced off of the ionosphere, or to be more correct, refracted through the ionosphere.

There are a few exceptions. If the receiving antenna is more-or-less within line of sight of the transmitting antenna, then the signal will be received in the same polarization as it was sent. Ground wave propagation is another exception; that requires vertical polarization, and generally requires lower frequencies (that are strongly attenuated in the daytime) and has shorter range than sky wave propagation. Ground wave propagation is typically how AM broadcast stations can be received beyond line-of-sight range during the daytime. Unfortunately, both of the mentioned exceptions have shorter range.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16856/long-range-hf-polarization, by Boppity Bop, user10489, Phil Frost - W8II, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
