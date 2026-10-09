# How do club codes stay secret?

*Tags: repeater · score 9*

## Question

To use auto patch, IRLP or other special repeaters, you need the club code from the local club I am part of, which is a DTMF code.

But I was thinking, DTMF can't be very hard to decode, and if someone (like an unlicensed guy with a receiver) records the repeater while someone uses the tones, and uses computer software to decode the tones, they could easily get the code and share it to anyone.

Do repeaters just hope that doesn't happen?

## Answer (score 7, by Dan KD2EE)

They stay secret because it takes a certain amount of effort and time to decode them - at the very least you need to record the tones and then feed them into a computer program. That means you need to record the entire repeater audio until you catch someone using the autopatch. Of course, you're right - once you have it recorded, it's trivial to decode.

I would imagine the reason this doesn't happen all the time is that there's no reason why an amateur radio operator should be trying to access a system he isn't allowed to. The repeater's core community would quickly recognize an unauthorized operator. The repeater owner is allowed to deny access to an individual - if he's caught abusing the repeater features, he can be advised he isn't welcome there, and if he returns, [he may be warned and fined by the FCC](OK%20to%20use%20any%20repeater.md). It could easily become an escalating issue the club changing the code and the attacker learning the new ones, but any persistent abuse like that would warrant a quick response from the FCC, which is really easy if the user is a licenced amateur and transmitting his call sign. If he isn't identifying himself, [clubs regularly use "fox hunting" to locate the source of a radio transmission](Direction%20finding%20How%20to%20find%20a%20stuck%20FM%20transmitter%20on%2070cm.md), and any jamming would be persistent enough to allow an individual or small group to find the source's location pretty easily.

## Answer (score 3, by Javier Henderson)

It's a bit of security through obscurity, but some repeaters won't transmit DTMF tones they receive. In those cases, unless you are monitoring the input frequency, you won't have anything to decode.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/467/how-do-club-codes-stay-secret, by Skyler 440, Dan KD2EE, Javier Henderson. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
