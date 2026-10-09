# Signal Source Block of GNU Radio

*Tags: software-defined-radio, gnuradio · score 4*

## Question

GNU Radio has a Signal Source Block which considers a set of variables to produce an output, namely sample rate, frequency and amplitude.

In signal processing, we define a basic waveform by its frequency, number of samples within the period and its amplitude. This holds true for waveforms such as Sine, Cosine, etc.

In GNU Radio, the sample rate doesn't really mean sample rate. And the frequency does not mean the frequency of the signal. This is really confusing to understand. I insert a screenshot of my build below

My question is, if sample rate is defined in the signal generator box, we do not need another throttle box. Because the Signal Generation box must know that it shouldn't generate more than the amount of samples it's advised in the configuration. However, if we remove the Throttle Box, the CPU goes to 100% and PC gets Stuck.

I would like a bit of clarification of on this issue. I'm sure I am wrong. People who made GNU radio must have been very smart people who have had a specific reason for doing this. I would like to know that reason.

## Accepted answer (score 8, by Marcus Müller)

You're on to something very right!

In signal processing, we define a basic waveform by its frequency, number of samples within the period and its amplitude.

I'd go a step further: In digital signal processing, the actual frequency doesn't "exist" any more. It's just "a periodic signal with a period of $T$ samples".

So that's exactly why for example digital filters are usually denoted relative to half the sampling frequency $f_s$ or simply $\pi$.

So that's exactly what the signal source does: It just takes your input of sampling rate and signal frequency, calculates $\frac{f_{sig}}{f_s}$ – and gets a value for how many samples a period should have (or how much of $2\pi$ to advance phase per sample – which is really nothing but just dividing $2\pi$ by that number).

Thus, a signal source configured with $f_{sig}=10,\, f_s = 100$ does *exactly* the same that a signal source with $f_{sig}=0.2,\, f_s = 2$ does.

GNU Radio doesn't even have any notion of what this sampling rate means – it just processes samples as fast as it can. That might seem strange at first, but when you think about it, every block that takes a "sampling rate" parameter just needs that value to "interpret" some other frequency (or time) with respect to that.

In a flowgraph where there is some SDR or other sampling device (an *osmocom source* getting data from an RTL-SDR, or the *USRP Sink* bringing samples to an USRP, or just an *Audio Sink* that attaches to a speaker, to give three examples), the samples actually only start flowing at the sampling rate physically in the hardware – GNU Radio still tries to get/give the samples as fast as possible.

For hardware sources, the mechanism is simple: GNU Radio asks the source "hey, do you have $N$ samples for me", to which the source usually responds as fast as it can, i.e. it will output the sampling rate of samples per second on average (but in "chunks" – GNU Radio doesn't push singular samples around. That would be far too much overhead). That limits the average rate of samples flowing through a flow graph; still, the pure software blocks will take these samples and process them as fast as possible, and then wait for the next chunk. That allows for maximum throughput – everyone works as fast as possible, and if they're done early, that's good (in fact, necessary), because it frees CPU to let the other blocks do their work, the OS do its job and so on.

Now, a hardware sink will simply take some time, the number of samples offered per iteration divided by the sampling rate, to consume the samples. That will simply put "pressure" on the buffers (GNU Radio buffers, ie. what connects blocks with each other are simply of limited size), because when a buffer gets full, the block that puts samples into that buffer simply doesn't get asked to do that until there's enough space in there again.

So, that's the situation with hardware blocks in your flow graph. Now, with software-only blocks, there's nothing slowing down the flow of samples – no hardware source that simply doesn't give your more than its physical sampling rate, and no sink that doesn't consume samples any faster.

Thus, in your flow graph (without the *Throttle*), GNU Radio simply asks the *Signal Source* to produce as many samples as there's free space in its output buffer. The *Signal Source* happily obliges and fills that buffer with a cosine of 32 samples per period – and then tells GNU Radio it's done doing that and it in fact did produce so-and-so-many samples. GNU Radio takes that info and tells the GUI Sink "Hey, there's so-and-so-many samples in your input buffer, get to work!", and the sink just goes ahead and processes these as fast as it can. It signals GNU Radio when it's done how many of the samples that it was offered it actually consumed – and GNU Radio then knows that this portion of the buffer is free again

Since that happens as fast as possible, this flow graph tends to eat up two processor cores completely, because GNU Radio is clever and maximizes throughput by distributing different blocks to different concurrent threads – that way, the source can already be producing the next chunk of samples, while the sink is still consuming the first one, leading to a scenario where there's practically no waiting for new input – there's always something to be done. Again, in a scenario where you want to process millions of samples per second coming from a hardware source, or going to a hardware sink, this is **very** desirable – simply because the throughput would be hard to achieve if everyone would be waiting most of the time instead of everyone trying to work as fast as possible on their own CPU core.

*Throttle* does exactly *nothing* to the samples. It's really just a "copy the bytes from the input to the output buffer" operation. But it just lets that copy action sleep() for a while to achieve an *average* throughput of the sample rate you configured. It's thus really just a tool for simulation at medium rates. Never use *Throttle* in conjunction with a hardware block – no two clocks are exactly the same, and if your hardware samples but a little faster than your Throttle throttles (because that's done with a rather inaccurate CPU clock time), you'll end up damaging your signal somewhere, either because your hardware sink didn't get things fast enough and had nothing to convert to analog when it was time, or because your hardware source completely runs out of buffers to put received samples to, and has to drop them.

## Takeaway

It's important to know that GNU Radio, and DSP in general, don't care about real-world sampling rates at all. It's just math applied to a sequence of numbers. How fast that sequence passes through the processing doesn't matter to the results of the math – the only point when these numbers get a physical meaning, and hence, a real sampling rate, again, is when they're passed to or from some sampling hardware.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6960/signal-source-block-of-gnu-radio, by Denis, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
