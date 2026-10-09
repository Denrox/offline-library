# Signal path to maximize RFI rejection in an urban environment

*Tags: antenna, wire-antenna, rfi, antenna-system, noise · score 5*

## Question

Urban ham here (Cambridge, MA - FN42ki - KC1JZE) looking for tips to make this hobby possible in the city. I rarely can hear both sides of HF phone transmissions, and have yet to make contacts despite dozens of attempts on 80/40/20m using commonly described CQ etiquette over a full week. I do occasionally pick up what I assume are LatAm Spanish ham contacts. I've shut down breakers to whole house and run on 12V battery and saw some improvement but still not able to make contacts. Most webSDRs I connect to see to have much clearer signals and far less noise than my rig.

I've been soaking up resources like [RFI Noise at Antenna](Can%20I%20reduce%20RFI%20noise%20at%20the%20antenna.md), and Common Mode Noise Filter - Coax - Palomar Engineers®, and this PDF. Also have read the AARL book Small Antennas for Small Spaces.

What reasonable investments can I make in my signal path that will reject noise on a tiny plot of land (a tiny backyard with a tree)?

Right now my signal path is:

- Antenna: 50' medium gauge wire from fence to ~50' tree, dropping vertically down
- 4:1 LDG unun, ground connected to a pre-existing natural gas feed grounding wire - appears to be tied to copper/metal headed into the street
- 50' LMR-400 stiff cabling snaked into a basement office/ee lab
- LDG AT-200 ProII tuner (not grounded, but grounding has not made much apparent difference), tunes most bands around 1:1.5 - 1:2.6 SWR
- 3' RG8X coax
- ICOM-7300 grounded with a 20' run back to the same ground point (doesn't make much difference if disconnected.)

I've tried a few different end-fed long wire non-resonant antenna configurations but not seeing different results.

What is the right order of things to change? On the table:

1. Remote tuner with grounding wire
2. Counterpoise in addition or in replacement to ground connection
3. Addition of common mode choke at tuner and/or receiever
4. Addition of feedline chokes at unun or near entrance to house
5. Swapping to a loop antenna
6. Trying one of these DX canceling phasers with active antennas
7. Roof mounted antenna
8. Learn CQ

Much appreciated for the collective wisdom here.

## Answer (score 3, by Phil Frost - W8II)

**Definitely do:**

- Counterpoise in addition or in replacement to ground connection
- Roof mounted antenna

Or generally, some improvement to the antenna.

Your existing antenna sounds like effectively a vertical with no radials. This means much of the ground current is in the soil. The soil is a resistor. Resistors convert electrical energy into heat.

The ICOM-7300 is capable of 100W which should be sufficient for SSB when conditions are good, but not if 90% of that power is just making warm dirt.

I would see if your signal is even heard on some WebSDRs, in conjunction with VOACAP to see what combination of bands, times, and locations are likely to work. You won't make many contacts if no one can hear you!

Thus, my first recommendation is to focus on the antenna. A good antenna will help you on receive and transmit, and costs very little.

One way to go is a dipole. A dipole requires no radials, is cheap, easy to install, and works *great*. It needs to be at least a quarter wavelength high (but even higher is better) and a half-wavelength long. Depending on the space you have this might limit operation to higher frequencies. I'd suggest 20m to start, simply because there's a lot of activity there.

Another way is to install radials, at least 16 of them. But it's a lot of work, and in the city there's often not enough space on the ground.

A roof mounted vertical is a way around this. My first station was in a suburban 1/4 acre lot with a 1000 square foot ranch. I had a 4BTV in the center of the roof, with 16 radials which ran to the edge of the roof. This worked well because the roof was the largest flat space where I could lay radials.

Unfortunately this roof antenna was also pretty noisy since the house wiring was only a few feet below. If you can do it, I'd recommend the dipole first: if you can string it up in 50' trees to get it farther from the house that will reduce the RFI. But either will be a big improvement over your current antenna, I bet.

**Highly recommended:**

- Addition of feedline chokes at unun or near entrance to house

In the city there's really not much you can do about the ambient RFI, but you can get the antenna as far away as possible from nearby sources. But without a common-mode choke, the feedline *is* the antenna, and it comes in the house and connects to the radio, which is connected to the house wiring, which is connected to computers, switch-mode power supplies, etc. Without a choke, all these RFI spewing devices are literally *directly attached* to the antenna.

At a minimum, a [choke at the feedpoint](Using%20a%20balun%20with%20a%20resonant%20dipole.md) is a good idea. Another one at the entrance to the house can't hurt. If you like, [measure the common-mode current](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md) to quantify the improvement you get from a particular configuration. Remember that by reciprocity, if you measure a common-mode current on something when transmitting, that thing is also part of the receiving antenna.

Your "turn the house breaker off" test is also a good one. Ideally you're receiving RFI only from your neighbors. After getting the common-mode current under control, you might work to identify noisemakers in your own home and put chokes on them, making them less efficient radiators.

**If you want:**

- Learn CQ [assuming you mean CW]

