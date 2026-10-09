# Pseudorange in VHF band navigation and precision phase tracking

*Tags: software-defined-radio, vhf · score 6*

## Question

I am thinking on what is the practical limit of precision for VHF positioning system (like currently obsolete and gone "Transit" system).

It is well known how GPS receivers calculates pseudorange to each satellite to calculate the position of the receiver - GPS transmits PRN signal at 1 MBit, so by just counting the "chips" you can get pseudorange precision down to 1us which is 300m, and by tracking the phase you can get much more precise (ultimately to the point where you are limited by oscillator phase noise and ionospheric delays).

But in VHF we typically don't have bandwidth to transmit 1Mbit PRN signal even if it's below noise level, and one will have to use much lower speed, like 19200. Obviously length of 1 bit at 19200 is extremely long.

The question is what is the practical limit on precision of phase tracking of the signal given that it's VHF and bitrate is mere 19200?

Is it possible to track the phase with ultimate precision by recoding the data with SDR and after decoding the data we go back in history, and try every possible signal start time by maximum SNR using this now known data? It seems that in this case phase resolution will be limited by SDR sample rate and phase precision will be limited by length of the data packet and physical limitations (phase noise, ionosphere, e.t.c).

## Accepted answer (score 3, by Dave Tweed N3AOA)

Interesting question, and I'm surprised you haven't had any responses before now.

There's no fundamental limitation to the time resolution you can achieve, even in a bandlimited channel. Consider a carrier modulated by a continuous 1-kHz sinewave. A DFT can make a very accurate measurement of the phase and amplitude of this modulation. The resolution is limited by the number of samples used in the DFT, and the accuracy is limited by the amplitude and phase noise introduced by the channel.

Assuming the channel noise has zero mean, then longer DFTs (more samples, longer integration times) give you better results.

It isn't difficult to set up a simulation of this kind of system in any sort of math-processing system (e.g., Matlab, octave, numpy, etc.). Generate the signal, add the channel distortions to it, and then do the DFTs on the resulting samples and see what kind of distribution you get in the measurement errors. I would be surprised if you couldn't get down to 1 µs accuracy with "reasonable" noise levels and integration times.

In order to turn this into a complete time-of-flight measurement system, you could add additional tones that carry data that would allow you to resolve the cycle-counting ambiguities.

Back in the late 1990s, I was doing some experiments trying to determine just how much accuracy I could extract from the time signal transmitted by the Canadian time station CHU. The problem there is that they only transmit 10 cycles of a 1-kHz tone every second (to create an audible "tick"), and the fading/multipath on the HF bands make it impossible to maintain any sort of phase coherency from one burst to the next. It was interesting to watch this on an oscilloscope.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6111/pseudorange-in-vhf-band-navigation-and-precision-phase-tracking, by BarsMonster - R2AYN, Dave Tweed N3AOA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
