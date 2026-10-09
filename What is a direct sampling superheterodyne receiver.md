# What is a "direct sampling superheterodyne" receiver?

*Tags: superheterodyne · score 9*

## Question

Browsing the specifications for the IC-7300, I noticed it says the receiver system is a "Direct Sampling Superheterodyne" with an IF of 36 kHz.

I was confused by this, since I thought "direct sampling" means the received RF is amplified and filtered, but not mixed; and a superheterodyne employs a mixer. Thus a receiver can not be both direct sampling and superheterodyne. NI seems to corroborate this understanding.

So what is the IC-7300 architecture really, and what is a "Direct Sampling Superheterodyne" receiver?

## Answer (score 2, by hotpaw2)

The 7300 is a direct sampling receiver, since it samples RF at well above twice the the band frequency of interest.

**However**, there is more than one signal path with more than one bandwidth and center frequency involved. Although one of the signal paths is direct sampling (likely the widest bandscope) other digital signal paths may not be as wide. Those sub-bands can have narrower bandwidths and be offset within one of the wider signal paths (by far more than a BFO tone). Since the frequency of, say, a CW signal can be significantly offset from the center of some signal path, that can make some of the intermediate signal paths into intermediate frequency or IF signal paths, since their center frequency can be different and offset (from both DC and from the CW carrier frequency, by far more than a BFO tone).

This is because a direct sampling receiver can have such a wide bandwidth, that a (usually complex) heterodyning mixer (or two or more!, often inside an FPGA) might be required to pre-process the data so that an affordable DSP or CPU can finish the SDR processing. This means the directly sampled RF result is direct conversion data, but other data paths may be heterodyned or mixed down into intermediate frequency signal paths, before being further heterodyned or mixed and filtering down to a final baseband for demodulation.

Another example: The common RTL-SDR-v3 RTL2832U chip can direct sample MF and low HF by sampling at 28 MHz (in bypass mode from using the front-end mixer such as an R820T2), but then the RTL chip mixes down and ships data over the USB port as an offset IF frequency stream with a lower sample rate of 240k or 2.4Msps (etc.). So the front-end hardware portion (the ADC) can be direct sampling. But the software on the PC only sees a narrower bandwidth IF frequency data stream (and the software possibly uses yet another internal IF frequency data path before demodulation). If an IF frequency signal path is necessarily involved, what would the total system be called other than a superhet?

So, from the hardware point of view, direct sampling. From the SDR software point of view, a superhet. In an integrated receiver or transceiver unit containing **both** the hardware and the SDR/DSP software, such as the IC-7300, both. (is it a desert topping?)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19922/what-is-a-direct-sampling-superheterodyne-receiver, by Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
