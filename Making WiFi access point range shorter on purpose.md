# Making WiFi access point range shorter on purpose

*Tags: antenna-construction, wifi · score 3*

## Question

Not sure if this is the right place to ask, but I'm trying to build a system of multiple WiFi access points that are spread out across a store.

Since every smartphone and WiFi enabled device regularly sends out a "discovery"-packet to check if hotspots are around, I'm trying to keep track of that and see where people go inside that store, to have statistics on how many people that look at the display window actually go inside and to the checkout and similar things.

Now my problem is that the WiFi signal of my access points goes way too far and every smartphone gets detected on all hotspots.

How would one go about shortening the distance of a WiFi signal?

## Answer (score 3, by Glenn W9IQ)

For a device to register with the access point, it must receive a transmit signal from the access point (AP). This largely consists of the AP transmitting its SSID so that it can be detected by the client device. If the client does not see the SSID, it often cannot detect the AP unless it is in active use by another client. The goal is therefore to effectively reduce the detectable range of the SSID.

One method of shortening the range is to reduce the transmit power of the AP. Many APs have a configuration menu setting that allows you to reduce the transmit power. You may wish to experiment with various settings to see what works for your situation.

Another option is to deliberately degrade the antenna performance by shortening it. This would largely be experimental and non-reversible but simply clipping the antenna shorter with a stout wire cutters will have this effect. If the AP has more than one antenna, they must all be clipped or alternatively leave only one installed and clip that antenna. Continue to clip the antenna(s) shorter until the desired range is achieved.

A third option is to use an attenuator. These devices reduce both the transmitted and received signal level. They are available in various levels of attenuation denoted by dB ratings - the large the number, the more the attenuation. Start with a 20 dB attenuator for each antenna and experiment from there. You will need to find an attenuator that fits the connectors of your AP antennas and the AP itself. Sometimes some connector adapters are required.

A fourth option is to attempt to shape the pattern of the antenna. Consider putting the AP in a larger tin can (like a popcorn can) so that it's antennas is well contained in the depth of the can. This will largely restrict the effective range to an area that projects as a cone from the open end of the can.

Keep in mind that AP frequencies are in the microwave region and are very susceptible to bouncing off of objects to reach their destination. This may frustrate some of your efforts to reduce the range. You may need to combine some of the above options to reach your goal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10300/making-wifi-access-point-range-shorter-on-purpose, by Silverquark, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
