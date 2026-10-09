# Can larger antennas damage an HT radio?

*Tags: antenna, receiver, ht · score 8*

## Question

Can adapting a larger antenna such as a Diamond X-50 or larger mag mount damage an HT radio? Would it overload the receiver?

## Answer (score 13, by tomnexus)

A larger antenna shouldn't damage a handheld radio. In a quiet area, it will make its receiver more sensitive, and it will radiate more power when transmitting.

Try to keep a receiving antenna away from a transmitter, to reduce the risk of damaging the receiver. I suspect we've all gotten away with it - my 50 W, 2 m mag mount was 30 cm from my car radio antenna and it wasn't damaged.

What you might find when adding an efficient, higher gain antenna to a handheld, is that it gets overloaded by strong signals near the amateur bands, making it *more difficult* to hear the station you want. (This isn't dangerous, the power levels are still very small).

Handheld radios are a compromise because of their small size and battery power, and often have a) less effective filtering and b) less robust receive amplifiers. Pre-amplifiers can be made more resistant to strong signals, by running them at a higher current. A handheld radio can't afford to waste 150 mW, so they use lower IP3, lower current amplifiers. c) finally the handheld expects to have a fairly poor antenna on it, which attenuates all the signals, so the receiver will be designed for that.

On a viewing platform on hilltop in the middle of a city, I've found that my handheld, with its short antenna, was nearly useless. All kinds of noises were breaking through and overlapping with the amateur signals.

If the purpose of the larger/higher-gain antenna is to improve receive, you might couple it with a band-pass filter (either commercial or DIY) that can greatly mitigate out of band interference from strong signals... BUT at the cost of some insertion loss for both transmit and receive. There's just no free lunch!

## Answer (score 12, by user10489)

A larger antenna can mechanically damage an HT if it is physically supported by the HT (it can stress the connector on some designs), but if it's on a feed line instead it shouldn't matter.

Besides just being awkward to use that way, I wouldn't want to connect RG-8 directly to my HT with a rigid adapter for the same reason.

## Answer (score 6)

No, it will likely improve reception because the HT antenna is severely compromised and done all the time in mobile applications to use an external antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22501/can-larger-antennas-damage-an-ht-radio, by Radio Rails, tomnexus, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
