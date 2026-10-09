# Receive Data on Specific Frequency

*Tags: diy, digital-modes, equipment-design · score 5*

## Question

So if I were to build a simple AM radio transmitter just using say, my Arduino, an oscillator, and wire for an antenna (this is all crude I know, but work with me here) and use it to transmit data collected or what have you, how do I receive and decode this signal? I understand if I'm using say an MP3 player and the same idea I could just tune in to the frequency of the oscillator on a modern AM radio, but I want to send and receive data.

I get the basics of the transmitter side, but I don't grasp the receiver side as well. I'd also prefer to only receive the signal I sent out, so only receive on the 1.2 MHz channel, or what have you, if that's possible. What I'm saying is I don't want a tunable receiver, rather just a receiver fit for the transmitter's exact frequency, in a perfect world.

## Answer (score 4, by Phil Frost - W8II)

Sending data is not so different from sending audio. You just have to come up with some kind of symbol which represents one or more bits of data. For example, you could encode your data by speaking "1" or "0" into a microphone.

Someone at the other end listens to the audio and types in the numbers, and boom, you are sending data.

Of course you probably want something easier for electronics to encode and decode so you can replace the humans with electronics. So maybe you say a 1000 Hz tone is a "1", and a 2000 Hz tone is a "0". Now you have invented AFSK.

Or maybe you realize this is using a lot of transmitter power and radio bandwidth to send not very much information. You realize that you can detect the presence of an AM carrier, even if there's no tone but just silence. So you decide that to transmit a 1, you transmit a carrier, and to transmit a 0, you transmit nothing at all (the absence of a carrier). Now you have invented on-off keying.

These are just two of many possible digital modulation methods.

As for the other part of your question about tuning, it doesn't really matter, nor does making a non-tunable receiver simplify things very much. You still need to design an oscillator or a filter (the two are very similar, electronically) at some particular frequency. If you don't need to tune, then the design of this component might be a little simpler, but all the other bits of the receiver are the same, and those other bits are most of the work.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3824/receive-data-on-specific-frequency, by user2278224, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
