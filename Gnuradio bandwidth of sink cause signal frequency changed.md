# Gnuradio bandwidth of sink cause signal frequency changed?

*Tags: gnuradio, frequency, bandwidth · score 4*

## Question

System is debian 10 with gnuradio 3.7.

untitled.grc create simple flow graph as below:  
The only difference between 2 flows is bandwidth of gui sink,cause 2 different signal frequency as below:

Why Gnuradio bandwidth of sink cause signal frequency changed?

## Accepted answer (score 5, by Phil Frost - W8II)

Gnu Radio doesn't really know anything about frequency in cycles per second (Hz), only cycles per sample. The left of the chart is -0.5 cycles per sample, the middle is 0 cycles per sample, and the right is +0.5 cycles per sample. It's up to you to enter the correct numbers for "bandwidth" and "center frequency" if you want the scale on the bottom to correctly map the frequency back to cycles per second.

For example, your two signal source blocks are configured with a sample rate of 32k and a frequency of 10k (Hz). This means they will output a signal at a frequency of:

$$ \require{cancel} {10\mathrm k\ \text {cycles} \over \cancel{\text{second}}} \times {\cancel{\text{second}} \over 32\mathrm k\ \text {samples}} = {0.3125\ \text{cycles} \over \text {sample}} $$

Try configuring these signal sources to output 20 kHz at a sample rate of 64 ksps: you'll find they output the same thing, because 20/64 is also equal to 0.3125.

If you know the sample rate, then you can divide a frequency in Hz by the sample rate to get frequency in cycles per second.

Or you can multiply by the sample rate to convert cycles per sample to frequency in Hz.

None of the blocks know the sample rate except what you configure in the block's parameters. Any block that asks for or provides any number in Hz is implicitly making this conversion between cycles per sample and cycles per second. If you enter incorrect information in these parameters, you will get incorrect results.

The default GRC project has a variable sample_rate, and the "Bandwidth" parameter defaults to that. You might want to change that if you are decimating or interpolating the sample stream, but in the example provided you'd want to leave it at the default so the GUI sink's "bandwidth" is equal to the signal source's "sample rate".

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18842/gnuradio-bandwidth-of-sink-cause-signal-frequency-changed, by kittygirl, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
