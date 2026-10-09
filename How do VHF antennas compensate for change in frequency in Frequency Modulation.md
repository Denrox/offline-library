# How do VHF antennas compensate for change in frequency in Frequency Modulation?

*Tags: antenna, antenna-theory, antenna-construction, fm · score 3*

## Question

I would like to understand how antennas specifically, compensate for variability in the frequency while receiving FM waves in VHF. The way FM works is that the receiver system - receiver and antenna locks on to a central frequency to receive a signal. Now, once the central frequency is locked how does the antenna vary its \lambda to receive the modulated wave ( at the new frequency)? Or does this antenna have a frequency tolerance? E.g. λ * 0.95 to λ * 1.05. The extra 0.05 accommodates the variation in frequency due to modulation?

Reference to how FM works: [How does FM station have fixed frequency when FM modulation changes the frequency?](How%20does%20FM%20station%20have%20fixed%20frequency%20when%20FM%20modulation%20changes%20the%20frequency.md)

Edit: Specified the 2m Band.

## Accepted answer (score 6, by Mike Waters)

Most VHF+ antennas are not that narrow banded. They usually have a low enough Q.

Thus, there is usually no need for a tunable antenna.

Also, antennas are generally not any different regardless of the modulation type.

## Answer (score 10, by user10489)

All modulated signals, not just FM, have a bandwidth. The antenna has a bandwidth, which must be wider than the modulation of the signal you are using.

Note that receive bandwidth and transmit bandwidth may be different, but generally it is actually difficult to make an antenna with a bandwidth so narrow (for either) that it would be a problem with FM.

## Answer (score 6, by Kevin Reid AG6YO)

Or does this antenna have a frequency tolerance?

This is closest, but the antenna, itself, does not actually have a “frequency tolerance” (more usually called a *bandwidth*). Rather, the antenna's properties, including impedance/SWR, radiation pattern, and losses, vary with frequency, and the range of frequencies over which you *can* transmit are mainly determined by your transmitter's ability to cope with varying impedance of the antenna — i.e. how high a SWR it can transmit into.

If you read the documentation for an antenna, it may specify a frequency range, but that will always mean something like “the SWR will be no higher than [x] between frequency [a] and frequency [b]”. If you choose a higher acceptable SWR, the range becomes wider.

However, this is more relevant for tuning range than for the ability to transmit FM — **typical antennas will have usable SWR over a *much* wider frequency range than any individual signal's bandwidth or FM deviation.** Consider this: if they didn't, then you couldn't change your transmit carrier frequency without modifying the antenna, since a meaningful change of transmit frequency is one which is wider than an individual signal's bandwidth!

(Some types of antennas amateurs use, such as the “magnetic loop” antenna, have much narrower bandwidths to the point of requiring retuning — changing the antenna impedance to be favorable at the desired frequency — for frequency changes within a band. These antennas have their own tuning mechanisms designed for frequent use, unlike dipole or vertical antennas where the tuning mechanism is usually “cut to the correct length”.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18774/how-do-vhf-antennas-compensate-for-change-in-frequency-in-frequency-modulation, by Bartha, Mike Waters, user10489, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
