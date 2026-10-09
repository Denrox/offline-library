# Will two nearby yagis on different bands interfere when transmitting at the same time?

*Tags: antenna, yagi · score 3*

## Question

I'm working on a digital ham radio project that will require two 2m and/or 70cm yagi antennas to be transmitting and receiving in somewhat close proximity to each other. Each will have it's own transceiver.

A few questions:

- If I went with only 2m antennas, but they were pointed in different directions, how far apart would they have to be to not interfere with each other (or blow out the other's transceiver)?
- If I went with one 2m and one 70cm antenna, are there any concerns with them being close to one another?
- Should I add any bandpass filtering to either system?

Note that each antenna will have it's own transceiver for this project, so I need to ensure the two systems don't interfere or damage each other.

Until now I've only ever operated a single system on a single band, so I'm not sure what considerations I should be careful of for multiple active yagis.

Thanks!

## Accepted answer (score 2, by Andrew)

The answer to your questions depends on a number of things.

1. RF output power of the transceivers.
2. Maximum allowable input signal for the receivers before damage will occur.
3. Out of band rejection specs for the receivers.
4. Exactly which directions the antennas are pointing.
5. Radiation pattern of the antennas.

And you need to consider the following.

1. Interference to operation of each radio from the other.
2. Damaging the receivers due to excessive signal amplitude from the other radio when it's transmitting.
3. If you are transmitting on both radios at the same time, damage caused by an increase in SWR caused by close proximity of the other transmitter.

Definitely, if you go with different bands for each transceiver and use 2 m for one and 70 cm for the other, then the possibility of interference and damage is much reduced.

Also, the less output power, the less possibility of interference and damage.

Due to the factors involved, it's hard to say how far apart the antennas should be.

As a very generic guess, i would say that you should keep the antennas at least a few wavelengths away from each other, and not pointed towards each other, so let's say minimum 4 - 6 m apart, and note that it seems most modern radios have protection on the receiver input so damage is not likely, though you may want to check this.

The increase in SWR caused by transmitting at the same time is definitely a problem, i would just check with an SWR meter to see if it changes when you key up the other transmitter.

If you are using two different bands, and keep both antennas pointed away from each other, so long as the distant signals you are receiving are not too weak, you shouldn't need band pass filters.

Hope that helps !

## Answer (score 2, by user10489)

A few things to consider here:


Yagi antennas have a moderate front to back ratio. The isolation is greater front to side. If they are pointed in exact opposite directions, they will eat each other's back lobes, which are substantial.


70cm and 2m are third harmonics, and in some cases, a 2m antenna works well on 70cm, so isolation is difficult for the antenna. If the geometry isn't carefully selected, very likely the two antennas will interact which can warp their radiation patterns.


2m and 70cm are separate bands, and it is trivial to make a filter circuit to isolate them well, and most radios have that, so there actually should be minimal interaction between them, and damage at moderate power is extremely unlikely.


When doing satellite work, people frequently use things like the Arrow yagi, which puts a 2m and 70cm antennas interleaved on the same boom, cross polarized from each other. This is used for simultaneous transmit and receive (at 5w however), so at least in this circumstance, separation is not an issue, although the cross polarization does give some isolation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21074/will-two-nearby-yagis-on-different-bands-interfere-when-transmitting-at-the-sa, by User5754448, Andrew, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
