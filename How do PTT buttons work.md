# How do PTT buttons work?

*Tags: baofeng, transmitter, audio-interface, microphone · score 6*

## Question

I'm really new to this, and I was wondering how the whole PTT system works? I have a headset with microphone, and a Baofeng UV-82 radio. I know the radio has its own PTT button, but is there any kind of PTT button that could be attached to it via wire as simply as possible?

Thanks!

## Answer (score 15, by Glenn W9IQ)

The basic PTT (push to talk) button on the HT is a simple switch that is normally open and when it is pressed, the switch is closed (conducting). Internally to the radio, this applies power to the PA (power amplifier) stage of the transmitter, it idles the receiver, it switches the frequency synthesizer to generate the correct transmit frequency and a number of other "housekeeping" actions.

An external PTT switch is easily added. Here is a nice diagram from the miklor.com site.

You can see the switch to the far left of the circuit. It is wired to the outer most "ring" of each plug. Closing (pressing or toggling) that switch will cause the radio to transmit.

Here is the schematic from the same site showing the dual PTT and the optional data connection:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12218/how-do-ptt-buttons-work, by Jack. D, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
