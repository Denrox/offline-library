# SDR with the Raspberry Pi

*Tags: software-defined-radio, receiver, rtl-sdr, modem · score 4*

## Question

I wanted to explore digital modes by connecting a Raspberry Pi via audio cables to a transceiver. However, I realized that thanks to the clock generator, the raspberry pi can produce RF signals directly. Adding a square to sine wave converter, a band pass filter and an amplifier, this could be used as the transmitter. There is good software in GNU Radio and PiTx. FM signals can be produced. As far as I can tell it is possible to generate SSB directly on the pi but I haven't understood yet how.

**Q1: Is it possible to directly generate SSB on the pi?**

On the receiver side, things look a bit more tricky. It requires a down converter and a very fast analog to digital converter. The good news is that they appear to be very cheap, e.g. R820T2

**Q2: Would combining a cheap dongle such as the R820T2 enable me to operate in half-duplex mode with the Raspberry Pi?**

I'm mainly interested in playing with the radio, so any band is fine. If I were forced to choose, I would prefer 50MHz.

Apologies for this open-ended question, any suggestions welcome.

M0HXS

## Accepted answer (score 4, by natevw - AF7TB)

Yes, with some important qualifications, you can "directly" generate SSB on the Raspberry Pi. The rpitx software you mention does that, and in combination with an RTL-SDR type dongle you would indeed have a sort of half-duplex transceiver. So in short: yes (Q1) and yes (Q2).

Based on that exact combination, qtcsdr is an app that aims to make your Raspberry Pi into a amateur radio transceiver.

Of course, all the filtering that goes into both a good receiver and — more exigently — a **legal** transmitter are "sold separately"! This is the most important qualification.

I would assume that rpitx (and qtcsdr, which uses it) generates a much, much messier signal than even the most infamous CB amplifier driven hard. (At least your signal will be much quieter :-) Check out the QRPi shield — it's not just a low-pass filter like is often needed in a typical RF chain, but rather needs to be a full band-pass filter to reign in the Pi's spurious emissions.

As far as how the SSB generation actually *works*, that is a fascinating subject and I wish I knew too: [How does rpitx generate arbitrary SSB data with a clock peripheral?](How%20does%20rpitx%20generate%20arbitrary%20SSB%20data%20with%20a%20clock%20peripheral.md)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6774/sdr-with-the-raspberry-pi, by Edgar H, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
