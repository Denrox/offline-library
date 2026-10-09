# LoRa radio transceiver for PtP mesh?

*Tags: diy, packet, mesh-network · score 8*

## Question

I am very new to general RF/radio in general other than basic WiFi, but I'm looking at the feasibility and cost of a long range (>200M between nodes, sometimes probably 500+M) in flat terrain, relatively low power (solar + 12V SLA, short term usage) and *probably* fairly low bandwidth needs (couple of hundred Kbps?), but bi-directional/fully shared. So in starting doing some searches/research, I came across this SX1276 based module (https://www.adafruit.com/product/3072) that's relatively cheap, even if I need it for a few dozen or more nodes.

My concept is to use a fixed mesh, or star mesh topology as the distance between a centrally located node and the furthest away may be as much as 2+ km, possibly 3+. That's long term planning, my first attempt would likely be a handful of nodes perhaps 400m-600m from a central point. The advantage of this area is flat as a pancake, although lots of varying height temporary structures, although the antennas would not be placed very high, 6-10 feet off the ground so they may or may not have perfectly clear line of sight.

Based on my reading of LoRaWAN, it's really designed to be a central star network topology without much bi-directional communication, in general. And LoRa could, in theory, perhaps, do a mesh network but it'd need a non-trivial amount of software layered on top of the transceiver access code.

I did come across https://ieeexplore.ieee.org/document/8048465/ which is very interesting. In my naive reading of it, it implies that if you simply immediately re-transmit each packet once received (and ignore it once you've re-transmitted it) you essentially can flood a mesh network of LoRa devices reasonably efficiently despite collisions and such. I did see there's more to it than that with seeing to do offset concurrent transmission and other bits that I didn't get to. If that concept actually works reasonably well, it shouldn't be too difficult, in theory, to put a basic layer on top of a LoRa transceiver to spread data through a mesh (that doesn't actually know about each other really) in an easy to implement fashion which spans several square kilometers.

So...disabuse me of this and show me how naive and unknowing I am and I should tuck my tail between my legs and run away :)

## Answer (score 2, by W2CAM)

A few comments on amateur LoRa:


As others have pointed out, the datarate is measured in tens of bytes per second. Not thousands... Forget about file transfer!


LoRa is spread-spectrum and therefore can be used on the 1.25m-band and shorter, with maximum 25W PEP.


Enhanced propagation at 1.25m (versus 33cm where LoRa is typically used) opens up exciting possibilities of range. I would expect range similar to a well-equipped 2m SSB/CW station.


LoRa is a modulation scheme (analogous to FM), while LoRaWAN is a protocol and topology (analogous to an analog Echolink repeater system).


There's a project called "loraham", spearheaded by the hacker Travis Godspeed, which gathered quite a bit of interest. It is a PTP mesh in the spirit of APRS. https://github.com/travisgoodspeed/loraham

## Answer (score 2, by cmm)

Ham LoRa does seem to exist, although I haven't seen any mention of it around the Boston MA area.

I think to make best use of LoRa on Ham frequencies, one could use the European version that works in the 70cm band. With that, one could use higher power level (limited by one's local power limits which vary by physical location) and better antennas -- Yagis for fixed, point-to-point service and verticals for multipoint repeater service.

For protocols, one could use something based on UUCICO (the basis of UUCP), the old Unix protocol behind UseNet and mail.

But one ham in a region isn't enough to be interesting.

73, K1UZK (once WA1JMS)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10401/lora-radio-transceiver-for-ptp-mesh, by Drizzt321, W2CAM, cmm. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
