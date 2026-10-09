# Multiple simultaneous tunings with SDR

*Tags: software-defined-radio · score 10*

## Question

I just found out about WebSDR, and I was wondering how is it possible that many listeners listen and tune to different stations simultaneously. Which components/technologies allow this, and how does this roughly work?

## Accepted answer (score 10, by Kevin Reid AG6YO)

Software-defined radio is radio where the signals are sampled and converted to digital data early in the process. This means that like any digital data, they can be copied without loss of quality. Computers can execute the same calculation many times. Thus, a SDR program can take one input and process it *differently*, as if it were many different radios.

That's the fundamental concept. However, making this work still requires you to have the digital signal you need — all of the hardware which works in the analog domain, gathering the radio waves and converting them into a digital signal, must be able to *simultaneously* receive everything everyone wants.

This turns out to not be hard at all with modern electronics. Every radio signal has some bandwidth — some *range* of frequencies which it occupies. (A signal at exactly one frequency conveys no information.) SDR receiver hardware takes the signal and converts it to digital samples using a sampling rate that is high enough to preserve the entire bandwidth. If you take a receiver capable of receiving a wide-bandwidth signal and tune it to where several narrower (and closer spaced) signals are present, the digital signal resulting contains *all* of those signals, at different frequencies within itself.

Such a multiplexed signal is then processed in software using digital versions of the same components that an analog radio would — mixers, filters, and demodulators — to extract individual signals.

A multi-user software-defined radio simply has to run a differently-configured copy of those components for each user.

Then the only remaining matter is that the receiver hardware is capable of bringing in a signal of enough bandwidth and sample rate to contain all the users' desired tunings. This is *exactly the same technology* as enables high data rate digital wireless communications — **high sampling rate ADCs** to convert those digital signals.

The other element of such an SDR is a antenna suitable for receiving the entire bandwidth. Generally, *any* antenna *can* be used for receiving across a wide bandwidth, but the signal level will be much weaker away from the optimal frequencies.

For “higher” bands (VHF and up), a single antenna of ordinary design can do the job, just as antennas for scanners do.

Receivers for all of HF, like the University of Twente WebSDR, take the approach of using a physical antenna that is, loosely speaking, equally bad at all frequencies of interest, followed by a built-in amplifier (LNA) to increase the signal level for the receiver — most famously in this context, the PA0RDT “Mini-Whip” design.

Note that “all of HF” is just 30 MHz, which is not that much these days. A single Wi-Fi signal can occupy 40 MHz.

## Answer (score 4, by Phil Frost - W8II)

Tuning in an analog radio is accomplished by adjusting oscillators or filters so the desired station falls within the radio's passband. For a SSB receiver, this passband is somewhere between 3 and 6 kHz wide. The output of the demodulator then goes to a speaker. The filters can't be wider than that, otherwise you'd hear nearby stations.

If the output is fed into an analog to digital converter such as a computer sound card, you now have an SDR. With an analog solution, tuning two stations would require a physical set of filters, oscillators, and mixers. But in a computer it's just another instance of a program running, so it's easy to have any number of concurrent listeners. The analog passband can be wider since digital filtering can further narrow the passband as necessary.

With most of the processing done in the computer, the analog radio can become simpler. For example see the Softrock Lite II, which is an analog radio for about $20 USD. You provide a computer and a sound card to make it an SDR.

The Softrock is a cheap solution, and the low sample rate of the sound card limits the bandwidth that can be processed. But with a little money it's possible to upgrade the analog to digital converter to one operating at a sample rate of tens or hundreds of MHz, and add an FPGA to handle the increased computational demand. Since the radio isn't transmitting the antenna doesn't need to be especially efficient, so a small whip into a high-impedance buffer makes a good wide-bandwidth antenna. With a sample rate of 30 MHz it's possible to tune the analog radio to 0-30 MHz and have the entire HF band (and everything below it) available to users over WebSDR.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9510/multiple-simultaneous-tunings-with-sdr, by Cobe, Kevin Reid AG6YO, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
