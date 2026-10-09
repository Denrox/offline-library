# SDRPlay RSP1 and broadcast band (AM) interference

*Tags: software-defined-radio, filter · score 4*

## Question

I heard the SDRPlay RSP2 has an AM notch filter, but I don't want to spend that much money. How is the RSP1 for broadcast band interference? Will I need a preselector? I already have an MFJ-1020c but am hoping to sell it to offset some of the cost of the SDRPlay.

## Accepted answer (score 2, by Hamsterdave)

It's not great, especially if you're in a densely populated area, but frankly neither is the RSP2. The RSP2's most compelling feature is arguably the High Z input, which does not include the AM BCB filter.

You'll see images throughout the LF and MF frequency range if you have strong AM stations in the local area. An additional preselector (it has a set of preselectors already built in) will help a bit, but a proper AM BCB band stop filter, a grounded metal enclosure, and particular attention to preventing common mode current on the feedline will get you a long way toward entirely eliminating overload.

The High Z input significantly improved performance on HF and LF, with better sensitivity particularly below 3MHz, and a bit better SNR as well, perhaps because of changes in how the signal is routed through/around the preamp.

If you're going to use it primarily for VHF and up, the RSP1 will do just fine. If you're going to use it for 80-10m, with a bandstop filter, I think you'll find it quite usable. If you want good low band performance, the 2 is worth the extra money, to be sure.

## Answer (score 2, by Bill Sproul)

I bought the RSP2, and it suffers from AM broadcast band interference on HF bands, even with the AM/FM filter on. I have a 1Kw transmitter at 1350KHz about 4 Km from my house, and it bleeds thru on all HF, however when you select a ham band it seems better ??? Anyway, I am building a high pass filter to cut out anything below 2 MHz, there is no other option. Or you can buy one. I love the receiver, no regrets, if I lived further from the transmitter I wouldn't have any issues.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7691/sdrplay-rsp1-and-broadcast-band-am-interference, by K8KV, Hamsterdave, Bill Sproul. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
