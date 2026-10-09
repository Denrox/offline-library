# Unlicensed TV broadcasting power limit (Band I)

*Tags: united-states, legal, vhf, transmitter · score 5*

## Question

I'm curious what is the legal limit for unlicensed TV signals being transmitted on the VHF Band I?

This seems ill defined. The part 15 FM rules I am assuming don't apply here. And I don't think it can be illegal at all power levels because even old VCRs and TV tuners will leak a little RF. So what is the limit?

## Answer (score 5, by mrog)

Since you mentioned part 15, I'm guessing you're asking about the rules in the United States.

If you look at part 15 subpart C in detail, you'll see that the frequencies in the VHF I band (44 - 87.5 MHz) have some specific unlicensed uses, mostly related to audio transmissions (wireless microphones, cordless phones, etc.) Since the question is about TV signals, most of those don't apply. The only exception I can see is §15.235, which doesn't specify a specific application (except for saying that it can't be a cordless phone). However, that section is for a very narrow band: 49.82-49.90 MHz. Since NTSC signals require 6 MHz of bandwidth, that band isn't nearly big enough to accommodate a typical video application.

That leaves white space devices as the last remaining option. The rules for these devices are complicated. The available frequencies vary by location and time. The maximum allowed power levels vary depending on the frequency and the characteristics of the device. It's possible to transmit with a range of several kilometers with the right gear, but you have to carefully follow some fairly complicated rules.

Because the question referenced unintentional leakage, I'll point out that it's covered by different rules. Part 15 subpart B has the specifics.

## Answer (score 4, by hobbs - KC2G)

It's illegal at all power levels. If you "leak a little RF" then there is something in Part 15 that applies (e.g. this section for VCRs and cable boxes) *and* the device needs to be certified. If you broadcast *intentionally* then there isn't anything that allows it at all, at any power level.

## Answer (score 2, by Glenn W9IQ)

Yes, you may broadcast (called an "intentional radiator") video transmissions but only on unused TV channels 14-51 (UHF, not VHF) as so called "white spaces". Read Part 15 regulations part 701 and on for the requirements and restrictions. Here is the introduction to this section:

This subpart sets forth the regulations for unlicensed white space devices. These devices are unlicensed intentional radiators that operate on available TV channels in the broadcast television frequency bands, the 600 MHz band (including the guard bands and duplex gap), and in 608-614 MHz (channel 37).

Also reference the FCC web site on this topic.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12568/unlicensed-tv-broadcasting-power-limit-band-i, by Synaps3, mrog, hobbs - KC2G, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
