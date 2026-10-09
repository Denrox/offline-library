# Would retrofitting an external antenna to a smartphone be feasible?

*Tags: antenna, diy · score 3*

## Question

I'm not sure if this is the proper StackExchange site, but you guys know RF and I don't know who else would know better.

I take the commuter rail to work every day. I have 60-70% cell phone coverage. I can regain 500 hours of my life per year if I could maintain a reliable data connection all the way in.

I've thought of switching carriers to get a hotspot device that supports external antennas, and carrying a 8dBi antenna in my backpack to place on the train table. Then I thought perhaps I can do the same with my cell phone and save that hassle.

I looked into the teardown of my device - the LG G5. It has two connections which would become perfectly accessible with some carefully drilled holes in the back cover. See bottom right:

Would gaining access to these ports, locating an adapter, and hooking up an antenna be effective and/or even possible in this scenario?

I could get a soft case with holes drilled in the right places, hot glueing the adapter cable to it for strain relief.

I also love the idea of being able to have a 2 foot antenna on a magnet on the top of my car next time I go camping or for a remote roadtrip.

## Answer (score 2, by Kevin Reid AG6YO)

From general radio-equipment principles, there's no reason you *can't* do this. However, there are many caveats, and it may be impractical without technical information you can't have. Here's the points you should consider:


It may be illegal to use a device with a modified antenna. This is true of some radio services in the US; I don't know if it's true of cellular radio and you haven't specified a location.


Those connectors may not be antenna ports, but serve some diagnostic purpose, or be for Bluetooth or WiFi antennas rather than cellular antennas. **You need to find this information.**


An antenna used for transmitting (as cell phones do) must be impedance-matched to the transmitter. If not, there may be damage to the transmitter. Some degree of mismatch is tolerated (and it is possible that the existing antenna is severely mismatched due to being small) but unless **you have the datasheet for the transmitter chip** you don't know what its limits are, or even what the optimum impedance is.


If one of those ports is an antenna port and is not *normally* occupied by an antenna connector, then it must be the case that you will be connecting your antenna in parallel with the built-in antenna. Connecting two antennas in parallel reduces their impedance (see previous point) and combines their radiation pattern (which is probably not significant if your new antenna is substantially better, but is still worth noting).

## Answer (score 2, by Edwin van Mierlo)

I would not do this, unless you are prepared to damage your phone.

There are multiple antennas in a mobile device, examples could be 850 MHz, 1700 MHz, 2100 MHz, 2600 MHz for GSM/3G/4G/LTE.

Some of those antenna's may be dual-or-multi-band, or MIMO — or other technologies. Simply "connecting an antenna" to an unknown port on a board, may result in damaging the circuit. Besides that, the ports you are mentioning may be there for diagnostics for the manufacturing process of the board/circuit.

Some antennas would be for WiFi and GPS as well.

I would not modify your mobile device, unless you have intimate knowledge of the circuitry.

What you could do is look into a small 12V/battery-powered 3G booster. There are various shops which would sell them; however you will have to carry the booster, the battery, the donor antenna, and the distribution antenna with you on your journey.

I have a booster from http://www.myamplifiers.com, for base install, and it did work for me. But as that is a home install it is a different piece of equipment. There are amplifiers made for mobile installations which run on a 12V supply, but I have no further experience with those.

Furthermore, in some countries/areas the use of a booster is illegal; you may want to look into this.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6136/would-retrofitting-an-external-antenna-to-a-smartphone-be-feasible, by Kavi Siegel, Kevin Reid AG6YO, Edwin van Mierlo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
