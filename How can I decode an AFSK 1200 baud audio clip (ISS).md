# How can I decode an AFSK 1200 baud audio clip? (ISS)

*Tags: digital-modes, packet, ax.25 · score 4*

## Question

I'm a new ham. The past few days, I've had a few nearby passes of the International Space Station. As it was going overhead, I managed to record what I believe to be 1200 baud AFSK transmissions from it (AX.25) - from it's 145.825MHz Packet Radio downlink. I have an audio file of one. I am trying to figure out how to decode it and haven't had any luck. I've tried QTMM from SourceForge (playing the recording into my computer microphone) - but got no decode.

I have an audio file which has three distinct burst of what appear to be data (with very little noise during these bursts). Both nights, these burst only occurred while the station was nearest to me. Thus, I'm positive I have good audio - just can't figure out how to demodulate!

## Answer (score 6, by Kevin Reid AG6YO)

Audio which sounds perfectly fine can be noisy or distorted (notably, by FM deemphasis) enough to prevent digital decoding.

At a minimum, you should get rid of the microphone step and feed your audio directly into the demodulator program.

You don't say what OS you're using, but I have had success demodulating APRS messages using multimon-ng. It can be set to accept raw input (16-bit at 22050 Hz); you can use an audio editor (such as the free Audacity) to convert your recording.

(Note that multimon-ng will take the AFSK audio signal and give you text-format AX.25 messages, but it will not actually parse the APRS content into human-readable text except as APRS has some readable fields already; you would need another program to handle that. At least you'll be able to see if the messages are recoverable at all.)

## Answer (score 2, by user6024)

Just a suggestion, but have you considered the possibility of it being an SSTV transmission? I would download an SSTV decoder and run it through that, using various encoding methods (e.g. Robot32, PD180, etc.) and see what you get.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2041/how-can-i-decode-an-afsk-1200-baud-audio-clip-iss, by Brad, Kevin Reid AG6YO, user6024. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
