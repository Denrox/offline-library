# SDR sampling bandwidth - do the bits per sample matter?

*Tags: software-defined-radio, diy, theory, electronics · score 21*

## Question

I'm looking at data converter chips for a homebrew SDR design, and I see that I can choose not just the sampling frequency, but also the bits per sample.

Obviously the sampling frequency has to be several times the target frequency, but what effect does the bits per sample have on the signals I can receive and transmit?

Will I be ok with cheaper 8 bit ADC and DAC devices, or will I need to look at 10, 12, or 16 bit converters to experiment with SDR?

My primary concern is for HF usage with 200Msps converters and above, with sampling at the antenna, essentially, rather that downconverting, or mixing prior to the sampler.

## Accepted answer (score 18, by Phil Frost - W8II)

The bits per sample will affect the dynamic range of your receiver.

There's a lot of math that I'm sure you can find, but here's the intuitive explanation:

A digital signal can represent only discrete quantities, where an analog signal can represent infinitely many quantities between any two discrete quantities the digital signal might represent. The difference between the actual analog signal, and the represented digital signal, is an error, and is called quantization noise.

If you have more bits, the error, and the noise is less. Of course, if there are larger sources of noise (the preamplifier, ambient RF noise, etc) then the additional noise introduced by quantization doesn't matter.

Thus, it makes sense on as SDR to adjust the preamplifier's gain so that the noise floor is just above the quantization noise. Otherwise, you are wasting a lot of bits just carrying noise.

This maximizes the bits available for actual signal, which is good, because it also maximizes dynamic range, or how much power can be received by the receiver before it clips (the digital signal can represent a signal only so big). This is of particular concern for SDRs because of their wide receive bandwidth: you may not be listening to that guy with the S9+ signal, but your receiver is. If that signal is strong enough to hit the limits of your ADC, then you get clipping, which will introduce harmonics all over the band, making you unhappy. You could turn down the receiver's gain, but then the very weak DX station that is just above the RF noise floor will be below the quantization noise.

The resolution (number of bits) for the DAC is not really as critical, since you don't need a lot of dynamic range to transmit. You will still have quantization noise, but since the digital signal can trivially be scaled to use the full range of the DAC, the noise is usually negligible. An approximate model is the noise floor will be 6 dB below the signal for each DAC bit. For an 8 bit DAC this gives a noise floor of -48 dBc, sufficient for many applications. Further improvements can be made by noise shaping combined with analog filtering of the output. Or simply upgrading the precision of the DAC may be the most economical solution: DACs are cheaper than ADCs.

So, 8 bits is more than sufficient for experimentation, but this is definitely a "more is better" situation. It all depends on the performance you require, and also your ability to build the rest of the receiver to utilize the full capabilities of the ADC.

As mentioned by others in comments and answers, it is also possible to reduce the quantization noise by oversampling the signal of interest, then decimating the resulting data. For example, say we are interested in signals up to 30 MHz, so we require a 60 MHz ADC. If we use a 240 MHz ADC, but the analog input has no frequencies above 30 MHz, then we have four times more samples than required.

We could simply keep only 1 in 4 samples, but if we first use a digital low-pass filter we can actually remove some of the quantization noise. This is because the quantization noise will be distributed through the spectrum: from 0 to 120 MHz, the maximum at our 240 MHz sample rate. Low-pass filtering then removes the noise between 30 MHz (our upper range of interest) and 240 MHz, so we've effectively removed some of the noise by averaging it out.

The math works out so that for every 4x in excess samples, it effectively adds another bit to the resolution, or increases dynamic range by 3dB. For example, an 8-bit, 240 MHz ADC is equivalent to a 9-bit, 30 MHz ADC.

## Answer (score 4, by sm5bsz)

