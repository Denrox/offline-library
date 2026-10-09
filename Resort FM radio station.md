# Resort FM radio station

*Tags: united-states, legal, fm, software, station-identification · score 12*

## Question

I stayed at a resort in the U.S. recently that is located in an unpopulated area with virtually no radio reception. To fill the gap, the resort has its own FM station that can be heard only within the resort (about a minute after you drive off the resort, it fades away completely). When you tune to the station, all you hear is one pop song after another, with fade/overlap between the songs. There is no station identification, commercials, or any other content.

The only resort employee I could find that knew any details about it said that he was the one who selects the playlist, using a desktop computer application but he didn't know anything about the radio transmission technology.

Does anyone have any information about this type of station? How does the transmitter connect to the software? What kind of equipment (antenna, etc) would it use? What is the software he's using? Where does it fit legally (FCC, etc)? How the heck are they able to keep the coverage area so tightly defined?

## Accepted answer (score 13, by SDsolar)

I believe you have encountered a Part 15 radio station.

United States Code of Federal Regulations, Title 47, Part 15 (47 CFR 15) covers such things as garage door openers and the like. As such, and due to the fact that they are unlicensed by definition, there is no station-identification requirement. Note that this section covers both intentional and unintentional radiators.

According to the FCC, in OET Bulletin 63: (October 1993), page 15, operation on the FM broadcast band is limited to an effective radiated output of

```
250 uV/M as measured at 3 Meters distance

```

This was originally intended to provide roughly a 200-foot transmission range. And you can have as many transmitter as needed to cover a larger area.

A typical Part 15 FM radio transmitter is the Ramsey FM100B.

Note that there is no limit to the number of transmitters that can be operated, so it is possible to cover an entire city block or more if you have enough transmitters.

(The Ramsey FM100B was also offered for overseas buyers as a 1 Watt transmitter through the addition of a secondary power amplifier board)

For longer distances, Part 15 AM is often a better choice because of the availability of radios like the Chezradio Procaster, which is FCC type-certified when operated with the integrated antenna.

Part 15 AM is limited to 100mW power output and a 10-foot antenna-to-ground length.

This opens many possibilities especially in terms of range. For instance, a Procaster on a rooftop with a 20-wire radial system (a counterpoise, or artificial ground) can often reach more than a half mile in radius.

Software: For low-budget radio stations, one of the best automation systems available for free is ZaraStudio.

The particular FM transmitter shown above has 2 RCA input jacks for each Line, and a 1/8" (3.5mm) jack for Mic Input. In other words, it has an internal mixer.

The only cable required to connect to a Line input from a PC is a generic one like this:

New 3.5mm 1/8" Stereo Male to 2 RCA Male AUX Audio Stereo Adapter Y Cable Cord

**As with all things FCC, the cardinal rule is that the station operator bears full responsibility to avoid interfering with any other licensed service.**

There is an active Part 15 community presence on the WWW. There are many types of antennas in use, including carrier-current where powerlines are the primary radiators.

If you are interested in setting something up yourself it is worth the time to search around and learn from the experience of others.

## Answer (score 2, by Richard Fry)

Of interest here: in the areas under the jurisdiction of the U.S. FCC, legal unlicensed operation in the FM broadcast band is limited to systems producing a maximum field intensity of 250 µV/m at a distance 3 meters in every direction from the transmit antenna. The applicable Rule is found in 47 CFR §15.239.

That maximum **free-space** field of 250 µV/m @ 3 meters will be produced by a simple, linear, 1/2-wave, center-fed dipole radiating an r-f power of 11.43 **nano**watts (0.000 000 011 43 watts).

However most of the "Part 15 FM" transmitters commercially available are rated for output powers of 10 **milli**watts or more.

It is up to the transmit equipment user to comply with the law, but probably few users of Part 15 FM systems know what that requires, or how to achieve it.

The FCC is active in finding and citing unlicensed operators who do not comply with §15.239.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9184/resort-fm-radio-station, by JoelFan, SDsolar, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
