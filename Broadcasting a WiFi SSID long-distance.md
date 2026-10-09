# Broadcasting a WiFi SSID long-distance

*Tags: antenna, equipment, transmission, wifi · score 7*

## Question

Which equipment would be good for broadcasting a WiFi SSID the longest possible range? We're making an orienteering race in a forest and would place a sender somewhere high over the trees, transmitting a WiFi signal into the forest. The SSID should be picked up by the participants with a regular smartphone, but no actual communication is needed. The message will be written in the SSID itself.

Can someone guide me to which antenna or equipment would be most applicable and give the longest range possible? We don't expect omni-directional functionality, but could perhaps purchase several of the same antennae to widen the transmit angle.

## Answer (score 7, by Kevin Reid AG6YO)

Assuming you are in the US (sorry if I'm wrong, but you didn't specify!), normal WiFi falls under Part 15 regulations which [limit the radiated field strength, not the transmit power](What%20are%20the%20%28US%29%20rules%20about%20unlicensed%20low-power%20transmissions.md). This means that, assuming the transmitter is not underpowered, you cannot legally increase the range using directional antennas.

Supposing you did so anyway, hooking up multiple directional antennas to the same transmitter will split the input power among those antennas, so you're back to where you started.

Here are your available legal options:


Make sure the WiFi AP you use actually transmits the maximum legal power and has an antenna with a suitable pattern. (In particular, a so-called “high-gain omnidirectional” antenna will radiate mostly in the horizontal plane and less in the "up/down" directions, which might be good for the range or bad if your terrain is not flat or the antenna isn't oriented properly.)


Use multiple APs arranged in a large circle. This only extends your range by the radius of the circle. (Multiple APs in the same location would increase the total power radiated but not in a way useful for communication since they're not coordinated.)


Obtain an amateur radio license, which will allow you to transmit more power. The 2.4 GHz ISM band used by WiFi overlaps with an amateur radio band, so you can use stock WiFi equipment together with directional antennas and/or power amplifiers, provided that you:

 - include your assigned callsign in the SSID
 - configure the device to use a channel which is in the amateur band, rather than autoselecting

I haven't done this myself, so I can't advise on the exact details of doing this, but it's fairly popular so you should be able to find information easily.

This **does not** require the other participants to obtain a license.

## Answer (score 2, by Prasanna)

So...A couple of things here:

1.

According to FCC regulations, a fixed point-to-point link can actually broadcast well above the 30 dbm rule. In fact, you can go up to 52 dbm EIRP.

2.

In order to get that high, you will need to regulate the output power of your router. You can do this digitally in the router settings or by putting in-line attenuation at the output of the transmitter. You can buy them from Mini-Circuits online.

3.

A high power antenna increases the range by concentrating the power into a narrow beam which covers a smaller area, which is measured in dbi (decibels-isotropic). You can buy them here.

4.

The only tricky part is that you may have to buy antenna adapters in order to connect the output of your router to the antenna itself. The output of the router is typically reverse polarity, so you will have to check that.

5.

If you set up a point-to-point link, your devices can receive the SSID without connecting, so you can still tx at a higher power level.

Hope this helps!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3834/broadcasting-a-wifi-ssid-long-distance, by sune, Kevin Reid AG6YO, Prasanna. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
