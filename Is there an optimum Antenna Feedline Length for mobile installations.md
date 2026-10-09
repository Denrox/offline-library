# Is there an optimum Antenna Feedline Length for mobile installations?

*Tags: mobile, feed-line, coaxial-cable, vhf, 2m-band · score 13*

## Question

I bought a ham radio antenna mounting kit for my car that includes ~16' of coax. One end has a trunk lip NMO antenna mount, the other end has a re-solderable PL-259.

I asked the sales person if it is best to shorten the coax after installation to only the length required to reach the radio transceiver and they said "I would just leave it, the length is already optimized for maximum efficiency at the factory".

I've heard of this before (mostly from CB Radio installers) but don't actually know if this is true or understand **why/if there is an optimum feedline length for VHF/UHF FM use** (vs Citizen's Band AM HF). I intend to be setup for both VHF/UHF but will operate primarily on 2M VHF and so any trade-offs should be optimized for the 2M band.

My SWR on 2M at my club's repeater frequency is 1.7. Would shortening the length change the SWR or only change the losses incurred due to the SWR?

I have a nice space in the trunk, normally used for a sub-woofer if you purchased an optional "premium stereo" with the car - in my case this space sits empty. I plan to keep the radio transceiver body in the trunk with the remote head unit up front. This would allow me to keep the antenna feedline shorter and make for an aesthetically clean installation. This would also allow the antenna feedline length to be something around 5-6ft if shortening it would be beneficial (although I could just coil up the unused ~10ft or so).

## Accepted answer (score 13, by Phil Frost - W8II)

In the absence of common-mode currents, then the optimum feedline length is 0, because a longer feedline only increases your feedline losses. These losses are due to the resistance of the wire, dielectric losses, etc. and are specified in dB per unit length in the coax datasheet. At VHF and up, these losses can be significant even at car lengths, especially with less expensive or smaller feedline.

When you do have [common-mode currents](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md), then the feedline is effectively part of the antenna. Changing its length does the same thing as changing the length of the antenna: it can alter the radiation efficiency and impedance (and thus SWR) of the antenna. Even in this case, it's hard to say just what the "optimum length" is, because feedlines tend to be routed to, around, or near other conductive objects (like the radio chassis, and through the negative power supply lead, the car body), and these too will alter the operation of the antenna.

There's nothing special about CB: it's still just radio, and a properly designed and installed station still has no significant common-mode currents, and the feedline should still be a short as possible. The issue is that CB operators have more interest in superstition than a proper understanding of RF engineering. A popular CB antenna is a vertical which is installed with no ground plane, or an insufficient ground plane. In this case, [the feedline acts like the missing half of the dipole](How%20to%20reduce%20RF%20in%20the%20shack%20when%20using%20vertical%20HF%20antenna%20%28no%20radials%29.md), so the feedline length absolutely is essential to the operation of the antenna. While you can indeed "tune" your "antenna" in this case by altering the feedline length, this is usually *bad advice*. [Addressing the common-mode current problem](Using%20a%20balun%20with%20a%20resonant%20dipole.md), rather than fiddling with feedline length until you happen to get a good antenna, usually yields a more robust and predictable result.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1628/is-there-an-optimum-antenna-feedline-length-for-mobile-installations, by BenSwayne, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