For HF usage with 200 Msps converters and above, an 8 bit ADC will provide very good performance. You write: "the sampling frequency has to be several times the target frequency" but that is not true at all. It is possible to do under-sampling, listen on e.g. 144 MHz with an ADC running at 10 MHz. If you sample at 20 MHz and have an analog bandwidth of 200 MHz and set your SDR to receive 4 MHz you will find that signals at 4, 16, 24, 36, 44, 56, 64,... up to 200 MHz will provide the same output, appearently 4 MHz in the SDR. They are all aliases of different order. If you insert a filter that picks the range 144-146 MHz and rejects everything else you have a 144 MHz receiver. You would need more than 8 bits however because of the low sampling rate. Note that the digital side will have the noise from all the alias frequencies. Do not insert a wideband amplifier after the filter! When you sample at 200 MHz or above to receive HF signals you are under-sampling. With an interest in the range DC to 30 MHz you need a very simple filter to suppress everything above 170 MHz. Certainly you would make cut-off lower to avoid FM BC and other stuff, but the filter is extremely uncritical. On the digital side the bandwidth would be 100 MHz, but you would apply a filter to reduce the bandwidth to 2.4 kHz (SSB.) The bandwidth reduction is a factor of about 41000 (56 dB) which means that you gain 9 bit so the SSB S/N comes from a 9+8=17 bit (narrowband) ADC.

In case you would use the undersampling strategy at 20 MHz, S/N would be 10 dB smaller because the bandwidth ratio would be 10 times smaller.

Conventional direct conversion receivers (Softrock and similar) typically use "16 bit" soundcards which have a noise floor of about 2 bit and a real range of 14 bit. They sample at 96 kHz so the bandwidth ratio to SSB bandwidth is 40 (16 dB) which means they give an S/N of about 14+3 bit = 17 bit. Similar to what you would get with an 8 bit ADC at 200 MHz. (An 8 bit ADC typically has a noise floor well below 1 bit.)

Note that any ADC needs a RF voltage on the input that sweeps several ADC levels. Severe artifacts appear if the ADC gives the same value almost always. There has to be significant signals that sweep across several ADC levels.

Today, with advanced graphical processors it might be interesting to use few bits at very high rates. Already the 8 bit RTL-SDR.com at 2.4 MHz can produce reasonable results: https://www.youtube.com/watch?v=NYhVvtbqaD0 With 8 bit at 240 MHz you would do 20 dB better! More cost effective would probably be 10 bit at 100 MHz (9 dB better ideally, but more like 6 dB better in real life since the noise floor vs a single bit is likely higher in a 10 bit ADC than in a 8 bit ADC.)

## Answer (score 4, by pyHazard)

The number of bits in the converter will set the maximum dynamic range of the resulting data stream. This is approximately $\textrm{SNR} = 6\,\textrm{dB} \times \textrm{Bits} + 4.8\,\textrm{dB}$ (for a full scale input sine wave).

However, as with everything in life, this is only the beginning of the story. The data sheets for the converters will typically list the SNR achievable with the chip when used in the most efficient manner. For fast, larger bit sized converters, this is almost always less than the $\textrm{SNR}$ shown above, so bit size becomes much less critical than the rated $\textrm{SNR}$ at the operating point you expect. In addition, since you appear to be leaning towards the faster wide-band ADCs, I will assume you are interested in block processing of entire bands. In this situation the $\textrm{SFDR}$, or spurious free dynamic range, is important since large signals may end up covering up small signals on other bands or other regions of the band. This is often less than the $\textrm{SNR}$ spec and may be your limiting factor.

At the heart of your question was “How do I choose the bit size of my converter?” Well, the simplest answer is that you must match it to the dynamic range of your RF front end output, meaning to make sure your $P_{1\,\textrm{dB}}$ or saturation point is near the top of your ADC's range and the noise floor is less than $\textrm{SNR}$ below that.

So far I have only spoken of ADC's. For the DAC's you do not have to worry much about the quantization noise since you will be following your DAC output with a filter. For the DAC the number of bits will set your dynamic range, of course; however, you do not have the near signal-far signal dynamic range problem so the bits are much less important. The $\textrm{SFDR}$ is still very important since you do not want to send spurs out or have to manage them.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/607/sdr-sampling-bandwidth-do-the-bits-per-sample-matter, by Adam Davis, Phil Frost - W8II, sm5bsz, pyHazard. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
