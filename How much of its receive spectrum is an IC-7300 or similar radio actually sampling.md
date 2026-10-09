# How much of its receive spectrum is an IC-7300 or similar radio actually sampling?

*Tags: software-defined-radio, icom-ic-7300 · score 4*

## Question

I'm curious as to what the sampling strategy is for radios like the IC-7300.

For example, I can set my waterfall display span to be up to +/- 500kHz around the tuning point, i.e. I can see a megahertz of spectrum in real time on the screen.

So how is the radio doing that?

Is it directly sampling the (amplified) RF? If so, is it sampling the radio's entire receiving range? The IC-7300 can receive up to 75MHz. So is (per Nyquist) sampling at 150MHz?

Or does it do some heterodyning down (or up, for low enough frequencies) to some IF with a 1MHz bandwidth, sample at twice that fixed IF and then apply the narrow IF filter to get just the frequency I want to listen to and send that on to the demodulation and audio amplification stages?

## Accepted answer (score 2, by Simon Farnsworth)

The IC-7300 receive section works in stages; the first stage is all-analogue, and consists of the attenuator, followed by a set of analogue filters to remove power outside the band of interest, followed by the pre-amp.

The second stage is an ADC, which based on experiments with a powerful out-of-band station at about 93.8 MHz is probably clocked at the same 124.033 MHz as the DAC.

Everything that reaches the ADC is then supplied to the FPGA, which both generates the waterfall, and filters down to 36 kHz for the DSP to use. The analogue filtering is set up so that there should be no aliases present in the input to the ADC; this allows the FPGA to process based on the theory behind bandpass sampling.

Note that this implies that 4m (70 MHz) support is done via an alias - the IC-7300 analogue filters are used to limit the frequency band to 70 MHz to 74.8 MHz, and then the ADC filters at 124.033 MHz, which means that 4m is undersampled, and thus the FPGA's processing has to be aware that this is an alias.

## Answer (score 4, by gschro)

The RF signal passes through analog filters (selected using relays based on RX frequency) to remove out-of-band energy. It also is optionally amplified by two analog pre-amps. Then it is directly sampled - no analog down-conversion.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23033/how-much-of-its-receive-spectrum-is-an-ic-7300-or-similar-radio-actually-sampl, by QuantumMechanic, Simon Farnsworth, gschro. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
