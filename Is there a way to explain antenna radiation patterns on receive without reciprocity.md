# Is there a way to explain antenna radiation patterns on receive without reciprocity?

*Tags: antenna-theory · score 3*

## Question

I don't consider myself an expert, but I have a fairly decent understanding of radio. I belong to a club that includes a number of people who have less theoretical background.

I understand that reciprocity for an antenna means that we can calculate properties for an antenna when transmitting, when it is more intuitive and then we "hand wave" and say that reciprocity exists and because of that, we can apply the same parameters to an antenna being used in receive mode.

Is there a way to explain this to someone with less experience without having to invoke reciprocity?

Edit: the following is a secondary part of this question and is of lesser importance.

If not, is there a way to explain it to someone with more experience at a higher level than Maxwell's equations or the like?

Also I am not questioning Reciprocity, but it may not be intuitive to some. The comment by Brian K1LI may imply the best answer. "Don't try to explain **without** Reciprocity, but **explain Reciprocity**, if necessary.

Clarification by a simple example: If I want to explain why a Yagi has a null on receive, I can invoke reciprocity and say there is a null in various places or gain in various places because that is what it looks like when it is transmitting. Some people may be fine with that, especially if I explain why the principle holds, but It may not be an obvious answer.

Added April 17: I'm not sure what answer to accept. Most of them have some useful or interesting pieces, but none of them really provide a good answer to my question. What is the proper protocol on this site? I'm happy to write up an answer that is a combination of what was said by everyone, but I also want to give credit to those who have provided answers.

## Answer (score 3, by Brian K1LI)

If I want to explain why a Yagi has a null on receive, I can invoke reciprocity and say there is a null in various places or gain in various places because that is what it looks like when it is transmitting.

You could take that approach, but it isn't the only approach you could take. As with any antenna, the explanation begins with the nature of the (transverse) electromagnetic wave that arrives at the antenna:

This linearly- and vertically-polarized wave - so called because of the orientation of the electric field vectors - will induce the largest currents in a conductor that is perfectly aligned with the $E$ field: a "vertical," in ham parlance.

At a great distance from the transmitting antenna, each of the $E$ field vectors extends to form an $xy$ plane; this plane is a *wavefront*, a plane on which the amplitude and phase of the $E$ field is everywhere the same. Depending on the relative orientation of the transmitting and receiving antennas, the wavefront will arrive at an angle, $\theta$, to the receiving antenna conductor:

At each point where the wavefront intersects the antenna, the $E$ field will have a component along the direction of the antenna conductor which can induce a current in the antenna. As the wavefront proceeds to cut across the antenna conductor, the arrival time of the wavefront will be delayed from the earlier points of intersection, introducing a *phase difference* between the currents induced at the successive points of intersection. Summing the amplitudes and phases of the individual interactions determines the total current on the conductor. Finding this response for all arrival angles establishes the pattern of the antenna.

In the case of a dipole - which, we should remember, may be an element of a yagi - the maximum induced current occurs when $\theta$=0 because all of the $E$ field vectors align perfectly with the antenna conductor and arrive at the same time (i.e., no phase differences). Conversely, when $\theta$=90$^\circ$ - that is, when the wave arrives "off the side" of the antenna - there is no component of the $E$ field along the direction of the antenna, so no current is induced.

## Answer (score 2, by Brian K1LI)

According to Wikipedia, the Lorentz Reciprocity theorem loosely states that:

...the relationship between an oscillating current and the resulting electric field is unchanged if one interchanges the points where the current is placed and where the field is measured.

As shown in the citation, Maxwell's equations can be manipulated to show this is correct, but a simple experiment may help to understand it intuitively.

Place two, center-fed, vertically oriented, half-wave dipoles 10 wavelengths apart:

Using antenna simulation software, driving dipole 1 with a 1A RF current source induces a peak current of 26mA in dipole 2. Conversely, driving dipole 2 with a 1A RF current source induces a peak current of 26mA in dipole 1. This demonstrates the effect of reciprocity.

There is nothing special about the nature or disposition of the two antennas in the example. Repeating the experiment with the two antennas in any arrangement produces the same reciprocal result, as long as the antennas are in each other's far field. You can measure the pattern of antenna 1 by moving antenna 2 throughout the space surrounding antenna 1, while keeping antenna 2 "aimed at" antenna 1. Using a very short dipole for antenna 2 approximates the pattern of an isotropic radiator, making such "aiming" less critical.

## Answer (score 2, by Phil Frost - W8II)

Sure, you "just" have to calculate the electromagnetic waves generated by the transmitter, how these will interact with the receiving antenna and the mobile charges in them, and how this will result in transmitting electromagnetic forces through the antenna, ultimately to the feedline, and then the receiver.

It's really a problem no different than transmitting, but in the other direction. Maxwell's equations already provide the mathematical basis for doing this, and software exists to numerically solve the problem. For example if you've ever modeled a Yagi in NEC, each of the parasitic elements is in a way a "receiving" the radiation from the other elements around it.

So in invoking reciprocity isn't necessary to explain radiation patterns, though it is often more practical. It's often easier, either in simulation or in a real test, to consider the antenna as transmitting then measure the field around the antenna, than it is to set up a transmitter and measure the received power, then move the transmitter and repeat the experiment dozens or hundreds of times until the antenna pattern is resolved with sufficient resolution.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13253/is-there-a-way-to-explain-antenna-radiation-patterns-on-receive-without-recipr, by user3034958, Brian K1LI, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
