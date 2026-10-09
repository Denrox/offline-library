# Is it possible to overload APRS?

*Tags: aprs · score 8*

## Question

Does APRS have a limited capacity in terms of beacons? What happens when an APRS frequency experiences a large number of packets?

## Accepted answer (score 6, by trafficone)

When two packets are transmitted simultaneously on the APRS frequency in a local area, it is unlikely that either will be understood. As the packet density in an area increases, the chances that two packets will be transmitted simultaneously increases. This issue is compounded by the presence of digipeaters which can unintentionally flood an area with packets from a small number of sources.

The question then isn't a matter of the number of beacons, but the frequency of packets in a local area. Given a local area of 2 people where each send a 1 second packet once in a 10 minute interval, there's a 1/600 chance you will overlap with the other station. Once you get 100 stations together, without getting too much into probability, you can expect to get an APRS packet out a little over once an hour.

## Answer (score 3, by Adam Davis)

In areas with a lot of APRS traffic, when you as a receiver are seeing a lot of collisions, one way to reduce the problem is to reduce your receiver sensitivity. You make your area of reception smaller, and thus see fewer beacons. As the spectrum grows crowded and people do this the problem will manage itself to some degree. Of course you reduce your area, but as long as you and others intelligently repeat the messages (via radio or internet) then everything will still get through.

In the future I expect some to start using sector antennas, and possibly MIMO technologies to resolve the issue. It's not trivial to separate simultaneous transmissions, but it is possible. You can start experimenting with SDR, multiple antennas, and not only separate different simultaneous transmissions, but also provide some amount of positioning information.

At the moment most don't view it as a big problem. Transmissions are often rather redundant and repeated frequently enough with enough random jitter that even blind beacons will get their message out more often than not, and if you wait you'll eventually get the information you're looking for. Certainly it would be good for those in congested areas to use more advanced beacons that pay attention to traffic and avoid stepping on other transmissions.

If you're trying to collect every 10 minute temperature reading from a remote station, though, and the station doesn't provide history or redundancy, then APRS is not the right solution. It's really a "best effort" but not guaranteed service, and should be treated as such.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/801/is-it-possible-to-overload-aprs, by JC Hulce, trafficone, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
