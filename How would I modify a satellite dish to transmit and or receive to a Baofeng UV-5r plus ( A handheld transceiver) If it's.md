# How would I modify a satellite dish to transmit and/or receive to a Baofeng UV-5r plus? ( A handheld transceiver) If it's possible

*Tags: ht, antenna-construction · score 9*

## Question

I have an old satellite dish just lying around and was wondering how to hook it up to my baofeng uv-5r plus.

## Answer (score 13, by Paul)

Maybe.... A big project and probably not practical starting out. Would make a conversation piece or odd recycling project. How are you going to point it? Smaller antennas may work just as well.

A modern "Dish TV" or "DIREC TV" (R) that is about a foot across is practically useless for amateur radio transmitting and receiving.

Below is a stock picture (Wikimedia) of an old 1980s style home satellite tv dish, about 8 to 15 feet across. That's what you want to play with, if you have the time, energy, and patience.

These were popular in the early 1980s to receive pay TV channels like HBO direct from the satellite, unencrypted, without paying. Once these channels were encrypted and consumers were asked to pay, the huge dishes started disappearing from homes and into the landfills.

Now the Baofeng uv-5r is a 144 Mhz / 440 Mhz handheld radio with 5W output. This kind of handheld radio is suitable for use with local repeaters. With more gain you can get into repeaters a little further away. You **might** be able to hear the SO-50 satellite with a gain antenna, but this depends on the noise figure of the Baofeng and I'm a bit skeptical. A Yaesu VX-8R can sometimes do it.

However, you don't necessarily need a 10 foot dish for this. You might hear the satellite with something handheld, like this portable yagi made by Arrow Antennas from aluminum arrow shafts

A more practical choice for adding range is a 2m/440 vertical or a 2m/440 yagi. To hook these to your radio you would need an adapter cable to go from the PL259 or N connector on the coax from the external antenna down to the radio connector. Don't use a straight through adapter as torque from the large coax and connector can tear the SMA antenna jack from the PC board inside the Baofeng.

So back to the topic of dishes.

Here are some examples of dish recycling by Hams:

- Converted to 1296 Mhz antenna, looks like a small helix is feeding it
- VE2AZ converted a TVRO dish to 1296 Mhz for Moonbounce

So let me tell you why the dish is not such a great choice for 144 Mhz or 440 Mhz, but how you might be able to turn it into something interesting.

A dish is a good choice for high gain at microwave frequencies (several Ghz = several 1000 Mhz, wave length is a few inches or centimeters). It is worth noting that Internet Wifi is around 2400 Mhz and there is an overlapping ham radio band.... so an old large TV dish might make a great wifi antenna. It works by focusing the signal onto a feed point. At these frequencies the radio waves act more like light and the curved dish surface reflects a chunk of the radio waves the diameter of the dish from the target to arrive in phase and combine at the much smaller feed point suspended above the dish. The principal is the same in a reflector telescope, with the dish and the bottom mirror the reflectors. These work in part because the dish/reflector surface is large compared to the wavelength of the signal.

But at VHF frequencies a wavelength of the radio signal is 2m or around 6 feet. A dish is little more effective than a simple single element reflector in a yagi or quad.

At UHF frequencies the dish still has some gain. But not a lot.

Many of these dishes were steel, so you could find a magnet mount 2m/440 antenna (like for an automobile), attach it to the dish and call yourself "done". I can't imagine a good reason for doing this.

A large dish could also be used on 440 Mhz either by modifying the feed or turning it into a helix antenna. It might be usable on 144 Mhz by turning it into a helix antenna.

Modifying the feed is described in some of the old ARRL Antenna Handbook articles. I seem to recall one suggested feed for a dish is a dipole or set of crossed dipoles. The dipole or dipoles run parallel to the dish surface at some height above on the feedpoint axis. If you want to try to use it for 440 Mhz you would make a 1/2 wave dipole wire antenna and attach it to the center support above the dish, near the old feedpoint. It might be best to remove the old feedpoint and arm entirely and replace it with something non conductive that can allow moving the dipole up and down. You would need to adjust the height of the feed above the dish for best signal strength before determining where to make a permanent attachment.

You would also need to check the SWR if you want to use it for transmitting.

A bit more challenging is to create a 2m helix based on the satellite dish, with the dish as the rear reflector. This involves supporting a helix of wire above the dish, and admittedly it is a project. Each loop of the helix is about a wavelength worth of wire and the travel is a little less than a 1/4 wavelength per round trip around the helix. See Helical Antenna Theory or Wikipedia Helical Antenna.

I've made a 70cm helix antenna suitable for receiving low earth orbit ham radio satellites from bamboo and a Wal Mart Pizza Pan as the reflector.

Transmitting to the satellite is done on 2m with a more traditional antenna.

But with a large dish, and a way to point it, it becomes possible to make a 2m helix antenna, or perhaps make a dual band helix by making the spirals concentric.

While a conversation piece, helix antennas do not have more gain than yagis or quads that you can build or buy in the ham radio marketplace.

## Answer (score 2, by N8HU)

You can turn a small dish antenna into a 2m, 1 1/4m, and 70cm antenna by cutting 3 slots into it. The dish really has room to cover all 3 bands with a coax attached in the appropriate locations for each band. This has nothing to do with the current feed horn. In fact you can cut a slot antenna into any piece of sheet metal that is large enough for your desired freq. FYI, a horizontal slot antenna has vertical polarization.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/526/how-would-i-modify-a-satellite-dish-to-transmit-and-or-receive-to-a-baofeng-uv, by Sudo_Cats, Paul, N8HU. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
