# What does radiation power mean?

*Tags: rf-power, transmitter · score 5*

## Question

I would like to ask you what it means when it is written that a transmitter has 10 dBm power.

Does that mean that 10 dBm is provided to the antenna, or that 10 dBm is measured at particular frequency at the receiving side?

## Answer (score 6, by Juancho)

This means that the transmitter output power (to the antenna) is 10 dBm (which is $10^{1.0}\, \rm{mW} = 10\, \rm{mW}$).

Normally this is valid at the rated output impedance. If the transmission line or antenna are not matched to the transmitter output impedance, less power will be effectively irradiated by the antenna.

## Answer (score 2, by Joseph Freivald)

The power rating is at the output of the transmitter at the rated frequency. Feedline, impedance mismatch, antenna efficiency, directivity and gain and other losses & gains will affect the Effective Isotropic Radiated Power (EIRP).

EIRP is a measure of power output of the antenna in reference to a theoretical antenna that radiates power equally in all directions in free space.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4897/what-does-radiation-power-mean, by Nexy_sm, Juancho, Joseph Freivald. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
