# Getting Started with Digital Modes on VHF on Linux

*Tags: digital-modes, software-defined-radio, vhf, 2m-band, linux · score 10*

## Question

I am interested in learning about digital modes using 2m and Linux.

I have a couple of older 2m rigs (HTX-212 and an old Yaesu) with no additional hardware, like a TNC.

What current resources exist for hardware setup and software configuration for this type of operation?  
I am also willing to consider the use of a Sound Card interface, but everything I have found so far refers specifically to the SoundBlaster cards and Crystal cards of olde.

Would software defined radio be a better option for what I am attempting to experiment with?

## Answer (score 6, by Phil Frost - W8II)

2m isn't a good band if you want to do anything digital. Digital modes just aren't very popular on 2m. I think the only digital activity you are likely to find is:

- D-STAR
- APRS

D-STAR uses GMSK, but the data for voice transmitted on that channel relies on a proprietary codec called AMBE. Any software that can encode or decode it is almost surely illegal, especially if you didn't pay for it. You could purchase something like a DV Dongle which has an AMBE ASIC in it. You could also just buy an Icom radio. But that's not much of a learning experience, and probably not what you had in mind.

D-STAR has a data mode which isn't based on anything proprietary, but aside from a talk at Hamvention, I've never run across anyone actually using it.

APRS is easy to find, but it uses an ancient AFSK modulation. It's horribly slow and inefficient in terms of power and bandwidth for what it does. It might be fun to play with, but you won't learn much about good engineering or modern technology from it.

Fldigi is great software for digital modes on Linux, but here's the real problem: nearly all 2m rigs are capable of only FM operation. They don't have a [linear amplifier](What%20is%20a%20linear%20RF%20amplifier.md), which rules out a huge class of modulations, but also the "data" input goes through the FM modulator. For some digital modulations, it's possible to design an audio input which will go through an FM modulation and end up transmitting the right thing on the air, but most software isn't designed to work this way.

Sure, you can connect some PSK31 software into the audio input of an FM radio, and get it back at the audio output of some other FM radio and even send messages, but what you are sending over the air isn't PSK31, it's FM with PSK31 in it. All the nice things about PSK31, like narrow bandwidth, are lost.

Fldigi, as well as most other digital mode software, is designed to be connected to an SSB radio. This is because [SSB is basically a null modulation](Up%20converted%20audio%20transmission.md): all it does is take the audio input, and shift everything up to wherever the radio is tuned. You can modulate or demodulate anything through SSB because it doesn't change the signal except by shifting it in frequency.

My advice: if you want to learn about digital modes, and you don't have an HF rig, get a cheap SDR kit. The cheapest one I know of is the SoftRock. You will have no difficulty finding digital activity, day or night, on 20m.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2449/getting-started-with-digital-modes-on-vhf-on-linux, by Rob Gibson, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
