# Using a Duplexer and Diplexer in Series

*Tags: repeater, crossband-repeat, duplexer · score 3*

## Question

I have 3 Motorola CDM750s that I’m using to build a multi-purpose, portable, temporary repeater. There are 1 VHF and 2 UHF radios. I want to be able to use it as either an in-band UHF repeater or as a UHF/VHF cross-band repeater. I have a duplexer tuned to the UHF frequencies I plan on using and a UHF/VHF diplexer for the cross-band configuration. The antenna will be a Diamond X30A dual band base/repeater antenna.

I would like to make it fairly simple for someone to change the configuration. I wonder if I could run the duplexer and diplexer in series so it would be unnecessary to reconfigure the antenna cabling. Basically, the 2 UHF radios would go to the duplexer and then the antenna feed from that goes to the UHF side of the diplexer, where it combines with the VHF feed.

I realize I’ll have to use the same input frequency on both the in-band and cross-band repeaters, but that’s not a big deal.

Is there any reason why this wouldn’t work?

If this is a bad idea, I would appreciate alternate suggestions.

## Accepted answer (score 6, by Glenn W9IQ)

Yes, it will work with the proper attention to details. I have done the same in the past at two repeater sites to take advantage of the coverage of the dual band antenna.

Do take care as the third harmonic of two meter frequencies can come close to 70 cm frequencies. You will want to plan your frequencies to keep as much separation as possible. Making the 2 meter radio the receiver when cross banding largely avoids this issue.

Care should also be taken to use double or quad shielded coax with N connectors throughout and to carefully decouple all control lines and power cables between the radios. You may also need to incorporate additional shielding between the radios.

Before building the repeater, it is a good idea to check the spectral purity of the transmitters with a spectrum analyzer. This can save hours of frustrating debug time later. When you have the SA setup, also check the UHF to VHF ports isolation of your diplexer. I found that performance to specs varies widely.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10321/using-a-duplexer-and-diplexer-in-series, by Lance, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
