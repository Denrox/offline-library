# How to find something disrupting car key fobs across a parking lot?

*Tags: rfi, fox-hunt · score 5*

## Question

Apparently there's a parking lot in which car key fobs are messing up:

Key fobs that suddenly won't unlock vehicles. Cars that won't start. Alarms that go off for no reason and can't be quieted. Something mysterious is thwarting drivers outside a grocery store in the small Alberta town of Carstairs — and it's sparking all kinds of theories.

The problems have been happening for weeks in the parking lot outside the Westview Co-op grocery store in Carstairs, a town of about 4,000 about 60 kilometres north of Calgary.

A longtime employee at the dollar store right across the street from the Co-op says it's all she hears some folks talk about when they come into her store to buy a battery for their fobs — and then discover that doesn't solve the problem.

"I've been at the dollar store almost four years," Laura Strate said, with a laugh.

"It's just bizarre. People are actually scared to go to the Co-op now because they don't know if their cars are going to start."

–"Something mysterious is blocking vehicle key fobs from working in a small Alberta town" (2019-01-30)

Seems likely that the problem's radio interference, unless someone's having fun.

In a related discussion at HackerNews, someone commented:

Call in a couple of ham radio operators who like to foxhunt and they should be able to point you in the general direction of the problem within minutes. If the effects are as localized as they say it should be able to be pinpointed within an hour.

**Question:** How would a HAM radio operator go about finding the source of interference in a scenario like this, where car key fobs are malfunctioning across a parking lot?

## Accepted answer (score 8, by Glenn W9IQ)

There was a similar problem in the US a few years ago and it turned out to be a new shop sign that had a defective ballast that emitted a wide RF spectrum.

Most key fob systems operate at frequencies of 315 MHz for North American made cars and 433.92 MHz for all others.

The direction finding equipment would involve a programmable receiver or a portable spectrum analyzer, an attenuator, and a directional antenna. The spectrum analyzer may be more helpful in this situation because it allows a view of a broad range of frequencies at once.

The direction finding technique involves aiming the antenna in all directions to find the strongest signal. The operator then moves in that direction. As the signal gets stronger, it may be necessary to increase the attenuation so as to not overload the receiver with the signal and to have the peaks and nulls in the directional pattern of the antenna be more apparent. Sometimes it may be necessary to deliberately veer off course in order to get a different bearing on the signal, allowing the operator to effectively triangulate on the location of the signal.

This sequence of turning the antenna and moving in the direction of the strongest signal continues as the operator zeroes in on the exact location of the signal. When the operator gets quite close, the operator may install a less sensitive antenna or even remove the antenna to further reduce the signal strength.

As @JonCuster points out sometimes you can use a much simpler kit of just a programmable radio and a basic antenna. You determine direction by using your body to block the signal. So it may work in a pinch but the earlier described equipment will generally be much more reliable and flexible.

Amateur radio (ham) operators frequently call this technique "fox hunting" in an obvious nod to the English sport. It is also known as radio orienteering or simply amateur radio direction finding (ARDF). Many ham clubs organize fox hunts as a fun and healthy outdoor activity for their members. These culminate in a world champion event known as the World ARDF Championship where the best from around the world meet to match their skills.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12744/how-to-find-something-disrupting-car-key-fobs-across-a-parking-lot, by Nat, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
