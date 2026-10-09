# How to connect this Active Antenna Loop and 100MHz Upconverter?

*Tags: hf, rtl-sdr · score 3*

## Question

I have bought the two devices in the image. The 100MHz Upconverter with a SMA connector is used to upconvert HF/MF signal for RTL-SDR to demodulate. I found that there is signal from the antenna (tested by using another radio), but I can detect no signal when connecting to upconverter. I think I have connected them wrongly. May you advice the way of connection?

The model of Antenna Loop is Degen 31MS. The up convertor information is located at https://code.google.com/p/opendous/wiki/Upconverter Mine is using 100MHz v1.0 version.

My method to connect is to try to use a small wire to connect the "hole" of SMA connector with the audio plug. I have tried to contact with different part of that audio plug, still no luck.

## Answer (score 2, by WPrecht)

Looking at the Google site you posted, it looks like this is the expected setup, so there probably isn't any gross incompatibilities, but I think you skipped looking at the large vector network analyzer graphs on the first page.

The upconverter is attenuating the signal by between 10dB and 76dB depending on the frequency. Remember that dB is a logarithmic measure of the ratio of the signal strengths ($10 log_{10}$ $\frac{R_{output}}{R_{input}}$ in this case); therefore a 10dB attenuation means the output signal is $\frac{1}{10}$ as strong as the input signal and at 76dB attenuation, the signal would be less than $\frac{1}{1,000,000}$ as strong.

So assuming the input signal is something off the air that may not be that strong to start with and adding in the losses for the connectors and cabling, etc, the signal is probably below the detection threshold of the SDR. Seems like an RF preamp might be called for.

In fact, the FAQ at the bottom mentions this:

**Why not add an amplifier to overcome the 10dB conversion loss? :** Since the Noise Figure of an RF system is most dependent on the Noise Figure of the first elements in the signal chain, it does make sense to place an LNA at the antenna port. I just wasn't sure if most users would have their Upconverter at their antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1663/how-to-connect-this-active-antenna-loop-and-100mhz-upconverter, by Harold Chan, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
