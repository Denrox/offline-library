# Linux based SDR spectrum capture via CLI

*Tags: software-defined-radio, contest, linux · score 4*

## Question

I need to setup a Linux box to run unattended capture of about 10 MHz - contiguous worth of spectrum (Hardware must support between 500 kHz and 200 MHz) targeting voice (mix of AM and FM voice broadcasts), and another process to selectively demodulate certain frequencies.

So all of these operations need to be command line / scriptable, free of a GUI.

My questions are as follows:

1.

What are the best hardware options for this considering the bandwidth and frequency requirements and availability of stable linux drivers? (I was thinking one of the SDRPlay family of devices but would welcome input on this.)

2.

The recommended utility/stack/drivers for capturing the raw samples based on the answer for #1 (or SDRPlay if no preference) (?)

3.

The recommended utility/stack for selectively demodulating and producing wav or .mp3 audio outs. (?)

(For example if someone has setup something like this (again not Windows) for recording/logging spectrum for HAM contests, that would be a similiar application to what I need)

## Accepted answer (score 5, by Marcus Müller)

What are the best hardware options for this considering the bandwidth and frequency requirements and availability of stable linux drivers. (I was thinking one of the SDRPlay family of devices but would welcome input on this)

So quick summation of your requirements:

- at least 10 MHz analog bandwidth and 10 MS/s (complex) or 20 MS/s (real-valued) sampling rate
- Be able to capture signals between 0.5 and 200 MHz
- Stable linux drivers
- Proven interface to software in which to implement selective demodulation

What are the best hardware options for this considering the bandwidth and frequency requirements and availability of stable linux drivers. (I was thinking one of the SDRPlay family of devices but would welcome input on this)

To make this clear: I'm affiliated with Ettus. But I really think their USRP devices make a pretty good match. We offer awesome support for our customers (or so I'm told).

They all work with UHD, the Ettus driver framework, which is free&open source, and works beautifully with GNU Radio, which lends itself excellently to the task at hand, especially thanks to the flexible and immensely CPU-effective polyphase channelizers. I'd recommend you look into the GNU Radio Guided Tutorials; there's also a *GNU Radio LiveSDR environment* that you can flash onto a USB stick and boot from so you don't have to install things locally.

If you can use an upconverter, go for a B200mini (small & cheap), B200 (basically same as B200mini, but with space for GPSDO and GPIO pins, might be useful) or B210 (B200 with twice as many RX and TX chains) for cost reasons. By themselves, their LOs are tunable from 70 MHz to 6 GHz, and their instantaneous bandwidth is up to 56 MHz. USB3. They have configurable analog bandwidth and if you configure that to the 56 MHz max, and tune to the 70 MHz minimum, you could still observe (70 - 56/2) MHz = 42 MHz signals, even if you don't use a high sampling rate - all USRPs have digital tuning built in, so that you can ask the DSP logic on the USRP it self to shift a signal in frequency prior to decimating the hardware sample rate to the user sample rate you requested:

If you want to avoid the separate upconverter, go for a USRP that accepts WBX or UBX daughterboards; if you're going for multiple channels and need max fidelity, the costly TwinRX daughterboards. In your case, a N200 USRP + WBX daugtherboard could cover 10 MHz upwards, with a UBX you can basically digitize DC till 6 GHz seamlessly. These use Gigabit ethernet – which is very nice, because you can shut them away somewhere and just run a network cable to your PC.

SDRPlay does do the 10 MHz bandwidth, too, but that's its max; I haven't tried it myself. The driver is closed source and hence it's illegal to distribute GPL software linked to it; SDRPlay has made no attempts to correct that or even help the community to develop a inspectable driver themselves.

I'd rather go for the HackRF if I wanted to save money; proven driver, nice folks developing it, truly dedicated to supporting the open source community around that. They don't compete with Ettus for RF specs, I think, but really, great product, too.

The recommended utility/stack/drivers for capturing the raw samples based on the answer for #1 (or SDRPlay if no preference) (?)

I already mentioned GNU Radio. It comes with everything you need: A graphical designer for your signal flow graphs, if you prefer that. It generates python code that sets up the actual runtime; the signal processing is mainly done in C++ and highly optimized C. The Mailing list is pretty active and, in my opinion, extremely helpful.

GNU Radio is a signal processing *block*-oriented framework. You instantiate blocks that transform their input(s) to one or several outputs, and connect them before starting the flow graph. GNU Radio then takes care to get the data from A to B, and to maximize throughput.

It's, as far as I can tell, the most important FOSS SDR framework.

For example, not only does it come with ready-to-use easy-to-configure filter blocks, and channelizers, it also comes with ready to use FM demods, a lot of ecosystem with e.g. folks that demodulate OP25 in GNU Radio, and much more.

Regarding hardware interfaces: as mentioned, UHD, and thus, all Ettus devices, work seamlessly with GNU Radio. Same goes for many other devices, such as the famous RTL dongles, the HackRF, bladeRF, and quite a few more, through the excellent efforts of gr-osmosdr, which integrates a lot of drivers. There's also what I'd call a driver stub for the SDRPlay in there, but as said, you can never download a binary that links gr-osmosdr with the SDRPlay library, because, frankly, SDRPlay's licensing is inacceptable in a free-software-dominated landscape. I wonder what the purpose of making your driver proprietary is, if it's a driver you need to offer so that people can use your hardware.

Regarding GUI: There's exactly no GUI, unless you add one of the GUI blocks, e.g. to have a spectrum visualization. You'd not necessarily do that on the computer you're using to capture the signal – you could write a capture GNU Radio application, which you control remotely or just via scripts, which sends selected, reduced data to another computer for visualization e.g. again with GNU Radio. Doing so is as simple as having one of the several network sinks in the capture flow graph.

The recommended utility/stack for selectively demodulating and producing wav or .mp3 audio outs. (?)

Same as above – your framework should get you from hardware driver to audio file (or even audio driver output); it wouldn't be much of a useful framework. GNU Radio does that.

## Answer (score 3, by hotpaw2)

4 Raspberry Pi's each with an RTL-SDR dongle may well be cheaper than just one of the higher bandwidth SDR capture devices or a high end Linux PC. They run Linux. Network them together, with each one capturing a 2.5 to 3 MHz slice of the RF spectrum of interest, totalling over 10 MHz. That will also allow offloading your main Linux box, and allow doing significant parallel signal processing on multiple of the higher-end/newer/multi-core Pi's. You can easily run RTL-SDR IQ captures (and signal analysis) headless, via ssh and the command line, on multiple Pi's from a centralized Linux PC (or Mac).

There now seem to be Pi variants for under $10 USD.

Downside is that the cheap RTL devices only capture 8-bit samples, and are easily front-end overloaded.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7159/linux-based-sdr-spectrum-capture-via-cli, by jbrown, Marcus Müller, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
