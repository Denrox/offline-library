# Advantages of IQ mixer versus direct sampling SDR architectures?

*Tags: software-defined-radio, receiver, transceiver · score 3*

## Question

What might be the advantages, if any, of HF SDR architectures that use a mixer between the ADC/DAC and RF, versus those that sample or generate RF directly (at 0 Hz on up) with a fast ADC or DAC?

Are the advantages/disadvantages different depending on target use (QRP/SOTA vs. multi-operator contesting, etc.)?

Both types of HF radios and rigs seem to be currently marketed, and/or offered as kits, and at least one vendor offers both as an (expensive?) add-on option.

## Accepted answer (score 4, by user10489)

Direct conversion with lower distortion vs mixers with inexpensive ADC is only the first differentiation between the two methods.

The original advantage of using a mixer is that you could vary the intermediate frequency used by the mixer to change the frequency of interest and have a fixed frequency output from the mixer to feed to second stage filters, amplifiers, and demodulators. It is difficult and expensive to make filters that can change frequency, so this is a huge advantage. SDR eliminates the need for fixed frequency demodulation, as it's all math, and can work equally well at any frequency the hardware supports.

The remaining question is if it is still useful to have fixed frequency hardware filters on the output side of a mixer. For a well isolated strong signal, these hardware filters are not better than what can easily be done in software. However, if the signal of interest is either close in strength to the neighboring signals and noise, or if there is a strong signal near in frequency to a weak signal of interest, then hardware filters can significantly attenuate surrounding signals while passing through the weak signal of interest. (This is called "sensitivity". I'm also glossing over details such as AGC, and multiple amplifier+filter+mixer stages.)

How useful this is depends on the signal to noise ratio between these signals, and the sharpness of the analog filter vs. the dynamic range of the A/D converters in the SDR. If the SDR has a wide dynamic range (which translates to bit depth of the samples on the software side), it can easily exceed the sharpness of a hardware filter, but maybe not the attenuation (in decibels). For instance, a cheap 8 bit A/D converter has 48 decibels of dynamic range. A good (but expensive) analog filter might have 60db of attenuation of noise, and a (large) cavity filter might have 120db of attenuation and isolation.

Some high end radios made in the last 10 years take advantage of both good hardware filters and good SDR front ends (with more than 8 bits of depth) and get the best of both worlds. However, in the last several years, the quality of good A/D converters has gone up and the cost gone down to the point where the dynamic range of SDRs and their software filters are starting to exceed the capability of small hardware filters so that the same manufacturers are discontinuing the hardware filters.

We are currently in a transition period to a new mode of radio technology. This is the third or fourth such transition since the inception of radio, converting parts of the radio from analog to digital while improving quality.

## Answer (score 5, by Phil Frost - W8II)

A direct-sampling SDR doesn't require a mixer, which can simplify the design. Also, provided the receiver has sufficient dynamic range and processing power, a direct-sampling receiver can monitor all the bands at once.

On the other hand, a direct-sampling SDR must have an ADC and DAC at a sample rate above twice the maximum frequency. So for an SDR that covers all HF, the sampling rate must be at least 60 MHz, in practice more to provide some room for the filter roll-off.

High-frequency ADCs are expensive. The resulting data is also computationally expensive to process, usually often an FPGA to do the initial digital filtering and decimation.

In contrast, the addition of a mixer allows a much cheaper ADC and lower bandwidth digital stream: the ADC sample rate needs only to be wide enough to accommodate the widest bandwidth signal of interest. For amateur HF this is usually less than 4 kHz, within the capabilities of any audio interface and easily processed by any PC made in the last decade.

Theoretically the mixer adds distortion and eliminating it should could lead to better performance, but in practice designing a good mixer with modern components is neither difficult nor expensive. For example, the SoftRock Lite II sells for $21 USD and includes anti-aliasing filters, a mixer, and a fixed-frequency oscillator.

A mixer also allows for more flexible analog filtering options, which might be of some value in situations where the ADC lacks sufficient dynamic range due to a strong adjacent signal. In a direct sampling architecture you'll typically have a bank of *preselector* filters which isolate a particular band with the objective of reducing the input power to the subsequent stages and thus the required dynamic range. However these filters will be fixed in frequency, and if you don't have the filter to isolate a strong interfering signal, you're just out of luck.

A mixing architecture will also have some fixed filters to eliminate mixing products, but then will have another filter at the IF, which is probably 0 Hz in most SDRs. This filter must at least be sufficient to avoid aliasing at the ADC, but the radio may offer a selection of filters of a few widths which will be selected according to the bandwidth of the signal of interest.

In a mixing architecture this filter can effectively be moved in frequency, and it's likely to be narrower than the preselector filters as well. This makes it more likely this filter can be used to exclude a nearby, strong interfering station which would otherwise overload the ADC.

While this may be a useful capability in the right circumstance, it may not ever be useful unless your receiver is near another transmitter. Also keep in mind all the stages before this filter (so: the mixer, and any filters and buffers between it and the antenna) are still subject to the full power of the interfering signal, so any nonlinearities in these components will still be problematic. Very difficult interfering signals are best addressed, if possible, with a passive filter before any active components.

So I would say the most important practical differences come down to cost and maximum bandwidth. If you want to monitor 80 meters and 10 meters at the same time with the same radio, you'll need a direct sampling receiver. But it will cost more, on account of the high-speed ADC and FPGA.

If you're content monitoring less than 100 kHz of bandwidth at a time, then a cheap mixer-based SDR will be much more affordable. If it's of the variety that uses the computer's audio interface, then it's worth spending a little money on getting a good one since this is the main determinant in the receiver's performance, and the built-in audio interfaces in most computers are terrible.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16028/advantages-of-iq-mixer-versus-direct-sampling-sdr-architectures, by hotpaw2, user10489, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
