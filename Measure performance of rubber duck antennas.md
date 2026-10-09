# Measure performance of rubber duck antennas

*Tags: antenna, impedance-matching · score 3*

## Question

I have a handful of no-name rubber duck antennas which came in stock with different brands of handheld radios. I also have a short Nagoya NA-701.

I would want to quantitatively compare them and decide which of them perform better than others in otherwise equal conditions.

I have:

- tinySA
- NanoVNA
- various attenuators
- calculator, paper, Wikipedia

What metric should I use and how could I conduct the experiment?

Initially I assumed that SWR should give indication of which antennas are better, since the less power being reflected back the more power being sent to air. But it appears isn't true since a dummy load can have SWR 1:1 and still not transmit anything at all.

I could use a DMR hotspot and just compare reported dBm and error rate of each antenna.

How would you solve this problem? What is the scientific way of doing it?

Specifically VHF/UHF, specifically rubber ducks, same size, same shape, same frequencies, same power 5-8W.

## Accepted answer (score 4, by Marcus Müller)

What is the scientific way of doing it?

The S11 measurements (equivalent to SWR or reflection coefficient with your "NanoVNA" network analyzer) you can already do, and: Antenna test chambers :)

You have the problem you want to know how much power leaves the antenna – and in which directions how much, ideally. (For your rubber duckies, for example, you probably do *not* want it to have a very deep "null" direction – your mobile handhelds are supposed to work in any orientation.)

So, you go and mount your antenna under test on a stand, at a sufficiently large distance from a calibrated reference antenna, put in a defined power into either antenna, and measure the amount of power that reaches the other antenna. You note that number (and if you have, also the phase), rotate the antenna under test by some degrees around the vertical axis, repeat the measurement, and repeat the test.

You get something like that if you draw the amount of power you got in any given direction (relative to the direction where you got the most, in dB):  
When you're done with one axis, you rotate the other, until you have all directions, looking from the center of your antenna, covered that you care about.

From that follow a few requirements for antenna test setups:

1. a reliable reference antenna (if you want to know how good your tested antenna is, a *calibrated* one, for which you know how the relationship between incident wave field amplitude and measured power is)
2. that antenna should ideally only "look" in one direction – you don't want noise from the rest of the world to affect your antenna, and also
3. the room with the setup in should be well-shielded against the outside and also
4. the room should have no reflection (although it's a shielded box, this is the expensive part)
5. you need a reliable measurement device for powers (if you want to know how good your antenna absolutely is, it needs to be *calibrated*)
6. a reliable source of RF power (bla bla calibrated)
7. your antenna stands need to be very robust (for the reference antenna) and ideally easily and reproducibly allow you to rotate your antenna (for the antenna under test)

Now, your existing vector analyzer can do points 5. and 6., probably. Nice!

Let me quickly sketch that for you. You care about the S12 in this measurement, i.e., how much power reaches from the antenna under test to the reference antenna:  
Nice. A solid wooden contraption or tripod for both antennas, two low-loss cables long enough to place them more than ~ 2 wavelengths apart and you're set. (You would first calibrate out the effect of the two cables by making a loop between the two ports of the network analyzer, but that level of *de-embedding* is bread&butter for VNA usage, I'm sure there's tutorials on that.)

Problematic is going to be the problem that the place you're doing this in is either going to be subject to interference from other people transmitting on the frequencies you're interested in, or you'll be in a cellar somewhere, where power will reflect like crazy off the walls, and you'll have a hard time doing a good measurement. (Because you never know whether you are seeing mostly the energy directly coming from antenna 1, or your antenna 2 is sitting in a place where reflections and direct path cancel out, or add up constructively.)

That's why people that measure antennas for science (and/or for a living) have *anechoic chambers*, clad with *RF absorbers*. They look very science fiction on photos, and, honestly, if you ever stand in one, you'll first be fascinated and then want out quickly – these absorber cones not only absorb RF, but are also pretty OK at swallowing sound, and an acoustically "dead" room with dim lighting feels *very wrong* to a human. Anyways, because of the sci-fi-ness of it, here's a classic photo of one that I've actually been in. The helicopter model is in storage in a room next to the operator room with the VNAs. The helicopter's not to scale, but the room is still a very large hall, completely covered in these absorbing polymer foam cones.  
Cables run from the antenna stands (one of which someone screwed a helicopter model to, the other) to below the floor, and out to the VNA.

You won't build something like that, sadly, unless you have a very rich uncle or such. So, you'll have to live with the interference! You first reduce that by using a high-gain antenna as reference antenna – in my sketch, a horn antenna is used, for that reason: you're still sensitive to interference, but at least only from *one* direction.  
You can also add an amplifier to the cable between VNA port 1 and your antenna under test – that way you get better SNR in the presence of other people on the air, but you need to de-embed with the amplifier in place.

You'd then make your stands high enough to avoid any significant amount of direct reflection from antenna 1 to 2 via the floor, and operate away from buildings, parked cars etc that might reflect significant amounts of power, too.

Of course, that leads to error bars in your measurements – better than nothing, but not great. If you were doing this for science or commerce, you'd simply pay an antenna test lab that has access to such an anechoic chamber to do the measurements for you. Obviously, that is expensive, so there's no sense in characterizing "cheap" antennas. Buy an antenna that comes with a radiation pattern as in Fig. 1 for at least the horizontal and vertical plane, or a complete 3D radiation pattern.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22730/measure-performance-of-rubber-duck-antennas, by Sergey Kostrukov, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
