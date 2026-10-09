# What makes cellphone transmissions so energy cheap?

*Tags: rf-power, efficiency · score 19*

## Question

The modern cellphone can carry on a full duplex conversation for a time period measured in hours on a battery half the size of my handheld transceiver. My transceiver can barely receive for that length of time on its pack, nevermind transmit, and that's if I have a huge antenna much more unwieldy than the antennas included in modern phones..

One issue is that the cellphone in urban areas only needs to transmit a few miles, and the receiver can be significant more energy expensive to pick out weak signals. In terms of our hobby, Repeaters are equivalent - allowing a smaller, more energy efficient handheld appear to be a big transmitter nearby - but the handheld is still an energy hog, and still limited to a small area around the repeater. Besides, the average cellular phone will still work for hours of talk time even when the nearest cell site is 10 miles away.

Given that the technology exists, what is it that's preventing our amateur radios from achieving such good energy efficiency while still reaching a dozen miles for voice communications?

## Accepted answer (score 12, by WPrecht)

Remember that carriers are selling bandwidth, that’s it. Actually, they are overselling it, exactly like cable modems (but that's another story). If everyone in the coverage area of a cell tower tried to make a call at once, most of them would be unhappy.

The carriers paid a boat load of money for their chunk of spectrum and their overriding goal is to maximize their use of their chunk. Since there is (in theory) competition, there is a focus on quality of service since all the plans seem strangely similar in price.

Towers are expensive, but as the others have mentioned, phones only have to transmit a few km at most to hit a tower and often less than 1 km in urban areas.

Cell phones use a heavily optimized spread spectrum digital mode that is focused on short haul weak signal work. Towers have a limit of 100W (omnidirectional) or 500W directional, however, in practice towers typically transmit in the range of 25-60 watts.

In most countries cell phones are limited to 2W PEP, however most modern cell phones have a peak power of about 300mW and are typically transmitting in the 100mW range.

In order to limit interference with adjacent sites, cell towers actively manage the transmit power both in the tower and on phones throughout a call, even between words. In this case, what’s good for the carrier is good for the consumer since their drive to minimize power use means the phone’s battery lasts that much longer.

***Contrast this with HTs*First batteries** – Economy of scale has let cell phone manufacturers use custom LiPo batteries for years where these are only now becoming standard on HTs. Lots of the HTs out there have NiMH or even NiCd batteries still; a lower energy density.

**Power** – If a cell phone were to transmit 5W PEP FM, it would run dead just as fast as an HT with the same size battery. The energy efficiency is in the mode used and the fact that the required range is very low.

**Role** – Cell phones are designed to work only where people typically go: on the roads, shopping areas, cities and the infrastructure is sited to handle that. However, people that use HT’s typically spend a good part of their time in places people don’t go as much: parks, woods, mountains. So you’d need more range even if you were using the same mode.

As Phil mentioned, we’ll see advanced features in add on modes first like D-STAR (Icom) and C4FM FDMA (Yaesu). Of course, these guys are looking to sell radios, to there’s no incentive (yet) to agree on a protocol. Initially this will just allow add on services. It would take something major before people start replacing repeaters with ones that actively manage power. Heck, it’s all some clubs can do to keep a basic 2m repeater up 24/7/365 on volunteer labor.

## Answer (score 8, by Phil Frost - W8II)

You are making an unfair comparison. HTs and amateur repeaters use the same technology now as they did forever ago. If you want to compare HT performance with cell phones, compare it with one of these:

In that light, I think HTs fare favorably. Modern HTs have grown more modern batteries (NiCd -> Ni-MH -> Li-ion), but the RF bits have seen about as much technological advancement as the brick phone above.

Modern cell phones have a whole ton of technological development that HTs haven't. For example, beam forming, digital modulation (many generations of it!), sophisticated DSP, and dynamic transmit power. All of these things serve to make better use of transmit energy. Economies of scale dictate that cell phones have received orders of magnitude more engineering time than HTs.

As for why amateurs haven't adopted these technologies, I guess laziness. There is no economical incentive for amateurs to do all this stuff. The profitability of a repeater isn't tied to the number of the number of customers it can service. Development of HTs is limited by compatibility with repeaters and other HTs. There's no service contract that expires in two years, which, if renewed, subsidizes the purchase of a new transceiver. And, the FCC isn't likely to regulate more strictly how amateurs are allowed to use their spectrum, as they do with cell carriers.

The only time you might get some development is when some HT manufacturer thinks they might be able to sell some repeaters (Icom, D-STAR). Occasionally there are innovations among a small subset of hams that are more technologically inclined (codec2), but I'd wager it will be a long, long time before support for such things becomes ubiquitous, simply because most people are content with what they have, and there's little economical incentive for change.

## Answer (score 5, by PearsonArtPhoto)

There are far more cell phone towers than repeaters. Imagine if you lived only 2 miles from a repeater. You'd probably hit it with only 1W all the time, and have no problems getting a full quieting signal. Cell phone towers are commonly even closer than that.

As far as receive only, you should be able to receive for a long time on a simple battery. Perhaps there's some amplification of weak signals going on, but I'm not sure. Think of a portable FM radio, the batteries in that should last for quite a while, especially if using headphones and low volume, which is probably comparable to a cell phone near someone's ear.

Also, cell phones have a protocol designed specifically to use low power, ie, digital modes. There is a strong signal sent to get their attention, then they automatically drop in power to the lowest transmission power required to make the connection.

Bottom line is, for Amateurs to have similar service levels, there would have to be some sort of a centralization, which would complicate the system. It could be attempted, and I think has been, for SHF signals, but overall, Amateur Radio is decentralized. However, some gains could definitely be made by moving to digital modes, and some sort of feedback to the device on the signal quality so the power transmission could be appropriately managed.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/955/what-makes-cellphone-transmissions-so-energy-cheap, by Adam Davis, WPrecht, Phil Frost - W8II, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
