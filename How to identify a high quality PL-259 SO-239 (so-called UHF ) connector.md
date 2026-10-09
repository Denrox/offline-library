# How to identify a high quality PL-259/SO-239 (so-called "UHF") connector?

*Tags: pl259-so239-connector · score 3*

## Question

How do you identify that a UHF Connector (PL-259 & SO-239) is of a high quality and build?

Do you identify specific materials in the construction, gold plating, or other characteristics? How will I be able to determine these at a glance when browsing through a sale bin?

## Accepted answer (score 8, by Phil Frost - W8II)

UHF connectors are tricky, because they're not a very good connector by modern standards to begin. They have only a few redeeming qualities:

- They are common on amateur radio equipment
- The socket can accommodate a banana plug

Due to their non-constant impedance design, an unavoidable consequence of being designed so long ago, they don't work well above 30 MHz. They're also inherently not weather-resistant on their own, so you have to be really good about taping them outside. Personally I only use them on the back of radios that come with them: every other connector I've installed is N (anything outside), BNC (anything inside I might connect/disconnect frequently), or SMA (small things).

That said, if you still want UHF connectors and want "good" quality, I'd look for two things:

1. A well-known brand, like Amphenol
2. Silver plating

You may find silver plating in some sale bin, but it may be difficult to find something that's not made in China to the cheapest possible specifications. I've used these and sometimes they work well enough, but it would be prudent to test any cables you make with them by putting a dummy load on one end, an antenna analyzer on the other (or even just a transmitter and an SWR meter) and jiggling the connectors on each end to ensure the SWR stays at 1:1.

Your best bet, counterintuitively, is to look for old, surplus equipment contemporary with the design of the connector. The silver will likely be oxidized and the connector will look terrible, but don't worry, it will work anyway. If the corrosion is really bad it's easy to clean off with a silver cleaner or any of the homemade concoctions you can find on the internet.

Otherwise you'll have to order the connectors new from a reputable distributor (ie, not ebay), and they'll set you back several dollars each.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13048/how-to-identify-a-high-quality-pl-259-so-239-so-called-uhf-connector, by Amin Shah Gilani, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
