# Building a portable event repeater

*Tags: diy, repeater · score 10*

## Question

How does one go about building a portable repeater for use at events? Preferably at low cost, and with a minimum of bulky parts (so it's travel friendly).

Obviously you'd need a pair of radios to handle RX and TX, taking into account that the TX radio will probably have an above-average duty cycle.

I'd imagine you'd also some sort of controller to add courtesy tones / send out a station ID. I know there's some commercial options out there, but most of them look rather expensive (thousands of dollars, US), and not terribly small. I'd like to imagine that most of this work could be done with a specially equipped Raspberry Pi?

Then there's the issue of antennas. I know you can use a duplexer to share a single antenna, but I think those are also large and expensive. Can you make due with two antennas, given sufficient separation? Any other options?

Anything else I'm missing?

*As a bonus consideration: My primary purpose would be for amateur radio, but it would be awesome if it could be somehow reconfigurable to work as a repeater for GMRS purposes (legally, in the US). There's very little information out there about GMRS repeaters, which is rather surprising.*

## Answer (score 2, by M0LMK)

You can simplify this a lot if you can set up and use a cross band repeater instead of an in band unit (licence dependent).

Units like the Yaesu FT-8800 have a cross band repeat mode built in as standard and will just need a single antenna and a power supply or battery.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3668/building-a-portable-event-repeater, by Trevor Johns, M0LMK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
