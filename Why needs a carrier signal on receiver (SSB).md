# Why needs a carrier signal on receiver (SSB)

*Tags: ssb · score 5*

## Question

why does the receiver needs to add a carrier signal to the SSB signal?

I am new to ham radio and can't so much.

## Accepted answer (score 3, by Martin Ewing AA6E)

The SSB signal needs to be converted to the audio range so that you can hear the modulation normally. The carrier that you inject acts as a frequency reference, defining the translation of each RF frequency to an audio frequency (after detection). If you are transmitting a 1 kHz tone at 14,200 kHz, upper sideband, you are sending a single frequency, 14,201 kHz. The receiver needs to inject 14,200 kHz "carrier" so that you will end up with 1 kHz audio after detection.

## Answer (score 5, by Juancho)

You need to add a carrier in order to perform envelope detection, which is the standard detector in most applications.

If no carrier is added, the signal envelope is centered around 0, so the detected output is full-wave rectified. The carrier adds a DC component to avoid the zero crossing of the envelope.

## Answer (score 4, by Kevin Reid AG6YO)

As Juancho already mentioned, adding a carrier to the signal is needed for envelope detection, one particular demodulation technique (which can be seen as locally converting the signal to an AM, or more precisely *vestigial sideband*, signal).

However, *any* SSB reciever, no matter how it is designed, *must* in some sense have a signal at the carrier frequency (or an intermediate frequency and the carrier frequency ± the IF). This is because the demodulator must, one way or another, translate the SSB signal from its original carrier frequency to zero (putting the “sideband” into audio frequencies), and in order to perform that translation, whether in electronics or in software, one must produce a signal at the frequency one is translating the signal by.

(At least, I haven't heard of any methods that don't have that as a component, and it's hard to see how something else could work — what defines the tuning frequency, if not a signal at that frequency or a known offset of it?)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5108/why-needs-a-carrier-signal-on-receiver-ssb, by Axel, Martin Ewing AA6E, Juancho, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
