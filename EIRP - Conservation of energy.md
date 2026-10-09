# EIRP - Conservation of energy

*Tags: theory · score 3*

## Question

I have a theoretical question about EIRP.

EIRP is calculated by summing the power of the radio (the intentional radiator, IR) plus the gain of the antenna (dBd/dBi) minus the sum of the losses. The calculated value is equivalent to the power which a isotropic radiator would need to provide the same power density as the original antenna in the direction of maximum gain.

Is this statement true:

"Since antennas are passive elements it would not be possible to measure more power on any given theoretical client than the power (Watts (Energy/Time)) provided by the I.R. The gain of the antenna increases the power intensity, applying the same amount of power to a smaller area but does not change the total radiated power."

## Accepted answer (score 3, by webmarc)

I **think** what you're asking is: If a radio+antenna system transmits X Watts, then regardless of the configuration of EITHER the transmitting antenna OR the receiving antenna, the power measured at the receiving antenna can never be MORE than X Watts.

And that would be correct.

An isotropic radiator of 50 Watts would spread that power out evenly on the surface area of a sphere (${4\pi{r^2}}$) so that 50 watts diminishes rather quickly with distance from the radiator.

An antenna with gain will reshape that energy distribution into something with greater density in some areas and less (or none) in others. But no practical antennal will EVER put all 50 Watts into a single direction and zero power in all other directions.

This means that there is already far less power arriving at the receiving antenna.

And the receiving isotropic antenna will be sensitive to energy from all directions equally. Designing it for gain in a direction has the practical effect of making it appear "larger" in one direction and "smaller" in others, but there is no way to make it appear SO large that it will capture ALL of a transmitted signal. The measured gain for the receiving antenna is in terms of dBi again, NOT dBm.

## Answer (score 3, by hotpaw2)

That’s just conservation of energy.

In the one dimensional case, 100 mW would “isotropically” radiate 50 mW backwards and 50 mW forwards. A one dimensional 3 dB directional gain would just move that energy around to radiating all 100 mW forwards. If you put a set of receive antennas both in front and behind that 1D transmitting antenna, they would capture the same sum total amount in both cases (minus system losses).

The 3D case just moves that ratio-ing around to fractions of a sphere or steradians.

## Answer (score 2, by Juancho)

The following statement:

The calculated value is equivalent to the power which a isotropic radiator would use to provide the same power of the system.

is somewhat confusing.

The calculated value for EIRP is equivalent to the power an isotropic radiator would **need** to provide the same power density as the original antenna in the direction of maximum gain.

This needed power is greater than the power fed to the antenna: the isotropic radiator distributes power equally in all directions, while the original antenna concentrates power in the direction of maximum gain.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20039/eirp-conservation-of-energy, by 377ohms, webmarc, hotpaw2, Juancho. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
