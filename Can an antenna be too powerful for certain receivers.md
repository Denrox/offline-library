# Can an antenna be too powerful for certain receivers?

*Tags: antenna-theory, receiver, wire-antenna, tecsun · score 7*

## Question

I'm brand new to shortwave radio and have been researching what kind of a receiver to get. I'll use it on the antenna I'll build (longwire, 50-100 feet) for shortwave listening; no transmitting. Right now I have my sights on a Tecsun PL-360 as it's affordable and has an external antenna port. My question is: Would the portable ~$40 Tecsun get damaged somehow by a 100-foot antenna because it's designed to work with shorter, portable antennas? I really don't know if that's something I need to worry about when only receiving.

The reason I want such a cheap receiver and not something better but more expensive is because I just want to make sure the antenna's working properly. Once I'm happy with it I'll hook it up to an RTL-SDR device and plug that into a computer. I just don't want to spend hundreds on a receiver I'll only use a few times.

## Accepted answer (score 9, by Glenn W9IQ)

Would the portable ~$40 Tecsun get damaged somehow by a 100-foot antenna because it's designed to work with shorter, portable antennas?

Unless you are within a kilometer or two of a very high power transmitter, there is no chance of your antenna collecting enough power damage your receiver.

You are more likely to cause damage to your receiver from static build up on the antenna or nearby lightning strikes inducing too much power into your receiver's front end. Disconnecting the antenna and shorting it to ground when not in use and adding a basic lightning protection circuit will mitigate this potential. On a receive only antenna, another technique to bleed off potentially damaging static build up is to connect a 5-10 meg ohm, non-inductive resistor between the receiver end of the antenna and ground.

## Answer (score 3, by Autistic)

Your proposed big antenna could be too much for a cheap receiver. You probably will not blow any front end transistors, but MW or AM overload could give spurious responses, birdies, blocking, cross modulation etc. An experimental small series cap starting at say 10pF will improve matters by making the long antenna think that it is a short antenna. This reduces the signal input but it also reduces the noise. I found this quite workable 40 years ago. Cheap solid state SW receivers had BJT Autodyne converters. Front-end selectivity was not good, especially when there was no tuned RF stage. Modern cheap receivers can have a broadband antenna input which could even be worse. You could build a simple tuned preselector which would improve any receiving system.

## Answer (score 2, by Marcus Müller)

So, the magical relationship between antenna size and your receiver is that a larger antenna tends very much to have a larger *effective area*, which simply means it extracts field energy from a larger area that the radio wave you want to receive penetrates.

In other words: you get more *power* at your receiver. That's cool, because more power means "more power relatively to the noise inherent to your receiver's electronics", which means it's possible to receive weaker signals without them being "drowned" in noise.

The thing is that, in fact, receivers in effect are sensitive measurement equipment, and you don't want to overload them. Technologically, it's (almost) always preferably to have a *low noise amplifier* (LNA) as the very first element in your receiver's signal chain, and these are often constructed with very fine structures of a semiconductor process that is less prone to noise, but more sensitive to being damaged by too much power than your average silicon semiconductor. But I digress, as for the shortwave band, "normal" amplifiers are totally fine, and the chances that a cheap AM broadcast handset comes with an impressive LNA are rather slim, seeing that you typically just buy an IC that does the AM and FM reception integrated in one small package for you, and that those ICs have been around for four decades now, allowing for a huge range of cost/quality tradeoffs.

Now, usually, you rely on your receive signal still being weak, even with a larger antenna, and that it won't fry your receiver, lest you put your long wire receive antenna next to your neighbor's transmit antenna.

Now, your device of choice doesn't come with any rating for maximum input power – which isn't surprising, since its been designed with the antenna you see on the pictures in mind, and it probably works unless you directly couple that antenna into a transmitting circuit:

"AM Antenna" is of course a mislabeling. Antennas generally don't care about the modulation used, what is meant is "long-, medium- and shortwave antenna"; the shape suggests (as does its purpose) it's a ferrite core antenna.

You won't get happy when you attach your long wire antenna the same way you attach this ferrite core antenna: These antennas are high-impedance and very selective. Hence, the port where it's plugged in will also be very high impedance, and that will make it practically impossible for the receiver to get significant amounts of power from your long wire antenna, which has low impedance, which needs to be "sunk" into a matching-impedance receiver.

So, don't do this to you – if you want to observe the power coming from your antenna, either borrow, buy or build a power meter (I've learned not so long ago that there's logarithmic power meter ICs, these would be fun to try out), or:

Really, an SDR dongle comes for 6 to 29$. It won't be perfectly matched to your long-wire antenna, either, but much, much better than the port on the Tecsun thingie. You get signal samples instead of some arbitrary FM & AM demod combo IC that will do *anything* to the received signal. These samples would not only make it very simple to decode the audio of AM broadcasts, but also allow you to get a quantitative comparison of different antenna behaviours, over MHz'es of bandwidth, instantly. Oh, and thanks to the fact that there's free & open source software, you can not only receive "boring" AM broadcast, but also things like FreeDV, or, depending where you live, broadcast standards like DRM (shortwave AM replacement in India, and Australia; India just build a small 1MW transmitter, so, I don't know, but I think it's possible that one could receive it from rather far away if conditions are good).

So, not only would an SDR dongle be cheaper, it would also be more versatile and better suited for the job.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10054/can-an-antenna-be-too-powerful-for-certain-receivers, by fishfritters, Glenn W9IQ, Autistic, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
