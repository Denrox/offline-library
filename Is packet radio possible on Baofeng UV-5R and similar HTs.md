# Is packet radio possible on Baofeng UV-5R and similar HTs?

*Tags: vhf, uhf, packet, audio-interface · score 18*

## Question

I am curious to know if it is possible to do packet radio on VHF/UHF using the UV-5R... I have seen some invasive hardware hacks, but without modifying the radio itself (firmware, hardware) it's my understanding that you can only toggle send/receive using the 2.5mm/3.5mm TRS ports.

## Accepted answer (score 3, by user400344)

In the end I used 'amodem' ( see https://github.com/romanz/amodem ). After a few calibration steps, I could get decent I/O rates - considering the nature of the medium.

Compression of archives is necessary, and may be considered unethical. But the compression algorithms (e.g. 7zip, xz) are public, and anyone paying attention can read the data.

Rates of >=19200 baud (~2.4kB/s) are easily accomplished internationally, while IIRC 57600 baud (~7.2kB/s) are realistic domestic.

Hope others can use this as an intro to PR.

## Answer (score 12)

You sure can. It's been done before with a Baofeng HT, a Raspberry Pi, a USB sound card, and some custom cables and some open-source sound card modem software. This article explains a step-by-step approach.

This article shows how to create a custom cable for interfacing a Baofeng HT with an Android phone (but should be sufficient for figuring out the wiring for the USB sound card so you can interface with your Raspberry Pi - specifically, you'll probably need to separate the right/left audio from the mic and PTT for the sound card's separate mic/audio jacks). Of course you could use the custom cable and an Android phone or tablet running the APRSdroid software mentioned in that article. There are also ready-made cables like the BTECH APRS-K2 TRRS / APRS Cable.

In the first case, the Raspberry Pi is acting as the TNC; in the latter, the Android and APRSdroid are serving that function.

The point of this cable is to connect the input and output audio cables of your computing device (smart phone, raspberry pi or whatever) to the radio. By setting the VOX and squelch settings just right (e.g. "*VOX at ~2, Squelch at ~1*"). Then the computer takes the role of the modem and does modulation (for transmitting, triggered by the VOX setting) and demodulation (for receiving, triggered by the squelch setting).

I hope this helps.

## Answer (score 3, by Rob McNicholas)

I was able to get a Baofeng HT working with packet, but had to adjust a number of menu items. (The tricky one that is poorly understood is Squelch Tail Elminate or STE.) My suggestion, assuming you're using something like a signalink to do PTT:

- Set "battery save" mode to OFF (menu #3).
- Set TDR-AB (menu #34) to A - this ensures your radio transmits on channel A.
- Set STE to OFF (menu #35)
- Set RP-STE to OFF (menu 3#6)
- Turn "roger beeps" off (menu #39)
- Set VOX off (menu #4)

If you're not using something external to handle PTT, you may need to leave VOX enabled and set to ~2.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6545/is-packet-radio-possible-on-baofeng-uv-5r-and-similar-hts, by user400344, Rob McNicholas. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
