# Does modulation affect propagation?

*Tags: propagation, transmission, modes · score 10*

## Question

Does the modulation scheme, whether OOK, SSB, AM, FM, a digital mode, etc, affect the propagation of a signal?

## Accepted answer (score 9, by Phil Frost - W8II)

It depends on what you mean by *propagation*. If you mean, *does the modulation scheme affect the physical means by which EM energy gets from point A to point B?*, then the answer is *no*. Mostly, EM propagation is linear, so the differences in modulation have little effect on how the wave propagate.

However, if you expand *propagation* to include the intelligibility of the signal at the other end, modulation can make a very big difference. Though propagation can practically be considered linear, it is not time-invariant. On VHF and UHF it's common for the transmitter or receiver to be moving. At HF, the ionosphere constantly changes, significantly altering propagation. Across all the amateur frequencies, there are properties about the radio channel that vary with time.

Different modulation schemes may be more or less robust against the disruptions encountered in practical RF channels. For example, the frequency division multiplexing used in FreeDV provides good robustness against comb filtering caused by multipath propagation. It also provides forward error correction for additional robustness. This is why FreeDV can transmit a 1275 bit/s voice codec with better reliability and less bandwidth than 300 baud FSK.

The differences among analog modulation schemes are less complex, but they still exist. CW works well for communication under adverse conditions because all of the transmitter power is focused in a very narrow carrier. On the other hand, AM spreads this same transmitter power over a wider bandwidth, and in that same bandwidth there is more noise the transmitter must overcome. Thus the principal advantage of SSB: it eliminates power wasted in the carrier and the 2nd sideband which carry no information. Furthermore, the wetware that decodes the baseband signal in analog modulation schemes is much better at detecting the pure tone of CW vs. the complex sound of a human voice in AM or SSB.

## Answer (score 4, by Dan KD2EE)

Usually, the answer is no. While modulation may affect the acceptable Signal to Noise ratio, allowing a given signal to be received from further away or in worse conditions than a different modulation, that happens at the receiver, the propagation is the same. The only factors of a radio wave that affect propagation, once it's in the air, are the field strength, frequency, and polarization.

The only slight wrinkle in this that I can think of has to do with multipath distortion. Multipath distortion happens when signals are reflected by multiple surfaces and take more than one path from transmitter to receiever, of different lengths. Radio waves move at about $3*10^8 m/s$, so if one path is $35cm$ longer than another, and the radio wave is at $440MHz$ (with a $70cm$ wavelength), then they will arrive and cancel out perfectly. The modulation can affect this somewhat - but not by very much - simply because a CW signal has a much tighter bandwidth and is affected much more uniformly by multipath distortion than a very wide band (or even frequency-hopping) signal would.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/763/does-modulation-affect-propagation, by Adam Davis, Phil Frost - W8II, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
