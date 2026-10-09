# Would it be possible for a software-defined FM receiver to demodulate two signals on the same frequency?

*Tags: software-defined-radio, receiver, fm · score 10*

## Question

When two FM signals are transmitted on the same (or about the same) center frequency, either you hear only one or you hear that noise I'm sure most of you have heard. Would it be possible for a software-defined receiver to track both signals and demodulate both of them, and play them at the same time? I'm thinking of a receiver that would make FM doubles sound like SSB doubles.

## Accepted answer (score 5, by hotpaw2)

Yes. A high sample rate (much higher than the audio frequencies modulated) SDR plus an FFT based demodulator could play both as a mix, but not always separate the two. You can clearly see the wiggles from two separate FM signals in a high sample rate high resolution waterfall, except where they overlap. You don’t have to be “captured” by only one frequency deviation track if you capture the entire possible bandwidth as IQ samples, and not just make the incorrect, but common, assumption by locking onto just one deviation track. The problem becomes tracking which signal is which when the original audio amplitudes, thus FM frequency deviation tracks, match, or criss-cross. But if you simultaneously tracked two sets of frequency deviations, both the high one and the low one, then demodulate both of those tracks, an STFT/FFT based SDR demodulator could play a mix of two FM signals in the same channel, assuming both are clearly above the noise floor.

As an alternative to a high res STFT/FFT 2D matrix for FM deviation tracking, a parametric best fit of two sinusoids to the captured IQ data stream might work even better, assuming only 2 FM signals of near constant RF amplitude in the same channel. The problem then converts to deciding when there are actually exactly 2 signals worth demodulating and mixing, and not just one signal plus a track of noise that should be ignored.

## Answer (score 4, by user10489)

In theory, it would be possible for an SDR to capture the primary signal, demodulate it, and subtract it from the total signal and extract the second signal from the remains and demodulate it.

Practically, this is a bit more difficult, and extracting the primary signal won't be perfect (even when you can hear the primary, it still gets noise from the secondary), and any defects in extracting the primary signal will significantly degrade the second signal. Also the likelihood of success of that heavily relies on your AGC and the bit depth and sensitivity of your ADC and how much of the secondary is left after subtracting the primary. If the AGC turns down the gain to the point where the secondary is under the noise floor of the ADC, it's just not going to work.

Also, if you are hearing it as buzzing, that means that the radio failed to capture either of the signals because they are too close in power. In this case, it is unlikely you'll have any luck separating them.

Having said that, who knows if someone could get extra clever and find new ways to separate the signals and improve the results. DSP leaves a lot of room for possibilities. Unfortuantely, while there has been some work on this, it is not a well studied problem and probably nobody has tried to commercially exploit it or is likely to try.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20870/would-it-be-possible-for-a-software-defined-fm-receiver-to-demodulate-two-sign, by Someone, hotpaw2, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
