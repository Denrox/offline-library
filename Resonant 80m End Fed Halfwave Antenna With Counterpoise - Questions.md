# Resonant 80m End Fed Halfwave Antenna With Counterpoise - Questions

*Tags: impedance-matching, balun, counterpoise, efhw · score 4*

## Question

Originally, I built an 80m EFHW, 130.5 feet long cut for approximately 3.58Mhz. I attached a 49:1 UnUn at the feed point 13 feet above the ground with coax back to the shack. I did not use a counterpoise but tied the secondary of the UnUn transformer to shield of the coax. It worked very well, out to Australia on the West and out to Russia on the East. The antenna is shaped like an inverted V, both ends at 13-15 feet in the air, the apex is about 45 feet in the air. The Inverted V apex is raised to 30 degrees above horizontal. The SWR was reasonable on 40m, 1.9.

I decided to experiment and built the same inverted V shape with a wire 117 feet long with feed point connected to the same 49:1 UnUn. This time I am using a 13.5 foot wire for a counterpoise, no connection to coax shield, overall length is again 130.5 feet. The 80m dip in SWR now occurs at 4.0Mhz and not at the 3.58Mhz as expected. I doubled the length of the Counterpoise and there is no difference. The dip is still 4.0Mhz. I wanted to tune the SWR dip by changing the length of the Counterpoise. I doesn't look like I can. What am I missing????

## Answer (score 2, by Raonoke)

Originally, I built an 80m EFHW, 130.5 feet long cut for approximately 3.58Mhz. I attached a 49:1 UnUn at the feed point 13 feet above the ground with coax back to the shack. I did not use a counterpoise but tied the secondary of the UnUn transformer to shield of the coax.

Unless you used a common mode choke, the outside of the coax cable serves as (a long) counterpoise. As the shield is now part of the antenna, it picks up all the electrical noise in the vicinity and the noise floor is raised on 80m.

I decided to experiment and built the same inverted V shape with a wire 117 feet long with feed point connected to the same 49:1 UnUn. This time I am using a 13.5 foot wire for a counterpoise, no connection to coax shield, overall length is again 130.5 feet. The 80m dip in SWR now occurs at 4.0Mhz and not at the 3.58Mhz as expected.

For 3.58MHz the antenna (main wire) needs to be lambda/2 at 3.58MHz (about 130.6 feet) and the counterpoise 0.05 lambda (about 13 feet) long.

You actually don't need the extra counterpoise wire. Tie both primary and secondary of the UnUn to the shield of the coax cable and put a good common mode choke about 13 feet away from the transformer. This avoids common mode currents and helps reducing the noise level.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22609/resonant-80m-end-fed-halfwave-antenna-with-counterpoise-questions, by Ron K5TDF, Raonoke. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
