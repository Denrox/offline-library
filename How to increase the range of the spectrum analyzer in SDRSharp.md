# How to increase the range of the spectrum analyzer in SDRSharp?

*Tags: rtl-sdr, spectrum-analyzer, sdrsharp · score 3*

## Question

I'm trying to visualize the frequency band utilization during a GSM phone call using SDR. Ideally, I would like to plot the whole 900 MHz range, i.e. 876-959 MHz. However, even setting the zoom to the minimum I'm only getting a band of about 2 MHz on display (here: 899-901 MHz):

How can I display a wider frequency band on the spectrum analyzer and waterfall graphs?

## Accepted answer (score 4, by OH2FXN)

Unfortunately you cannot increase the bandwidth much: the sampling rate in RTL2832U is at maximum 3.2 megasamples / second. In theory (Nyquist theorem) you could get ±1.6 MHz banwidth, but that is already pushing the limits of your hardware. The ± in the bandwidth comes from the fact that you are sampling the I and Q, or signals with a 90° phase shift separately.

If you don't need real time data, you could try to sample 2 MHz at a time and then patch these samples together. I have played around with the post-processing in Python, so let me know if you are interested?

I just found out that there's a RTL-SDR scanner project that samples spectrum piece by piece. This of course won't give you the waterfall view.

## Answer (score 5, by hotpaw2)

If you use SDRSharp with an Airspy Mini, instead of an RTL-SDR, the supported sample rates allow up to 6 MHz bandwidth, due to the use of an ADC with a higher sample rate than the RTL2832 is capable of.

For a wider bandwidth display than 6 MHz, you either need to use different software that can scan or stitch across a frequency range, instead of directly capturing that entire range at once, and/or more specialized hardware (such as Ettus USRP or LimeSDR units, and/or PCi bus SDRs) which can support higher sample rates and data bandwidths.

## Answer (score 2, by Jack0220)

HackRF One will give you 20MHz bandwidth. Edit for more detail: If you buy the HackRF One instead of the Noelec SDR dongle, you will have 20MHz instead of 2MHz. Note that the HackRF One costs about $300 which is still 10 times cheaper than a spectrum analyzer but 15 times more expensive than the SDR dongle you currently have.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19963/how-to-increase-the-range-of-the-spectrum-analyzer-in-sdrsharp, by Dmitry Grigoryev, OH2FXN, hotpaw2, Jack0220. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
