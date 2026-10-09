# Can I capture stereo IQ signals from WebSDR?

*Tags: software-defined-radio · score 3*

## Question

When I set my sound device to record from the monitor/loopback source, I can capture the signal from WebSDR in my browser in an application like Audacity.

Looking at the captured signal more closely reveals that both the left and right channels of the stereo signal are identical. As a result, I cannot demodulate properly from the captured signals.

Is this a limitation of WebSDR? I can capture stereo audio correctly from other websites (e.g. YouTube).

## Accepted answer (score 3, by Kevin Reid AG6YO)

You could call it a limitation of WebSDR, but WebSDR intends to give you *demodulated* audio, audio for *listening* to, which an IQ signal is not suitable for (even if the signal is audio-like as in SSB and CW, the 90° phase shift of the quadrature component will make for unpleasant listening).

That said, you **can** take a SSB signal you've captured and turn it into an IQ signal. This does not add any useful bandwidth that wasn't present in the original, of course, but it could help if it's what the demodulator you want to use needs.

The Hilbert transform takes a signal and creates a 90° phase shifted version; if you replace one of the stereo channels with the transformed signal, then you have an IQ signal — specifically an *analytic* signal, one whose frequency content is entirely in the positive half of the spectrum. If you need it 'baseband' (centered around 0 Hz) then you frequency shift it downward after the transform.

Both of these steps should be doable using any DSP tools suitable for SDR; here's how you might set it up in GNU Radio. (The value in the rotator block is $-\pi/2$, a frequency shift of one quarter of the sampling rate.)

However, **none of this is actually necessary** if the demodulator you are trying to use afterward either knows how to take SSB input (in which case your recording is just fine the way it is) or can be told to look for the signal it wants at an arbitrary frequency offset.

This is because the spectrum of any 1-channel signal is just symmetric about zero. You can treat it as if it were IQ and as long as your next step is to apply a bandpass filter within one of the mirrored halves, there's no difference.

On the other hand, if your demodulator expects the recording to contain *only* the intended signal (plus noise), rather than apply a channel filter itself, then you do need to use the transformations I described above.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14912/can-i-capture-stereo-iq-signals-from-websdr, by Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
