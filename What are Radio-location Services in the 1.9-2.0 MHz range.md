# What are Radio-location Services in the 1.9-2.0 MHz range?

*Tags: united-states, hf, frequency, 160m-band · score 4*

## Question

I'm currently studying for the General Exam and in looking at charts of the new frequency privileges have run across a restriction I would like to have further defined. In the 160 meter band the books all say "1.90 MHz thru 2.0 MHz should be treated as a secondary allocation as we are required to avoid interfering with Radio-location Services in that range."

What are Radio-location Services at 1.90-2.0 MHz?

## Accepted answer (score 6, by Glenn W9IQ)

I wish you well with the general test!

The radiolocation services in question are defined in CFR 47 §2.106:

NG92 The band 1900-2000 kHz is also allocated on a primary basis to the maritime mobile service in Regions 2 and 3 and to the radiolocation service in Region 2, and on a secondary basis to the radiolocation service in Region 3. **The use of these allocations is restricted to radio buoy operations on the open sea and the Great Lakes**. Stations in the amateur, maritime mobile, and radiolocation services in Region 2 shall be protected from harmful interference only to the extent that the offending station does not operate in compliance with the technical rules applicable to the service in which it operates.

EDIT

I got to thinking about the comment by @RichardFry and wondered, how likely would it be that a ham could interfere with a fisherman trying to locate one of these beacons? Here is a rough first order analysis.

The output power of the buoy beacons run from 4 watts to 15 watts. The buoy antenna is a relatively short whip. So if the fisherman is searching for a 4 watt buoy in a 10 statute mile (8.6 nautical mile) radius and we assume the gain of the whip antenna is -10 dBi, a ham with a 100 watt transmitter and a 3 dBi gain antenna would have to be less than 220 miles away to have a signal equal to the buoy. That is a free space path loss calculation and the real path loss is likely to be greater so the ham would have to be even closer or use more power. It also does not account for the directionality of the fisherman's receive antenna which statistically speaking would be pointed unfavorably with respect to the ham's location.

Based on that very rough estimate, it seems very unlikely that the right distance, location, frequency, and time factors would come together to cause any real interference to the fisherman's objective. And if these factors would happen to align, the interference would be quite temporary.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12972/what-are-radio-location-services-in-the-1-9-2-0-mhz-range, by Dave G, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
