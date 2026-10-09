# What determines the optimum frequency range for the transmission of signals?

*Tags: antenna, propagation, satellites, frequency · score 4*

## Question

What determines the optimum frequency range for the transmission of signals in a system that's transmitting electromagnetic signals between an antenna on the surface of the earth and an orbiting satellite antenna.

## Answer (score 4, by Juancho)

Many factors, and since your question is so broad, a broad answer follows:

The signal bandwidth (amount of information per second) will determine a minimum carrier frequency. In practice, the modulated signal should have a bandwidth of not more than say 1% of the carrier frequency.

Then, at lower carrier frequencies, you need to consider antenna size (which can be too large for a satellite), and ionospheric effects (mostly in HF range).

Commercial satellites communicate in the microwave range (L band, all the way to the K bands and above).

At high carrier frequencies, atmospheric attenuation becomes a problem. Also clouds and rain provide attenuation in the K bands.

Small amateur radio satellites normally operate in UHF and VHF, but those frequencies allow for a very small bandwidth (1200 or 9600 bits per second).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3774/what-determines-the-optimum-frequency-range-for-the-transmission-of-signals, by Max, Juancho. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
