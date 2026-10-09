# Mic ground vs ground

*Tags: equipment-design, microphone, audio-interface · score 3*

## Question

Why do most radios have a microphone ground as well as a Ground?

I have found that simply using one ground and tying the microphone as well as the PTT (and audio out, 5v out or whatever else is in the I/O) to work just fine.

## Accepted answer (score 5, by Martin Ewing AA6E)

The problem you could run into is RF feedback into the sensitive mic input. This is particularly a problem if you run "QRO" - high power. It is best to use shielded multi-conductor cable, with the shield being used as the return for the PTT control. The mic output (signal and ground) are separately carried to the mic input connector, where the mic "ground" may actually terminate at the (sensitive) mic amplifier internally.

This way, any RF currents (or possible 60 Hz AC pickup) are carried by the shield ground, which is generally terminated directly at the case of your radio, and they are kept away from the low-level audio amplifiers.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5023/mic-ground-vs-ground, by Skyler 440, Martin Ewing AA6E. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
