# Dipole versus ungrounded end fed for HF RX

*Tags: antenna-construction, hf, wire-antenna, dipole, end-fed-antenna · score 5*

## Question

I've built a 2 meter ground plane antenna that works pretty well for RX and has a decent SWR on 2 meters with my Alinco. However, I'm experimenting with SDR quite a bit and would really like to build something for weak signals, especially CW and RTTY at less than 50 MHz.

To that end, I was thinking of building a large dipole, but I'm getting advice that says that an ungrounded end fed wire run up the side of the house would likely perform far better.

First, is this true? Second, if it is true, why is it true?

*Note:* I am planning to use this antenna for *RX ONLY*, so I'm not really concerned about frequency matching on the length of the wire or dipole arms.

## Accepted answer (score 5, by user5258)

An end fed wire may not necessarily work BETTER for reception, but it should be effective and it is much simpler to put up. You might pick up a bit more hash noise from local RFI sources with an ungrounded configuration though, due to common mode currents induced on the outer shield of the feedline.

Feeding the wire through an isolation transformer, and grounding the end of the secondary winding opposite the antenna wire, and then also grounding the shield of the feedline at some distance from the antenna where the feedline enters your house would help reduce noise, and provide more safety for your equipment.

Other good configurations for reception of weak signals might be:

- Run the wire close to the ground (6ft) with a counterpoise wire on the ground beneath, and then short the FAR end to the counterpoise wire through a large resistor and feed the two wires at the other end via a matching transformer and ground the shield of the feedline where it enters your house.
- A fairly small loop of wire with a tuning capacitor at the point opposite the feedpoint, fed via a matching transformer. The loop can be rotated for best signal pickup or to null out local noise sources.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5210/dipole-versus-ungrounded-end-fed-for-hf-rx, by David Hoelzer, user5258. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
