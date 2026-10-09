# Are there any active ham satellites orbiting that use the 5cm band?

*Tags: antenna, satellites · score 7*

## Question

I see that 5cm is available for satcom in amateur radio. Are there any active satellites for that?

If so, what satellites and are their TLE's available?

## Accepted answer (score 7, by Marcus Müller)

Yes!

SatNOGS is a pretty cool crowdsourced satellite observation / recording system, and they have a database of known satellites. By the way, if you're using GPredict, the transmitters.json that describes all transponders is just a SatNOGS database dump.

what satellite

https://db.satnogs.org/transmitters ; click on list, sort by downlink frequency, look for 5.65 GHz ; there *is* one amateur satellite transponder, it seems.

Since remote stations (and what could be *more* remote than a satellite in space?) need to be registered, the "official" way would be going through all relevant national registries (FCC, OFCom, BNetzA, …) and looking for amateur radio satellite registratiobs, but a) seems like work, b) "registered", especially in the era of self-built micro-satellites is not overly indicative for "operational".

TLEs

typically, yes. NORAD will have data, and for that satellite,you can display its position through the TLEs downloaded from www.celestrak.com in Gpredict. Nifty! (for some reason, Gpredict doesn't show the ground path, I don't know why exactly)

The orbit, rendering curtesy of celestrak, is polar:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20213/are-there-any-active-ham-satellites-orbiting-that-use-the-5cm-band, by KJ7NLL, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
