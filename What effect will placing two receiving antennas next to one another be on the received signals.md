# What effect will placing two receiving antennas next to one another be on the received signals

*Tags: receiver, wifi · score 4*

## Question

I'm planning on using 2 receivers that operate on the same frequency. So there's no confusion I'm talking about WiFi signals (but I'm trying to do some cool amateur radio stuff with it!) so the frequency is 2.4GHz. One of the main things I'm working on is building a nice big antenna (high gain) to be able to have a usable signal over more than 10s of meters. Now ideally, since these two receivers will have the same frequency, I could place both receivers at the focal point of the antenna and have the one dish with 2 receivers - but I'm worried that there will be a loss of signal since the antennas are blocking each other to some extent. Is this the case? I'm looking for an experienced person to give me there best guess really!

## Answer (score 2, by KD8EVL)

As your comment mentions, since you're *transmitting* also, you will have issues.

Placing two antennas within ~1/2 wavelength of each other will cause them to inductively couple - effectively connecting themselves to each other. This results in detuning both antennas, as well as the high power Tx RF getting routed back down the other antenna, possibly damaging the receiver. I did this once with 2m mobile rigs - I had my HT connected to a magmount placed too close to the antenna for my 50w mobile, resulting in a fried protection diode in the HT.

As others have asked, what is your goal in having two receivers? If you're trying to run two different networks, why not just overlay a virtual SSID on the same AP?

73 de KD8EVL

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1183/what-effect-will-placing-two-receiving-antennas-next-to-one-another-be-on-the-, by FraserOfSmeg, KD8EVL. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
