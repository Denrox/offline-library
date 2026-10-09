# Can sub GHZ frequency can be used in space communciation?

*Tags: satellites · score 3*

## Question

Is it possible for a sub GHZ frequency (Say 300 Mhz) can be used for space communication for small satellites such as a cubesat? What are the advantages and disadvantages for this.

## Accepted answer (score 4, by Juancho)

Most cubesats communicate in a combination of VHF and UHF for both uplink and downlink.

Advantages:

- Better link budget (lower free-space attenuation).
- Cheaper ground station (radio equipment, cables, antennas).
- Lots of support worldwide in amateur bands (144 and 430 MHz bands).
- No need for directional antennas (and fine attitude control) on the spacecraft.

Disadvantages:

- Limited bandwidth (in the order of 10 kbps maximum).

Only a few cubesats have S or X band downlinks, and always as high-bandwidth extension to the main TT&C downlink.

## Answer (score 3, by Phil Frost - W8II)

Certainly possible. 300 MHz is not a very low frequency for satellites. There are a great many amateur satellites operating on the 2m band, around 145.8 MHz.

Going much lower, there are allocations for satellites on the 10 meter band, from 29.3 to 29.51 MHz. There are fewer amateur satellites operating here, but they do exist.

In fact, early in space exploration history, HF was used regularly for communications. For example, Yuri Gagarin in Vostok 1 sent several reports via HF.

HF for space communication has the same advantages and disadvantages as it does for terrestrial communication, more or less.

The big advantage: HF supports skywave propagation, so you may get propagation beyond line of light. There are layers of the ionosphere that are high enough to still be above some low Earth orbits. For example, Vostok 1's orbit varied between 168 and 327 km; the F layer is around 300 km.

Also, lower frequencies require less sophisticated technology, generally. Of course this is becoming less of a concern in modern times since microwave radios are commodity items now.

The big disadvantage of HF is that antennas are larger and frequency allocations are more expensive and less available. As an example, the 70cm amateur allocation in the US goes from 420 to 450 MHz and is 30 MHz wide. You could fit the entire HF spectrum in that. Commercial availability of spectrum is similarly rarer at lower frequencies.

Additionally, high-speed communications are more difficult at HF due to the higher fractional bandwidth required. As an extreme example, ELF communications can take several minutes to send just a few characters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3685/can-sub-ghz-frequency-can-be-used-in-space-communciation, by Sujay sreedhar, Juancho, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
