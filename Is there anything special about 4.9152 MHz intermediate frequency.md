# Is there anything special about 4.9152 MHz intermediate frequency?

*Tags: diy, qrp, superheterodyne · score 8*

## Question

I noticed that there are several QRP transceivers that use 4.9152 MHz intermediate frequency. For instance, John Dillon, WA3RNC uses it in Penntek TR-25, TR-35 and TR-45 transceivers. Also a very close frequency (4.914 MHz) is used in Elecraft KX1.

Does anyone know what is so special about this particular frequency? Does this has something to do with avoiding spurious signals? Or this frequency just happened to be convenient in terms of availability / price of the crystals, filter impedance / bandwidth, the fact that it's easier to get more gain on lower frequencies (comparing to 9 Mhz or 12 Mhz), etc? Or maybe there is some other reason?

## Accepted answer (score 4, by ha3flt)

There are not so many frequencies you can find quartzes for in large quantities and cheap and with specific parameters. If you have a lot of a value that comes in handy when you want to build a ladder filter for IF stages because you need a lot of them to find matching ones.

4.9152 MHz is so common because a lot of "important" frequencies used in the microcontroller and DSP world can be produced by simple divisions. One example is to generate clocks for microcontrollers those can divide UART speeds from them with the smallest possible error, deviation (max. 38400 bps in this case). https://en.wikipedia.org/wiki/Crystal_oscillator_frequencies

This ~5 MHz value is out of ham bands (and most of the commercial SW bands), so you can used it for them as IF. And as you already wrote it, a lower IF frequency (not 9 or 10 MHz or above) can be handled easier, by cheaper semiconductors and simpler design, and especially by beginners. And such values like 4.9152 MHz might be useful in DSP for radios, so if you take everything into account, it might be reasonable to choose this freq. as a home standard.

But these are not intended to be stronger points than those in other answers, I just tried to find some reasons, too.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21541/is-there-anything-special-about-4-9152-mhz-intermediate-frequency, by Aleksander Alekseev - R2AUK, ha3flt. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
