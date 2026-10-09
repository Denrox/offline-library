# How to make ELF-ULF antenna myself?

*Tags: antenna, antenna-construction, antenna-modeling, lf, ulf · score 3*

## Question

I want to check the EM pulse between 3HZ-3kHZ with N9041B UXA Signal Analyzer,it seemed the only antenna I can use is Aaronia MagnoTRACKER,but the price is not affordable.

Then I plan to make ELF-ULF antenna myself,could you pls give me some thought to start with?

## Answer (score 2, by Jack0220)

If you need calibrated output then you probably won't be able to do it. That's why they are so expensive. It's like a \$20 SDR dongle versus a \$2,000 spectrum analyzer, with the most notable difference being that the spectrum analyzer is calibrated and tells you how much power is at each frequency. If you don't need calibrated output and just want to get a pretty good feel of what's there, then you should totally build your own antenna.

## Answer (score 2)

Years ago I used a simulation like this one for the same purpose.

The antenna you refer to is a tuned antenna, so it is not wideband. The antenna that I made is a wideband, really flat response (conversion from field strength to output voltage is frequency-independent).

Conclusion: the difficulty is the design of the low-noise amplifier. Depending on what you want to measure (strong signal or low-level signal in the noise) you can use a ferroceptor with many windings and loaded with 50 Ohm (not sensitive but doing the job) up to a large loop antenna with a transformer and a low-noise amplifier.

When you are used to a simulator with noise analysis: the basic model added can help you with a quick start. F Sessink

Forgot to say: dimensions in meters.....

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19995/how-to-make-elf-ulf-antenna-myself, by kittygirl, Jack0220. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
