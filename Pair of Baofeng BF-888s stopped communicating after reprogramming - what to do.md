# Pair of Baofeng BF-888s stopped communicating after reprogramming - what to do

*Tags: baofeng, radio-programming, germany · score 3*

## Question

I got 2 Baofeng 888s off Amazon and reprogrammed them to the 16 legal channels (for unlicensed use) in Germany, up from 446.00625 MHz in 12.5 kHz steps.

I used both CHIRP and a software called ZT-V68 to make sure they are identically programmed. So both in CHIRP and in ZT-V68, when I download the settings from radio one and then compare them to the downloaded settings from radio two (making sure that it is actually downloading and showing me the new data from the other radio) — these software data files look identical. All the settings are the same. I disabled the "scrambler" in everywhere, and set all channels to "low".

But the radios are not communicating with each other. Why on earth can that be?

## Accepted answer (score 5, by Glenn W9IQ)

One other setting for each channel that may be giving you problems is Duplex/Simplex. Make certain it is set to Simplex or equivalently "no offset". This feature, when turned on, causes that channel to transmit and receive on different frequencies - typically for using the radio with a repeater.

Viel Glück!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12752/pair-of-baofeng-bf-888s-stopped-communicating-after-reprogramming-what-to-do, by user14157, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
