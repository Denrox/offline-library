# Bridging LAN over ~1-2km distance

*Tags: antenna, digital-modes, diy, repeater · score 4*

## Question

A friend of mine and I live across a lake from each other, and recently we thought it'd be fun to try and connect our computers together somehow across that distance. Running cable from either side is expensive, difficult (no boat), and probably illegal (or is regulated in some boring way), so we thought radio would be a good approach to the problem. We're aware that there are people selling products that solve this problem, we'd like to do as much of it ourselves as possible. While we might be fairly technical when it comes to computers, radio stuff is certainly not our strongsuit. Thus, we've decided to use this as a project to learn more about the subject.

Our goal is to somehow connect our LANs together via radio, as though there was an ethernet cable connecting our switches. If possible, It'd also be neat to be able to expand the system so that we could relay from his place to, say the beach we go to that I can't see from my house, and maybe from that bridge somewhere further up the lake. Our houses are in direct visual contact with each other, and my limited knowledge of radio suggests that we might try some sort of a directional antenna. Other than that, I have no idea how to approach this project.

While a solid and detailed set of instructions would be lovely, we'd much more prefer an answer that contained resources we could check out to learn more about what we're doing, what solutions to our problem are available, and how we might implement them ourselves. Learning is the primary goal of this project, after all!

## Accepted answer (score 4, by AndrejaKo)

My advice here is to avoid the amateur radio service completely and instead go with license-free spectrum, perhaps around 2.4 GHz or 5 GHz. There are more than enough WiFi products that can solve your problems.

My advice for research directions would be to look for let's say parabolic antenna for your band of interest:  
  
plus an access point. For access point, my advice would be to look to one of the third-party GNU/Linux distributions for routers and similar equipment. Fro example OpenWRT. Then look for the devices on their supported list and find one you like. OpenWRT and the like will give you more than enough options to fine-tune the WiFi settings you have and will also be able to improve security in the long run. since they actually receive updates, unlike stock firmwares for cheap units. The down-side of this approach is that if you want modern features such as antenna diversity and spatial multiplexing, you'll need two to four antennas per AP, which can get costly. A ballpark price for an antenna could be around USD 50 plus maybe USD 50 to USD 100 for an AP, plus low-loss coaxial cabling and installation costs. Keep in mind that the traditional distance between antennas i simpler diversity or multiplexing setups should be half of wavelength or odd multiple of it.

Or maybe a combination unit that has both WiFi card and an integrated outdoor directional antenna with sufficient gain could be interesting:

Such units will usually have wired Ethernet connection on them and can be powered over Ethernet using standardized PoE or their own proprietary power injectors. They can have several integrated antennas (pictured unit has two), meaning that they can take advantage of antenna diversity or spatial multiplexing in one unit, but it will be a somewhat compromise solution, since quite often, there's very little that can be done to have many uncorrelated antennas in small space. Price could be a bit higher than an access point plus one antenna, but will in general be lower than access point plus two good antennas. The pictured unit goes for around 115€, just to give you a reference point. Also with this type of solutions, you usually completely avoid the coaxial cable loss between the radio and the antenna, since the unit is fed by classical Ethernet.

Next, there's the part where you should calculate how much gain you actually need. You'll often be able to find tables with minimum signal strength needed for various modulation types from WiFi equipment manufacturers in tables such as one on this page.

You should use that information to give yourself a base-line of how much power you need at the receiver.

Next step is to take the antenna gain in dBi and subtract the cable loss in dB from it and then repeat the calculation for the receiver. This will give you a sort of let me call it "effective" antenna gain, that you can later on use for different types of calculators. Cable loss is calculated by getting the manufacturer's specification that will list it usually in loss per meter, per foot or per 100 feet/30 meters or per 100 meters and then add the loss of the connectors, if you want to be really picky.

After that, you can go to a Friis calculator such as this one and use it to calculate the path loss for your distance and put the info from your equipment such as the gains you calculated previously and the transmitter power. The output will be received power, which needs to be higher than the minimum power needed for the speed you want to use, plus some more decibels for extra safety margin, just in case of bad weather or similar. If the numbers don't fit, you can try to do trade-offs. You could switch to a higher-gain antenna, but that would be more expensive, you could move to a lower-loss cable, you could try to use a higher-power transmitter, but that can very easily be illegal if you break the local rules and so on.

Finally, there's the part where you should decide which band you want to use. If you want to use regular WiFi bands (meaning cheap equipment), you should do a "site survey" of some sort. Basically, you need to see which channels are free in the area. In general, 2.4 GHz is the band with larger antennas, cheaper APs and is more crowded. The path loss is lower in this band.  
In 5 GHz band, the antennas are smaller, there are more channels and usually much less users (this is VERY important for a good-working link). Also the newest IEEE 802.11 ac standard only works in this band. You'll also have more space for use of wider bandwidth transmissions. The path loss here is usually higher, so you can expect your signal to be around 6-7 dB weaker than in 2.4 GHz band. Equipment is also somewhat more expensive.

With latest AC equipment, you can expect a bit less than 1 gigabit per second speeds with a good WiFi installation, but that can somewhat deteriorate with weather.

Finally, let me remind you to check local regulations on WiFi equipment. In some cases, you might have restrictions on antenna types, antenna gains, EIRP, outdoor installations, so that even though WiFi is in general considered license-free, the your specific application might need registration or license or might be (in the worst case) simply illegal.

## Answer (score 3, by Kevin Reid AG6YO)

This answer hasn't got very many links, but I hope it has a lot of useful keywords for further research.

#### Technical

People often want to do this and are disappointed that it's not practical. The good news is that because you have a clear line of sight, you have many options. (The absence of obstacles is *far* more important than the distance.)

The typical solution to your problem could be called a *point-to-point microwave link*. The equipment consists of a transceiver and dish antenna at each end. You will need to find mounting points for the antennas which are well clear of any trees blocking the direct view, and aim them precisely at each other.

The “microwave” part of the name just means that it's using frequencies in the 300 MHz - 3 GHz range, much higher than classic broadcast and two-way radio, which is relevant because it allows high bandwidth and small antennas, at the price of the equipment being much more tricky to design and build.

#### Legal

What you are asking for may in fact *not* be “Amateur Radio” in the sense of this site's title. The reason for this is that Amateur Radio is a legally defined subset of radio operations: licensed 'amateurs' have permission to freely use a substantial amount of radio spectrum *under certain conditions*. Those conditions restrict the content of messages sent, in ways which are incompatible with carrying Internet traffic; most notably, *encryption* is prohibited. (I'm most familiar with the U.S. (FCC) regulations but my understanding is that similar rules apply worldwide, via the ITU.)

Therefore, you have two options:


You can create a network which uses IP, Ethernet, etc. but which is *separate* from the Internet. On most modern operating systems, just hooking up a separate Ethernet adapter (via USB, PCI, etc.) to each computer is sufficient to make this work as you want it to. You would then need to avoid using any software which encrypts its traffic to talk to your friend('s computer) — for example you could use HTTP (web browsers and servers) but not HTTPS. (I could comment on how to think about security given this constraint, but that would be a whole other question-and-answer.)


You can obtain a license for your particular link. However, this can be expensive, as it is intended for serious commercial use — a little research suggests that the total costs might be in the area of \$1000 - \$3000 in the U.S., for a 10-year license.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6019/bridging-lan-over-1-2km-distance, by haze, AndrejaKo, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
