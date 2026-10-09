# Basic antenna matching theory?

*Tags: antenna, antenna-theory, loop-antenna, antenna-modeling · score 5*

## Question

I'm fairly new to antenna matching, other than having built a base loaded vertical.

I'm also new to EZNEC and I tried to simulate an horizontal loop. I arbitrarily chose a 10x10M loop, so I added 4 wires, 10M each, 5 segments each (20 segments max on the free eznec version), 9M above ground. I configured the alternate feedpoint impedance at 300, 450 and 600 ohms.

The SWR sweep at 300 ohms shows SWR >100 up to about 7MHz, and it decreases and stays between 3 and 10 as frequency increases. Does this mean this antenna can't be tuned to the 160M band, or does this just mean that the impedance is so different from 300 ohms that the SWR is useless?

I would like to feed this loop with a balanced L network tuner. Series inductance, and shunt capacitance. At 2MHz, EZNEC shows an impedance of 23 + 2000j. Does this mean that I need to use a capacitor with -2000 ohms impedance at 1.8MHz, which would to compensate for the +2000 j in my loop?

Or in short,

can a 10x10M loop, 9 meters above ground, be matched to work on the 160M band?

(I suppose this will be a "cloud warmer" at this band, but still)

## Answer (score 4, by hobbs - KC2G)

Does this mean this antenna can't be tuned to the 160M band, or does this just mean that the impedance is so different from 300 ohms that the SWR is useless?

A little bit of both. If you get an off-the-shelf matchbox, which is usually advertised as being good for a 10:1 range or even less, then you can expect that it won't be able to make this antenna do 160m. If you build your own matching network you can "tune" pretty much anything, but the high SWR does give you some indication that the resulting system may be inefficient, narrow-band, or both.

I replicated your model in 4nec2 (except with more segments), and came up with a pretty similar frequency sweep to yours. But the feed impedance at 2MHz comes up as 0.12 + 1129j, not 23 + 2000j. This aligns with my expectations; a loop that size shouldn't have anywhere near 23 ohms of resistive component near 160m. In fact, the real part is <1 ohm on my plot up until 2.5MHz.

But let's say we want to tune it out. Lucky for me, my tool has an automatic network calculator, so I select "high pass L", and a 50-ohm Z0 (no point making things harder by trying to bring it all the way to 300). It suggests me a 70.3pF series cap (which is indeed about -1130j ohms at 2MHz) and a 195nH shunt impedance... hmm, something's off here, there's a precision problem. That's a bad sign, but let's press on. Okay, if I tweak the values to 69.98pF and 635nH, it tells me that I get 48.1 - 0.75j ohms at 2.0MHz, for an SWR of 1.04, which should make anyone happy.

**But**

this is a problem... assuming typical values of Q for capacitors and inductors, this matching network will eat up more than 90% of the power going into the antenna. Not only is that bad for your actual output power, it means that your matching network has to be built to dissipate all of that heat.

and *this* is a problem as well... we adjusted the network with fiddly precision for a good match at 2.0MHz, and we got that, but the system 2:1 SWR bandwidth is from 1.999 to 2.001 MHz. 2kHz! Not even enough for a decent SSB signal. The 10:1 SWR bandwidth is only 8kHz wide.

So yeah, maybe that does mean that the antenna "can't be tuned"... at least in a practical sense. I'm not an expert in this stuff but I don't think that changing the matching topology would improve things by any significant amount.

And by the way, yes, it's a cloud warmer, with a predicted maximum gain at 65° elevation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15479/basic-antenna-matching-theory, by hjf, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
