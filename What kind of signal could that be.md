# What kind of signal could that be?

*Tags: modes, signal-identification, hackrf · score 5*

## Question

When running a spectrum analyzer, I noticed that a cheap chinese plane remote is outputting on a frequency of 2448MHz. When I recorded that frequency using hackrf_transfer and opened the file in audacity, I got the data from the screenshot.

Could anyone help me identify the modulation/type of signal?

I suspected FM, but failed to reconstruct the original waveform from the Q/I data...

## Answer (score 2, by Marcus Müller)

If you look at the regions without "jumps", it looks like sine waves 90° out of phase: that's a residual frequency error!

Because we don't have your raw data, we can't try that, but I suspect if you correct the remaining frequency error, these regions become constants.

Since the amplitude of the sine waves are constant, and if they are actually 90° out of phase, their magnitude when understand as complex sinusoid is a constant, as well. Since frequency shifts doesn't change magnitude of a signal, the complex constants you get after frequency correction would all have the same magnitude as well – leaving only phase to carry information.

Now, the transitions between these constant-phase regions seem pretty extreme. Maybe you didn't sample with sufficient bandwidth, or your receiver is numerically clipping/wrapping around, or maybe the pulse shape is just really bad, or maybe the information is actually in the transitions or their position. So, while it is almost certainly some form of FSK, it might well be a differential FSK, or a FSK-pulse-position modulation or something else rather strange.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23697/what-kind-of-signal-could-that-be, by Daniel D., Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
