# How do I discover APRS coverage?

*Tags: rf-power, digital-modes, aprs, packet · score 12*

## Question

I'm considering adding simple APRS transmitters to my vehicles. I'd rather just put one in and forget about it, but I understand there are areas of the US where a stronger transmitter would be required to successfully send an APRS update packet.

Are there coverage maps, similar to cell phone maps, which will help me understand where APRS should work and where it might not?

How powerful an APRS transmitter do I need to get approximately 75% coverage in the US?

## Accepted answer (score 9, by Dan KD2EE)

Coverage maps are a thing that is notoriously difficult to do right. There are some very complex programs (Radio Mobile is the one I know the most about) which can generate coverage maps if you're prepared to wade through the technical details and the quirks of the software. Unfortunately it's not as easy as drawing a circle of a certain size around each digipeater. Furthermore, power isn't the only factor - 5W vs 30W isn't going to make any difference at all compared to the night-and-day difference between an NMO-mounted mobile antenna vs an HT laying across your passenger seat.

You can use the aprs.fi maps (warning: uses a google map overlay, it can be slow on some computers) to see all APRS activity. There's a button along the top right allowing you to filter out everything except APRS stations or digipeaters. You'll see that there are areas of very dense coverage - I'm looking right now at Baltimore, Philadelphia, up the NJ turnpike to NYC, and along the coast - but then there are wide areas that are empty, either because there are no digipeaters, or simply no one has sent a packet from there in the past 24 hours. An HT connected to a real mobile antenna, properly mounted on your vehicle, is equal to or better than 90% of the users you're seeing on that page, so if you use that setup you will get coverage anywhere that you see other users getting coverage on that page, with the possible exception of the outskirts of less heavily populated areas.

You could do better by using a 50W mobile, but even that is only a 10dB improvement and will only extend the coverage areas by a few more tens of miles, it will not magically give you coverage in the "dead spots" on that map. You also often do not want to run maximum power on something digital like APRS anyway unless it's a radio specifically intended for it - running "at the limit" can make your transmitted signal more dependent on the whims and quirks of the final amplifier, which can introduce nonlinearities which actually make your signal harder to decode. Plus, if you're signal is so powerful that digipeaters can hear you but you can't hear them, you risk stepping on signals that you can't hear, meaning that not only will you not get repeated, whoever you stepped on won't get repeated either.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/315/how-do-i-discover-aprs-coverage, by Adam Davis, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
