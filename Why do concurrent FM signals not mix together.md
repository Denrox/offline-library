# Why do concurrent FM signals not mix together?

*Tags: propagation, physics · score 14*

## Question

Generally when I hear two conflicting signals they do not mix together, but rather one dominates then the other. This phenomenon can be observed on FM broadcast station when driving out of range from one station into the range of another. During the 'in between phase' they generally do not mix but rather one dominates and they flip flop being the dominant signal. Why is this?

## Accepted answer (score 10, by Dan KD2EE)

I understand why you think it should mix - that's what happens with SSB, for example. The difference with FM is that in FM, at any instant, each station's signal is only at one frequency. If you slowed the signals down and watched through a spectrum analyzer, you could watch the two signals, and you'd see two peaks at constant amplitude, moving independently. The frequency (of the carrier) is modulated based on the audio signal amplitude, so that peak will move within the channel, but it's always one peak. Your receiver latches on to the stronger peak, and that's what it decodes.

On the other hand, in single sideband, you wouldn't ever see a single peak no matter how much you slowed the signal down. In single sideband, the amplitude of the carrier is being modulated - it isn't that the peak is moving, the peak is actually being mixed with (multiplied by) the audio amplitude, so all the peaks from the audio signal would appear on your spectrum analyzer. In this case, there's no distinction between audio components coming from one source vs another - you could separate the signals if you wanted to using directional antennas, but with a single receiver all you're going to see is the two signals superimposed.

## Answer (score 10, by Walter Underwood K6WRU)

This is called the "FM capture effect" and is mostly a characteristic of the demodulator design. Demodulators with a strong capture effect detect the zero crossings of the signal. The zero crossings are only slightly affected by mixing two signals until they are nearly equal amplitude. The steepness of the waveform at zero crossing means that the stronger signal dominates. It takes a larger interfering signal to change the slope enough that the zero crossing moves.

FM demodulators usually include an amplitude limiter to increase this effect. Unless the noise happens near the zero crossing in the signal, it is ignored. Effectively, the limiter increases the steepness of the zero crossing.

When two FM signals of a similar strength mix, we get the distinctive "doubling" sound heard on repeaters. This distorted signal is caused by the non-linear mixing from the limiter.

In an AM envelope detector, the detector is very sensitive to the mixed signals. Also, the signals are linearly combined, so our ears can often distinguish the two signals.

## Answer (score 2, by AA6YQ)

That's a property of FM demodulation known as the Capture Effect: when multiple signals are present, only the strongest is demodulated.

This does not occur with AM or SSB demodulation, where multiple signals can be simultaneously demodulated.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/337/why-do-concurrent-fm-signals-not-mix-together, by Dan, Dan KD2EE, Walter Underwood K6WRU, AA6YQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
