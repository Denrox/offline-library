# Can I send to a D-Star reflector other than the one a repeater is linked to?

*Tags: d-star, reflector · score 4*

## Question

I want to send some test data via a reflector, to be picked up by my OpenSpot hotspot linked to that data reflector. My local repeater is pretty much always linked to another reflector.

There's not much activity though (especially locally, though technically I don't know if there's someone listening to the reflector), so I wouldn't feel bad tying up the RX on the repeater for a few seconds during quiet times. It's more disruptive to re-link.

Can I, and if so how?

That is, can I set UR and RPT and stuff to have just this burst go to a particular reflector?

It doesn't seem to be an option on the calculator. That only says how to "source route" to a repeater, or how to TX to *a callsign*, not to a given reflector.

Maybe I can TX to a call sign (my entry level call sign is still valid)? Will that work with an OpenSpot, or does it have to be a real repeater for that to work?

## Accepted answer (score 4, by rclocher3)

No, you can't transmit to a different reflector than the one your repeater is currently linked to. When the JARL designed the linking parts of D-STAR, they had in mind flexible user-driven routing to a repeater, or to the repeater that an operator most recently used. The reflector linking business is a very clever hack that works when the repeater operator loads software called DPlus on the gateway computer. DPlus is popular in most of the world, but from what I've heard, most repeater operators in Japan don't use it, probably because DPlus reflectors go against the linking philosophy that the JARL originally had in mind.

Anyway, because reflectors are a hack not envisioned by the inventors of D-STAR, you can't do fancy things like using URCALL, RPT1, and RPT2 to route your transmission to a designated reflector. To answer your last question, if you route to a call sign, you're not really routing to that call sign; you're routing to the repeater that that D-STAR-registered call sign was last seen on.

If you want to send data to be picked up by your OpenSpot, then the thing to do would be unlink the repeater, link the repeater to the reflector your OpenSpot is monitoring, and then unlink and switch the repeater back when you're done. That might be a little bit annoying to anyone monitoring the repeater, but personally I'm glad to hear someone using our local repeater for anything. In your shoes, I'd consider making a short announcement on the repeater (locally, not on a reflector) to tell people what you're doing. Someone listening might be very interested in such things!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17717/can-i-send-to-a-d-star-reflector-other-than-the-one-a-repeater-is-linked-to, by Thomas, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
