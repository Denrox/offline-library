# Zigzag line on CB band

*Tags: signal-identification · score 3*

## Question

I'm seeing this strange signal on the CB band around 27 MHz, at a glance it looks similar to NFM modulation, but it's just noise when tuned to. It's transmitted about every minute.

My setup is RTL-SDR with Nooelec NeSDR and a "noise-cancelling passive loop" antenna.

Any idea what could be the source?

At first I thought someone is messing with their frequency knob, but they would have gotten bored of that after a couple hours.

I have an I/Q sample from gqrx, but it's too large to attach here.

## Accepted answer (score 4, by Scott Earle)

This reminds me of the "bad old days" of poorly-aligned or poorly-designed transmitters (usually CBs in the early 1980s in the UK), where the transmitter would start the PA before the PLL had locked up, and so some rigs were notorious for making a kind of "farting noise" when their mic was keyed. This was emphasised by the fact that in the 1980s UK, CB was all FM only, and so changes in frequency had more of an effect on the audio.

The PLL (phase-locked loop) is the part of the radio circuitry responsible for generating the carrier frequency, and it generally works by a system of frequency dividers and a feedback loop, to generate channelised frequencies. Keying the microphone causes the PLL to generate the transmit frequency (which is different to the frequency it generates during receive, because of the IF offset). This starts the phase-lock sequence, and the PLL will start high (or low, but in your case it looks like it always starts high), and then will reduce the frequency until it has overcompensated and will start increasing the frequency until it has overcompensated, then reduce the frequency, etc. until it has locked on to the required frequency.

What should happen is that the circuitry should not engage the PA until the PLL has locked (and PLL chips have an output to inform when this has happened), which means that all this happens internally to the transmitter, and then it turns on the PA to start transmitting the signal with some power. But some poorly-designed radios start the PA as soon as the mic is keyed, presumably to simplify (and reduce the cost of) the circuitry. This usually results in some out-of-band emissions (especially if the channel being used is at the high-end of the band).

Sidenote: I always thought the frequency selection was particularly smart in these radios, and allowed for much cheaper designs to be used. The first IF was chosen to be 10.695MHz because FM broadcast receivers traditionally used a 10.7MHz IF and filters for those were everywhere, and hence cheap. But they chose 10.695MHz and not 10.7MHz because you could use a 10.240MHz crystal to both mix the first IF down to 455kHz (10.695 - 10.240 = 0.455), and to generate the 10kHz reference needed for the 10kHz channel generation, by simply dividing by 2 repeatedly (10.240Mhz = 10kHz x 1,024 - which is 2 to the power of ten). Very neat indeed. The second IF was 455kHz because AM radios traditionally used 455kHz as their (only) IF, and filters (plus coils, etc.) for a 455kHz IF were extremely cheap.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20413/zigzag-line-on-cb-band, by MightyPork, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
