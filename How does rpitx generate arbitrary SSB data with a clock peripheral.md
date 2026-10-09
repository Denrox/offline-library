# How does rpitx generate arbitrary SSB data with a clock peripheral?

*Tags: software-defined-radio, modes · score 7*

## Question

While it wasn't the first to do so, the rpitx software seems to be the most active and mature implementation of what its own comments call "a code fragment by PE1NNZ". The trick is explained in Guido's original Direct SSB Generation by frequency modulating a PLL article — but I don't quite understand how even the original works:

The PLL oscillator can be phase modulated by short manipulations of the configured frequency. Increasing the frequency temporarily and then restoring to its original frequency, will shift the phase upwards, while decreasing the frequency temporarily will decrease the phase of the signal. In this way the phase information for generating a SSB signal can be applied to the RaspberryPi PLL by means of frequency modulation.

This almost makes sense, but then he loses me a bit later:

After some experimenting, amplitude information can be completely rejected [… talks about generating an unsuppressed carrier …]

Now I suppose that if you have complete (and drastic) control over the phase of a sine wave, you can reproduce any other continuous signal simply by "walking" forward and backward along half a cycle of a sine wave — basically just slewing to whichever value between -1 and +1 is needed at the moment. Is that essentially what PE1NNZ's trick reduces down too, or is that a poor way to think about it?

Now even if I'm on the right track above, the rpitx implementation (source code) seemingly has an additional hurdle to overcome:

Rather than controlling the phase of a sine wave, my understanding is that with the Raspberry Pi "hack" the oscillator peripheral being used was meant to be a clock source. Wouldn't that then be a square wave generator then, i.e. generating (at least in its idealized form) only the peak -1 and +1 values and nothing in between?

Certainly I can see how discrete values could still generate an arbitrary waveform after filtering, for example pulse width or pulse-density modulation. But that does not seem to be the way either PE1NNZ or the rpitx contributors seem to be thinking about this — otherwise why not simply bit-bang any GPIO pin instead of using the clock peripheral!

Somehow rpitx is converting arbitrary I/Q data to RF signals through a huge range of frequencies (130 kHz to 750 MHz) — I'd love to understand the theory behind it! Could I use the same trick to turn an FM transceiver into an "All Mode" radio by injecting a suitably transformed input signal?

## Accepted answer (score 4, by Brian K1LI)

SSB comprises both amplitude and phase components. For any instant, plot the baseband signal's Q (quadrature) and I (in-phase) components on the y-axis and x-axis, respectively. The amplitude is the length of the vector from the origin to this (I,Q) point. The phase is the angle between this vector and the x-axis.

PE1NNZ modulates the amplitude of the clock driver by changing its drive strength. Only eight levels are available, corresponding to just 3 bits of audio resolution.

PE1NNZ is only able to modulate the frequency of the clock generator. Instantaneous frequency is the time derivative of instantaneous phase. PE1NNZ takes the time derivative of the phase by taking differences of successive phase calculations and changing the frequency of the clock generator accordingly.

## Answer (score 5, by Kevin Reid AG6YO)

This is an incomplete and theoretical answer as I haven't looked at rpitx in particular.

Rather than controlling the phase of a sine wave, my understanding is that with the Raspberry Pi "hack" the oscillator peripheral being used was meant to be a clock source. Wouldn't that then be a square wave generator then, i.e. generating (at least in its idealized form) only the peak -1 and +1 values and nothing in between?

Yes, but a square wave is a sine wave plus harmonics, and harmonics of a square wave of fundamental frequency $f$ are all at frequencies $2f$ or higher, so a receiver tuned to $f$ will not see the difference, and if it is low-pass filtered appropriately then there is no difference in the transmitted signal.

If this still sounds like a hack, or you wonder if modulation makes a difference, consider that it's perfectly possible to [make a RF mixer using a square wave and XOR](How%20does%20a%20switching%20mixer%20multiply%20the%20two%20signals.md).

why not simply bit-bang any GPIO pin instead of using the clock peripheral!

Again, I haven't looked at the hardware capabilities involved, but most likely, the peripheral can oscillate at a much higher rate than the Pi's processor can bit-bang the output, thus allowing for a higher carrier frequency. The software control need only operate at (perhaps some small multiple of) the sample rate of the modulating signal, not the RF rate.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6787/how-does-rpitx-generate-arbitrary-ssb-data-with-a-clock-peripheral, by natevw - AF7TB, Brian K1LI, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
