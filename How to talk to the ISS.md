# How to talk to the ISS

*Tags: satellites · score 7*

## Question

I have a UHF/VHF transceiver capable of transmitting on UHF and receiving on VHF or vice versa on channel mode.

I finally got a directional Yagi antenna so reception/transmission shouldn't be a problem.

I live in Colorado, USA.

Which frequencies should I use to listen to it, and eventually transmit?

What other frequencies should I program in for the doppler shift? (I will be switching between channels)

## Answer (score 7, by user)

According to the ISS Fan Club's Frequencies page, for FM voice transmissions the downlink (your listening) frequency is 145.800 MHz and the uplink (your transmission) frequency is 144.490 MHz, when covering ITU regions 2 and 3, including North America.

In ITU region 1 the corresponding frequencies are downlink 145.800 MHz and uplink 145.200 MHz.

There are other frequencies listed as well, but these would appear to be the ones that you would be most likely to use.

Since the ISS is in a low orbit, Doppler shift will be relatively significant. Software designed to calculate such things will likely be useful, but for a starting point you may want to consider the table included in the Yaesu FT-897D manual, page 68, for the frequencies involved in operating over the UO-14 satellite, which itself listens on two meters and retransmits on 70 cm:

$$ \begin{array}{ c r r l } \text{Channel #} & \text{Receive Frequency} & \text{Transmit Frequency} & \text{Notes} \\ 1 & 435.080\text{ MHz} & 145.9700\text{ MHz} & \text{Acquisition of signal (beginning of pass)} \\ 2 & 435.075\text{ MHz} & 145.9725\text{ MHz} & \\ 3 & 435.070\text{ MHz} & 145.9750\text{ MHz} & \text{Mid pass} \\ 4 & 435.065\text{ MHz} & 145.9775\text{ MHz} & \\ 5 & 435.060\text{ MHz} & 145.9800\text{ MHz} & \text{Loss of signal (end of pass)} \end{array} $$

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/741/how-to-talk-to-the-iss, by Skyler 440, user. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
