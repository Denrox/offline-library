# How do I use a signal generator + oscilloscope to measure feeder length?

*Tags: antenna, antenna-theory, feed-line · score 3*

## Question

I could relatively easily take the feeder down and use a tape measure but it’s more of a challenge to learn how to measure the length using my oscilloscope -Red Pitaya - but I have to admit I have no idea how to go about it.

## Answer (score 3, by hotpaw2)

A quarter wavelength of coax (shortened by its velocity factor) is a notch filter if the far end is left open.

So leave the far end open; and try feeding the coax from a frequency generator voltage source plus a series resistor at the near end; and sweep the frequency across a slightly wider range than is appropriate for an adjusted quarter wavelength to be your min to max estimate of your coax length. Use two scope probes on points before and after the series resistor, and look for the frequency causing the maximum drop in the ratio of waveform levels between the two scope inputs.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16318/how-do-i-use-a-signal-generator-oscilloscope-to-measure-feeder-length, by forestDM, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
