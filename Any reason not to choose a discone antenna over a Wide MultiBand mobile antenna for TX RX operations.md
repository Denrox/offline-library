# Any reason not to choose a discone antenna over a Wide/ MultiBand mobile antenna for TX/RX operations

*Tags: antenna, antenna-theory, vhf, uhf, antenna-system · score 6*

## Question

We are setting up a all-band radio in an emergency com center that's intended most for amateur band use, but since its' for emergency use will also be used in the public safety bands; (150-170)MHz, (470-512)MHz, (700/800)MHz, and possibly others if needed. We have a small tower to mount the antenna to. The person in charge of the project wanted to use a PCTEL PCTWSLMR Multiband mobile antenna, since its commonly used in the local police vehicles that are outfitted with this radio. I'm against using a mobile antenna on a tower, so researching I found TELEWAVE ANT280S Discone antenna. I was told that we shouldn't use a Discone for transmit because of poor performance, but I'm not sure why. The mobile antenna lists gain as unity and VSWR as 2:1 typical and 2.5:1 max. The specs for the discone are unity gain with a maximum VSWR or 1.5:1 accross 132 Mhz - 3 GHz. So I don't understand why the discone would be considered inferior to the mobile antenna in this case. I know that common wisdom is that a discone is for scanner type applications, but it seems that in this case that it would out perform the "out of the box" solution, which in this case is the Multiband mobile antenna.

So, is there anything I'm overlooking here as to why I shouldn't just use the discone for TX/RX applications? Thanks

## Accepted answer (score 1, by Brian K1LI)

A discone would appear to be an excellent choice for this application, provided it can be mounted away from conductive structures that would distort the radiation pattern. NEC-2 modeling confirms that the discone should deliver gain comparable to a dipole, but omnidirectional in the azimuth like a vertical, giving it superior performance to the unity-gain vertical.

The TELEWAVE ANT280S datasheet specifies the vertical beamwidth as 110$^o$. With vertical and horizontal beamwidths $\theta$ and $\beta$ specified in degrees and gain in dBi, Teletopix shows how to calculate beamwidth as a function of gain: $$G \approx 10 log \frac{32400}{\theta \beta}$$ Since an omnidirectional antenna has an azimuthal beamwidth of 360$^o$, the TELEWAVE ANT280S' 2.1-dBi gain translates to a vertical beamwidth of about 55$^o$, half the quoted value. It would be interesting to know why the manufacturer specifies the beamwidth as they do.

## Answer (score 5, by rclocher3)

The discone antenna that you mention cites "effective" gain of 0 dBd. I don't know what they mean by effective gain, but dBd means decibels compared to a dipole; 0 dBd would mean that the discone has the same gain as a dipole. That's OK gain, but certainly not great. Lots of other antennas would give you a few more decibels for not very much money.

I looked at the price of the TELEWAVE ANT280S, and the cheapest price I could find was $1,700. Wow! That's an expensive antenna! I'd think that you could buy very nice rugged base station antennas for the three bands you mention, and diplexers as needed, for a lot less than the cost of that discone. (Diplexers are used to connect two antennas to one radio, or two radios to one antenna. Triplexers, quadruplexers, etc. are also available.)

In my opinion, that's what you should do. You'd save money, and get more gain. The additional expense of the discone would only be justified, in my mind, if you had a definite need for the broad frequency coverage that is its main selling point.

A mobile antenna on a tower is a bad idea. A mobile antenna depends on a ground plane, like the roof of a car. You could jury-rig elevated radials to a mobile antenna to replace the ground plane, but why? A good base station antenna is far more rugged, is designed to be mounted on a tower, and needs no ground plane.

## Answer (score 2)

Discone antennas have a very wide bandwidth. Many HAMs like them for this reason for receiving. You can have one antenna and use it for 440, 200 and 2 meter. Some will also do 6 meter. You can also use them with non HAM frequencies like Weather, marine, and aircraft.

The downside is that for transmitting they have 0 gain at best and often have a slight negative gain. There are many far simpler antennas that easily out preform them for transmitting. Some HAMs will say they cannot be used for transmitting. For most discone antennas that is not true, You can transit using them, just not very well.

Personnal I'd prefer something like a J pole for omnidirectional or a simple Yagi if I want gain in one direction such as trying to reach a distant repeater.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16715/any-reason-not-to-choose-a-discone-antenna-over-a-wide-multiband-mobile-antenn, by Frank, Brian K1LI, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
