# Benefit to remote antenna tuner for end-fed non-resonant antenna?

*Tags: antenna, rfi, antenna-tuner · score 3*

## Question

Does addition of a remote feed-point antenna tuner affect the use of the coax braid as a radiator? If it no longer "radiates" in such a setup, what does? Is a shack or remote tuner better for surpression of common mode currents and RFI noise reduction?

Many references suggest use of an external tuner rather than a shack tuner:

"With a tuner at the antenna there is no mismatched tranmission line to exhibit increased loss due to a high VSWR. The coaxial transmission line between the tuner and the transmitter is operated at a low VSWR (near 1:1) and exhibits no extra loss."

At the same time, my understanding from other sources is that in a non-resonant antenna setup, the coax itself acts as a radiator.

## Answer (score 5, by Phil Frost - W8II)

The benefit of placing a tuner at the antenna (rather than at the transmitter) in any circumstance is a reduction in the SWR on the coax. This results in a [reduction of losses](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md).

There's a bit of myth that a bad SWR causes common mode current (radiating coax), but this isn't the whole picture. At the feedpoint, current is divided between the common and differential modes according to their relative impedances, just like current divides between parallel resistors. Common-mode current isn't the result of a bad SWR *per se*, but rather a differential mode impedance which fails to be significantly higher than the alternative (usually, the common-mode of the antenna, assuming there's a properly designed antenna such that it's possible).

For example, assume a [resonant dipole with a balun](Using%20a%20balun%20with%20a%20resonant%20dipole.md) which results in a common-mode impedance of 5000 ohms. The differential-mode impedance of a half-wave dipole is somewhere around 72 ohms.

With the half-wave dipole the SWR meter might indicate 75/50 = 1.44:1, not bad. Because 72 is much less than 5000, almost all the current will be differential mode.

Now imagine the dipole is a full wavelength long, where its impedance might be 5000 ohms. The SWR meter in this case will indicate something very high. Because the differential and common modes have equal impedances, half the current will be differential mode. One might conjecture a bad SWR leads to common-mode current.

But what if the end of the coax has not an antenna, but a short? In this case the differential-mode current is 0 ohms, and there will be no common-mode current. But there will be a horrible SWR.

Or consider a half-wave dipole as before, but with no balun and a feedline that is a quarter wavelength long. This will result in a very low common mode impedance: the coax in this case is effectively just as good as another dipole leg. There will be horrible common mode current problems, despite what's likely a good indicated SWR.

All current must be balanced by an opposite current somewhere, because charge is never created nor destroyed. An end-fed antenna is very much like a vertical without any radials. The balancing current comes from "ground", whatever that might be. It might the ground, as in Earth's surface. But usually the coax shield is closer and more conductive, and it functions as a single radial.

If you aim to reduce common-mode current in an end-fed antenna, you can do two things:

1. Add chokes to increase the common-mode impedance.
2. Add radials or some other kind of counterpoise to provide a lower impedance path for that balancing current. (In doing so you might also avoid Earth currents, increasing the efficiency of the antenna.)

Remember that the current will favor the lowest impedance path available, so adding chokes when there's not a lower-impedance alternative is futile.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10567/benefit-to-remote-antenna-tuner-for-end-fed-non-resonant-antenna, by Jeremy Gilbert, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
