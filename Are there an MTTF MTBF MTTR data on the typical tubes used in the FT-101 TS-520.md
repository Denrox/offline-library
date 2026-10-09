# Are there an MTTF/MTBF/MTTR data on the typical tubes used in the FT-101/TS-520?

*Tags: electronics · score 5*

## Question

I browse ebay.com for used rigs in good condition and approaching my shoe-string and ... There appear to be a decent quantity of boat anchors out there - FT-101, TS-520, TR-4 to name just a few.

By definition, a boat-anchor would date to the 1970s/1980s. Are there any MTTF/MTBF/MTTR data on the typical tubes used in one of these beautiful rigs?

I know it's a difficult question to answer because in all probability the answer would be 'It depends'. An old Ekco acquired by my grand-dad back in the early 1930s was still working in 2008 until it got water-logged - and later stuff dating to the 1950s/1960s are *still* in excellent trim!

## Answer (score 5, by Paul S)

The original RCA specs for 12BY7 and 6146 did not disclose estimated lifetime of the tubes. An average tube has a lifetime of 2,000-4,000 hours, sometimes much-much more depending on usage. Given a low transmit duty cycle on CW/SSB (compared to prolonged TX with digital modes), and the radio is properly tuned and maintained, the tubes may last a lifetime.

I have Kenwood TS-520 made 35 years ago. It has three original 6146A and two 12BY7A tubes. It's still in great shape just starting showing its age - the driver tube doesn't drive well on 10m anymore and so the output power on 10-15m bands is lower.

Tune-up is a good time to check your rig for maintenance requirements. As K4EAA explains here :

Notice how much drive is available. A fresh 12BY7A will provide more drive than necessary to swing the ALC Meter through its range, even on 10M. Low drive on any band shows that the driver tube is probably falling off in emission. It will continue to function for a while, but you might consider replacing it in the near future. Watch for falling drive level as the rig is keyed for a few seconds. A 12BY7A near the end of its life will fall off in drive within a few seconds or so of key-down. If you see your drive fall as you are watching, that tube is positively ready for retirement.

Check the sharpness of the dip in CW Mode. A broad, shallow dip means the finals are nearing the end. You will notice reduced power output as well, most noticeable on the higher bands. Check for falling plate current under key down conditions. Just like the driver tube, final tubes at the end of their useful life will jump to full Ip and then quickly start falling off. When you spot this, they are ready for recycling.

The HV position of the meter reads the plate voltage applied to the finals. The Kenwood hybrids utilize a voltage doubler circuit in the HV power supply, and aging High Voltage capacitors can result in low output. To check for this possibility, monitor the HV as you key the rig. It is normal to see perhaps 10% drop in HV when keyed. Anything much in excess of this might indicate failing capacitors.

**Don't buy these hybrid / tube radios to use for digital modes** - e.g. PSK31, RTTY - **as the tubes won't like it. For CW / SSB you're okay.**

The other issue with these rigs is VFO drift - your frequency will drift while the radio warms up.

The other parts that may require eventual replacement are electrolytic capacitors in the power supply and relays. The band / mode switches (contacts) may become oxidized with time and need clean-up / replacement too.

The replacement tubes are available sometimes on ebay. K4EAA has spare driver tubes for sale: http://www.k4eaa.com/parts.htm as well as some good info on using boat anchors properly. There is more info and manuals available from: http://www.n6wk.com/kenwood

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1967/are-there-an-mttf-mtbf-mttr-data-on-the-typical-tubes-used-in-the-ft-101-ts-52, by VU2NHW, Paul S. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
