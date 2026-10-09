# Up converted audio transmission

*Tags: modes, ssb · score 3*

## Question

I was thinking about all the different modulation methods and something came to my head. After seeing up converters that convert HF to VHF for SDR (software defined radio) dongles to be able to listen, I thought, "why not use up converted audio?"

- With appropriate filters to take out the highs and lows, it would only take up 4000 hertz max according to the telephone standards. That's less than AM!
- Simple receive, just down convert until its at the AF band.
- Better chance Aliens will be able to figure it out because it is just up-converted RAW audio. (Kinda joking with that one)
- And if nothing else, for example: bad spectrum efficiency, hard to pick up with any noise, etc., I certainly want to try it just for fun!

So would it work out at all, and if so how well?

## Answer (score 4, by Kevin Reid AG6YO)

Yes, this is a workable modulation. In fact, it's used all the time on HF; what you have described is *precisely* single-sideband (SSB) modulation.

The usual choice of filtering is for an occupied bandwidth of 3 kHz rather than 4 kHz, but that's just a parameter; the principle is the same.

The reason it's called single sideband is that if you use the simplest possible analog electronics to perform the upconversion (*mixing*), the transmission has two redundant sidebands above and below the carrier frequency (*double sideband*), rather than just one; the lower sideband also has the audio signal, but mirrored in frequency. This is wasteful of power and bandwidth, so single sideband is preferred, but significantly more complex to implement in analog electronics. (In a SDR, you've in a sense already paid the complexity cost in the generic hardware; the DSP to demodulate SSB is just as simple as that for AM.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2045/up-converted-audio-transmission, by Skyler 440, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
