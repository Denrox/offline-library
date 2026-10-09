# How can we determine what repeaters to use?

*Tags: license, ht, repeater, frequency · score 4*

## Question

My wife and I are studying for our Technician class licenses. We are thinking about how we could communicate with each other while both of us are at work, she being in Oakland, CA and myself in Pleasant Hill, CA. with several hills and about 15 to 25 miles between us. We are aware that our soon-to-be license type will limit our frequencies and power output. We also have not determined what handheld radios we'll be purchasing and are not looking for recommendations other than best frequency range and wattage output to use for this particular scenario, and if it would be possible to communicate with this distance and geographical features, even for just a few minutes during any part of the year.

## Accepted answer (score 3, by Kevin Reid AG6YO)

It sounds like you've gotten the characteristics of HF and VHF+ operating mixed up a bit. If you're going to use VHF/UHF repeaters to communicate, then your "frequencies and power" (and time of day) are almost always irrelevant and you either can communicate or not, with some variation due to weather.

There are two basic cases for repeater-based communication:


Both of you have a line-of-sight to the same repeater, and are close enough to it. In this case, with your radios appropriately set for that repeater (frequency, split, CTCSS tone), you can simply talk pretty much like simplex.


You each have a line-of-sight to *different* repeaters. In this case, you need to find two repeaters which have compatible *linking* systems (either part of a specific permanently-linked network, or having a controllable linking system like EchoLink or IRLP). Then you can contact one repeater, and in if needed instruct it to link to another repeater, at which point it's like the two repeaters are now one repeater (everyone hears everyone else).


Permanently linked repeaters can be treated just like a single repeater with a larger coverage area.


In the case of temporarily linked repeaters, however, you're now occupying two repeaters with your conversation — it's less convenient to share it with others than in the first case, since you can't just stop talking but need to also end the link. There's nothing wrong with doing this if the other repeater users don't mind, though.

In either case, you don't choose a frequency, you use the repeater's frequency. Your transmit power will affect how far you can be from the repeater, but an even better approach is to use a directional antenna pointed at the repeater, as this improves both transmission and reception. Of course, directional antennas are bulky and you may not wish to set one up just for this purpose.

For **you in particular**, I took a look at RepeaterBook, a user-updated database of repeaters, and found what looks like a good candidate for a single repeater usable by both of you: WA6HAM which is on a mountain directly between Pleasant Hill and Oakland, CA. There's an intervening hill on the Pleasant Hill side, and the database doesn't say how tall the repeater's tower is, so I can't say for sure whether it'll actually work, but it's worth a try.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6305/how-can-we-determine-what-repeaters-to-use, by Jonathan, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
