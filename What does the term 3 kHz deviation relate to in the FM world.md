# What does the term 3 kHz deviation relate to in the FM world?

*Tags: theory, fm · score 6*

## Question

I am confused when someone says "your audio levels are set right and has good deviation at 3 kHz" when talking about wide-band 25 kHz FM signals.

First confusion: Why are audio levels measured in kHz? I find it very misleading when you are measuring amplitude values.

Second confusion: I understand that FM works by deviating from the carrier frequency and will accept a frequency term for amplitude. Why is it 3 kHz though, not 25 kHz or 12.5 kHz for narrow band FM? I would assume perfect audio is when the transmitter is deviating the entire 25 kHz.

What is one measuring when talking about audio deviation? Why 3 kHz?

## Answer (score 7, by Kevin Reid AG6YO)

FM works by varying the frequency of the signal around the nominal carrier frequency. Because the frequency is varying, the signal is not a pure sine wave. Therefore, it necessarily has some energy in sidebands as well as the instantaneous frequency. The higher the audio frequency, the more the signal deviates from a sine wave, so the more energy ends up in the sidebands instead of at the instantaneous frequency.

If one works out the math, one finds that a FM signal has an infinite bandwidth (sidebands of arbitrarily high frequencies), but the energy drops off quickly as we look farther away, so in practice they are negligible (and may be filtered out).

3 kHz is the *deviation* of the signal — the amount the instantaneous frequency differs from the carrier frequency. Because there are sidebands, the occupied bandwidth is larger than the deviation.

If you have access to a software-defined radio or panadapter, try tuning it to the wideband FM broadcast frequencies. You'll see that even though the bandwidth of the signal is big enough to easily get a high-resolution look, it doesn't look like a single instantaneous frequency but a wide hump. These are the rapidly varying FM sidebands. In particular, when the station is quieter you may be able to distinguish a set of three or more peaks moving in concert — these are the result of the inaudible 19 kHz stereo-encoding “pilot” tone which is always present for a stereo transmitter.

“Why are audio levels measured in kHz?” Because FM maps the audio signal to frequency changes, so the only absolute measurement of the level *on the air* is the change in frequency. Any other way of measuring audio — sound pressure level, AF voltage — is inapplicable because those depend on the characteristics of the transmitter or receiver.

## Answer (score 3, by AndrejaKo)

Since the 12,5 kHz and 25 kHz were mentioned in the question, I think it might be a good idea to have an answer mentioning the Carson's rule.

The rule is used for approximate calculation of FM bandwidth, which is the kHz number referred to in 12,5 and 25.

$$ B=2(f_{dev}+f_{mod_{max}})$$

So that means that our bandwidth doesn't just depend on our deviation, but also on the highest modulating frequency.

Usually, you'll have some common combinations of maximum modulating frequency and deviation. For example, in 5 kHz systems, it's not uncommon to have a 3 kHz set as maximum audio frequency. From my interpretation of the quote in the question, I'd say that this are the 3 kHz it's talking about.

If we do the calculation, we get following: $B=2(5 \mbox{ }kHz +3 \mbox{ } kHz)=16 \mbox{kHz}$, giving us some space for filter slope and the power outside of the Carson's bandwidth, if we're using the 25 kHz step. If we do calculation for so-called narrow-band, we'd get something like this:$B=2(2,5 \mbox{ }kHz + 2,5 \mbox{ }kHz)=10 \mbox{ }kHz$, giving us extra 2,5 kHz space for imperfections.

Here we actually have some other considerations as well. Both transmitter and receiver need to have same audio bandwidth and same deviation in order for the system to work properly. If your deviation is too high, you run the risk of going outside of channel bandwidth and sounding over-modulated. If your deviation is too low, then you'll sound very quiet on reception. Why? Because your spectral lines that represent the tone will be too close together.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5024/what-does-the-term-3-khz-deviation-relate-to-in-the-fm-world, by Skyler 440, Kevin Reid AG6YO, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
