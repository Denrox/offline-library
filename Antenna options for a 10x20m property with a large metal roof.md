# Antenna options for a 10x20m property with a large metal roof?

*Tags: antenna, antenna-construction, hf · score 7*

## Question

I live in a house that sits in the middle of the city, in a lot 10x20m in size.

The first 6x10m are covered by a metal roof with a rather low angle (IIRC only 50cm difference between the highest and lowest point). The rest is concrete roofing.

I would like to set up an HF rig at this location again. Many years ago my dad had a 4 element yagi with a rotator for HF, and this metal roof did not exist.

What options do I have as far as antennas go? I'm severely limited by length to install dipoles. In practice I only have 10m "wall to wall" where I can bolt hooks to hang a dipole.

I thought of trying with a piece of iron pipe I have, it's about 63mm in diameter, 6m in length, attached to a wall with U bolts. I thought of moving to one side of the metal roof and see how it performs as a vertical antenna with the 6x10m roof as a ground plane. But I'm not sure if this would give any sort of reasonable result.

In practice, right now, I'm using some mobile vertical antennas on a tripod of sorts.

Here's a top and side view of my house

What are my options (ideally DIY but commercial solutions would be viable too) for this property? I don't have a particular band I want to operate.

## Answer (score 2, by Brian K1LI)

"If you can't fix it, feature it!" As @R2AUK points out, the metal roofs *might* act as a useful part of a vertical antenna. I recommend placing a mobile magnetic mount in the middle of the roof area:

A skilled person could fashion such a mount from available materials. The radiator could take many different forms. A mount like this with an 11-ft long "CB" mobile whip worked well for me on the 40-10 meter bands, with a short run of coax and a match box (antenna tuner) at the radio. (Note: the high resistance of a telescoping stainless-steel whip probably makes it **inappropriate** for transmitting.)

A "screwdriver" antenna uses a motor-driven variable inductor to match the vertical radiator to the feedline at the antenna.

Searching the internet for "homebrew screwdriver antenna" turns up plenty of interesting design and construction ideas.

## Answer (score 2, by Aleksander Alekseev - R2AUK)

Generally speaking, I wouldn't recommend to work from the middle of the city at all. Because of the high noise level your experience with ham radio will be awful. If you have ANY option to work on HF in a suburb, I highly recommend to choose this path. Personally I travel 1.5 hours to the country house (35 km from the center of the city) every Friday and travel back to Moscow every Sunday. This being said I don't know what the noise level in your QTH actually is, maybe it's not that bad.

I've experimented with some "indoor" (not actually indoor, see next) antennas and currently the results are following.

- A shortened vertical antenna (I'm using OPEK HVT-400B) on a balcony works reasonably well and it's more or less effective on 10-40m bands. There is nothing to do with this type of antenna on 80m even if the manufacturer tells otherwise. You need place for one or two radials to make the antenna work. This type of antenna doesn't work indoor, I've tried.
- Magnetic loop antenna (I'm using CHA F-Loop 2.0) on the balcony works reasonably well on 10-20m bands. It's not very efficient on 40m, although it's possible to make a few QSOs. There is absolutely nothing to do with this type of antenna on 80m. Magnetic loops don't require radials but are very narrowband and usually handle only 10W in digital modes and 25W in SSB. You should be not far from the loop to tune it every time you change the frequency. Magnetic loops don't work indoor despite what the manufacturer may say.
- A shortened DIY dipole ("Buddipole") didn't work well on a balcony, probably because of the proximity to metal objects. I'm going to test it outdoor in the nearest feature.
- A long wire antenna (23.5m) throwed from the window to a tree with a 8m counterpoise along the wall and MFJ-971 tuner works fine on 10-80m. The only problem with this antenna is that it's noisy comparing to a dipole or delta loop.

Please note that all these antennas are comprimise antennas. Their effectiveness cannot be compared to the effectiveness of non-comprimise antennas you can build in the suburb, like a (trap-)dipole or even more effective delta / quad loop.

In your case it's worth trying to build a vertical antenna on the metal roof. Personally I would attach a wire to a 7.2m long fishing rod, put an autotuner (like mAT-40 [1] or similar) in the bottom of the antenna and attach a few radials 5-10m long just in case metal roof will not work well as a ground. Such antenna will be multiband and should work well on 10-40m.

[1]: Hint - you can purchase a cheaper tuner, like mAT-30, designed for indoor usage, and make it suitable for using outdoor by filling it with silicon coating. Please note that mAT-30 is intended to be used only with Yaesu transceivers, but there are similar models for Kenwood and ICOM available on eBay.

## Answer (score 2, by Ted)

I have just put up a magnetic loop on a metal aircraft hangar roof. It plays! The antenna is vertically mounted on a tripod, and is 4' by 6' using 3/4" copper tubing. A dozen tests on 40 and 60M showed an average of 4- 6 dB better reports than a full wave delta loop at the same 20' height above ground using the same power.

The magnetic loop will also give you much quieter receive than a vertical or dipole, especially if it is rotated to null the worst local noise source on installation. Because the the null is within 20 degrees of the horizon, the loop is effectively omnidirectional for skywave, including NVIS.

The metal roof acts as a shield, so RF exposure is a non issue. For mounting, I'd leave the 18' pole alone. A 5-6' tripod with cement block weighted legs and a 10' pole in the center of the roof would work, since the bottom of the antenna only needs a few feet of clearance. Matching is done in the customary way, with the coax attached to a small loop opposite the tuning capacitor. Keep the control and feed lines symmetrical with the axis of the loop.

There is no reason to restrict power. Tuned with a 15kV vacuum variable capacitor, It'll handle a kilowatt. The tuning problem is easily solved with an off-the-shelf stepper motor, driver and encoder from a robotics supplier. No programming necessary, and easier than an antenna tuner (only one knob) Mount the motor at least 8" away from the antenna; use an on/off switch for stepper power as they are noisy.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13206/antenna-options-for-a-10x20m-property-with-a-large-metal-roof, by hjf, Brian K1LI, Aleksander Alekseev - R2AUK, Ted. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
