# FM squelch SDR algorithm?

*Tags: software-defined-radio, fm, squelch · score 4*

## Question

What signal characteristics in an SDR receiver signal path should be evaluated or computed to determine whether the audio output should be squelched or not? What sort of computed result should be compared against a scalar squelch "knob" setting?

I assume that for FM signals, the software should look at some characteristic in the demodulated audio data stream rather than in the IQ data stream for this determination. Is this correct?

(I am looking for algorithms, not any pre-coded solutions or circuits, as my goal is to write my SDR app in 100% Swift 3.)

## Accepted answer (score 5, by Kevin Reid AG6YO)

1.

The simplest squelch, applicable to almost all modes, and the one provided by most amateur radios' “squelch knob” as far as I've experienced, is power squelch: measure the signal power (in SDR, $I^2 + Q^2$), average over some short time interval, and compare against a threshold. This is done *before* the demodulator as the demodulator removes amplitude/power information.

The disadvantage of this technique is that the needed squelch setting varies with conditions: it must be higher than the noise floor (which varies depending on frequency and local conditions, yet lower than the minimum (allowing for fading/picket-fencing) carrier power of the expected signal.

2.

According to Wikipedia (and I think I've heard about this before from another source), there is a FM-specific technique for squelch:

A typical FM two-way radio carrier squelch circuit is noise operated. It takes out the voice components of the receive audio by passing the detected audio through a high-pass filter. A typical filter might pass frequencies over 4,000 Hz (4 kHz). The squelch control adjusts the gain of an amplifier which varies the level of noise coming out of the filter. The audio output of the filter and amplifier is rectified and produces a DC voltage when noise is present. The presence of continuous noise on an idle channel creates a DC voltage which turns the receiver audio off.

That is, this technique operates after the demodulator and simply looks for the high-audio-frequency noise which results from the absence of a consistent carrier, making the assumption that the expected FM signal will have different frequency content.

In software, this would consist of a high-pass filter → an envelope detector → averaging and comparator to control squelch.

This technique should operate equally well no matter what the RF environment. If it requires any “knob” at all, that would be the threshold for deciding when the noise is too much, which can probably be set generously high, but if not, it still depends only on the *audio* characteristics of the transmitted signals and not the RF characteristics.

3.

A transmitter may encode information in the signal to allow precise squelch. This is common on FM amateur radio repeaters. The most commonly used method is CTCSS (a.k.a. PL) in which a so-called “subaudible” audio tone is added to the signal. The receiver mutes when the tone is absent.

Because different tones can be used, this allows ignoring signals from other transmitters, provided that the intended transmission is stronger than the other (e.g. two repeaters with all their users significantly nearer to one than the other).

4.

It seems to me that there ought to be some technique which operates on the signal *before* demodulation to detect whether it contains more or less a single dominant frequency (as expected for a FM signal) as opposed to a “flat” spectrum of white noise (as expected for no signal), without depending on an assumption about the absolute level of the noise floor. But I am not familiar with any specific designs or how to implement them.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7231/fm-squelch-sdr-algorithm, by hotpaw2, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
