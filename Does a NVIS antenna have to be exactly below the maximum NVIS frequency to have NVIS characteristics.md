# Does a NVIS antenna have to be exactly below the maximum NVIS frequency to have NVIS characteristics?

*Tags: antenna, hf, nvis · score 3*

## Question

For example if the maximum NVIS frequency is 5 MHz in a given region, would a NVIS antenna have to be resonant at less than 5 MHz to have NVIS propagation characteristics or can it be slightly above the maximum NVIS frequency (say resonant at 5.5MHz or 6MHz).

Can non-NVIS antennas receive signals transmitted using a NVIS antenna?

## Accepted answer (score 3, by hobbs - KC2G)

There are two things going on here.

First off, NVIS *propagation*. This is a function of the ionosphere and of your *operating frequency*, not the frequency that the antenna is "resonant" on. If you are working below the critical frequency, NVIS "works". If you are working above the critical frequency, nearby stations will be "in your skip" and won't hear you. Say you're working at 7MHz and the critical frequency is 6MHz, then your skip distance will be around 360km; if the critical frequency drops to 5MHz, then your skip distance increases to around 600km. Stations inside that radius generally won't hear you (unless you can work them line-of-sight or groundwave, of course).

Second, "NVIS antennas". An NVIS antenna is simply one that has a lot of high-angle radiation, no major high-angle nulls, and relatively little gain towards the horizon. Usually, these are horizontally-polarized antennas at low heights (compared to the operating wavelength). You don't *need* an NVIS antenna on either end, — it's just a few extra dB of gain in the direction of interest. Under some conditions you might need those few dB, but generally not.

## Answer (score 5, by user10489)

NVIS is Near Vertical Incident Skywave

What makes an antenna NVIS is not the resonant frequency, but that its radiation pattern has a high elevation angle and is directed nearly up. What makes an NVIS antenna *work* is for the frequency in use to reflect at the angle it hits the ionosphere. If you are out of the usable frequency range (the range that reflects well), NVIS may not be very effective.

This varies, not by region, but by time and space weather conditions.

Can a non-NVIS antenna receive signals from an NVIS antenna? Sure... but if the incoming signal comes at an angle that happens to be a null in the receiving antenna, the signal may be attenuated. Most antennas are not that selective and there's enough spreading and scattering that this typically is not a big problem. (And horizontal antennas don't have an upward pointing null.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18796/does-a-nvis-antenna-have-to-be-exactly-below-the-maximum-nvis-frequency-to-hav, by Aiden Kaiser, hobbs - KC2G, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
