# Connecting Directional Antenna To Two Antenna Ports on NIC

*Tags: antenna, antenna-theory, wifi, microwave · score 3*

## Question

I want my n/ac Wi-Fi card to operate in a spatially directional manner. To achieve that I want to use a directional antenna(s). There is a slight complication though, because my Alfa AWUS036ACH network card has two omni-directional antennas.

Because of that, I'm confused on how I should connect a directional antenna to such a setup. I can imagine a few options, but I don't have the experience to judge what would give me the optimal gain in dBm.

I can see the following options:

1.

**Connecting two directional antennas and pointing them in one direction**. The problem here is that the antenna connectors are very close to each other and two directional antenna would not fit that close together. So, I would have to extend connector using cables and build some frame to hold the antennas. A lot of work, and cables incure signal loss.

2.

**Disconnecting one omni and connecting one directional**. Problem here is that I don't know if the NIC can work using one antenna.

3.

**Connecting multipatch antenna** -- quite expensive, but if that is the only option then I have to go with that.

Or maybe some other option?

## Answer (score 2, by Phil Frost - W8II)

Wireless NICs and APs have multiple antennas for MIMO. This means the device dynamically determines the coefficients for each antenna to combine them in the best way.

Often that means phasing the antennas to make an array with greater gain towards the other station and/or less gain towards interference sources. This is called *beamforming*. So your NIC is already "spatially directional" in a way. A device with more antennas could be even more directional.

Additionally, the device can find two sets of orthogonal coefficients and use this to double the data rate. This is called *spatial multiplexing*.

One solution to your issues may be to simply upgrade the NIC. Higher end devices may have 4 or even more antennas, and with more antennas in the array comes the potential for a more directional array. NICs are cheap enough this may be cheaper than buying antennas.

Alternately, attaching two directional antennas would work well. This allows the NIC to still gains the benefits of MIMO, while adding gain in the direction where you need it the most. Unless the cables are going to be very long, it's likely the cable loss will be more than offset by the additional gain.

Even if you attach just one directional antenna and leave the other omnidirectional antenna attached, the NIC will likely weight the directional antenna more heavily. Though this does mean you are less likely to get the higher data rates associated with spatial multiplexing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16428/connecting-directional-antenna-to-two-antenna-ports-on-nic, by Trismegistos, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
