# What is an undulator (as used for CW)?

*Tags: cw, history, morse-code · score 6*

## Question

There are historical references to a device called an "undulator" used for CW reception circa before and during WWII.

What is an Undulator (as used for CW recording)? How did they work (electronic or mechanical)? Why were undulators used for recording instead of audio tape recorders? What speeds of Morse code could an Undulator be used on? Were the results transcribed by automation or by humans? If by humans, at what speed could any transcription be done (e.g. faster or slower than the actual on-the-air CW WPM rate?)

## Answer (score 8, by Marcus Müller)

Since I can't answer this authoratively myself, but Mike Waters' comments indicate that search engine results of other people might be sparser than mine:

A link collection:

- Title/Link  Short Description
- Project Undulator  Restoration of a 1870s British undulator, with original manuals and details on the inner workings
- Radio Museum: Marconi high speed undulator UG6A  Brief fact sheet, photos
- UG6A manual
- Navy Automated Morse Code (CW) Equipment  US-American Tape recorders, heavy duty stuff it seems
- Hell Morse Recorder UR 39 (C) / RC 28  1952 catalog with working principle descriptions and demo video

What is an Undulator (as used for CW recording)?

A paper tape device for recording the on/off times of the morse signal as bipodal lines on paper. "Undulating" thus is the line on paper.  
How did they work (electronic or mechanical)?

Electromechanically, naturally.

Why were undulators used for recording instead of audio tape recorders?

Because nobody cares about the audio, they care about the letters, and storing the audio is extremely costly if you just need to know whether there is a tone or there is none.

Note that the U6GA mentioned in the links above claims it an invention from 1870; 150 years old. The magnetic tape recorder is a German invention from 1930, so 60 years later (so, the very first tape recorder is as far away from the invention of the U6GA, which judging by the type name, was not the first one, as a 1990 commercially available GSM phone is from the first magnetic tape in the world; the first undulator is much much closer to Isaac Newton thinking about why apples fall from a tree than to today).

Basically, at the point when people could record things on magnetic tape, they could also just transmit letters as such using teletypers/hellschreiber kind of devices, so the whole purpose of undulators, recording the long-obsolete Morse encoding for text, were obsolete at the point where continuous audio recording technology became available.

What speeds of Morse code could an Undulator be used on?

Glimpsing at the catalogs above: most models seem to be made for "reasonable" speeds up to 300 wpm, the US navy equipment claims up to 1000 wpms, but I do have my doubts about that – it would mathematically, let alone practically, have required CW channels well in excess of 2 kHz bandwidth, would be uncopyable by ear, and every sensible comms engineer post-1940 would have been smarter than to use Morse encoding at these throughputs.

Were the results transcribed by automation or by humans?

Humans; optical recognition of lines on paper is something that I'd date no earlier than late 1940s, and even then you'd be faced with the same problem as prior to the recording on paper: making textual sense of a "high"/"not high" signal (and that's the hard part). The late 1940s that's the time frame around which undulators must have become pretty obsoleted by teletypers and similar technology, too.

If by humans, at what speed could any transcription be done (e.g. faster or slower than the actual on-the-air CW WPM rate?)

At any rate you want. The line is on paper, waiting for as long as you want. Be it at the post office for the recipient to pick up the telegram, or on the helm of a battleship in a WW1 fight, possibly at different levels of "I hope this message finds you well,…".

## Answer (score 3, by Graham G8URP)

an "undulator" used for CW reception circa before and during WWII.

WWII? My then employer still had a Marconi UG-6 undulator in our radio lab in the mid-1980s.

While Marcus Müller has provided a comprehensive summary of undulator use for CW note that these devices are also fast enough to record demodulated radio teletype (RTTY) signals. The paper tape can then be read by eye, useful for fault finding or processing a non-standard signal that isn't recognized by a teleprinter.

How did they work (electronic or mechanical)?

The undulator itself is electromechanical. The demodulated CW or RTTY signal is applied to a solenoid which drives a pen sideways across the paper tape. The tape is driven along by a motor with adjustable speed.

The solenoid, which is comparable to the voice coil in a loudspeaker, is driven by a separate electronic vacuum valve/tube bridge.

The sideways movement of an undulator distinguishes it from a morse inker which uses its solenoid to drive a pen up and down onto the moving paper tape. This produces a written record of dots and dashes along the tape, hence giving rise to the terms mark and space which live on into teleprinter usage.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22627/what-is-an-undulator-as-used-for-cw, by hotpaw2, Marcus Müller, Graham G8URP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