It takes much less power to get an intelligible CW signal, so if you want to invest the time to learn Morse code, this certainly will extend your range. Many digital modes have sensitivity similar to or better than CW, so that's another route which doesn't involve learning Morse code. The FT8 and JT65 modes provided by WSJT software are a good example, though don't allow for free-form "rag-chewing". If that's your preference, you might look at PSK31 or even old-school RTTY.

**I wouldn't bother:**

- Swapping to a loop antenna
- Trying one of these DX canceling phasers with active antennas
- Remote tuner with grounding wire

[As discussed previously](How%20do%20active%20loop%20vs.%20passive%20loop%20differ%20in%20terms%20of%20noise%20rejection.md), loop antennas aren't really all that great.

Phasers could work theoretically: with a phased antenna array you have a more directional antenna system and can null out noise sources. But most of them are cheaply made, and I think you'll be disappointed.

A remote tuner might reduce feedline losses, but if you [do the math](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md) on the actual losses on 50' of LMR-400, you'll probably find they aren't more than a few dB. [A tuner won't provide any significant improvement to receive performance](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md). A grounding wire is irrelevant because there should be no common-mode current to ground in a proper antenna system.

## Answer (score 3, by Glenn W9IQ)

As a new ham, you may have more success answering a CQ since you will then know that you can at least hear the other station over your local noise. Answering a CQ also requires less finesse so you are less likely to be identified as a newbie. But we have all gone through this phase so I can assure you that once you get a few QSOs under your belt, you will be more comfortable and successful.

I would also encourage you to get active in a local ham radio club as you will find many mentors (also known as Elmers) that can look at your antenna situation and listen to your on the air practices. Club members may also have handy tools such as an antenna analyzer that they can bring with them to accelerate antenna troubleshooting.

With regard to your antenna, here are a few thoughts.

#### Radials

You describe your antenna as nearly vertical, coming down to a fence in your back yard. It appears that your backyard fence is typical metal chain link type fence. You may be able to use this as the other half of your antenna by connecting outer coax connection to the metal fence where the vertical wire meets it. A coax grounding block makes this an easy connection:

You could also use a lightning arrestor type device and connect the ground tab to the fence:

Make sure to waterproof this connection. At the same time, I would eliminate the connection to your gas pipe ground wire.

Doing this will change your antenna from an end fed, vertical wire to something closer to a vertical antenna with a ground plane (with the fence as the ground plane). This should give you a more favorable directional pattern.

#### Common Mode Current

Common mode current (CMC) is often not well understood by hams. When common mode current exists on a coax, or more generally the feed line, the coax becomes part of the antenna instead of simply being the feed line. This is usually undesirable as then your antenna comes directly into your shack picking up any noise close to the coax. CMC also alters the directional properties of the antenna. CMC can also alter the expected SWR of an antenna (but higher SWR does not cause CMC).

The best defense in your case against CMC is to use a high quality 1:1 choking balun (not unun) installed at the feedpoint of your antenna. The job of the choking balun is to "choke off" CMC so your coax does not become part of the antenna.

#### Try Eliminating the Unun

The 9:1 unun you have installed is likely not necessary and may even be detrimental once you install radials (e.g. your fence) as part of the vertical antenna. On 40 and 80 meters, your 50 foot vertical is already shorter than a 1/4 wave which means that it will have a low feedpoint impedance. The 9:1 unun will attempt to further reduce this feedpoint impedance making the SWR even worse. On 20 meters, the unun is of marginal benefit.

## Answer (score 2, by sm5bsz)

I suggest you investigate your local E-fields and H-fields. Then decide whether you want an E-field sensor (whip antenna) or an H-field sensor (a loop) for receiving. There are good reasons for using different antennas for receive and transmit. The receive antenna may have less than 1% efficiency - you just want it to not pick up local fields. The transmit antenna should have high efficiency but it does not matter if it picks up interference.

I suggest you look through all of these videos: http://www.youtube.com/watch?v=ItLkn8r4s3E (24 minutes) http://www.youtube.com/watch?v=zsZTX7MQSGQ (48 minutes) http://www.youtube.com/watch?v=kgMbaJDFu9M (55 minutes) http://www.youtube.com/watch?v=C65u7Pmz7a0 (21 minutes)

This is two and a half hours. You might find parts of it irrelevant to your problem (and boring) but it is all there for a reason, something that comes later may require an understanding of previous parts.

For interference fighting:

1) Eliminate problems at source as well as you can. Bad switch power in your own home can be replaced or provided with adequate filters. Some of your neighbours might be friendly and accept that you offer them another led light (or whatever) or place a ferrite core on some of their wires.

2) Investigate your local fields and select the optimum location for an E-sensor, an H-sensor or possibly several of them.

3) With more than one field sensor for receive you can use a phasing system to cancel one particular noise source. That can be done automatically with a two channel radio as you can see in the videos, but it can also be done manually.

With many sensors, many analog balancing units you could eliminate several of the local interference sources. Combine two sensors to eliminate a particular QRM. Then combine two other sensors to eliminate the same QRM. Finally combine the outputs of both combiners to eliminate a different QRM.

Of course digital technology could do this MUCH better, but to my knowledge there is no hardware available today.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10569/signal-path-to-maximize-rfi-rejection-in-an-urban-environment, by Jeremy Gilbert, Phil Frost - W8II, Glenn W9IQ, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
