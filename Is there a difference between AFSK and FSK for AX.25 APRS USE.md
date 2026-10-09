# Is there a difference between AFSK and FSK for AX.25/APRS USE?

*Tags: aprs, modem, ax.25 · score 7*

## Question

APRS uses the AX.25 protocol which assumes the Bell 202 AFSK modulation scheme to generate the actual radio signal. Is there any reason the same signal can't be generated directly with FSK without going through the audio frequencies?

My reading suggests that the advantage of AFSK is that the audio signal can be fed to any radio mike input. But if we ignore that, and assume a transmitter where the frequency can be controlled directly, can this be done? Would the signal be understandable to other APRS stations?

## Accepted answer (score 6, by Kevin Reid AG6YO)

My reading suggests that the advantage of AFSK is that the audio signal can be fed to any radio mike input. But if we ignore that, and assume a transmitter where the frequency can be controlled directly, can this be done?

Yes, and it is sometimes done for APRS on HF. (This is still "to the mike input", but the radio is doing SSB instead of FM.)

From the perspective of theory of communications, this is not much different than RTTY. (However, it would be better to use a more efficient digital modulation and error-correction coding.)

Would the signal be understandable to other APRS stations?

It would not be understandable to AFSK-on-FM APRS stations, because it is a different modulation.

Consider just one of the two tones — an unchanging tone going into a FM transmitter produces a varying frequency output. On the other end, If you attempt to receive a FSK signal with a FM receiver, you will get theoretically a square wave and likely in practice alternating polarity pulses (a high-pass-filtered square wave).

Can you decode that? Yes, but a standard TNC can't because it expects to do its own demodulation. (Insofar as FM and FSK are the same thing, a conventional APRS transmission is **modulated twice** between the bit-stream and the radio wave.)

## Answer (score 5, by David Rowe)

AFSK sent over a FM radio is very different to FSK, as explained in my blog post FM over FSK:

FSK over FM is not FSK when you look at the over the air waveform. The spectrum is no longer two tones bouncing back and forth.

Assuming you have a FSK modulator that takes 0's and 1's as input, then you will not be able to generate the same signal as AFSK over FM. If you have a FM transmitter that modulates the RF frequency based on the input signal level, then you could drive that from you software FSK modulator and generate AFSK over FM.

If you have a generalised SSB style up-converter with enough bandwidth (like a HackRF), you could generate the AFSK signal in software, and use that to modulate a software based FM modulator, and up-convert that entire signal to RF.

## Answer (score 2, by Phil Frost - W8II)

FSK is a modulation where the instantaneous frequency corresponds to a binary baseband signal. Given:

- $x_m(t)$ is the baseband signal, perhaps a binary square wave taking values of -1 and 1,
- $f_c$ is the carrier frequency
- $f_\Delta$ is the deviation, roughly speaking the spacing between tones

then the modulated signal $y(t)$ as a function of time is:

$$ y(t)=\cos \left( 2\pi f_{c}t + 2\pi f_{\Delta }\int _{0}^{t}x_{m}(\tau )d\tau\right ) $$

Not by accident, this is exactly the same definition for analog FM. The only difference being the baseband signal $x_m(t)$ is analog, instead of digital. That is, FM and FSK are the same modulation, just with different baseband signals.

For AFSK, the same equation applies, only the carrier frequency is something in the audio range. Then, it's fed into an FM modulator, which applies the modulation a second time. Even without doing the math you can imagine applying this modulation function a second time results in a very different transmission.

On the other hand, a USB transmitter does nothing to the modulation besides shift it up in frequency. Or in terms of the equation above, it effectively changes $f_c$. Thus, AFSK over USB is actually just FSK. This is what makes USB transceivers useful for implementing novel modulations like PSK31, JT65, etc.

It's also possible to generate FSK with an FM transmitter by feeding the binary baseband signal into the audio input of an FM transmitter. It requires calibrating the audio gain, because "too loud" would mean too much deviation, or too wide a tone spacing. As an example, some of the MMDVM setups use this to modulate and demodulate DMR with an analog FM transceiver.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9567/is-there-a-difference-between-afsk-and-fsk-for-ax-25-aprs-use, by jgalak, Kevin Reid AG6YO, David Rowe, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
