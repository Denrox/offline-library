# Why don't monolithic HF transceiver ICs exist?

*Tags: hf, diy, transceiver · score 11*

## Question

HAM operators who build their own HF rigs typically do so using discrete components.

However, for VHF and UHF rigs, an operator can make use of monolithic transceiver ICs on the market

For example, there is this one for 30MHz ~ 1200MHz:

AK2401 Direct Conversion Transceiver IC

Why aren't there monolithic HF ICs like this?

It would seem that since the frequencies are lower, the circuit design would be easier. I can only think of an economic reason:

1. The market is small. Whereas VHF and UHF is used for commercial radios, a tunable HF rig is used mostly by hams only.

**Are there technical reasons we don't see monolithic HF ICs?**

## Accepted answer (score 10, by Marcus Müller)

Why aren't there monolithic HF ICs.

There are, in the shape of actual (broadcast) AM receiver ICs, which can most likely with minimal effort be also used to transmit.

However, are there technical reasons we don't see monolithic HF ICs?

Your market considerations are something I'd **very much** agree with. Why build a monolithic IC for something that is rarely needed, and if needed, can be done by the potential customer with low cost and effort without any dedicated ASIC? Let me elaborate:

You can often simply use the IF interface of a superhet UHF FM transceiver chip as direct HF AM circuitry. The older Philips FM receiver ICs are known to be prone to "accidental" HF operation by interference on the IF.

If you're only after AM modulation: What do you even need? All you'd need for transmission is a mixer – and the NE612 will happily do that. Same for superhet reception, followed by an envelope detector (a.k.a. diode).

Also, this is 2018 – you can actually directly synthesize all you need for HF transmission with any mid-class microcontroller (that'd be some IF at a rather low frequency, seeing that ham bandwidths in that band are very low, and something to mix that with, which can easily be generated with the chip-integrated PLLs and PWM units) plus an external filter, which might or might not be very complex – in the end, if you need little output power (e.g. to drive an amplifier), your an RC lowpass filter could easily work with large resistances and low capacitances, so it would be very compact. You typically don't need much in terms of high-pass filtering – your antenna simply won't work for lower frequencies (plus, high-pass filtering can be done with an CR high pass filter of the same order of size).

So, I'd argue, this is an SDR world:

- There's monolithic chips for everyone who wants them – just that they are cheap microcontrollers and need to be programmed with software to do what you want, and would, much like most monolithic UHF ICs, only need external filtering components; that includes both RX and TX capabilities.
- With (not that much) more expensive digital logic, you could directly sample (ADC) or directly synthesize (DAC) at HF frequencies any arbitrary waveform, which includes AM, FM, Digital Radio Mondial (DRM), Codec2, …
- And anything that can enough bandwidth of stereo audio (so, any midrange audio DAC with) can be abused as IQ baseband DAC, giving the same flexibility as the previous point; leaves you with the need for an external quadrature mixer (and those exist as monolithic ICs). Or you only use smaller bandwidth (a bit less than half of the Audio DAC's sampling rate or lesser), and go for low-IF and a single mixer.

Oh, by the way, the SteveM of Osmocom fame has just released his fl2k project, which... uses a monolithic IC that was designed to synthesize analog video (VGA to be specific) to convert things that are far higher in frequency than HF directly. So, there's literally a 5 € device on the market that can directly be used as DC..HF..UHF (and with harmonics, far above that) SDR transmitter on any PC-style hardware with USB3 for direct sampled HF with free software. USB2 would be totally sufficient for HF-typical bandwidths, too, but you'd need to exploit the third harmonic (or fifth).

## Answer (score 3)

At high frequencies, (3 30 MHz), the resonant component values (inductors and capacitors) would require physical sizes larger than may be practical on current IC fabrication equipment. I’m speaking strictly about conventional superheterodyne methods. On the other hand there are monolithic a.m. radio circuits that utilize the TRF (tuned radio frequency method) my understanding is that TRF is not a technology applicable to the complexities of current amateur radio requirements however.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10193/why-don-t-monolithic-hf-transceiver-ics-exist, by watkipet, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
