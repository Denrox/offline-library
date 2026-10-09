# What rules govern robotic teleoperations, when the remote device also transmits back telemetric information?

*Tags: united-states, legal, telecommand, telemetry · score 5*

## Question

I was looking through the FCC part 97 rules for robotic teleoperation, and it cites a one-watt figure for "model craft". However, it also allows higher power transmissions for remotely operated stations, and beacons.

The robot in question is a land vehicle that traverses very hilly/mountainous terrain, and having a higher power communications link would be very handy. Additionally, it sends back video and instrument readings from it's surroundings.

What rules govern such devices? I was unable to find such regulations.

## Accepted answer (score 3, by Phil Frost - W8II)

§97.215 has rules for "model craft". It says a station *may* be operated under those rules. To me, the intent of those rules is to allow for control of RC models without a break to identify every 10 minutes. I'd guess for a rover designed for Mars, a brief identification break is not a problem.

However, the rover is a station, and there won't be anyone at it. I'd think §97.213 Telecommand of an amateur station would allow operation in that case:

An amateur station on or within 50 km of the Earth's surface may be under telecommand where:

(a) There is a radio or wireline control link between the control point and the station sufficient for the control operator to perform his/her duties. If radio, the control link must use an auxiliary station. A control link using a fiber optic cable or another telecommunication service is considered wireline.

(b) Provisions are incorporated to limit transmission by the station to a period of no more than 3 minutes in the event of malfunction in the control link.

(c) The station is protected against making, willfully or negligently, unauthorized transmissions.

(d) A photocopy of the station license and a label with the name, address, and telephone number of the station licensee and at least one designated control operator is posted in a conspicuous place at the station location.

So the salient points seem to be:

1. Tape a license and contact information on the rover
2. Put a 3-minute transmit timeout on the rover
3. The controlling station must be an auxiliary station (which, among other things, limits you to VHF and higher frequencies)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7138/what-rules-govern-robotic-teleoperations-when-the-remote-device-also-transmits, by Tyzoid, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
