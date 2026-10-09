# Using an HF antenna for VHF scanning

*Tags: antenna, wire-antenna, antenna-tuner · score 3*

## Question

Are there any disadvantages (or advantages) to using a long-wire HF antenna for wide-band VHF reception?

Or would feedline losses make that useless compared to a ground level ducky or short whip? (for wide-band reception/scanning, e.g. well outside the 2 bands of the 2M/440 rubber duck antenna that came with the HT, or with the short whip that came with an RTL-SDR for ADS-B reception?)

Would using a balun or any sort of matching network between the wire HF antenna and a VHF HT or SDR make any difference?

## Answer (score 4, by Kevin Reid AG6YO)

There are many problems here, only one of which has to do with impedance:


Your antenna is (I assume) *horizontally polarized* whereas most VHF signals you might scan for (particularly ones where one end of the normal link is mobile, e.g. a car) are vertically polarized.


Your antenna will have a highly irregular pattern, with many nulls (directions in which the antenna receives almost nothing).


Your antenna will have an impedance and SWR which varies widely *within the band.* (Since it is not constant, there is no matching network which will help over the entire band.)

This is not a problem for receiving at all if your feed line is short enough or good enough that the loss is insignificant (compared to the strength of the signals you want to find). (But it does mean that if you look at a spectrum plot and see different signal strengths it isn't necessarily an accurate comparison.)

In order to determine the actual loss, you would need to know the ordinary (properly matched) attenuation of the cable (either empirically or per loss-per-length specification and length of your cable) and the impedance of the antenna at a given frequency.


The MF and HF signals received by your antenna (most notably AM broadcast stations), even though they are out of band, may interfere with reception of the VHF signals you want.

All that said, there's no harm in trying. If there's particular transmissions that you want to receive and you *do* succeed in receiving them, then you're good. But if you want to scan for things you don't already know are there, you probably want a vertically polarized, VHF antenna.

On the upside, if you *do* use a matching network, it will help eliminate out-of-band signals. The catch is that it makes things even less wideband, and if you want to make it adjustable to move across the band, well, that's an antenna tuner and VHF antenna tuners are not very common.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7316/using-an-hf-antenna-for-vhf-scanning, by hotpaw2, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
