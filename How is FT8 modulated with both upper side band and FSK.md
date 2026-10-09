# How is FT8 modulated with both upper side band and FSK?

*Tags: frequency, modes, ft8 · score 6*

## Question

This Wiki shows FT8 mode is USB and its modulation is FSK.

I don't get the difference between mode and modulation, I thought they are the same thing? Aren't signals modulated in a single method, transmitted and then demodulation with a receiver with the same method? Say a radio station modulates a sound signal with AM or FM but it doesn't modulate a signal with both AM and FM, that doesn't make sense!

So how can FT8 be both USB and FSK at the same time?

## Accepted answer (score 11, by hobbs - KC2G)

Remember that, theoretically speaking, a USB transmitter just takes a signal, shifts it up in frequency, and amplifies it. That means that if you take a 50Hz wide 8FSK signal centered at 1500 Hz, and you feed it into a USB transmitter with a dial frequency of 14.074 MHz with all of its voice processing and such turned off, what you get is a 50Hz wide 8FSK signal centered at 14,075,500Hz. And that's all that's happening here.

FT8 is FSK on the air, and it's FSK between the computer and the radio. Just one is at radio frequencies, and one is at audio frequencies, and a radio set to "USB" turns one into the other. A radio set to "LSB" would also (almost) work, except that all of the FSK shifts would come out backwards, which prevents it from decoding unless everyone else also uses LSB.

HF packet works exactly the same way — a TNC or PC generates a 300-baud FSK signal at a frequency pair of, say, 1600 and 1800 Hz, which is then modulated up to (e.g.) 10,149,200 and 10,149,400 Hz by a radio in USB mode with a dial frequency of 10.1478 MHz.

Some small dedicated transmitters actually do FT8 by directly adjusting the frequency of an RF synthesizer, which is "classical" FSK — although it's more commonly done for WSPR or FSK-CW than FT8.

The QRP Labs QDX is a fun case because it *also* transmits FSK modes by adjusting a frequency synthesizer, except it decides what frequency to use by "listening" to the audio coming into its sound card and picking out the dominant frequency. So it's a radio that interfaces to a computer in the same way as a USB transmitter, but it's *only* suitable for FSK modes because it can only output a single frequency at once, at a fixed amplitude.

## Answer (score 8, by hotpaw2)

FT8 is just FSK.

However, most legacy transceivers don't support direct digital to FSK modulation (and FSK to digital), but do support SSB modulation and demodulation (from and to audio). So these radios can be used to send FSK signals by converting audio FSK via USB modulation to an RF FSK signal (offset above the SSB suppressed carrier in USB mode). And in USB mode, these radios can demodulate FSK RF signals into audio FSK. And these audio FSK signals that can then be encoded and modulated (or demodulated and decoded) from digital data by DSP software running on some compute capable device (a PC typically).

So using USB mode is just an (obsolete?) implementation detail that is only part of an encoding/decoding process. Some newer SDR transmitters (and QRP transceiver kits) can directly synthesize an FSK RF signal from digital data, and not involve any SSB signal modulation at all.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21524/how-is-ft8-modulated-with-both-upper-side-band-and-fsk, by Dan, hobbs - KC2G, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
