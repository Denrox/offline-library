# HF Noise Level S5 to S9+18

*Tags: rfi, noise, parallel-dipole · score 5*

## Question

Since I got my HF radio a year and change ago, I've been able to hear very little except noise and the WWV time station on 10MHz. Noise seems to vary by band, but not how I'd expect:

- 80m: S7-S9
- 40m: S9+10-20
- 20m: S2
- 15m: S3
- 10m: S9
- 6m: S5

My setup currently looks like this:

My antenna is fairly low above my house, but even killing mains power didn't reduce my noise level by any noticeable amount. I tried plugging in my 2m J-pole and it - being basically deaf on all of these frequencies - had predictable low noise on all bands, with none above S3.

- The feedline for my 2m antenna has a similar-but-physically-separate path to my transceiver than the HF dipole does.
- The dipole is only about 15 feet in the air on the low side and 25 on the high side.
- The dipole, transceiver, and tuner aren't grounded, but any ground nearby would be ~20' from short 5kV power lines that run along one edge of my property. The power lines are parallel to the dipole and the dipole is currently in the only place that I can put it on my property. I've heard that putting ground rods in our soil is miserable and haven't done it yet.
- I live in a suburban environment.

Does my conclusion that the noise is likely to be coming in through the antenna make sense? Should grounding make a difference? What steps can I take to try to mitigate the noise?

Suggestions so far are basically:

- Classic foxhunt with a small AM radio
- Hitting powerpoles with a stick/mallet/sledgehammer (seriously) and seeing if this affects the received noise.

## Accepted answer (score 6, by Glenn W9IQ)

Some troubleshooting ideas:


Check your radio's power supply for noise by substituting a battery and disconnecting the PS from the wall.


Run your receiver on a battery and turn off your main breaker. Make sure any battery powered computers/tablets are fully powered off. If the noise reduces, turn off all branch breakers, turn the main breaker back on, and one by one turn on the branch breakers noting any change in noise.


Install an additional 1:1 balun close to your radio. This sometimes helps prevent local noise pickup on the coax outer shield.


Check your coax for any open or marginal connections - especially the shield connections. Try substituting other coax.


Eliminate the tuner and short patch coax and note any change in noise levels.


Take your transceiver to a location in the country with a portable antenna and running off batteries to eliminate receiver problems. Alternatively take it to another ham's QTH that isn't suffering from noise to check it.


Borrow or rent a battery powered spectrum analyzer and walk your QTH and the neighborhood sniffing for RFI with a small dipole or loop.


After eliminating all other possibilities, call the power company and let them know you suspect a cracked insulator or bad transformer is causing RFI. They have techs that specialize in these sorts of problems.

## Answer (score 3, by Dave)

Just went through the same thing last year.

One hint - does the static level lower when it rains? if the answer is yes, very likely a bad insulator or distribution transformer.

Took my electric company almost 90 days to fix it, but went from +20 static down to S-2 or 3.

Also using a 160-10 fan dipole here. The problem insulator was at least 100 yards from my antenna.

The other advice is all sound as well!

73 es GL Dave - KB3MOW

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9160/hf-noise-level-s5-to-s9-18, by William, Glenn W9IQ, Dave. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
