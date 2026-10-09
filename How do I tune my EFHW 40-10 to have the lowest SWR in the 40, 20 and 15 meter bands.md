# How do I tune my EFHW 40-10 to have the lowest SWR in the 40, 20 and 15 meter bands?

*Tags: antenna-theory, hf, wire-antenna, impedance-matching, end-fed-antenna · score 3*

## Question

This is a reading from my RigExpert AA-35 ZOOM of my EFHW 40-10 inverted L with radials, and feedpoint 2 feet above the ground. Any thoughts as to how I can tune or move this antenna to get the lowest SWR in the 40, 20 and 15 meter bands? Thanks.

An update: I disconnected the ground lug on the box and moved the feed point up to 10 ft. Big difference. Hope to make more of a difference by increasing the antenna length.

Yet Another Update: Connected a 10 foot ground wire to the radial plate and got slightly better results (in green). If I ever care about 30 meters, I'll disconnect the ground.

And yet another update. Extended my antenna by 2.5 feet and get the following (red is longer wire, green is shorter wire):  
Final update: Antenna is in its "final" state, spliced with PosiLock connector and crimped with an aluminum sleeve at the end. 10 meters is a compromise for better SWR elsewhere.

## Accepted answer (score 5)

First you don't necessarily have to do anything. The SWR is below 3 for the bands and most transceivers can handle that OK.

If you want to try to get the resonate points inside the bands you will need to lengthen the wire. it is usually a good idea to start with too much wire and trim the length to bring the resonance down, but in your case it look like the wire is too short.

Ideally solder additional wire on the end and cover it heat shrink, then cover that with water proofing sealant. However you could get very similar results with a simple crimp splice or even just mechanically connecting the wire. If you don't provide some protection from the elements the connect will eventually corrode.

In theory you should be able to calculate the exact length of wire you need. In practice it is difficult to account for all of the factors. Everyone I know of doing wire antennas makes them long and trims them as need to get the resonance.

Currently the antenna is resonate at about 7.7 Mhz. You would like it to be resonate at 7.1 Mhz. Take the old resonate frequency divided by the new resonate frequency and multiply by the original length, (7.7/7.1)*65 = 70.5 or so. The result is about 70.5 feet which would have you adding 5.5 feet to the existing antenna.

I would probably add about 7 feet and trim as needed to get the resonates where i want it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16631/how-do-i-tune-my-efhw-40-10-to-have-the-lowest-swr-in-the-40-20-and-15-meter-b, by K8KV. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
