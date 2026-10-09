# How do emergency nets work?

*Tags: procedure, emergency, net · score 17*

## Question

In movies that depict amateur radio in emergencies, the hams' worldwide communication network invariably is able to pass messages between individuals. As an amateur that has been primarily interested in the technical sides of the hobby I am not at all familiar with how messages might be passed long distances through nets. I would like to pose the following two hypothetical questions:

1.

If the power grid and cell phones were down while I was a hundreds of miles from home with no direct communication path, what would be the best way to get a message to my family if my home and I both had access to a battery powered radio and small easily stored antennas?

2.

In the preceding situation, what could I do at home to facilitate that kind of message traffic for others?

For purposes of the question it should be assumed that when far from home no knowledge of the remote Amateur community and frequencies is know prior to the disaster. Knowing this for the home location seems reasonable. It is also assumed that direct communication is not possible.

## Answer (score 12, by user)

If the power grid and cell phones when down while I was a few hundred miles from home what would be the best way to get a message to my family if my home and I both had access to a radio and small antennas?

I'm going to make a few assumptions, here. You may want to consider them restrictions on when this answer is valid.

First, I'm going to assume that "having access to radios" means that you have a means to power them.

Second, I'll take a shot at "a few hundred miles" being 200 miles, or 300 km.

Third, I'll assume that the small antenna, while perhaps not optimal, [presents a good match to the transmitter](Why%20do%20I%20need%20to%20tune%20an%20antenna.md) at the height and operating frequency in use.

Fourth, I'll assume you have access to HF, both in terms of license restrictions as well as in terms of equipment. A few hundred km on VHF is not trivial; while certainly doable, it pretty much requires a fixed installation because of the limitations of line-of-sight propagation.

**If those assumptions hold,** then establishing communications even in a grid-down scenario is fairly easy. You'd probably be using a low HF band, depending on conditions most likely either 3.5 MHz (during the night) or 7 MHz (daylight), with the antenna near the ground. This results in what is called NVIS or Near-Vertical Incidence Skywave, in which the signal take-off angle is close to vertical. To achieve NVIS, the antenna should be no higher than a quarter of a wavelength above ground, which incidentally is what you'll usually end up with when setting up a temporary antenna to operate on the lower bands.

From there, those at your home would simply need to know where and when to monitor for your calls. The amateur term for this is a "sked" or scheduled contact. This can be as simple as "keep the radio turned on and tuned to 3755 kHz at all times" or something more elaborate like "listen for me at 7115 kHz at fifteen minutes past the hour 11, 12, 13 and 14 local time, and at 3845 kHz at fifteen minutes before the hour 20, 21 and 22 local time". The latter example gives you a total of seven opportunities per day to establish communications, four during mid-day and three in the evening.

To make it easier for those at home, you might want to pre-program any applicable frequencies in your transceiver's memory, or write them down clearly, as well as write down the [tuner settings](Why%20do%20I%20need%20to%20tune%20an%20antenna.md) for each frequency and a quick guide to operating the radio itself. While not strictly a requirement, it does make operating much easier; if something bad has happened, such as the power grid and cell phone network being down, anyone operating the equipment will likely be under stress; do what you can to make it easier on them.

In the preceding situation what could I do at home to facilitate that kind of message traffic for others?

Join a traffic-passing net, or even just regularly participate in informal "net-like" on-the-air gatherings and make others aware that they exist. Depending on your location this will take different shapes, but your local amateur radio club will likely be able to provide locale-specific guidance.

Keep in mind that, as the question indicates, traffic-handling nets are point-to-point (as radio communications) but *not necessarily endpoint-to-endpoint*. The idea is to get traffic *closer to its intended destination*, not necessarily to get it to its destination immediately. It may be possible to get the traffic to its intended destination with a single "hop", but more likely is that it will require a few hops between the original sender and the intended recipient. (In the simplest of cases, neither the sender nor the recipient has access to amateur radio, but the traffic is passed over amateur radio without relays, in which case you have three hops: sender to operator, operator to operator, and operator to recipient.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/635/how-do-emergency-nets-work, by pyHazard, user. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
