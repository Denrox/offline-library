# What ways are there to extend an antenna?

*Tags: antenna, antenna-construction, wire-antenna · score 5*

## Question

I am using an arduino micro controller with a LoRa radio module to communicate. The shield has 2 ways of connecting an antenna: either a SMA jack or a hole for soldering.

Now my problem is this: I need to get the antenna away from the module itself, so that i can get the antenna out of the container of the arduino. What ways are there of doing this? Can I just use a wire? But on the other hand, would that wire not act as an antenna itself? Are there special cables or something?

## Answer (score 9, by Marcus Müller)

You have an SMA connector – use that! You can buy ready-made coax cables with SMA connectors on both ends.

As mentioned, what you want is a coax cable. The electromagnetic wave travels *within* the cable, so, no, if not damaged and properly attached to the radio and to an actual antenna, it won't double as antenna.

Very much like your TV cable doesn't emit radio waves.

## Answer (score 2, by Rob Scott)

You can make a solder-able on aerial with a length of screened wire. On the board end separate the screen from the wire inside it. The centre wire is soldered onto the hole for the aerial. The screen is soldered onto the nearest earth point. (Make sure it does not short against any thing.) At the other end you remove the screen for a section of the length, thus just the inner wire is left exposed. This is then placed where you want it to be. The screen is just that - a screen. Make the length of the exposed wire [for a frequency of 868MHz ] 8.2cm in length. Reference = Page 30 of https://partner.orange.com/wp-content/uploads/2016/04/LoRa-Device-Developer-Guide-Orange.pdf (I am Rob Scott of scott_electronics@yahoo.co.uk )

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7472/what-ways-are-there-to-extend-an-antenna, by user5227744, Marcus Müller, Rob Scott. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
