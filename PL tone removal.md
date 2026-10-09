# PL tone removal?

*Tags: tone-squelch · score 8*

## Question

How are PL tones (CTSS, et.al.) typically removed from the audio of received VHF FM repeater signals?

Is it done with a fixed high-pass filter? Or a notch, when using a transceiver with the PL tone configured correctly? Or dynamically, by assuming any constant low tone detected is hum to be removed by an auto-adaptive notch?

Or is it sometimes not removed by filtering because the tiny speakers on handheld receivers don't have sufficient low frequency response?

## Accepted answer (score 8, by Walter Underwood K6WRU)

I would expect some low-frequency roll-off in the amp and the speaker. You could check by putting headphones on the speaker output.

Wikipedia says that a 300 Hz cutoff high-pass filter is common.

https://en.wikipedia.org/wiki/Continuous_Tone-Coded_Squelch_System

Also, the CTSS tone is injected at a lower level than the voice content, usually 15% of full deviation. That is about 8 dB below full modulation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13019/pl-tone-removal, by hotpaw2, Walter Underwood K6WRU. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
