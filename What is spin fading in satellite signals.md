# What is spin fading in satellite signals?

*Tags: satellites · score 6*

## Question

Why do signals from satellites experience "spin fading" as the satellite rotates? What are the effects that spin fading has on a radio signal?

From test question: T8B09

## Accepted answer (score 7, by Paul)

Take the simplest case of a VHF dipole receiving antenna on board a spin stabilized satellite.

-----------O------------- Here is the satellite now.

```
\
\
\
\
\
O                       and here is is a bit later
\
\
\
\
\

```

As the satellite spins, the dipole rotates, and the resulting polarization of the dipole also rotates. For instance it may go from horizontal polarization to vertical and back again.

If you transmit to the satellite with a horizontal or vertical polarized yagi, your transmit yagi will sometimes have the same polarization as the receive at the satellite and sometimes it will not. When the polarizations are different there can be cross polarization loss of up to 20-30db.

This is the phenomena behind spin fading. It can be corrected by using circular polarization at the transmitting or receiving location or both. The loss of a linear polarization antenna from/to a circular one is about a constant 3db over the case where both of the antennas are circular polarized, and because it is constant it is not affected by spin.

If you have a couple of loose polarized sunglass lenses, you can place them against each other and rotate one of them while keeping the other stationary, you will see a similar effect with the variable attenuation of light travelling through the pair of lenses.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/768/what-is-spin-fading-in-satellite-signals, by JC Hulce, Paul. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
