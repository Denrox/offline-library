# Is it possible to measure antenna trap with MFJ225 without help of PC?

*Tags: measurement, antenna-analyzer, trap · score 3*

## Question

I have MFJ225 antenna analyzer. I measure coax trap filters by connecting this analyzer to PC and using IG_miniVNA application. That works fine.

But, sometimes I need to make such measurements in portable where I do not have PC available.

A friend has MFJ259 and he uses grid dip coil adapter to successfully measure traps. I tried using his adapter but got no results - meaning no DIP at all.

## Answer (score 2, by Phil Frost - W8II)

You can put a one-turn loop on the analyzer and use that to couple into the trap. There will be a dip in SWR where the trap is resonant.

Here's a picture from the RigExpert manual:

Connect that single-turn loop as if it were an antenna, and do an SWR sweep. The notch is the resonant frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7587/is-it-possible-to-measure-antenna-trap-with-mfj225-without-help-of-pc, by Pedja YT9TP, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
