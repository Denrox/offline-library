# Using a Morse code key with a computer?

*Tags: cw, remote-control · score 19*

## Question

Are there standard ways to connect a hand key (straight or paddle) to a contemporary computing device (PC laptop with no parallel port, Mac, Android, iOS device, etc.) for developing or improving ones Morse code sending skills?

If so, can one use this setup to do hand-key QSOs, either using a remote transmitter if appropriately licensed, or directly over the internet?

## Accepted answer (score 9, by Andrew)

A really easy way to do this is to take an old USB mouse (or even a new cheap one) and solder the key across the left mouse button. You can then use key directly as mouse button input on most computers and Android phones (with an OTG cable) and use with Morse software or websites expecting mouse input e.g. :-

http://morsecode.me

http://www.web-adventures.org/MorseBlitz/

For hours of fun and practice.

Update: Your question inspired me to do a little better so I created this blog post in the hope that it's useful http://whaley.org.uk/andrew/blog/2017/04/28/morse-code-cw-via-usb/

It covers 2 methods; the quick mouse option but also something a lot more versatile which isn't that much more effort.

## Answer (score 6, by Phil Frost - W8II)

How you do this will be dictated by the software you select. However, most software I have seen uses some of the control lines on an RS-232 serial port. Calling it a "standard" might be a stretch, but there seems to be a convention:

More at the source, F8EHO.net.

It's also possible to use some of the other control lines to drive an opto-isolator or relay which in turn connects to the key jack on your radio. Thus, your computer looks, to the transmitter, as an external keyer. Again, no real *standards*, besides those imposed by the software you select.

No doubt, it is possible to send Morse code over the internet. Any application that can send audio over the internet could do it, for example, Skype. You'd simply need to set the input of your audio-over-internet application to be the output of your morse-code-keyer application, instead of a microphone. Of course, there is no *standard* way to do this either, just as there is no standard communication program, or standard keying software, or standard operating system.

## Answer (score 2, by Kevin Reid AG6YO)

Well, I can't answer as to “standard” as I'm just learning myself, but I can think of a couple of ways to do this without getting into completely custom interface hardware and drivers, or needing an interface with directly readable signal lines like a serial port or parallel port which is less common these days:


Connect the key to a *code practice oscillator* that has a line-level audio output, then connect the audio to your computer's line-in.

(I can't find a good existing explanation to link here! A code practice oscillator is just a device with key input, audio output (usually with a built-in speaker), and an internal oscillator so that it can produce an audio tone that is switched on and off by the key input. I don't know how commonly available a line output is.)

This would allow you to practice using “decode Morse from audio” apps, which I understand are available on smartphone platforms, for example. It could be used to transmit using a remotely controlled transmitter; if in SSB mode (and the CPO's output is a good sine wave, which is worth checking), the result is equivalent to CW (though probably less clean), but in FM or AM modes it is modulated continuous wave.

For practice rather than transmission purposes, it would be adequate to use a CPO without line output, and a regular microphone attached to your computer that picks the sound up.


Turn the key into a keyboard keyswitch. This could be done by connecting it to the appropriate points on the switch matrix of a regular keyboard; you might also be able to find a specific-purpose device (or plans for one) for connecting arbitrary switches as keyboards, for the arcade-cabinet or assistive-device (for disabilities) markets, but I haven't looked hard myself.

This requires software which will interpret a keyboard key as a Morse key. I don't know anything about the existence of such; I just mention this option because from a computer-peripheral-interfacing perspective it's the most fitting.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1256/using-a-morse-code-key-with-a-computer, by hotpaw2, Andrew, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
