# How to calculate if low-pass filtering is sufficient?

*Tags: diy, software-defined-radio, amplifier, filter · score 8*

## Question

An answer on this question [Suggested method for boosting 0.05 watt transmitter up to 10+ watts?](Suggested%20method%20for%20boosting%200.05%20watt%20transmitter%20up%20to%2010%2B%20watts.md) suggests putting a filterless 19dB amplifier between the HackRF (or similar general-purpose SDR) and a larger amplifier — so only the final stage includes much in the way of filtering.

Is some caution warranted here for spurious emissions?

As far as I can tell, the HackRF's own filters are *before* (from a transmit perspective) its RF amplifier stage.

The project's block diagrams aren't very helpful in this regard, but http://www.wimo.com/hackrf-sdr_f.html has a detailed write up ("After the antenna input two MGA-81 GaAs MMIC amplifiers follow, one serves the input, the other the output path.") and provides this frontend block diagram:

So after its filtering, the HackRF adds a +14dB gain of its own. After which, we might add something like the PennyWhistle, QRP-PA 2008 or PA-100 to boost the SDR's still-small signal closer to the 5W range — something like another 15–25dB further gain. Finally we might put this through something like the HF-Packer or HARDROCK-50 amplifier which provides another ~10dB gain, before the signal finally getting filtered again by that amp's LPF section.

Is all this gain going to add more spurious emissions than the power amplifier's LPF section is likely designed to handle? I've been told that one really should filter after every stage of amplification, but in this setup the signal goes through three stages before filtering. Perhaps the "pre-amp" stages are much easier to keep clean/linear, or is that a bit too optimistic?

How could I use the specifications for each of the pre-amp stages to determine all the expected types and levels of spurious emissions they are adding? Do these harmonics compound from one stage to another, i.e. if the input to the external pre-amp is already not clean how do I take that into account when calculating the distortion it will add?

## Answer (score 3, by Phil Frost - W8II)

There are a couple reasons to filter between each stage.

Firstly, if you don't want to transmit those harmonics, then there's not much point in amplifying them. If you have an amplifier capable of a 10W output, but half the power is in undesired harmonics, then you are only getting a useful 5W out.

Secondly, you may want your amplifiers to be linear, but they never are exactly linear. In practice you'll get some degree of intermodulation distortion due to the different frequency components in the signal mixing with others. These intermodulation products have the potential to become spurious emissions if they aren't somehow removed before the final output.

If you don't filter between stages, then the distortion (both harmonic and intermodulation flavors) from one stage goes into the next. This increases the power at the input, and distortion gets worse with increasing power. It also means more frequency components to mix with others, compounding the issue.

How much filtering is enough? Well that just depends. By examining the signal at each stage with a spectrum analyzer (or my cheap substitute: another radio) you can see how much distortion is added by each stage and add the appropriate filtering.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6184/how-to-calculate-if-low-pass-filtering-is-sufficient, by natevw - AF7TB, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
