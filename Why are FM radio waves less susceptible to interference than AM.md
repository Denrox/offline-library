# Why are FM radio waves less susceptible to interference than AM?

*Tags: fm, microwave, am · score 3*

## Question

When studying modulation of radio waves (or of most electromagnetic waves for that matter) I came across this question:

**Why are FM waves less susceptible to interference than AM waves?**

I know that in FM the frequency has been modulated to carry the signal by superimposing the signal wave to the carrier wave and for AM the amplitude has been varied by a similar process.

However, what I don't understand is why FM radio waves are less susceptible to interference.

Is it because when two waves interfere it is easier to change the amplitude as compared to the frequency, if so why?

## Accepted answer (score 4, by Marcus Müller)

The waves (to be correct: the *signals*) are exactly as suspectable to noise for both modulations!

What's different is the receiver:

As the name suggests, Amplitude Modulation (AM) works by taking the input (audio) signal, and using its strength, to modify the amplitude of your carrier wave. The AM receiver hence only has the amplitude of the received signal to recover the original audio.

In Frequency Modulation (FM), the input signal's amplitude is used to change the *frequency* of the carrier wave. The receiver then tries to detect the frequency changes, and reconstruct the original audio signal as the change in frequency observed.

The absolute strength of the received signal hence doesn't matter for FM, and is the only thing relevant for AM.

Now, noise as we usually look at it, is *additive*, meaning that it changes the receive signal amplitude. Hence, AM is especially badly suited to deal with noisy channels (a *channel* in signal theory is everything that happens to a signal between transmitter and receiver).

**Edit:** Your questions continue:

I see, and is there a particular reason why noise only seems to affect aplitude?

physics. Noise is "random" energy that changes the observed voltage with a positive or negative sign. It adds to the signal. Really, just simple addition of voltages.

By the way, as I said, this goes for **additive** noise. There's *other* types of noise, but luckily, we're technically able to avoid a lot of those, so you don't have to worry about these (much harder to compensate) types of noise.

If two waves of different frequency superimpose shouldn't the frequency of the resulting wave differ to that of the original one?

No. That doesn't happen. There's intermodulation in non-linear components, but that doesn't change the frequency, it merely creates new frequencies.

Now, if you have a strong interferer, your FM receiver might "lock" onto that instead of the station you actually want to listen to. But that's interference, not noise.

Also, if Noise power related to signal power (1/SNR) gets too high, your receiver might not be able to estimate the "instantaneous" frequency of the signal within the noise – then you get garbage out. But that implies a really bad reception.

Doesn't interference with noise

*Interference* and *Noise* are two different things. Please don't mix the terms. Interference is someone else interfering.

suggest superposition with waves of all kinds of frequencies?

No. Noise is a random process and as such doesn't necessarily have a frequency. Many types (but far from all types!) of noise we consider are modelled to be *white*, ie. statistically contain the same amount of energy at all frequencies (if you take the spectrum of a theoretical, inifinitely long observation of noise). But that doesn't mean that your instantaneous noise realization contains a specific set of frequencies. That's the difference between statistics and events: If you have a chance of $10^{-7}$ to win the lottery jackpot of 10 Million € every week, it doesn't mean that you'll get 1€ every week.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6312/why-are-fm-radio-waves-less-susceptible-to-interference-than-am, by MystMan, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
