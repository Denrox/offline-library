# Is this simple description of SSB correct?

*Tags: receiver, ssb · score 4*

## Question

I was recently asked to explain why a "carrier injection oscillator", or CIO is needed in an SSB receiver but not in a transmitter. This is the explanation I gave, and I would be grateful for comments on its validity.

I find the usual diagrams confusing, and a verbal explanation better so here is a basically correct, but very simplified explanation. An SSB transmission is derived from an AM signal within the transmitter, which (AM) is produced by mixing the audio with the carrier. If the audio is a single tone, say 1 kHz, and the carrier is 1 MHz, we get the carrier 1 Mhz and the mixer products, 1 Mhz -1kHz and 1MHz + 1kHz, or 1.000, 0.999 and 1.001 Mhz, all transmitted and received. An SSB transmitter does the same but with a filter that removes all RF frequencies except just those of one sideband, so we may get just 1.001 MHz, the upper sideband, transmitted. To get the original signal back the original carrier, 1 MHz is mixed with this, and among the multitude of mixer products we pick out the three we want, and we have the same as the original AM. "1 MHz is mixed with this" is what is meant by "carrier injection", and it needs an oscillator, a CIO, to produce it. Note the the CIO is necessary in the receiver only, not in the transmitter.

ANSWERED

Thanks to the answer from Kevin Reid, I have amended the text, and this is now my explanation. I have tried to avoid too much detail:

I was recently asked to explain why a "carrier injection oscillator", or CIO is needed in an SSB receiver but apparently not in an SSB transmitter. This is my explanation.

I find the usual diagrams confusing, and a verbal explanation easier to follow, so here is a basically correct, but very simplified explanation.

In fact, for SSB, both the receiver and the transmitter require RF oscillators. They may be called different things in the two cases, but they are playing essentially the same role: defining the carrier frequency.

In an AM transmitter the signal is produced by mixing the audio, from some external source such as a microphone, with a carrier which is produced by an RF oscillator within the transmitter. From the mixer, if the audio is a single tone, say 1 kHz, and the carrier is 1 MHz, we get the carrier 1 Mhz and the mixer products, 1 Mhz -1kHz and 1MHz + 1kHz, or 1.000, 0.999 and 1.001 Mhz: all these are transmitted and received. The detector stage of the receiver removes the RF components to leave the audio signal.

An SSB transmission is derived from an AM signal within the transmitter, with an additional filter that removes all RF frequencies except just those of one sideband, so, in the case cited, we may get just 1.001 MHz, the upper sideband, transmitted. To get the original signal back in the receiver the original carrier, 1 MHz, is mixed with this, and among the multitude of mixer products we pick out the three we want, and we have the same as the original AM for the detector stage. "1 MHz is mixed with this" is what is meant by "carrier injection", and it needs an oscillator, a CIO, to produce it. Note that the oscillator is called the CIO only in the receiver: in a transmitter it is called the RF oscillator, or VFO if the transmitter is tuneable.

## Accepted answer (score 5, by Kevin Reid AG6YO)

Your description is not wrong, but your premise is. In the system you describe, both the receiver and the transmitter require oscillators at 1 MHz. They may be called different things in the two cases, but they are playing essentially the same role: *defining the carrier frequency*.


In the transmitter, the oscillator's frequency is *added* (in the frequency domain) to the audio signal, producing an RF signal.


In the receiver, the oscillator's frequency is *subtracted* from the received RF signal, producing an audio signal.

In practice, SSB receivers and transmitters both have more than one oscillator — one *variable-frequency oscillator* (VFO) plus one or more fixed *intermediate frequency* (IF) oscillators. This is not fundamental to the modulation, but rather a technique to make implementing the required filtering more practical.

If you are receiving AM rather than SSB you can avoid having any oscillator in the receiver at all, in favor of a variable filter, as used in crystal or TRF receivers. However, this is the opposite of your claim. (It is possible because the carrier present in the transmitted signal essentially replaces the function of the local oscillator in the receiver.)

## Answer (score 2, by Brian K1LI)

Elmering a new ham on this subject suggests to me that you might want to tweak your description. Specifically, an SSB signal is not typically derived from an AM signal.

The simplest form of amplitude modulation is "on-off keying" - simply turning a carrier wave on and off. The spectrum of such a signal includes the carrier plus sidebands at the keying rate. We hams refer to this as "CW."

If you smoothly change the amplitude of the carrier wave, rather than just switching it on and off, you get a similar but more complex result because *varying* the carrier amplitude is more complex than simply turning it on and off. Still, the result comprises spectra at the frequency of the carrier and sidebands that correspond to the modulating signal. This is "AM."

The type of SSB generation you describe is referred to as the "filter" method. It does not begin by generating an AM signal. Instead, it begins by *multiplying* together the carrier wave and the modulating audio signal in a circuit called a balanced modulator. The resulting spectra comprise *only* the sidebands - the carrier is cancelled in the multiplication. The sideband filter only has to attenuate the unwanted sideband.

An SSB/CW receiver uses a "product detector" to recover the sideband information, whether that information is from discrete on-off keying or from continuous modulation. (Note how the word "product" reminds us of "multiplication.") The product detector performs the same function as the balanced modulator. but instead of producing RF from a carrier and baseband inputs, it produces baseband output by multiplying RF input with a carrier.

As an aside, a "balanced mixer" can be used as a balanced modulator. The multiplication process is the same.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5387/is-this-simple-description-of-ssb-correct, by Harry Weston, Kevin Reid AG6YO, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
