# End-fed wire antenna lengths

*Tags: wire-antenna, end-fed-antenna · score 7*

## Question

I want to use an end-fed wire antenna, but what would be the best length of wire for the 20m and 40m bands?

Is there a way to work this out?

This is assuming a tuner will be used.

## Accepted answer (score 1, by Phil Frost - W8II)

The length doesn't matter much. If you make it the right length, then it will present a good match to your feedline, but if you have a tuner, and either place it near the antenna or use a low-loss feedline, then that doesn't matter.

It's also possible to get really unlucky and pick a wire length that's outside of your tuner's range. What these lengths are depend on your tuner and also the wire's surroundings and also the ground system. Odds are that most lengths are fine though, so the easiest solution is to pick a length based on something else (like, the room you have available) and if you get unlucky, roll the dice again.

Also, if the wire is too short, then it won't be a very effective radiator. If the wire is longer than half a wavelength, then making it longer doesn't make it any more effective. Making it shorter than half a wavelength doesn't suddenly stop making it working either, so if you don't have enough space to put up a full half-wavelength that's fine, too.

Fact is, if you can effectively couple RF current into something that's large relative to the wavelength and is a good conductor, you get an antenna. The bigger problem with end-fed antennas is subtle: it's actually only half the antenna. The ground is the other half, and I don't mean Earth. I mean whatever is attached to the other half of the feedline. If you are using a tuner that has just one wire coming out of it, then the other half is the tuner's chassis, and whatever is connected to it. If you are concerned about making a good antenna, my advice would be to learn more about end-fed antennas work, and interact with ground, before worrying about length.

## Answer (score 4, by Glen Ellis K4KKQ)

I have used an End-Fed Long-Wire antenna for many years. I have used it on 80M, 40M, 20M with 1:1 SWR... I did NOT try for the shortest long-wire possible. I did use a Long length which is several Odd Quarter-Wave-Lengths of my target bands 40M and 20M.

It is 186 feet long, up 17 ft, in the shape of a letter "Z" and controlled by a Antenna Tuner and fed via 52 Ohm Coax, 32 ft long. It is a copy of the BASIC SIMPLE LONG WIRE ANTENNA found at w8ji website for antennas  
and http://www.w8ji.com/long_wire_antenna.htm

My Long Wire has aprox. 11.5 quarter wave lengths on 20M. My Long Wire has aprox. 5.5 quarter wave lengths on 40M. Being aprox. odd quarter wave-lengths of the target band is important. The Antenna Tuner will load an End Fed Long Wire effectively, especially if it is cut to aprox. an Odd Quarter Wave-Length of your target band... 186 ft / 16.5 ft and 186 ft / 33 ft... The entire antenna is #12 stranded insulated copper.

The Antenna Tuner is a 1977 HeathKit HFT-9, a small QRP size tuner of the Cap-Coil-Cap double"L" design. Super simple. I use an MFJ-813, QRP-SWR-WattMeter calibrated model, and run 1W commonly.

As for effectiveness, I have worked most Europe, All States, and Hawaii at QRP/p 1 W with this antenna.

For Tuning to get more bands, as an experiment, I simply wrapped up 5 or 10 or 15 feet of the end in a tight loop, wrapped tape around it, and let it dangle. The Tuner brought in 80M, 40M, 30M, 20M, 21M, at SWR 1:2 and less. When adjusted slightly for 40M and 20M, the SWR can be 1:1 always, as the tuner is adjusted slightly to get the entire band.

The "other half of the Long-Wire" is called a "Counter-Poise" which can be aprox. 10% to 15% of the long-wire length. My Counter-Poise is aprox. 23 feet long, and dangles away from my Long-Wire Antenna. ... Counter-Poise is NOT grounded to anything. Nada, Zilch, No Ground. W8JI writes "adding ground rods can decrease RF efficiency when an insulated counterpoise is used." I have verified this by experiment. Inside the Shack, at the Antenna Tuner, there is a solid earth ground for the all the equipment, including the ground of the Antenna Tuner. ...

This is similar to the standard Antenna we use at all our Field Day Installations with great success. We toss our Long-Wires over Tree tops and dangle the counter-poise away from the Long-Wire.

... Read the easy text written by W8JI .

... Hope that helps. Glen Ellis, K4KKQ, CW/QRP 59 years.

## Answer (score 2, by Frank Mooney)

I have used both 107 and 71 ft lengths, but didn't see much difference as my old KW At-230 tuner tuned both just fine.

I fed them through a 9:1 balun and 50 Ω coax with 25 ft of coax back under wire, possibly acting as counterpoise, but I'm not sure about that.

Everything is well grounded in my shack. It worked pretty good on 40 & 20m.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1859/end-fed-wire-antenna-lengths, by Phil_12d3, Phil Frost - W8II, Glen Ellis K4KKQ, Frank Mooney. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
