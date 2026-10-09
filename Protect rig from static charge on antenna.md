# Protect rig from static charge on antenna

*Tags: antenna-construction, wire-antenna, equipment-protection · score 13*

## Question

**How can I continuously discharge static from my end-fed antenna?**

My Electraft K2/100's autotuner (schematics) has an SWR bridge using two 1N5711 pin diodes. These diodes get blown if any static builds up on the antenna. I've replaced them four times now. It's nice that I can replace them, but I'd rather not buy diodes in bulk.

I keep the antenna disconnected when I'm not using it, but sometimes forget to disconnect it when I'm done. Plus, static can build up when operating--rain puts a terrific static charge on the antenna. So I need some kind of protection from static.

I've read that I can use a resistor or coil between the antenna and ground to bleed off static, but I don't know what to build or buy.

My antenna is end-fed wire slung out of a tree and run through a small hole in the wall. There's just a few feet of feed line between the rig and the antenna.

The RF ground is a ground rod just on the other side of the wall and connected to a jumper cable wire also poked through the wall. The jumper cable connects to a copper pipe mounted to the bench. Connected to the ground pipe are:

- The rig's ground lug
- The tuner's ground lug
- One side of the balun

The ground rod is not connected to the house's electrical ground.

The AC ground is connected only to the station's linear power supply.

The antenna, RF ground, and feedline all meet at a 1:1/4:1 switchable balun.

The rig outputs 100W on 80M-10M, but I operate mostly on 40M and 30M.

## Answer (score 4, by Phil Frost - W8II)

A resistor works. A coil works too. Even a very large resistor is sufficient to dissipate a little static. The advantage of a coil is that it can afford some additional lighting protection, shunting some of the strike current to ground at the antenna so surge protection farther down the feedline has to deal with less. A coil can do this because a significant portion of the strike current is at lower frequencies. A resistor, on the other hand, will probably just be vaporized before it can do much.

You can calculate the loss (and thus, the necessary power rating) of the resistor knowing the feedline impedance and transmitter power. For example, with a 100W transmitter and a 50Ω antenna feedpoint, we can figure the RMS voltage at the feedpoint is:

$$ E = \sqrt{PR} \\ 70.7\:\mathrm V = \sqrt{100\:\mathrm W \cdot 50\:\Omega} $$

If we had a 10kΩ resistor, then the loss would be:

$$ P = E^2 / R \\ 0.5\:\mathrm W = (70.7\:\mathrm V)^2 / 10000\:\Omega $$

Note this is an approximate solution that is valid only if the resistor is much larger than the feedpoint impedance. We probably want at least a 1W resistor here, but more would not hurt. Using a larger resistance (say, 1MΩ) reduces the resistor power. We can also see that the power goes up with the square of voltage. If you have a 1kW station, you will need a very much larger resistor.

You can make a coil easily enough by winding some solid wire around a suitable form, then removing the form. A soda can works, but it's not especially critical. You will want to add enough inductance that it doesn't significantly change your antenna tuning. For lower bands you need more inductance. If the inductance is too low, then you will need to shorten the antenna, thus making it capacitive. This is actually a useful thing for mobile antennas, but I digress...

A lighting arresters will also by nature provide protection against static build-up. Their datasheets should provide a clamping voltage or a turn-on voltage. When they are working, they guarantee that the voltage between the feedline conductors will never be much greater than this. If this voltage is also below the threshold that damages your radio, you're golden. If you do install a lighting arrester, do be sure to [install it correctly](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md).

## Answer (score 3, by James Palmer)

As hotpaw2 mentioned already, a basic search yields a wealth of information about RF chokes and bleeder resistors. Mainly, you need to decide what you're ready to set up. For a bleeder resistor, somewhere around 10k$\Omega$ up to 1M$\Omega$ seems appropriate. Make sure the power rating is high enough.

The nice thing about an RF choke is that it can have a relatively lower resistance to ground for static charges, and a high impedance for RF power. I would guess an old transformer might even work, it just needs a few hundred millihenries.

http://hpfriedrichs.com/radioroom/bleeder/rr-bleeder.htm

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2276/protect-rig-from-static-charge-on-antenna, by Wayne Conrad KF7QGA, Phil Frost - W8II, James Palmer. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
