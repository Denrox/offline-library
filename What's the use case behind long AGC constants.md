# What's the use case behind long AGC constants?

*Tags: receiver · score 4*

## Question

So my shortwave radio has adjustable AGC constant with settings between 0.1 s to 8 s.

I always find myself using the fastest AGC settings. Often, I experience 20-30 dB fades and if I use the slower AGC settings, what happens is that the station is too weak to be received until the AGC compensates.

On the other hand, I can't seem to figure out why or when would I want to use the slower AGC constant.

## Answer (score 8, by hobbs - KC2G)

CW is one reason. CW is on-off keying, so if the AGC reacts at a timescale similar to or shorter than the transitions of the signal, it will partially cancel the signal, making it "muddy" and more difficult to copy. 15wpm morse has a dit length of 0.08 seconds, making a dah or an inter-letter space around 0.24 seconds, so a fast 0.1s AGC will do it quite a bit of harm. This doesn't really explain the *very* long settings, but it does explain why an AGC constant of 1 second or so is useful.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10455/what-s-the-use-case-behind-long-agc-constants, by AndrejaKo, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
