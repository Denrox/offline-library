# Identifying signals in the satellite exclusive band

*Tags: satellites, signal-identification · score 6*

## Question

I have just started playing with SDR so I downloaded the relevant amateur band plan for my location, the UK. Tuning around I found things like POCSAG/FLEX pagers as expected and amateur radio (e.g. FM repeaters) at frequencies matching the band plan.

However I also found some signals just above 145.8Mhz, which I noticed from the band plan is reserved in the UK:

145.806-146.000, 12 kHz, All Modes - Satellite exclusive

I am using an Ettus SDR and a Comet SMA703 antenna, which is designed for 144/400/1200Mhz. However, with this tiny antenna I was not expecting to receive anything from space, especially indoors.

An example of the signal is shown below:

There are a few more similar signals just a little higher up:

Some seem to be a fixed tone, some sound like they might be morse code when using the CW-U mode in gqrx.

I have been looking for around 30 minutes and none have shifted in frequency or disappeared. I had a look at a satellite list and used WXtrack to see what was overhead, but nothing seemed likely.

Can anybody tell me what these signals are likely to be?

## Accepted answer (score 9, by Phil Frost - W8II)

I'm guessing many those signals are just noise. A fixed tone carries no information, so there would be no reason for a satellite (or anything else) to transmit it intentionally.

The noise could be from an oscillator in some nearby electronics, or even from within the receiver itself. The noise may not even be at the frequency it appears in the waterfall: nonlinearities and intermodulation can make signals appear at frequencies where they actually are not. Sometimes you can identify these spurious signals by changing the LO frequency of your receiver and noticing how the signals move. For some, you may see them move by something other than the change in the LO. For example, if you tune the LO down by 100Hz, the signal may move by 300Hz.

## Answer (score 2, by Rich)

LED and CFL lights are a known nuisance to hams. It could possibly be one or some equally non-EMC conscious electronics.

http://www.ukqrm.org.uk/lighting.php

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2458/identifying-signals-in-the-satellite-exclusive-band, by David, Phil Frost - W8II, Rich. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
