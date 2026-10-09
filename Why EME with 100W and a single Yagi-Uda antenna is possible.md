# Why EME with 100W and a single Yagi-Uda antenna is possible?

*Tags: math, eme · score 7*

## Question

Recently I've been reading about EME and there was one thing that surprised me. Many sources claim that EME has path loss for 2m band about 252 dB. In the same time they claim (one, two):

Recent advances in digital signal processing have allowed EME contacts, admittedly with low data rate, to take place with powers in the order of 100 Watts and a single Yagi–Uda antenna. [About 8-9 elements according to other sources.]

100W is 50 dBm and the common sensitivity of the receiver is about 0.11 uV (the number for Yaesu FT-991A, SSB @ 2m band) or:

```
>>> from math import pow, log10
>>> 10*log10(1000*pow((0.11/1000/1000),2)/50)
-126.16184634019568

```

... -126 dB. Assuming that all 50 dBm are radiated straight to the moon (ideal radiation pattern of the antenna):

```
>>> 50-252
-202

```

... we are not even close to -126 dB. So what is actual relation between path loss, receiver sensitivity, and also used power and antennas gain?

## Accepted answer (score 16, by hobbs - KC2G)

1.

You didn't include antenna gain at all. That number for the path loss is a starting point assuming *zero* gain (isotropic antennas) on both ends. This isn't a realistic situation, because of course the vast majority of the signal from an isotropic antenna doesn't reach the moon at all, but it's conventional for calculating link budgets. A 9-element Yagi has a gain of about 13.4 dBi, so one of these on each end gives an improvement of 26.8 dB.

2.

A receive pre-amplifier at the antenna makes the minimum discernable signal of the receiver basically irrelevant. With enough gain, we can bring any signal above the receiver's MDS. Instead we're concerned about the noise floor, which is characterized by something called "system noise temperature". An achievable value of noise temperature for 144MHz, without any heroic measures, is 300 K, which equals a noise-in-2500Hz of -228.6 + 10*log(300 * 2500) = -169.8 dBW = -139.8 dBm (ref).

3.

JT65 decodes at 27dB below the noise-in-2500Hz, so our target is -167.8 dBm.

4.

Now adding it all up we have 50dBm (transmit power) + 13.4dB (tx ant gain) - 252 dB (path loss) + 13.4 dB (rx ant gain) = -175.2 dBm. Compared to our JT65 receive threshold of -167.8 dBm we're still 7.4 dB short. So close, but still very far! How do we resolve this? Well... the truth is that a small station can't be heard by another small station. But a small station can be heard by a *larger* station, with a bigger antenna. So let's replace one of the 13.4 dB, 9-element yagis with a 2x2 array of 10-element yagis as described by KL7UW. These have a gain of 21.3 dBi. Now we're at 50 + 13.4 - 252 + 21.3 = -167.3 dBm, just squeaking in at half a dB above the JT65 decode threshold.

There's a lot of variables here... there's room to improve things slightly (lower noise preamps, maybe a 200W transmitter, maybe some "ground gain" with the moon near the horizon), and also room for things to get worse (if cables aren't done very carefully, if the moon is in a "noisier" part of the sky, if the moon is further away than usual), but I think this goes to show that a "small" 100W-and-9-elements station is right in the ballpark of being decoded by a medium-sized station, under good conditions, which is exactly what people are reporting, and that it isn't 75dB away.

If the other end is a *really big* station (HB9Q, KP4AO, DL7APV, or the like) it becomes possible for a smaller station to work them even under less-than-ideal conditions, and there are even people who have worked them with 2 elements, or a dipole. Antenna gain is a very powerful thing.

## Answer (score 3, by Phil Frost - W8II)

From the linked manual:

Notice these sensitivities each specify a mode, and some threshold (10 dB S+N/N, 12 dB SINAD). For digital modes a bit error rate (BER) would be specified.

Some modes are more sensitive than others. For example, WSPR takes 2 minutes to send a call, transmit power, and grid square, whereas the SSB transmission of the same information would take perhaps five seconds. If each is transmitted at 10 W, the WSPR signal contains a total energy of:

$$ 120\:\mathrm s \times 10\:\mathrm W = 1200\:\mathrm J $$

whereas the SSB signal contains:

$$ 5\:\mathrm s \times 10\:\mathrm W = 50\:\mathrm J $$

Detecting 1200 joules of radiated energy is much easier than 50 joules. Even though they each have the same amplitude, the WSPR signal is transmitted over a longer time. The noise which obscures the signal is random: over time it averages to zero. The signal is not: the longer it is measured, the more bias it introduces into the detection. Thus, given a sufficiently low data rate ("admittedly with low data rate") and sufficient attention to the details of propagation effects and appropriate engineering to overcome them ("Recent advances in digital signal processing") it's possible to establish communication at lower amplitudes.

## Answer (score 3, by Richard Fry)

RE: *...So what is actual relation between path loss, receiver sensitivity, and also used power and antennas gain?*

The Friis transmission equation is useful to determine such for a free-space, far-field propagation path (see the example below).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15974/why-eme-with-100w-and-a-single-yagi-uda-antenna-is-possible, by Aleksander Alekseev - R2AUK, hobbs - KC2G, Phil Frost - W8II, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
