# GNU Radio - Signal Keeps Getting Smaller?

*Tags: software-defined-radio, gnuradio · score 3*

## Question

Really bizarre issue here. Here is an image of a signal taken from SDR Sharp:

Freq: 926.365M Bandwidth: 30k

Now, using the above measurements, here is this same signal observed in GNU Radio with the QT Waterfall Sink at 5M sample rate:

Here is the same signal at 2M sample rate:

Here is the same signal at 10K sample rate:

And at 1K:

This cannot be possible?!

My GNU Radio flow is as simple as possible, but here's what it looks like:

Can anyone explain this? Surely as I close in on the signal, it should be filling up the Waterfall much more.

## Answer (score 3, by Kevin Reid AG6YO)

Most likely, the sample rates you are asking for are unsupported by the hardware. The osmocom source is just a wrapper around a bunch of specialized device drivers, and generally you're not going to notice if you don't get the sample rate you asked for unless you're also e.g. using an audio sink so you hear the audio skipping.

If you're programmatically interacting with the source you can get a list of supported sample rates, but this isn't easy within GNU Radio Companion; the usually convenient thing to do is look at the source code within gr-osmosdr for the interface for the particular hardware you're using.

In order to actually get a lower sample rate, you must start with a supported sample rate and then use a decimating filter block (there are many) to convert to the one you want.

Note that having a high sample rate is not necessarily completely wasted; the information in the extra samples, as processed by the filter, allows you to get more dynamic range as if your ADC had more bits per sample.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9432/gnu-radio-signal-keeps-getting-smaller, by JWinstanley, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
