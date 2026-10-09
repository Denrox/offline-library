# Why do receiver sensitivities vary so much with frequency?

*Tags: receiver, frequency · score 5*

## Question

I was looking for a 2.4 GHz WiFi antenna to catch a weak free WiFi signal, and amplify it so I can use it. I found Ruckus Metroflex NG, which can receive signals down to -108 dBm. Which is amazingly weak; however, while searching for such an antenna, I couldn't help noticing that 900 MHz receivers, such as LoRaWAN have a sensitivity down to -136 dBm. This is literally weak enough that at 1W transmission power, you can catch the 900 MHz signals of anything you can see on earth -- even of the highest planes.

So I thought, OK, the lower the frequency, the longer the waves, and the easier to catch them. But apparently, that's not the case. GPS receivers, which operate at the intermediate frequency of 1.575 GHz, go down to a whopping -164 dBm acquisition sensitivity for the RXM-GNSS-TM-B (and even lower tracking sensitivity). So, what gives? Why is there such a huge discrepancy in the required strength of a signal before it's detected?

## Accepted answer (score 6, by Phil Frost - W8II)

Detecting a signal is not a question of amplifying the signal: the problem is distinguishing the signal from the noise.

Noise by nature is random: individual observations are unpredictable, but as more observations are made the average tends towards zero. By averaging more observations, the noise can be made arbitrarily close to zero.

Signals are not random. The presence of the signal introduces a predictable bias into the noise. As more observations are taken, these biases add. By sending the same *predictable* signal for longer, more observations can be taken, and that accumulated bias representing the signal can be made arbitrarily large.

So one way to make a signal easier to detect is to send bits at a lower rate. All else equal, this means more energy is put into transmitting each bit, and thus its easier to know if a bit should be a 0 or a 1. Consequently the minimum detectable signal power can be lower.

Thus there's a fundamental tradeoff between speed and sensitivity. WiFi can operate at multiple speeds, and the speed is negotiated dynamically to find the highest speed that's just barely detectable under the current conditions. Consequently you'll get higher speeds when the AP is only 3 meters away, and lower speeds when it's on the other side of a large building. At some point even the slowest WiFi speed (6,5000 kbit/s) is no longer detectable and communication fails entirely.

LoRaWAN is designed for low power and long range, and consequently it runs at a lower speed: 27 kbit/s. Being 240 times slower than even the slowest WiFi speed means it can be much more sensitive.

GPS is designed for even lower power and longer range. GPS is somewhat unique in that its primary purpose isn't communication. This means the bitrate can be extremely low: 0.050 kbit/s. Consequently GPS receivers can be extremely sensitive.

## Answer (score 2, by Brian K1LI)

We can drill down a bit further into the answer given by Phil Frost - W8II. The datasheet for the Ruckus Metroflex NG wireless router you cite quotes the receiver sensitivity vs. data rate:

We notice a logarithmic relationship between data rate and sensitivity: $$\mathsf{10log(\frac{2Mbps}{1Mbps})=3.0dB}$$ $$\mathsf{10log(\frac{5.5Mbps}{1Mbps})=7.4dB}$$ $$\mathsf{10log(\frac{11Mbps}{1Mbps})=10.4dB}$$

which track the sensitivity differences between the various data rates quoted by the specs.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13278/why-do-receiver-sensitivities-vary-so-much-with-frequency, by Alex, Phil Frost - W8II, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
