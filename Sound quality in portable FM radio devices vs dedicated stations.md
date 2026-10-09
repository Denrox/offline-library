# Sound quality in portable FM radio devices vs dedicated stations

*Tags: fm, bandwidth, music · score 4*

## Question

When speaking to a portable radio transmitter the sounds usually gets distorted. However in radio stations that are dedicated to play music the sound is significantly better. First of all, why? And second how can I make it better? The system I use can transmit from 30Mhz to 87.975Mhz with 30Khz bandwidth (military system) and I want to play music over it (I connected the audio input to my phone). I know it's a radio problem because when I use wire the sound is better.

## Accepted answer (score 7, by SDsolar)

Bandwidth: Broadcast FM stations are spaced 200 KHz apart, with the intention of allowing this kind of signal structure without interference:

The FM broadcast bandwidth of just more than 50 KHz is quite sufficient for near-CD quality stereo.

Normal broadcast FM uses multiplexing so the main channel includes L+R - both channels - what we call Mono. Then there is a subcarrier that sends L-R. The receiver detects the pilot signal (subcarrier) and lights up the "stereo" light, so the receiver knows to use a demultiplexer to separate the L and R signals which it then sends to your amplifier and speakers.

Sound quality: FM broadcast stations always use audio processors that are specifically tuned to make it sound better than any handheld radio's microphone circuitry will be able to duplicate.

(This one is roughly $10,000)

They also incorporate pre-emphasis so the roll-off of higher frequencies in the receiver IF bandpass filters are not as audible.

Dolby sound operates on a similar principle - to counteract artifacts introduced by the entire receiving chain including the speakers.

It takes a lot of work to properly tune the audio processor at a broadcast station.

Thus there is no comparison to a ham signal with 5 KHz deviation and no audio processing, with a small microphone. It can be easily heard.

The military system you describe operates with 30 KHz deviation. The receivers probably also have a 30 KHz bandpass filter, which means theoretically it should be able to reproduce up to 15 KHz audio frequencies.

But no filter is has perfect "cliff" edges, so there will be some kind of gradual roll-off at the higher audio frequencies.

One thing you can do with it for music, short of adding an audio processor, is to provide some sort of pre-emphasis.

This can be done with a regular equalizer on the input.

In broadcasting, to really tune it up well you would want to put a pink noise source (maybe an app) into the transmitter, then watch on a receiver with an audio spectrum analyzer. Adjust the transmitter's audio-input equalizer until you get a flat response end-to-end.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9397/sound-quality-in-portable-fm-radio-devices-vs-dedicated-stations, by Adam Katav, SDsolar. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
