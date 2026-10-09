# Wifi passive repeater (antenna to antenna connection)

*Tags: antenna, repeater, wifi · score 8*

## Question

I have two buildings. Building A has wifi (2.4GHz) infrastructure, Building B doesn't. One side of building B can pick up the wifi signal from building A. I want to passively extend the signal through to the rest of building B, using two antennas and a short piece of coax.

Supposing I put a decent directional antenna (24dBi) in building B, pointing at a WAP in building A, then joined that to an omnidirectional antenna with a short (50cm) piece of coax. In this scenaria, for the omni antenna, would it be better to have a large (e.g. 12-15 dBi) antenna, or a small one (~7 dBi) (assuming the smaller one can still cover the range of the building)?

I am aware an active repeater would be better, but I'd like to get some thoughts on this scenario.

Background reading: https://web.archive.org/web/20141026222347/http://www.netscum.com:80/~clapp/wireless.html

## Answer (score 5, by Phil Frost - W8II)

Trying to extend coverage in this fashion isn't worth doing. Even with highly directional antennas, most of the power transmitted doesn't end up in the receiver. Thus, your "repeater", which is really two antennas joined by coax, has very little power available to transmit.

We can do some math.

Let's assume that your buildings are 40m apart, and your transmit power is 20 dBm (the legal maximum on 2.4 GHz in the US). Let's further assume that you have 24 dBi antennas on the Wi-Fi AP and your repeater. We can use the [Friis transmission equation](What%20does%20the%20Friis%20transmission%20equation%20represent%20and%20how%20is%20it%20derived.md) to calculate how much of that power is received by the repeater:

$$ 20 \:\mathrm{dBm}\ + 24 \:\mathrm{dBi} \ + 24 \:\mathrm{dBi} \ + 147.6 \ - 20 \log_{10}(40\:\mathrm m \cdot 2.4 \:\mathrm{GHz}) \ = -4 \:\mathrm{dBm} $$

So, assuming no losses in your repeater, it makes the 20 dBm transmitter look like a -4 dBm transmitter. Or put another way, the repeater introduces 24 dB of loss. By reciprocity, this loss works in the other direction as well: how ever much power is received by the repeater from the clients, the AP will see it as 24 dB less.

Besides that loss, which is substantial but maybe not impossible, you have a new problem. While the AP might hear the nodes in the external building, other nodes won't. This is called the hidden node problem, and will result in transmit collisions which seriously degrade the performance of your network.

To solve your problem, best is to run Ethernet to the building, and install an AP. If Ethernet is not possible, then use a cross-band Wi-Fi repeater. They are available for $100 at any big-box electronics store, where they are usually called a "range extender". You are going to spend at least that on antennas and coax for your passive repeater solution, which will not work as well.

Regarding which omni-directional antenna is better, it's impossible to say, generally. An isotropic antenna has exactly 0 dBi gain, by definition. However, such an isotropic antenna can not be physically realized, the closest we can come is a dipole, which is 2.15 dBi in free space. Of course, the presence of the Earth or anything else conductive around the antenna changes that.

In any case, any antenna with higher gain works by being more directional. Remember that the antenna's radiation is a three-dimensional function. An "omnidirectional" antenna radiates equally in all directions in one dimension (typically, azimuth), but this says nothing about how it radiates at different angles of elevation. Thus, an antenna that is still "omnidirectional" but quotes a higher gain is either:

1. an outright lie by Chineese marketing departments, or
2. radiating more horizontally, and less up or down.

Depending on the orientation of your antenna, and the location of your radios, this could be good or bad. What you want to do is minimize radiation in directions where you don't want coverage, which will in turn maximize radiation in directions where you do want coverage. Which antenna achieves that depends on your particular environment.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2146/wifi-passive-repeater-antenna-to-antenna-connection, by askvictor, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
