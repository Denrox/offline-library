# Is there an 802.11 Wi-Fi module that allows direct access to the PHY layer

*Tags: wifi · score 3*

## Question

I am looking for an RF chip that offers a set of bit-rates similar to the PHY bit-rates used in IEEE 802.11 (144 Mbps-900Mbps in 2.4/5GHz bands). I want to embed it on board with a processor with my own firmware. I wish to write my own MAC layer.

To be clear, I went to be able to write a simple program that selects a modulation, frequency and tx power, then loads a raw payload (based on some logic) and transmit. On the receiver end, similarly, there is a program to set a certain modulation/frequency and begin listening. An interrupt is fired at the beginning of receiving a frame. I have been looking everywhere on Digikey, RF Components, Mouser etc. but I do not see any chip that has a clear indication in its datasheet that it allows raw tx/rx. Any idea of any chip that does that?

This is a common feature in IoT chips like AT86RF215. There are 31 different 802.15.4 modulations including OFDM. But I am struggling to find a chip that shows explicitly in datasheet how a specific modulation is selected like the IoT AT86RF215 chip.

I know this can be done with SDR in a USRP. But I am looking for an existing off-the-shelf module.

## Answer (score 4, by webmarc)

"Wi-Fi" is a trademark referring to the 802.11 family and has layer2 definitionally baked in.

If you want to roll your own layer2, you specifically do NOT want WiFi or 802.11 family chips.

You may have luck finding what you're looking for by searching for "single chip transceiver."

FWIW this seems like an example of the XY Problem, where you're asking about your attempted solution rather than your actual problem. Perhaps you would consider backing up and sharing what you're trying to accomplish with this solution?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21447/is-there-an-802-11-wi-fi-module-that-allows-direct-access-to-the-phy-layer, by user1933458, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
