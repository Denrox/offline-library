# NMO bicycle mount antenna has unexpected SWR

*Tags: antenna, mobile, transmission-line · score 4*

## Question

I built a bicycle antenna mount featuring an NMO connector to allow quick changes. With a 2m 1/4 wave monopole it gives reasonable SWR results (1.4 or so in the band of interest), with a particular dual-band it gives reasonable SWR results (1.7 or so on 2m, 1.1 or so on 80cm), but with an 80cm 1/4 wave monopole SWR=3.2@450MHz, SWR=1.05@510MHz.

The 80cm 1/4 wave monopole has my attention. It is a Childs Antenna Model QB 430. It appears to be a well-made antenna and I believe it is operating properly. The radiating element has a length of about 156mm which I think is about right for transmitting at 440MHz however with SWR ~=3 it seems odd.

My suspicion is that it has something to do with how the QB 430 antenna interfaces with the NMO mount, introducing some sort of capacitance at the feed point. Photos are below.

1 - overall system. The thick area around the feed line are ferrite beads, expected to provide 1000+ Ohms common mode impedance between 140MHz and 600MHz. Feed line is apprx 480mm long, LMR 195 cable. Feedline was moved for the photo so as to be more easily seen. The implementation is that it runs along the center of the base plate staying in the plane of the wheels until under the rack, where it then runs to one side of the rack's bottom support.

2 - NMO mount on the right, QB 430 antenna base on the left. Because of the way the antenna interfaces with the mount, I use the brass disk for the interface; according the the NMO mount manufacturer, that disk is for HF antennas. It is not obvious from the picture but the brass disk connects only to the center wire in the NMO mount however it is wide enough that perhaps capacitance is an issue. At VHF and UHF there is a different mounting system (see Photo 3)

3 - NMO mount on the right, dual-band antenna on the left. This antenna uses an interface consistent with what the NMO mount manufacturer is expecting. Notice the large brass disk is not present.

4 - NMO mount with the brass disk (inverted, so the pin can be seen). The pin fits in the center hole of the NMO, holding the brass disk in place. The center hole mounting point is surrounded in plastic, this holds the brass disk 1 or 2 mm above the aluminum surroundings. (EDIT: I did not originally realize it, but there is an additional insulator I neglected to put on. Sadly, putting it on does not make any difference. The insulator is not shown in the photos.)

Could it really be the brass disk causing this problem? If so, I guess it would be easy enough to just get a smaller one (where would I find one? There is a pin on the underside that mates to the NMO mount.) If not, what else could be causing this? Somehow the antenna seems to be electrically shortened, which points to a capacitance of some sort. Maybe I can just add a matching network?

Additional information: The antenna analyzer shows some sort of resonance --presumably the feedline being a multiple of $\lambda/4$-- at 410MHz. At 444MHz it seems to still be "recovering" from this resonance and the impedance is 36.2-j53$\Omega$. So maybe I just need to make the feedline longer or cut the antenna longer? (I made small changes to the feedline; it does make a difference but none of the changes I made were big enough to make enough of a difference.)

## Accepted answer (score 3, by rclocher3)

I'm just guessing here, but perhaps the problem is your ground plane. Your Childs Antenna Model QB 430 is designed to be mounted to a motor vehicle that presumably offers a relatively-large ground plane perpendicular to the vertical antenna.

Your ground plane is different. The main part of your ground plane, otherwise known as the bicycle frame, extends forward perpendicular to the antenna, but doesn't extend to the sides or to the back. You have some elevated radials that do extend to the sides and the back a bit, but not perpendicularly; instead they seem to go more downward than outward.

I wouldn't be surprised if the difference between a typical ground plane for that antenna and the ground plane that you're using explains the higher SWR. You could test the theory by installing the antenna on a car or truck, and then measuring the SWR. Perhaps someone at your local club has a car or truck with an NMO-mounted antenna that could be used for the test?

You might consider trying an HT antenna, which is designed to operate with less of a ground plane. An HT antenna would be less efficient than a mobile antenna of course, but I have a feeling that it would solve the SWR problem.

## Answer (score 3, by Bruce)

This Bruce, the guy who sold you that antenna. A good ground plane is key to a 1/4 wave like that. Another fix would be a shunted antenna. I make those too. I make a 5/8 wave, it is little bigger and longer, but requires very little to no ground plane.

## Answer (score 2, by Synchros)

I have a far less-optimized antenna mount on my bike (without the ground radials). Did you build the ground radials yourself, or was it a kit? You're bike mobile, it doesn't need to be perfect - in fact, do be more concerned about your safety (not injuring yourself with your antenna) than about minimal SWR. After all, if you're on the bike, you're a significant impact on your signal!

Your driven element is a bit short for 430-450 MHz. Is the dual-band antenna providing a good SWR on 440 MHz? If so, I'd look at the antenna, not at the mount. Given the low SWR at frequencies higher than desired, I'd test with a slightly longer, single-band whip.

The dual-band antenna may or may not require a ground plane. I have a dual-band Diamond SG7900, and it doesn't need a ground plane. On the other hand, if your dual-band is 1/4 or 5/8 wave on each band, it will need a ground plane.

As an aside, the brass insert gets removed when you are operating on HF. Leave it in for VHF/UHF. I have several of these Larsen mounts, and they operate similarly: https://pulselarsenantennas.com/wp-content/uploads/2017/01/ASB11-Cable-Assemblies-Mounts-10.pdf

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13357/nmo-bicycle-mount-antenna-has-unexpected-swr, by Chris K8NVH, rclocher3, Bruce, Synchros. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
