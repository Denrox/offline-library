# Open Source Library for Digital Mode

*Tags: digital-modes, software, rtty · score 3*

## Question

I want to play a bit more with programming side of digital modes. However, a quick Google search turned up lots of software and some general explanations but no open-source library implementing such a code.

For example, I would find a library that encodes and decodes messages from/to plain text to either text output or sound most useful.

I was looking particularly at RTTY, FSK and PSK31 as they seem to be the simpler modes around.

Does anyone have any experience or useful pointer in this area?

## Accepted answer (score 5, by Marcus Müller)

What you describe is Software Defined Radio! Hurray!

So, everyone having read my answers knows: I'm a GNU Radio fanboy.

GNU Radio has to be understood as the Free&Open-Source LEGO of Software-Defined Radio:

It comes with a huge library of signal processing blocks, which one can combine to build complex applications. Itself, it's not a library to be used to decode any particular standards, but you can download modules that combine GNU Radio blocks to do that.

You can write your own blocks in C++ or Python, and to build flow graphs out of blocks, you'd typically use Python or a graphical design tool called the GNU Radio companion.

FSK, for example, can be astonishingly easy to decode; if you neglect the need for synchronization, a complete FSK decoder might look like:

which does nothing but convert an input signal stream to a stream of estimates of the current frequency. You'd of course would want to have things like filtering, sanitation, conversion to bits, and packetization, but again, there's already modules that do that for you; see the list at

https://wiki.gnuradio.org/index.php/HamRadio

They've got RTTY, PSK31, and a lot more (FSK is really just a general modulation scheme – there's a lot of modes that use it!).

What I feel I should mention is that you can, for example, use gr-dtv, the digital TV transmitter library within GNU Radio, to transmit extremely low-bandwidth TV – think of the digital evolution of SSTV, by using gr-dtv with appropriate MPEG transport streams that contain low-rate video and e.g. Codec2 audio.

I'd like to take the chance to highlight a few GNU Radio projects that are of interest in this context, but aren't specifically related to amateur digital modes:

- GQRX is probably the most famous GNU Radio standalone application. It's a spectrum visualizer, and audio demodulator. I don't know from the top of my head whether it does digital modes (it probably doesn't), but it's extremely useful when trying to find a signal in a wide bandwidth receive signal
- gr-inspector is awesome, in that it allows to estimate signal parameters out of life signals automagically
- gr-noaa is interesting if you already happen to have a dish and a feed capable of receiving NOAA satellite imagery, or a good helical antenna

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6753/open-source-library-for-digital-mode, by Edgar H, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
