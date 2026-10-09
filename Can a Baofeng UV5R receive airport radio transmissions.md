# Can a Baofeng UV5R receive airport radio transmissions?

*Tags: baofeng · score 4*

## Question

I have tried programming approach frequencies into my baofeng and cannot hear any transmissions. Freq programming was done using a desktop computer connected to the radio to frequency 121.9MHZ. Nothing was heard, just standard background static. Here is the radio: https://www.amazon.com/Baofeng-Warranty-Dual-Band-Radio-Improved/dp/B00HX03AMA Baofeng UV5R v2

## Accepted answer (score 13, by Kevin Reid AG6YO)

As far as I've read, all Baofeng radios do FM only. The majority of aircraft communications uses AM, so whether or not it can be tuned there, you would not hear the audio, just approximate silence (quieter the stronger the signal).

This is because to a FM receiver's perspective, an AM signal is unmodulated (the frequency stays constant), and vice versa (in a FM signal the amplitude stays constant).

In some cases, the speech may be very faintly audible, due to imperfect circuits in both the transmitter (causing frequency variation in the transmitted signal) and the receiver (having unintended sensitivity to amplitude variations).

In the reverse case — attempting to receive a FM signal using an AM receiver — this can actually be used practically (improvised “slope detection”, tuning with an offset and allowing the frequency modulated signal to be converted by the edge of the receiver's filter to an amplitude-and-frequency modulate signal).

## Answer (score 6, by Marcus Müller)

From the amazon page you've linked to:

Frequency Range: 136-174 / 400-479.995 MHz.

So, no, you can't receive 121.9 MHz.

## Answer (score 4, by MPf)

It is far from being ideal, but it is possible. UV-5R can get below the specified range (google Chirp) and although it is an FM radio, it can (under some conditions) receive an AM modulated audio signal. The quality is bad, but if the signal is strong, it is audible. I've tested this on ATIS from a nearby airport (~131 MHz). What also helps is to set WFM and tune slightly off the carrier frequency (in my case 6 kHz up was the sweet spot). Seems to be working approx. down to 126 MHz. Although the frequency can be set even lower, it doesn't seem to receive anything (tried with TinySA).

**!Never ever transmit on that band (rather even disable the TX capability in VHF band in the SW)!**

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6995/can-a-baofeng-uv5r-receive-airport-radio-transmissions, by jason97m, Kevin Reid AG6YO, Marcus Müller, MPf. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
