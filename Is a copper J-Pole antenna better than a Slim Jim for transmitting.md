# Is a copper J-Pole antenna better than a Slim Jim for transmitting?

*Tags: antenna, vhf, j-pole · score 4*

## Question

I live in a fairly sheltered valley but there are several hill-top VHF repeaters that I can receive very well. However the one repeater in particular I want to transmit to, I can't reach well. I know my signal is reaching it, because it will auto-respond its call sign when I transmit, but I get reports that my signal is unintelligible.

I've using a BaoFeng F9V2+ with a Nagoya NA-771 antenna and I've also tried a Slim Jim but have not been successful at getting an intelligible signal through.

My question is, would using a copper-pipe J-Pole be any more likely to be successful than the Slim Jim or are they pretty much equivalent?

## Answer (score 6, by Glenn W9IQ)

The slim jim antenna has no more or less gain than a J pole antenna - despite many Internet claims to the contrary. Any perceived difference in gain is likely due to CMC (common mode current) since both antennas promote CMC on the feedline.

There is an argument to be made that a larger conductor improves efficiency and therefore gain. But for antennas that are at least 1/4 wavelength or longer, as in this case, the effect will typically be in the sub dB range.

You may also find references to the TOA (take off angle) being different between the J pole and the slim jim. Antenna range measurement and simulations show this to not be the case. This apparently came about when Fred Judd, G2BCX stated that the slim jim has a better TOA than a (5/8 wave) ground plane. This comparison was later morphed on the Internet to be a comparison between the slim jim and a J pole. Any such perceived difference in TOA is most likely attributable to CMC.

## Answer (score 4, by Kevin Reid AG6YO)

I'm not familiar with empirical results for these particular antenna designs, but in general, [an antenna constructed out of thicker conductors will have a wider bandwidth](Does%20antenna%20width%20shape%20affect%20resonant%20frequency%20like%20length%20does.md). That is, its impedance will be more consistent across the band.

Theoretically, this is an improvement because you will get a better impedance match across the band, including the input frequency of your target repeater. However, the actual effect is likely to be small (unless you have a particularly long or lossy feed line between your radio and antenna), and it might even happen to be worse if the new antenna is not well tuned.

Unless it's really cheap and easy for you to build a copper J-pole, consider building or buying a Yagi type antenna — even a 3-element one — and aiming it at the repeater. This *will* improve your signal strength.

## Answer (score 4, by user10489)

In a situation like this, gain helps a bit, but usually height helps more. So whichever antenna you can get higher will probably work best.

Also there are some odd propagation things around mountains, check out knife edge propagation and fresnel zones. Without getting into technical details, you can take advantage of constructive and destructive interference of multipath propagation by moving a small antenna within an area very roughly less than 1/2 wavelength to find the spot where you get the maximum reception. This spot will also give you the clearest signal when you transmit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11730/is-a-copper-j-pole-antenna-better-than-a-slim-jim-for-transmitting, by Brad McCarty, Glenn W9IQ, Kevin Reid AG6YO, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
