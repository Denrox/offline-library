# How do repeaters work? (The technical side)

*Tags: repeater · score 4*

## Question

I'm curious how AM and FM repeaters work.

Is the received signal demodulated and then remodulated at the new frequency or do they use some other technique?

## Accepted answer (score 6, by Kevin Reid AG6YO)

It is *possible* to repeat a signal without demodulating it. This is done on some amateur satellites where it is called a *linear transponder*. The advantage of this method is that it can carry multiple signals, and any mode, including SSB and CW. The disadvantage is that it retransmits all the noise it hears and cannot clean up the modulation along the way — very much like how putting an amplifier before your receiver can't improve the signal-to-noise ratio.

A typical FM repeater consists of a fairly ordinary receiver and transmitter, with the audio output of the receiver connected to the (microphone) audio input of the transmitter.

The second most critical element is a *duplexer*, which is a pair of very narrow filters which ensure that the receiver is not overloaded by the transmitted signal on the same antenna. (The less-usual case of a *cross-band* repeater, which has far more frequency separation between transmit and receive frequencies, does not need a duplexer.)

Finally, you usually have a repeater controller, which can be connected to the audio, PTT, etc. signals from/to the radios in order to implement additional features (repeater ID, time-out timer, repeater linking/phone patch, etc.).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6941/how-do-repeaters-work-the-technical-side, by vini_i, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
