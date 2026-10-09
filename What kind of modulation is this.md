# What kind of modulation is this?

*Tags: software-defined-radio, gnuradio · score 6*

## Question

I was able to demodulate a signal I've received in gnuradio. Here you can see my flowgraph:

But now I would like to be able to send data as well. But how should I modulate my data? As you can see I've demodulated with Quadrature Demod -> Hilbert -> Complex to Mag. To my understanding the reversing would be AM Mod -> something -> GFSK Mod. Is that correct? And if so what could I use as a reverse Hilbert filter?

Edit: Here's the wave I get after the Complex to Mag:

## Answer (score 11, by Kevin Reid AG6YO)

The Hilbert block in GNU Radio creates an analytic signal from a real-valued one by applying the Hilbert transform to create the Q (imaginary, quadrature) component.

The Complex to Mag block then discards the phase information in that analytic signal, keeping only the amplitude. Generally speaking, this is AM demodulation. This further agrees with your Add Const later on which is subtracting the offset resulting from the carrier.

Since you're then taking the output of that as the digital signal, it would be called *amplitude shift keying* (ASK) rather than AM. If the lower amplitude is in fact zero (I can't tell from the flow graph), then you have *on-off keying* (OOK).

Assuming it's OOK, the corresponding modulator would be a kHz signal source multiplied by your (repeated to have more than one sample-per-symbol) data bits.

This would then go into the opposite of a Quadrature Demod, which is a VCO. (No conversions to complex are needed.)

This combination of OOK with an audio-frequency carrier put into another modulator is commonly known as *MCW* (modulated continuous wave), though the term is more often used in the context of Morse code signals than other digital signals.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5578/what-kind-of-modulation-is-this, by Thanathan, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
