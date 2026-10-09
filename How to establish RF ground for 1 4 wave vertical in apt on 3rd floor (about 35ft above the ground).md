# How to establish RF ground for 1/4 wave vertical in apt on 3rd floor (about 35ft above the ground)

*Tags: vertical-antenna, grounding, bonding · score 3*

## Question

I am struggling to understand how to introduce an MFJ-931 artificial RF ground into my current system and am hoping for some help to sort out best practices. Although my use-case seems pretty common, I have not been able to find any helpful information on the Internet. So, I am hoping for your comments and suggestions.

Here is my configuration before introducing the artificial ground...

Where is the shack...

- I live on the 3rd floor of an apartment building about 35ft above the ground.
- I don't have access to an Earth via copper water pipes or grounding stakes.
- I use the ground in my A/C connection on the wall as the electric ground on the transceiver.

Antenna System... I have a 1/4 wave vertical antenna based on a 40m hamstick. My antenna system is not permanent and needs to be stealthily deployed when I use the radio at night. It is clipped onto a wooden rail on my balcony. Since there is no counterpoise, it is unbalanced. I don't have counterpoise because it would be too long for where I live and on the 40m band. Usually, I use a 40m balance diplole with two hamsticks, but I've found it to have very limited bandwidth within the usable SWR range. So, I wanted to see if things would improve by using a single vertical. The single, vertical hamstick is attached to 50 ohm coax going to Palamar 1:1 balun (CUBE Feed Line Choke Unun) to get rid of common mode noise. Coax runs from the balun to a Palamar Coax Common Mode Noise Filter. Coax runs from that filter to an Elecraft K3S transceiver. The only automatic tuner is the one that is built into the transceiver at this time.

For RF Grounding... I have a wooden desk and have placed a 1/16th inch aluminum sheet metal plate on top of it. I've drilled a hole in the aluminum ground plane for each device: my Elecraft K3S transceiver, power supply, and Elecraft P3 panadapter, and each device is connected its hole in the ground plane by a 10 AWG wire. The aluminum ground plane has a wire that attaches to the A/C ground.

For Electrical Grounding... The transceiver is attached to the A/C ground.

So, now I am stuck... I have an unbalanced antenna that needs counterpoise. I purchased the MFJ-931 to provide that counterpoise. My understanding is that I would insert the artificial ground as follows, but after doing so, no matter what I do with the controls on the MFJ-931 while transmitting a CW, the analog meter never moves.

- I connected the ground from the transceiver to the MFJ-931 "TO XMIT" connection on the artificial ground.
- I connected the end of a 100m, 10 AWG spool of copper wire to the Counterpoise connection on the artificial ground.
- I crimped an insulated end-cap on the end of the counterpoise wire. I set the sensitivity on the artificial ground to maximum. - - While transmitting a c2w at 1 Watt (to minimize interfering with others while testing), I rotated the inductance and capacitance dials, but the meter did not move. I noticed that my SWR was very high.
- I changed the frequency to one that would be around 2 when using two hamsticks as a dipole, but it didn't make any difference.

I apologize for such a long posting, but I wanted to describe what I have, what I've tried, and where I am stuck. Hopefully, these details and any guidance from our Elmers will be helpful to others, too.

Thanks for your time and interest, Mike

## Answer (score 4, by user10489)

There are three types of "ground" in a radio system:

- Electrical ground
- Lightning ground
- RF ground

Electrical ground should come from the outlet you get your power from.

Lightning ground would come from a ground rod and be connected to electrical ground somewhere close by. In an apartment, this is something you probably shouldn't mess with.

RF ground is a misnomer and really isn't ground at all. A dipole antenna is a half wave long. If you have a quarter wave antenna, it is a monopole, which is actually half of a dipole. The "RF ground" is really just the other half of the dipole. Since you are mounting this to wood, you need to make the other half of the dipole -- either by adding "ground" radials at the antenna, or just a single counterpoise wire that is about a quarter wave long (maybe a little longer). Even if you were mounting this to metal, you might still need to do this if the metal isn't large enough.

If you try to use your electrical ground as RF ground, that means you will be bringing RF energy into your shack, which can be very dangerous.

For a 40m antenna 35ft up on a balcony, you might be able to just drop a quarter wave wire to the ground as your counterpoise. This, however, might not be practical or may be dangerous to others depending on the situation and how close that wire will be to others. The MFJ-931 can't replace this missing counterpoise, and without it it is likely your coax will replace it and will radiate. The purpose of the MFJ-931 is partly to act as an antenna tuner to make up for the missing counterpoise and partly to stop the common mode current on the coax at the MFJ-931 instead of allowing it to get all the way back to your radio, possibly making the radio chassis itself RF hot. This basically attempts to fix a dangerous situation in a way that may work but severely compromises the performance of the antenna.

## Answer (score 3, by Louis Seaman)

First, make sure you don't confuse ground with a counterpoise (so called artificial ground) in an antenna system or radio equipment set-up; a counterpoise can NEVER act as Earth ground, while Earth ground might be able to act as a counterpoise. You describe your antenna as a "Ham Stick" design, which as far as I know, is a 1/4λ radiating element, and if you do not use a BalUn (which you should not, since that would cause your counterpoise to become a radiating element, inside your apartment), your antenna is unbalanced even with a counterpoise, but to be clear, you do need a counterpoise, which is I guess what you are trying to achieve with the MFJ device. Keep in mind that with a 1/4λ or odd multiple of a 1/4λ antenna radiator, a counterpoise is typically a 1/4λ of the operating frequency, or an odd multiple of it, although there is no point to making a counterpoise any longer than a 1/4λ, unless you were trying to achieve a multiband antenna, and therefore have a "fan" configuration.

The MFJ-931 box appears to simply add inductive and capacitive reactance to your counterpoise, as you determine its settings by watching your VSWR as you tune the MFJ device; so if the counterpoise were a too short or long, the MFJ would bring the voltage and current on the counterpoise, back into proper phasing. The meter shows current, and can likely also be used to optimize tuning, but your RF on your counterpoise may be finding an alternate path to ground through your AC wiring.

Also keep in mind that depending on where the MFJ-931 is located on your counterpoise wire, it may not be at a current loop, and therefore the ampere meter in the MFJ-931 is unable to detect current on the counterpoise; also realize that on 1/4λ antennas, current loop maximums occur at the feed-point and every 1/2λ from the feed-point.

If I were in your position, I would simply cut a 1/4λ wire, and let it hang from the coax shield side of the antenna feed-point, and make a choke out of the coax at the feed-point by wrapping the coax 10-12 times into a coil at about 14" or 36cm in diameter, and taping or zip tying the coil to keep its form. This way RF on your counterpoise stays outside your apartment, and the choke keeps RF on the shield from coming back to your radio, to a minimum.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21696/how-to-establish-rf-ground-for-1-4-wave-vertical-in-apt-on-3rd-floor-about-35f, by A Bit of Help, user10489, Louis Seaman. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
