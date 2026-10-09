# Advantages of IQ generation at Mixer Stage or within FPGA for SDRs

*Tags: software-defined-radio, rtl-sdr, usrp · score 7*

## Question

I draw two possible architectures for Software Defined Radios below.

In the first architecture, I,Q signals are generated at the mixer stage and two ADCs are required. The FPGA down-samples the samples from ADCs and forwards them the USB PHY. Digital Down Conversion is not mandatory in this design (pls correct me if I am wrong).

In contrast to the first design, the second architecture has only 1 ADC. It only creates the I,Q signals inside the FPGA with the help of DSP. The ADC samples at 2x the max frequency present at the input of the Mixer to avoid aliasing.

I am curious to know why an engineer should opt to go ahead with the 1st design over the 2nd design. It seems USRP N210 is having a very similar architecture to the first. So what disadvantages does the second design (I already know ADC needs to be 2X speed, so neglecting that fact) bring to the designer?

Also, what are some reasons to chose the second design?

Thanks for answering my questioning mind!

## Accepted answer (score 7, by Marcus Müller)

Well, the need for one ADC that's twice as fast is definitely a very important factor!

The same "it gets harder with rising frequency" argument applies to the anti-aliasing filter:

Building a low-pass filter of pass band edge frequency $f_{cutoff}$ and stopband start frequency $f_{stop}$ depends in complexity on how narrow the transition between pass- and stopband is, *in terms of passband width*. In other words, if you want your stopband to start 1 MHz after your passband ends, it's easier if your passband ends at 10 MHz than if it ends at 20 MHz.

Then, remember that SDR architectures are also born out of demand to fit a specific use case, which often entails specific communication standards.

This is kind of a recursive argument, but: Standards like LTE, WiFi, or DVB-T were invented with the quadrature mixer in mind. That means that they can work around the technological problems of the quadrature mixer (mostly, LO leakage leading to a DC spur, meaning that in all these OFDM systems, the DC carriers are left unused, as that's where you'd see your LO)!

## Answer (score 4, by Denis)

I would like to add a bit of my intelligence to this topic as I did some extra reading. This answer isn't a stand alone answer but merely a minute extension to the answer posted by Marcus Muller.

I feel like one strong reason to generate/extract I,Q waveforms at an earlier stage in architecture-1 is to stop the interference by negative frequencies.

More specifically, at the mixer stage, LO multiplies with the RF signal from the antenna. In that case, if the down converted band comes about/near 0Hz, then parts of the down converted band band may fall to the negative frequency side which will in turn fall back on top of the positive band. This will contaminate the whole intelligence. This process is elaborated below.

In contrast, if we extract IQ at at the earliest state, we eliminate this problem. This is because I,Q can represent negative frequencies. Hence, at times our LO goes near RF frequency, we can still sustain the intelligence of the message that was transmitted without corrupting it.

I hope I made some sense.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10454/advantages-of-iq-generation-at-mixer-stage-or-within-fpga-for-sdrs, by Denis, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
