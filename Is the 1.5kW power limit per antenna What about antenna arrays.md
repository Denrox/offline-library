# Is the 1.5kW power limit per antenna? What about antenna arrays?

*Tags: antenna, united-states, legal, rf-power · score 4*

## Question

My son KJ7NLL just got his general, and while we don't (yet?) have plans to transmit at 1.5kW, he asks if the 1.5kW limit is per-antenna?

If it is per-antenna, and you use an antenna array of 8 antennas (phased array, multi-antenna stack of Yagis, etc), then you could get 8x 1.5kW for things like EME.

This seems like an edge case, not sure if the rules cover it or not but would like to know to at least satisfy curiosity, perhaps even for future EME.

## Accepted answer (score 10, by rclocher3)

Here's 47 CFR § 97.313:

§ 97.313 Transmitter power standards.

(a) An amateur station must use the minimum transmitter power necessary to carry out the desired communications.

(b) No station may transmit with a transmitter power exceeding 1.5 kW PEP.

So sorry, you're only allowed a maximum of 1.5 kW per station, not per antenna.

I can anticipate a further question, "what about multiple transmitters, with one antenna per transmitter?" I'm no lawyer, but I'd think that the FCC would consider multiple synchronized transmitters transmitting the same thing on the same frequency with a phased antenna array to be a single station under the law.

## Answer (score 5, by user10489)

The 1.5kW limit is really per transmission. But there are other limits as well that may be reached first. Some bands have a much lower power limit.

Also, high on that list is safety, and this isn't just a good idea, it's legally required in the amateur radio regulations. Above 50w and certainly above 100w you should be doing an environmental study to make sure that people in the environment of your antenna are not absorbing radiation above safe levels. In a multi-antenna or multi-transmitter situation, the radiation from each adds up to a total that may not be safe. (Note: the FCC recently dropped the amateur radio exemption for low power stations. Now all stations are suppose to do an environmental study.)

Also, high gain antennas can focus power to unsafe levels even when transmitter power is low, and it is important to make sure people can't walk through the beam of such an antenna.

Physics may also limit your power. As your power level increases, SWR and loss in your antenna system become more and more critical. At high power levels, loss translates to heat, and enough heat can burn through components, and SWR becomes a multiplier for these problems. While low power stations try to minimize loss and swr for efficiency reasons (to make best use of power available), high power stations must fix these issues to operate at all.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17701/is-the-1-5kw-power-limit-per-antenna-what-about-antenna-arrays, by KJ7LNW, rclocher3, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
