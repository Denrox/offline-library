# How can I send a voice message from my PC to HT radios?

*Tags: ht, software · score 3*

## Question

I would like to know how to transmit a voice message from my PC by software, to my HT radios at a specific channel. My radios are Baofeng BF-A5.

Do you know of software to deal with it?

## Answer (score 4, by Kevin Reid AG6YO)

All you need to do this is the following components:


**A radio to transmit the message.** It doesn't have to be the same model as the HTs you want to receive the signal. In fact, it might be overall simpler and cheaper to choose a radio which has a built-in computer interface.


**A “sound card” for your computer**. It is possible to connect your computer's main audio output to your radio, but this is not to be preferred because you might transmit beeps or other incidental sound effects produced by your computer. Instead, get a “USB audio interface” or “USB sound card” to add an additional audio output to your computer. There are three options here:

 1.

Buy a standard USB audio interface and use a separate interface box to connect that to the radio.

The interface box is needed both to adapt the pinouts and potentially to break ground loops or for sorts of electrical issues.

1b. However, some radios may have electrically compatible audio jacks that don't need any interface circuit.

 2.

Buy a USB audio interface designed for connecting to radios. These will be more expensive but have built-in isolation. For example, the Tigertronics SignaLink USB is a very popular model. (It is sometimes accused of having inherent design flaws limiting its performance, but I don't know the details.)

 3.

Some radios have built-in USB audio connections. However, these are likely to be high-end expensive models.


**Software to play the message.** This can be any audio/music program, as long as it lets you select the output audio device to use rather than always using the system default device.

Note that all of this is the same equipment you would be using for some digital modes, such as APRS. In fact, I would strongly recommend that you **look into using the same equipment that people have used for APRS**, as this is a very popular application for computers hooked to radios.

Two caveats to that:


APRS stations sometimes use separate hardware to do the message encoding/decoding (a “TNC”). Look at setups that use a “software TNC” — you would use your audio player instead of the TNC software.


APRS stations are often battery-powered. I assume that you're doing this from a fixed station; in which case note that line-powering both the radio and computer may introduce a ground loop issue that wouldn't otherwise be present. This is only a problem if you're using option (1b) above.

Finally, if you get all this set up, you've got all the hardware you need to start operating with APRS, and (if you use an all-mode radio) other digital modes! Check them out!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4937/how-can-i-send-a-voice-message-from-my-pc-to-ht-radios, by Danilo, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
