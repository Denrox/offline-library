# Tips for HF Antenna with house near AM transmitter

*Tags: hf, wire-antenna, rfi, rtl-sdr, balun · score 3*

## Question

My back garden is very small - about 500sqft. I also live near an AM transmitter and requires an AM filter. I would appreciate some general tips on the best approach to receiving HF signals (Ham and Shortwave Radio) in such a small space.

I use an RTL-SDR with a Ham-It-Up converter v1.3 and a Raspberry Pi.

What kind of wire antenna setup would someone suggest for such a small space? I current have a signal wire (speaker wire) coming out of a window about 10ft AGL going to the top of a shed that is about 8ft AGL. I use NooElec's "Balun" with the wire going into one hole, and the other going to the Raspberry Pi's ground. I was thinking of running some speaker wire around the perimeter of the garden, with each end of the wire going to each hole of the Balun. Would that help?

Given my small height AGL I have, and the small size of the garden, I can't really do anything nice at all I don't think :(

I tried to increase the length of the above wire by twisting some more wire to the shed-end, and walk around the garden with the slack. I found that I got more noise with only the original piece of wire. More noise is generally a good thing for reception, as it means more signal is entering the device, right? Or am I totally off base?

Any further tips would be appreciated.

## Answer (score 3, by Mike Waters)

Very possibly, the solution is not related to your antenna*, but to *find and eliminate nearby noise at its source*.

It may very well be coming from something in your house. A quick way of finding that out is to power your receiving setup from a battery and then turn off your main circuit breaker**. If the noise drops significantly, the next step is to figure out which appliances, etc. are radiating the noise.

Often, it's a switching power supply. They are both prolific and notorious for generating RFI (noise). They are in our computers, chargers, and power supplies such as "wall-warts". Some are quiet, others not so much. A nearby ham friend's S9+20 noise on 20 meters dropped to S6 when we unplugged his son's laptop battery charger! I once had a computer that radiated noise even when it was powered off. I had to unplug it to stop the noise.

Another way of detecting noise is by carrying around a portable AM radio (a radio tuned to the VHF AM Aircraft Band is preferred to a BCB radio). Tune to a spot where there is no station, and see if the noise is louder as you approach a utility pole. If so, try shaking the pole and see if the noise changes. If it does, then you have nailed down the approximate source of the power line noise. However, noise can be carried to your pole from miles away. One arc last year was 8 miles south of me on the 7850 volt line that feeds my pole transformer. The engineer from the power company found and fixed it.

*A small rotatable and tunable receiving loop is often useful for nulling out a single source of nearby noise, such as something in your neighbor's house, an arc on the overhead HV power lines, **or a nearby AM broadcast station**.

** Properly shut down your computers first, of course.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13185/tips-for-hf-antenna-with-house-near-am-transmitter, by user14615, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
