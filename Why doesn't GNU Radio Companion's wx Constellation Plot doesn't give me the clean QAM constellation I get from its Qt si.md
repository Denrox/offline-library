# Why doesn't GNU Radio Companion's wx Constellation Plot doesn't give me the clean QAM constellation I get from its Qt sibling?

*Tags: software-defined-radio, gnuradio, rtl-sdr, modes · score 4*

## Question

Using a RTL2832U USB dongle, I set up GNU Radio to produce a constellation plot of APRS traffic on 144.8 MHz. The result is what I expected:

So far, so good. Why not try the same thing using the wx GUI instead of the Qt version I had used ? Here are the results... The constellation plot does not look the same at all and it is nothing like the clean QAM constellation I had expected and obtained using the Qt GUI:

Can anyone explain why the wx GUI's constellation plot does not behave as I expect ? Is it simply a case of different default settings and naive user expectations ?

## Answer (score 6, by Phil Frost - W8II)

There are a lot of things wrong here. Neither plot looks correct.

- There is no way that Qt plot is realistic for anything but a signal generator. Where's the noise?
- Where are the three missing constellation points in the Qt plot?
- APRS isn't QAM (it's AFSK over FM), so I'm not sure why you are expecting QAM.
- You don't have any filters, clock recovery, or really demodulation of any kind between the source and the sink. Normally you do all that stuff before the constellation such that each sample (and thus, each dot) corresponds to one symbol.
- From the parameters, it looks like WX sink has some clock recovery, but I doubt it's doing anything useful. I doubt it's syncing up with your intended signal. Usually you still need to do some filtering and decimation to at least get it in the right ballpark. The clock recovery is only intended to compensate for slow phase drift. It doesn't know nearly enough to demodulate the signal. For example, how does it know the symbol rate?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1978/why-doesn-t-gnu-radio-companion-s-wx-constellation-plot-doesn-t-give-me-the-cl, by Jean-Marc Liotier, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
