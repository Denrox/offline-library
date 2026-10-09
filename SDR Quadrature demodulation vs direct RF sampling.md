# SDR: Quadrature demodulation vs direct RF sampling

*Tags: software-defined-radio, rtl-sdr, direct-conversion · score 21*

## Question

I see that many SDRs use a quadrature demodulator and sample I and Q signals.

But is it possible to downconvert the RF signal instead, sample it with only one ADC, and get the same capabilities of digital postprocessing?

So if we want to observe 100-150 MHz bandwidth: we pass it through a 100-150 MHz bandpass filter, downconvert it to DC-50 MHz, and sample it with a 100 MHz ADC.

Will it work? And if it will - why is IQ so widely used?

## Accepted answer (score 15, by Phil Frost - W8II)

Sure, it would work. In fact, if you've ever used something implementing some digital mode that interfaces with an SSB tranciever, this is exactly what is happening. Many TNCs and most PSK-31 software is an example of this.

The reason I/Q is more frequently used is that it's simpler. If you want an SDR with 50 MHz bandwidth, you can do that with a single 100 MHz ADC as you describe, or two 50 MHz ADCs and I/Q sampling. Either way, it's 100 million samples per second, so the ADC complexity is essentially the same.

The difference is in the mixing. An ordinary mixer works by multiplying two signals. This creates two sidebands, the sum and the difference of the frequency components of the two mixer inputs. One of these sidebands must then be filtered out. Good filters are hard to realize, digital or analog.

However, if you have the signal in I/Q form, the signal can be multiplied by a complex exponential. This doesn't create sidebands: it directly shifts all the frequencies up or down by some frequency. This is more directly what we usually want to accomplish with a mixer.

There are additional benefits: the discrete Fourier transform (DFT), used in a great many DSP techniques, works on complex numbers. When we don't have I/Q data to provide it, then we must arbitrarily set Q to something (usually 0). As a result, half the result of the DFT (all the negative frequencies) are just a mirror of the positive frequencies, so they are discarded. This is computationally inefficient.

## Answer (score 4, by Alan Campbell)

One of the earlier SDR models, the HPSDR, had/has a single receive board: the "Mercury". It used a single high-speed ADC. Details are here.  
Once the RF is sampled and fed into an FPGA, it typically gets split into I and Q streams anyway. If you have a 120Msps ADC, for example, you could mix with a 30MHz SINE signal (0, 1, 0, -1, repeat) and a 30MHz COSINE signal (1, 0, -1, 0, repeat).

Benefits? Well for starters, you've halved the number of ADCs and associated amps, physical filters, etc. You still have them - but now they need to be implemented *In Code* in the FPGA. Separate I and Q channels also tend to have distortion problems around DC.

Drawbacks? You have to write more code. Some of that code (the complex exponential) can be quite hard to do well. **Edit:** Another expense-related problem: your single ADC now has to be twice as fast. This can *significantly impact* ADC cost, and even the circuit design.

As for your idea of looking at 100 - 150MHz: this is where *oversampling* comes in. If you sample a 60MHz signal with a 100MHz ADC, the Nyquist effect makes it "look like" a 40MHz signal, ie. reflected around the half-sample rate. A 90MHz signal will "look like" a 10 MHz signal. What would a 101 MHz signal look like...?  
It would look like a 1 MHz signal. This is oversampling.

Looking at a bandwidth of (up to) half the sample rate, while technically possible, is pushing things a bit. In practice, for the conditions you specified, I'd use ADCs rated at 160Msps (or higher), and expect data between 60 - 10MHz. Such ADCs don't come cheap, so I'd probably consider a single ADC version to start with.  
Also note how the frequency band got "reversed" by using the Nyquist oversampling. This can impact decoding analog TV (color burst in wrong location), SSB (LSB becomes USB), and commercial FM (stereo information in secondary signal).

## Answer (score 3, by sm5bsz)

It does not matter if you sample DC to 100 MHz with one 200 MHz ADC or two 100 MHz ADCs preceeded by the appropriate I/Q mixer. There are efficient algorithms to use the real-valued input from a single 200 MHz ADC to produce an output of 100 MHz complex FFT. Have a look here: https://www.youtube.com/watch?v=kxkd8e_ijw8 I do not think suitable routines are included in standard libraries, but it is not difficult, one feeds two subsequent time functions into I and Q, makes the transformation and finally takes the sum and difference of the signal and its mirror image. Direct sampling or down conversion both allow extremely good performance. In real life, today, direct sampling is better, many radios provide a dynamic range around 150 dBc/Hz (typical ham transceivers are around 125 dBc/Hz.) HB9DRI is developing a dual ADC unit that is soundcard compatible and that provides something like 163 dBc/Hz. As far as I can understand he will be able to supply a 144 to IQ mixer that will provide a dynamic range of about 160 dBc/Hz - but with X-tal oscillators to keep LO sideband noise really low. Today, direct sampling uses an FPGA to do digital down conversion. That means a rather complicated hardware and a high cost. Sampling perhaps 80 MHz with a single ADC directly into the computer would allow all the processing to be done in the computer where a GPU (Graphics adapter) could do all the filtering and bandwidth reduction that is needed. The video I linked to above shows operation on a very powerful computer, but rather than using 8 i7 cores I think I could use the K600 Nvidia board. OpenCL reports that the Nvidia GPU and the Intel GPU provide similar performance. Sampling 14 bit at 80 MHz provides an extremely good performance provided one has some kind of filtering on the input. A long-wire antenna might produce +25 dBm from the local MW station. One can not look for -130 dBm signals on 28 MHz having them present. Fairly simple filters are needed though.

Be careful when reading specifications. The music industry is horrible. They may specify 24 bit resolution on soundcards that have their noise floor 14 bit below saturation. Truncate at 16 bits would make no difference at all.

On your question: IQ is so widely used because the output fits to standard stereo soundcards and the data rate is so low that one does not have to care about algorithm efficiency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1196/sdr-quadrature-demodulation-vs-direct-rf-sampling, by BarsMonster - R2AYN, Phil Frost - W8II, Alan Campbell, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
