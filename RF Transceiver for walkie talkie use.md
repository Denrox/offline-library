# RF Transceiver for walkie talkie use

*Tags: diy, uhf, equipment-design · score 8*

## Question

I'm close to my EE. BSc finale and I'm looking to play around a little bit with the stuff I've learned. To be honest, I'm a little bit upset that after 4 years of learning communications theory, I'm not able to choose the hardware I need.

My idea is to build a half-duplex walkie-talkie with the following reqs:

- Low voltage operation. Till 5V.
- Range about 1.5 km LOS.
- ISM frequency use. (I prefer 433 MHZ UHF bands.)
- Single chip that doesn't require extra elements such as crystal or filters.

The idea is to install 2 walkie-talkies, one on each house. House are about 900m range. One has a direct window outside while the other is an interior office.

The application is for voice only. Considering the FM advantages I'll prefer it, but if there is a big difference of value then AM could be an option.

The chip I'm looking for must be the smallest that can be.

I've seen many chips (such as the following links) but I'm not sure that their digital buffers support voice applications.

http://www.hoperf.com/rf_fsk/fsk/21.htm  
http://www.melexis.com/Wireless-Multi-Market--Sensing/RFIC-Transceivers-27-to-950MHz/TH7122-121.aspx

## Accepted answer (score 3, by Adam Davis)

The chip you've linked is capable of analog FM transmission and reception, from 2.5kHz to 80kHz bandwidth. In the frequency range you're looking at it has a frequency resolution of 12.5kHz. It's very low power, with the right antenna it should reach your target LOS. Check out Figure 4.2 in the TH7122 and TH71221 Cookbook for an example showing how to use the chip as an analog FM transmitter, and figure 6.7 for an example of how to use it as an FM receiver. By combining the two circuits with the typical application circuit you can build a single-chip analog FM transceiver.

Note that your requirement, "Single chip that doesn't require extra elements as crystal or filters" is going to be hard to meet with any radio design. There are several inductors and capacitors used as filters outside most "single chip" transceivers. If you want any frequency stability you're going to need a crystal.

The Philips SA58646 is also a good choice, but again you're going to have to deal with a few inductors, capacitors, and a crystal.

Also note that with such low power devices your antennas are going to have to be very, very good, and probably very large. If you don't want to spend a lot of time and effort on antennas, or need small antennas, then you'll have to trade off some additional effort adding an RF amplifier to these devices and consuming more power.

Are you sure you don't simply want an off-the-shelf transceiver? If you're trying to avoid filters and crystals while building your own transceiver, it seems you might need a higher level solution than a DIY circuit. The radio linked is a cheap HT for the UHF band, runs on 3.7V, and has a 3W output. It's under $20, and if you remove the battery, casing, controls, connectors, then the one or two PCBs that are left are very small. It does appear to have a low power TX setting, so you should be able to set it to 1W output rather than the full output power if you have power consumption concerns beyond requiring low voltage. You may even consider modifying the radio to remove the PA and use the very low output prior to the PA, saving significantly more power.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1032/rf-transceiver-for-walkie-talkie-use, by Santiago, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
