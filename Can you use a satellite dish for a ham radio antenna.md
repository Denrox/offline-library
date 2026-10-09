# Can you use a satellite dish for a ham radio antenna?

*Tags: antenna, antenna-construction, equipment-design, equipment, improvised · score 11*

## Question

Can I use a satellite dish as a ham radio antenna? I was thinking that because there are two unused, working satellite dishes that have all appropriate wires attached conveniently to the roof of my house. Would there be a way to use the dish as a ham antenna? Maybe it cn be used with a few modifications. All google searches came up blank.

## Accepted answer (score 0)

Most TV satellite signals are between 915-MHz and 2.1-GHz. The 23-cm band (1240-MHz to 1300-MHz) does fall in this range, and a few hams have repurposed dishes for things like EME (Earth-Moon-Earth or "moon bounce") operation, but it's not a band many hams use.

The feed line for TV is usually 75-$\Omega$, not the 50-$\Omega$ typically used with ham radios. The LNB (Low Noise Block, TV downconverter) probably has filters that reject most ham frequencies to cut down on interference.

In short, for traditional 2-meter VHF and 440-MHz UHF it would not work and would require extensive modification. It would be far simpler to put a J pole or maybe a Yagi if you want a directional antenna.

## Answer (score 16, by progrmr)

You can use a satellite TV dish antenna for amateur radio use but how you use it depends on what frequency you want to operate.

The satellite dish antenna has two basic parts, the parabolic reflector and the feed (at the focal point of the parabola). The gain of the dish depends on the frequency you are using and the diameter of the dish.

A typical satellite TV dish probably has a LNA (low noise amplifier) at the focal point, along with a block down converter to change the received TV signal down to around 1 GHz so that it can be sent over a long coax cable to the TV with less loss (losses in cheap coax at 10 GHz are pretty high).

Unfortunately you can't easily reuse the satellite TV LNA and down converter (LNB) because it is designed for receive only and you will want be able to transmit. So you will have to build your own feed for the dish.

Those satellite TV dishes are about 20 inches in diameter, too small to use for 220 or 144 MHz VHF (unless you want to make a slot antenna, more below). It could work for 440 MHz UHF but the gain would be so low (~6 dB @440 MHz) that it would be easier to just build a yagi. It's much better at 1200 MHz, where the gain would be around 14 dB, or at 2.4 GHz about 20 db. A small dish works great at 10 GHz where you get about 32 dB gain. There is a gain chart is [this answer here](Relation%20between%20antenna%20physical%20size%20and%20gain.md).

There are articles explaining how to convert a satellite TV antenna to a stealth 2m (146 Mhz) slot antenna, such as here and here. You cut a slot in the parabolic dish which changes the dish from a passive reflector into the active element of the antenna. A horizontal slot gives you a vertically polarized antenna. Search for "ham radio slot antenna satellite dish" to find other examples and instructions.

## Answer (score 9, by filo)

Apart from using it as a ham radio satellite antenna (eg. for QO-100) or a microwave terrestrial antenna, you can turn it into a VHF slot antenna. Here is an example: https://w6nbc.com/articles/20xx-dishslot.pdf (keyword: "satellite dish slot antenna").

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16594/can-you-use-a-satellite-dish-for-a-ham-radio-antenna, by hopefulhacker-Reinstate Monica, progrmr, filo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
