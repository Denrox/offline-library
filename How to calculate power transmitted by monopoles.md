# How to calculate power transmitted by monopoles?

*Tags: receiver, dipole, transmitter · score 5*

## Question

I only studied monopole in sending mode or receiving mode alone but never in both modes together, I have this question which says:

Two vertical λ/4 monopoles are parallel to each other with 20 meters separation between them at 5 GHz. The first monopole is used as a transmitting antenna, while the second one is used as a receiving antenna to receive power from the first one. The transmitting monopole is connected to a 50 ohms lossless transmissions line. The input power to the transmission line of the transmitting monopole is 200 watts. What is the power received by the receiving monopole?

I tried to solve it as follows:

1. I know that quarter-wavelength monopole has impedance = 36.5 ohms so I calculated the reflection efficiency to be = 0.975
2. since no polarization efficiency is given and the line is lossless I assumed the total efficiency = 0.975
3. So the total power transmitted = $0.975\cdot 200 = 195 \,\text{watt}$
4. I found a law on the web called Friis transmission equation $$P_r = P_t\cdot G_1\cdot G_2 \cdot\left(\frac{\lambda}{(4\pi R)}\right)^2$$ and I already know that Directivity = 3.2 so $$ Pr = 195\cdot 3.2\cdot 3.2\cdot 0.975\cdot (0.06/(4\pi 20))^2 = 1\cdot 10^{-4} $$ which I think is too low power. What did I do wrong or how to use this law?

## Accepted answer (score 8, by Marcus Müller)

10⁻⁴  
which I think is too low power.

Why? Gut feeling says that is actually pretty good a transmission for such a distance.

Notice how your free space path loss is

$$\left(\frac{\lambda}{R}\right)^2\cdot\frac1{16\pi^2}\approx \left(\frac{\lambda}{R}\right)^2 \cdot \frac1{160}$$

and $\frac\lambda R=3\cdot10^{-3}, \left(\frac\lambda R\right)^2=9\cdot10^{-6}$, so it sounds pretty OK that only a tiny fraction of power reaches the receiver.

10⁻⁴ W is still -10 dBm. That's "screaming loud" in terms of received radio power. GSM phones work at -110 dBm. That's ten billion times less power.

To compare this to a different system running at around 5 GHz: IEEE802.11ac (modern Wifi), using a 80 MHz channel, can run at full 433 Mb/s (without even using MIMO) when received signal power is -50 dBm.

Also, the order of magnitude of the free space path loss coefficient highlights a different aspect: It really doesn't matter whether your antenna is perfectly matched. A couple centimeters in distance make up for your 97% efficiency. (also, strictly speaking, the quarter-wavelenght monopole doesn't have a 36Ω impedance, it has (36+j21)Ω or so impedance. Again, this doesn't matter in reality as much as people tend to think.)

## Answer (score 2, by tomnexus)

Your calculation looks all correct.

A quick conceptual way to check it is this:

- picture a 200 watt light bulb
- 20 metres away, work out how much light falls on an area of about ${\lambda\over{2}}$ by $ {\lambda\over{2}} $

This is the power received by the second antenna. The area of a 20 metre sphere is 5000 $m^2$ and the capture area is ${1\over1600} m^2$ so you can see the large ratio right there.

There is no polarisation loss, as you say, but I would call it mismatch loss, not efficiency. Although the net effect is the same, efficiency implies a loss of power in the antenna, while mismatch between 37 and 50 Ohms results in some power being reflected back to the source instead of being radiated.

The question doesn't say what the receiver impedance is, it's reasonable to assume 50 Ohms. Then you can calculate the mismatch loss on receive, which is the same as on transmit.

One last interesting point - the gain of the monopole is only 3, or 5 dBi, *when you are above the same infinite conducting ground.* So for this example to work, there would have to be a continuous sheet of metal, not just 20 metres long, but perhaps 40 x 40 metres, with the monopoles mounted in it. No problem for an example, but unlikely in practice. Perhaps this could happen on the top of an aircraft or a ship.  
The antenna described as "monopole_with_limited_ground" like you might make with a piece of wire and a tin can has a gain of more like 1.0 or 0 dBi, on the horizon, when considered as a whole, so the figures would be a bit different.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16791/how-to-calculate-power-transmitted-by-monopoles, by Marcus Müller, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
