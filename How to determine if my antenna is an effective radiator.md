# How to determine if my antenna is an effective radiator?

*Tags: antenna, antenna-construction · score 11*

## Question

So I build an antenna, tune it with the SWR and make it look great for a 50 ohm load.

That does not determine if it is good at getting a signal out or not, it could just be a 50 ohm dummy load.

With my completed home-brew antenna, what is the best way to determine if the signal power is actually "getting out", and not just eaten up by inefficiencies in the antenna.

I have a big problem and I never think my antennas work "good enough" compared to an already built antenna.

## Answer (score 9, by Phil Frost - W8II)

If you have a field strength meter, then you can use that. You can also use a 2nd radio, on a 2nd antenna.

But, consider reciprocity: anything you to do increase your transmit gain also increases your receive gain equally. So actually you don't need a 2nd radio, you can use someone else's.

Simply find a station that's transmitting, tune it in, and measure its strength. With a more efficient antenna, the received power of that station will be greater, and any efficiency gains (or losses) work for transmitting too.

It's easiest if you can find a station transmitting something with more or less constant power, like CW, AM, or most digital modes. SSB is tricky because the transmitted power depends on how loudly the operator is talking. If there's a commercial AM broadcast station handy, that could be a good target.

Getting an accurate measurement is somewhat complicated by the fact that S meters on many radios doesn't mean a thing. Usually the S meter simply indicates the AGC level. How does AGC level correlate to the received power? It's different on every radio, and may or may not be useful.

A cheap SDR like the Softrock or RTL2838 can be useful here. Typically these feed the host computer with data at a fixed RF gain, and then you just need software that can give you a good measurement of power. Most software has some scale on the waterfall or spectrum that will do the job.

## Answer (score 3, by Ron J. KD2EQS)

Do you make contacts with the home-brew antenna? If the answer is yes, it works.

If you have another antenna for that band, signal comparison should be straightforward. On the receive of course, and remote stations are often happy to help with signal reports as you switch between antennas and transmit.

Do you have other local hams that you can talk to separately, say with a HT? They can give you their receive strength for other (distant) stations on your antenna band, and you match frequency and see if you are also getting the same S-level as your friend gets on (presumably) a known good antenna. And both can try to call the remote station with the same power, and compare the reports you each receive.

A field strength meter may help to identify antenna signal strength as you walk around it (finding the "lobes"), obviously only works in a horizontal plane.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1975/how-to-determine-if-my-antenna-is-an-effective-radiator, by Skyler 440, Phil Frost - W8II, Ron J. KD2EQS. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
