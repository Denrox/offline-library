# Understanding WFM modulation

*Tags: software-defined-radio, receiver, modes, fm · score 3*

## Question

I am using "HDSDR" software to demodulate a WFM broadcast ("Classic FM" in the UK, on 100.1 MHz, 192 KHz bandwidth). I'm using an "SDRPlay RSP1" software defined radio and a cheap indoor discone antenna.

I'm trying to understand more about the audio demodulation and I'm puzzled by the spectrum display. Here's a screengrab...


Annotation "A" is (according to wiki) the "Pilot Frequency" at 19 Khz.


Annotation "B" is a rather fascinating pattern that is clearly part of the stereo audio modulation. But it is centred at 38 KHz, which is far above human hearing capability. Although I notice that it's also twice the pilot freq.


Annotation "C" is RBDS.

### Question(s)

What is the nature of the pattern in annotation "B"? When music is playing this area is rich with visible modulation. But when it's just a simple human voice (the radio show presenter) speaking this area goes totally invisible and blends into the background without a trace.

I vaguely suspect that a human voice (0 Hz to 4 Khz or thereabouts) lacks the dynamic range to show up on the AF waterfall. In contrast, a human voice speaking with some very quiet backing music (e.g. an advertisement track playing) does show up on the AF waterfall.

Is the station doing something special to the broadcast AF modulation during a musical segment, which is absent when the presenter is speaking? Or is it literally that the presenter's voice isn't rich enough in dynamic range to even show up at all?

## Accepted answer (score 12, by Kevin Reid AG6YO)

Your “B” is the stereo difference signal of broadcast FM stereo.

It is placed at twice the pilot frequency so that it can be recovered by having the receiver lock onto the pilot signal and frequency-double it to obtain the *subcarrier* signal marking the position of the difference signal. The receiver uses this subcarrier to shift it in frequency down to the audible range.

The difference signal is the right audio channel subtracted from the left audio channel. The receiver adds the difference signal to the basic mono audio to obtain the left channel, and subtracts to obtain the right channel.

Thus, **if the audio being played by the station is mono or mostly centered, the difference signal is zero or almost zero** and disappears from the waterfall.

The primary advantage of this modulation scheme is that it is compatible with mono receivers (and a stereo receiver can fall back to mono for better sound quality if the signal is weak).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9747/understanding-wfm-modulation, by Wossname, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
