# How can I generate a list of APRS IGates on 30m?

*Tags: hf, digital-modes, aprs, packet · score 5*

## Question

I am investigating using a Tiny Trak 4 with my portable HF radio to self-spot on SOTA activations via APRS on 30m.

I usually self-spot via a text message. When I don't have any cell coverage, I can sometimes spot using APRS on 2m. I am looking for a solution for relatively remote areas where I don't have any cell coverage and don't have any 2m digipeater coverage. If I can get APRS messages out on 30m that would do the job.

I can find references on the Internet to using APRS on 30m, but I don't find any information on where or how many 30m IGates there are or what the coverage is.

How can I generate or where can I find a list of APRS igates on 30m?

## Accepted answer (score 4, by Adam Davis)

The APRS system and protocol itself doesn't track iGate type or frequency. There is a list of active iGates, but there is no frequency information for them, or for the packets they receive.

Further no one appears to maintain a database of such stations.

However those that have used it indicate that the coverage is good enough that you really don't need to worry about coverage. Depending on the propagation you will almost always make it to an iGate regardless of your position on any of the continents.

However, it should be easy to generate such a list yourself over time. Start broadcasting APRS packets on HF and watch APRS-IS feeds for your packets. You should be able to determine what iGate passed them to the internet, and you can then find out the location of that iGate from its own APRS packets. This will have to be done slowly over time as propagation changes, and to avoid preventing others from using the band.

Note that in order to make packets as small as possible, repeating stations strip some information from the packet as they repeat it. This information would tell you what station(s) your packet has already gone through - in other words, your generated list of iGates will only show those iGates that actually placed your packet on the internet, not any inbetween that have repeated it. Further, some HF igates may not be directly connected to the internet, thus you might find a packet gets received on HF, repeated on 2M, then received by a 2M iGate connected to the internet. You'd see the last repeater in the packet on the internet, however since 2M is generally short-haul, it's likely that even if some packets are repeated via radios before hitting the internet you'll still get a good idea of the position of the actual HF receiver, since you're most likely interested in general regional positions of HF APRS gateways and repeaters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/715/how-can-i-generate-a-list-of-aprs-igates-on-30m, by Malcolm VE2DDZ, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
