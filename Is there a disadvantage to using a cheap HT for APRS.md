# Is there a disadvantage to using a cheap HT for APRS?

*Tags: digital-modes, ht, aprs, beacon · score 18*

## Question

Looking to build a cheap (not even inexpensive, just dirt cheap) APRS beacon transmitter. Right now you can get a dual band handheld transceiver with rechargeable battery, antenna, etc for under $31 [USD], for instance. I can't find a cheaper transceiver.

What are the downsides to using a Baofeng, Wouxun, or similar cheap HT for APRS? Are there ways to mitigate the problems, if any, of these units?

## Accepted answer (score 8, by Amber)

Most of the common disadvantages for Baofengs et al have to do with usability (e.g. poor user interface, odd squelch performance). The actual reception and transmission power is just fine. The majority of the disadvantages are negated when working with APRS, since it's the APRS modem interacting with the radio rather than a human being.

The main thing you'd probably still want to be aware of is the antennas; most of the cheap HTs come with poor-performing rubber duck antennas. Replacing the antenna is probably a good thing to plan for if you go with one of them, to help get a more reasonable signal strength.

## Answer (score 4, by oh7lzb)

Some of the cheap HTs, which were designed for voice, key up the transmitter quite slowly, and the transmitter also stays on for quite a while after the PTT is released. At least my older Puxings behave this way - they require a long txdelay in the tracker (delay from PTT down to the start of data transmission), and there's also a long "tail" after the data.

It might have to do with power saving methods, which can be disabled in radios which were designed for data (like the ham rigs with built-in APRS).

You can compare transmitter key-up/key-down timings by attaching another receiver to a computer, opening the squelch completely, and recording the APRS transmissions using a wave editor such as Audacity (free). Zoom in to the start of the transmission - it'll be quite easy to see where the txdelay flags end and actual data starts. If your tracker has a txdelay setting of 20 (200 ms - they're traditionally set in 10s of milliseconds), and you're seeing 50 ms of flags before data, the transmitter takes 150 ms to transmit. If you're seeing 150 ms of flags before data, the transmitter only takes 50 ms to wake up. On some of these SDR-based HTs the delay varies a lot.

Zoom in to the end of the transmission and see how long the transmitter transmits after the end of data, too. Some stay on longer, wasting more bandwidth than others for the same amount of transmitted data.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/835/is-there-a-disadvantage-to-using-a-cheap-ht-for-aprs, by Adam Davis, Amber, oh7lzb. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
