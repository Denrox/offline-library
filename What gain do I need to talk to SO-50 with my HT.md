# What gain do I need to talk to SO-50 with my HT?

*Tags: antenna, ht, satellites · score 8*

## Question

My HT has 5 W of power, a sensitivity of about 0.2 µV, and I would like to talk to the SO-50 with it. How much gain do I need in my antenna to make this work?

## Accepted answer (score 11, by PearsonArtPhoto)

The specifications from AMSAT for the SO-50 are:

The repeater consists of a miniature VHF receiver with sensitivity of -124dBm, having an IF bandwidth of 15 KHz. The receive antenna is a 1/4 wave vertical mounted in the top corner of the spacecraft. The receive audio is filtered and conditioned then gated in the control electronics prior to feeding it to the 250mW UHF transmitter. The downlink antenna is a 1/4 wave mounted in the bottom corner of the spacecraft and canted at 45 degrees inward.

So, what does all of that mean? First of all, the 5W signal you send has to make it to the spacecraft and be received. Let's just assume a uniform gain from the spacecraft to start with. Let's also start with a uniform gain from the HT. The satellite footprint is about 3000 miles, so let's just say the maximum distance to the satellite is 2500 km, accounting for height and the radial distance. It should be close enough to get an idea. That means the one way path loss is about 128 dB. That means your signal would need to be at least 100W to be received, given no gain, as can be calculated by $$10\times{}\frac{10^{128-124}}{1000}$$ Bottom line, you need a gain of at least 12dB to make the satellite, and a bit more margin would be helpful.

As far as the receiving, that's where things are a bit trickier. The power can be found by $\frac{V^{2}}{R}$, and also converting the $V$ from peak to RMS. $R$ is usually 50 ohms. When you take all of that in to account, the specified minimum detection for the signal is $$-124 \log_{10}\left(\frac{\left(\frac{0.2\mathrm{e}-6}{\sqrt{2}}\right)^2}{50} \times 1000\right) \times 10$$ (Basically, find power $\frac{V^2}{R}$, convert to mW, and convert to dBm). The satellite signal is only 250mW, and you're looking at the same path loss of the signal. The gain required is $10 \times \log_{10}\left(\frac{10^{128-124} \times 10}{250 \mathrm{mW}}\right)$, or about 26 dB. This is quite difficult to achieve, and usually requires a pre-amp to be effective, or a really good antenna.

Bottom line- Tx is 12dB, Rx is 26 dB, at max distance, and less for an overhead pass.

## Answer (score 2, by KC0ZMX)

I've personally worked SO-50 with a 5W HT using an Arrow antenna (http://www.arrowantennas.com/arrowii/146-437.html).

I don't actually know what the gain would be with that antenna, but with 5W and an antenna like that, you can work SO-50!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/316/what-gain-do-i-need-to-talk-to-so-50-with-my-ht, by PearsonArtPhoto, KC0ZMX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
