# Eliminating "pop" in headphones when speaker activates?

*Tags: ht, audio-interface, audio, speaker · score 3*

## Question

I spend a lot of time as an amateur radio public service volunteer, which means I often find myself wearing an earpiece for several hours. I've noticed that just about all cheap (and even some not-so-cheap) radios suffer from an annoying problem: they generate a loud "pop" whenever the speaker activates (because squelch opens or because key beep is enabled and a key has been pressed, etc). This ranges from "annoying" to "painful" depending on the radio.

Tragically, this isn't something that anyone ever covers in their reviews.

Would creating an adapter with an inline capacitor on the speaker wire reduce or eliminate the pops? Is there an existing product that would help here? I'm only slightly handy and creating a robust solution that wouldn't fall apart in the field might be a challenge for me.

## Answer (score 2, by Ryuji AB1WX)

If you just want to soften the pop even at the expense of a narrower audio bandwidth (less bass), then you could use a small series cap or, better yet, a 1:1 audio-frequency transformer used in old transistor radios from the 1960s and 70s. This approach is probably totally adequate for a CW-only operator (that's me).

I have those lousy rigs with loud pops... and the best way to deal with them is to modify the transceiver so that the amplifier is muted for the brief period when the pop occurs.

If you try to do that outside the transceiver as a standalone adapter, you'll either have to get the pop timing information from the receiver (squelch line, for example), or the T/R switch (for pops that occurs when you press or release the PTT).

Otherwise, I can think of using a cheap microprocessor to sample the AF signal, detect the pop, and mute that period, and **ramp up** to the normal signal (if abrupt on/off mute, you may very well create a new pop there), or keep removing the DC offset or the moving DC average (so the system will be an HPF). This will cause a delay of a couple of dozen milliseconds, possibly longer if you want to remove the pop thoroughly... It may be overkill, but STM32G431 or STM32F303 may be usable (with A/D and D/A built-in.. tho only 12bit). If you choose to go this route, the question becomes designing a state machine (for squelch open/close, RX->TX, TX->RX) and large transient detectors. The latter can be generic (could be triggered by legit large, abrupt signals other than receiver artifacts) or specific (e.g. matched filter bank; must be tailored for your transceiver but less likely to be triggered by other signals).

Thinking this problem in the back of my head for a little while, I think STM32G051F may be adequate for a job like this... it has 12-bit A/D and D/A. It may not even need state tracking. Just detect a pop and mute it, and reset the short-time average buffer at the pop timing. That short-time average is subtracted from the output buffer. Add a little earphone drive amp, and the project is done. This CPU is probably cheaper than the analog components like a small transformer.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23847/eliminating-pop-in-headphones-when-speaker-activates, by larsks, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
