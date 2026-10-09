# Chimney Flashing Affect on Dipole Antenna Resonance

*Tags: dipole, resonance · score 4*

## Question

I put up a 40m dipole off a metal mast attached to a chimney mount on a 25' roofline. The chimney has metal flashing on the top with a metal spark arrest dome on top. I have 125' of RG8X feeding an MFJ 1:1 Balun which is strapped to a metal mast and stood off by 3"-4". There's 2'-3' between the flashing and the dipole feed point; but, the balun/feed-point is only 3"-4" from the mast in the chimney mount. The challenge is that the antenna appears initially to be electrically too long - balanced line resonance most likely below 7mhz. So, starting at 7.025 the SWR is 1.4:1 and at 7.295 is over 2:1. Figuring the antenna length is too long, I started shorting it; 3"-6" at a time. And after shortening the antenna length by almost 20" on both sides; the SWR remains unchanged: Question is, Could the Balun be Bad? (The Coax was tested and is good to 200 watts over 125') Measured tests are as follows:

- **Frq  Starting  cut 3"  cut 6"  cut 5"  cut 3"**
- 7.025  1.5  1.4  1.4  1.4  1.4
- 7.075  1.4  1.4  1.4  1.4  1.4
- 7.150  1.5  1.5  1.5  1.5  1.5
- 7.225  2.0  1.8  1.8  1.75  1.75
- 7.295  2.5  1.8  1.8  1.8  1.8

As visible from the table; seems that no matter how much length is being removed from each leg of the dipole, the reflected power is minimally unchanged. Output power was set at 100 watts on a Yaesu FT-2000 with the exception that at 7.295 mhz; the only output achievable on this unbalanced antenna load was 70 watts out.

I've studied balanced vs unbalanced lines but with this anomaly, I'm unable to arrive at any concrete understanding as to why the line length is having a nil effect. The only conclusion I've arrived at so far is that the flashing, spark arrestor and mounting poll are inductively altering the electrical length of the dipole due to the limited spacing. For that matter there could be some level of an open-air capacitive reactance going on.

Note that at one point I pulled it off the roof and tested it at 4' above ground and the SWR at 100 watts was flat at 1.2:1 from 7.025mhz to 7.295 mhz.

Any thoughts or suggestions as to why this is occurring and a viable solution perhaps. Could the dualband VHF/UHF above it be interferring? The chimney mount stays; but, I should be able to manufacture some type of standoff to move the feedpoint out 1-2 feet from the metal mast.

See the photo:

## Answer (score 2, by tomnexus)

I think everything is working about as you would expect.

The impedance of antennas is very sensitive to their height above ground, and at 40 m you are always less than a wavelength away where the effect is strongest. This is why your antenna looks different to what you measured when it was on the ground. The ground losses also increase a lot when lying on the ground, which can make an antenna look perfect there!  
Here's a picture I made for a lecture:  
The roof flashing, metal in the chimney pipe etc, as well as your coax, should have no effect on the antenna because it's in the centre of the dipole, and goes down perpendicular to the dipole, following a line of zero electric field.

The balun is probably working. You may get quite different, even maybe better, results without it, but that will be because the feed line is now part of the antenna, which means the shack will be full of RF and you could have (more) trouble with RF getting into your computer if you're trying digital modes, your microphone and other TV/audio equipment, etc. You can test the balun by putting a 50 Ohm load on the other end, but it will need to cope with the full power of your transmitter.

That looks like a solid installation. Be careful that the wires don't touch the pole, as they come out of the balun.

Now on to the possible solutions:

You have probably ended up with an impedance that's a bit too high. Depending on the height above ground, the real part (at resonance) could range from about 50 ohms, to 70 ohms (which is 1.4:1 VSWR). To get to resonance, the dipole probably has to be a bit shorter, but the minimum SWR may still not go below 1.4:1 without modification. When you're experimenting, rather roll up the ends of the wire first, so you don't risk cutting off too muhch at first.

The classic solution is to lower the ends of the dipole - this lowers the impedance of the antenna both by the change in its geometry, and also by bringing it closer to the ground. This will increase the ground loss too, and bring the high voltage tips of the antenna closer to people, so it might not be the ideal solution for you. A variation on this is to keep them high up but move one or both of the legs so the antenna is not straight. This may pull the pole over so be careful.

The impedance will also be lower if you let the tips of the dipoles hang down, or bend them sideways in the plane to form a U shape. This can't just be the last 2 feet of the antenna though, you probably need to bend over the last 6-10 feet to see a significant change in the impedance.

Finally, if you shorten the legs significantly past resonance, and then add a pair of series inductors at the feedpoint, the impedance will be lower. To get perfect 1:1 in the centre of the band I estimate you'll need to shorten the wire by 5 feet on each side. This will make the antenna close to about 50 - j50 ohms, so the value of the *total* series inductor required will be about 1 uH.  
0.5 uH for each leg can be made by winding a coil of 8 turns spread over 3" on a 1" outside diameter plastic pipe, or alternatively 3 turns spread over 2" on a 2" OD plastic pipe.

A low-effort way to test this would be find such a pipe, drill two holes, and *wind the dipole wire itself* around the pipe, secure it with electrical tape. Then shorten the dipole by 6' each end by winding up the wire (adjust the final total length, not the wire length as you used some of it in the coil. Adjust the dipole length for minimum SWR.

This solution will reduce the bandwidth of the dipole, which may be a problem for you if you need to cover the whole band. You can also implement it partially - reduce the antenna by just 2' each end, and wind a smaller inductor. OR go slightly further, so the impedance in the centre goes even lower and the SWR rises again in the middle, this might get you slightly more at the edges. I used this online calculator but there are many.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21343/chimney-flashing-affect-on-dipole-antenna-resonance, by K5KUE - Conrad, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
