# What does channel spacing look like in the time domain?

*Tags: bandwidth · score 4*

## Question

I'm trying to understand how radio works, and the concepts of AM/FM modulation are relatively clear to me. My next hurdle, however, is the following: How does differentiating between signals with different frequencies work? I can't picture the different channels/frequency bands in the time domain.

How should I look at this?

## Answer (score 5, by Phil Frost - W8II)

Easy enough to graph at wolframalpha.com:

This shows two signals: one at some frequency (blue), and another at 15 times that frequency (magenta). The brown line is the two added together.

If you took this brown signal and put it through a low-pass filter, you could recover the blue signal.

If you put it through a high-pass filter, you could recover the magenta signal.

Now, if you had many signals in here, separated by less than a factor of 15, it would be quite difficult to separate them by looking at the time domain signal. But this is why we don't think of this problem in the time domain: it's hard. Separating the signals in the frequency domain is easy.

## Answer (score 2, by hotpaw2)

Just picture (or graph) the sum of 2 sinewaves of very different frequencies.

In "real-life" RF, the bandwidth including modulation is so small, in relation to the carrier frequency, that a single modulated signal would look just like a plain sinewave when graphed. If the bandwidth of different channels don't overlap in the frequency domain, then, given enough time (or length of captured signal), a filter (analog or digital) can unmix several channels much more closely spaced in frequency (than in your graph) within a summed signal, even if your eye can't on a graph of a shorter segment.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1221/what-does-channel-spacing-look-like-in-the-time-domain, by Lg102, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
