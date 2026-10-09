# What is the typical latency of a SDR setup running on a desktop computer?

*Tags: software-defined-radio, gnuradio · score 3*

## Question

It's well-known that the signal processing of an SDR adds a significantly amount of latency, the SDR software on the computer adds more latency due to data buffering, FFT, decoding, demolutaion, audio buffering, etc, not to mention that most computer systems aren't a real time system and have unpredictable delays as well.

It's usually not a concern, but can be a problem when one wants to extract the precise time-mark of a signal. To elaborate the question, imagine a SDR running on a typical desktop computer, operated by a program powered by GNU/Radio, and consider two scenarios:

1.

*Time Synchronization* - SDR is tuned to a frequency and listens for an incoming pulse. A pulse is generated at 00:00:00 UTC. Upon receiving it, the SDR immediately set the system's real-time clock to 00:00:00 UTC (for example, in a time synchronization experiment). What would be the error between UTC and system's real-time clock now? Ignore all insignificant sources of errors.

2.

*Time-mark extraction* - SDR is tuned to a frequency and listens for an incoming pulse. As soon as the pulse is generated, the SDR records the wall-clock time (for example, in a propagation-delay experiment). Assume the system's real-time clock has no error, what would be the error of the time measurable by the program?

Both questions ask for a simple parameter: The typical total delay/latency in the entire signal path of the an SDR setup on a desktop computer. We also assume the latency is not predetermined and calibrated to zero prior to these experiments.

I expect the latency is much worse than what the operating system on a desktop computer is capable of. For example, protocols like NTP uses a PLL-like algorithm and finish the time synchronization in multiple steps, an final error of less than 10 milliseconds over the Internet is not impossible given a datacenter network with symmetric routes (see this statistics), but extracting the time-mark of an one-off event is harder for a desktop computer with SDR, and I expect the delay of an unoptimized implementation has a latency of a dozen of milliseconds. If an accuracy comparable to NTP is required, it's better use a specialized circuit, not a SDR.

That all being said, while I can find some research papers and projects on the architecture of a low-latency SDR, I cannot find a solid measurement or analysis of latency/delay of a typical SDR, such as a RTL-SDR, HackRF, LimeSDR, with gqrx or GNU Radio. I was inspirited by Dan Luu's experiments on the typical latency between entering a keystroke and a screen update on various computer hardware, or the typical latency of latency between a keystroke and a keyboard scancode using a logic analyzer, some experiments for SDR software and hardware would be greatly useful.

I believe this can be an useful reference question. Any data, analysis, and measurements are appropriated. I think I could do some measurements in the future.

## Accepted answer (score 3, by hotpaw2)

The answer is that the SDR hardware devices are all very different, so is the optimization quality of the SDR code. So one pretty much needs to calibrate for their specific setup: device, current method of connection, OS, and software running.

I find network latency between the SDR hardware server and the software client to be one of the biggest variables, especially over multiple WiFi hops. But in general, there could be ADC buffering, FPGA buffering, hardware filtering and downsampling buffering, USB output buffering (depending on USB transfer block size), USB driver input buffering, OS network buffering (depending on MTU size), Ethernet buffering, WiFi access point buffering, OS driver IO buffering, application network buffering, SDR software filtering buffering, SDR demodulation buffering, audio processing buffering, OS audio driver output buffering, audio DAC DMA buffering, and etc. All these buffers are covering for latency jitter in the various interfaces, caused by asynchronous timing and contention for various buses, WiFi bandwidth, OS processes, and etc., which vary widely between setups.

Note that an SDR radio can shortcut many of these latencies by having all this hardware and software on a single board or a single chip running a real-time OS or even no OS.

I test SDR total system latency by keying a QRP transmitter (preferably fully analog) into a dummy load, then listening to the delay between my keyer sidetone and when I hear the sidetone out of one of my SDR apps. You can record these two in stereo and view the waveform rise-time deltas for a more precise measurement. Depending on which SDR device I'm using, and whether the data is hardwired or from an SDR server over WiFi. I can hear latencies of from around 100 mS to over 1 Second.

## Answer (score 2, by Brian K1LI)

Dr Warren Pratt, NR0V, introduced low-latency FIR filters to the 2018 SDR Academy. Dr Pratt reminded the audience that *mimimum phase* FIR filters deliver much lower latency than *linear phase* filters and opined that ease of design has driven the persistence of linear phase filters. I have observed a dramatic reduction in latency by switching to Dr Pratt's WDSP library in the SDRs I employ.

## Answer (score 2, by Aleksander Alekseev - R2AUK)

It's difficult to give an exact number, because the overall latency involves at least:

- Processing of the signal on the given SDR
- Transferring data over USB 2.0 / USB 3.0 / PCIe (depending on what is used)
- Latencies on USB controllers on both SDR and PC (+ USB hubs, if used)
- Latency caused by other USB devices (keyboard, touchpad, webcam, ...) on the bus. Note that USB devices are always pulled by the PC, USB device can't just push data over the bus without being asking for it.
- Latency in the device driver
- Latency between ring0 and ring3 levels in the particular operating system (involves process switching, data copying => memory latancy, etc)
- Processing of the data by the given software (GNU Radio / Python / C++)

My rough approximation would be that all this chain typically takes no more than 10 ms (probably much less). But it's difficult to give a more accurate number because there are too many unknown variables.

It's also difficult to measure this number experimentally. You could write an application that receives a signal, somehow replies to it, measure the time between sending request and receiving response (roundtrip time) and divide it by two. The problem is - where you can find a measuring equipment with near-zero internal latency? I can only think of using an analog transmitter and receiver and measure the roundtrip time using an oscilloscope.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15384/what-is-the-typical-latency-of-a-sdr-setup-running-on-a-desktop-computer, by 比尔盖子, hotpaw2, Brian K1LI, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
