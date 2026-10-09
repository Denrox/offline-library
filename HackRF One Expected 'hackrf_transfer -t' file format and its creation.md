# HackRF One — Expected 'hackrf_transfer -t' file format and its creation?

*Tags: software-defined-radio, hackrf · score 5*

## Question

What **file format** does the HackRF One **expect on the command line**, using the -t option with hackrf_transfer?

Also, how would I **create or convert** that format from a standard WAV file?

I was expecting the following to transmit a 36 second wav file:

hackrf_transfer -t test.wav -f 145500000 -p 1 -a 1 -x 47

But it just quits (without intervention, despite what it says) after 1 second or so, with the following:

```
call hackrf_sample_rate_set(10000000 Hz/10.000 MHz)
call hackrf_baseband_filter_bandwidth_set(9000000 Hz/9.000 MHz)
call hackrf_set_freq(145500000 Hz/145.500 MHz)
call hackrf_set_amp_enable(1)
call hackrf_set_antenna_enable(1)
Stop with Ctrl-C
 3.7 MiB / 1.000 sec =  3.7 MiB/second

User cancel, exiting...
Total time: 1.00032 s
hackrf_stop_tx() done
hackrf_close() done
hackrf_exit() done
fclose(fd) done
exit

```

## Accepted answer (score 6, by Kevin Reid AG6YO)

Outside of the -w receive options, hackrf_transfer always deals in 8-bit signed IQ samples, raw with no file headers.

You must also make sure that the sample rate of the data matches the sample rate specified on the command line and is a rate supported by the HackRF hardware. WAV files contain the sample rate information in a header, but raw files have no place to put it, and in RF signals it can be undesirable for programs to attempt automatic sample rate conversion anyway.

### Modulation

Before considering converting a WAV file, you need to ensure you actually have RF (IQ) samples, not audio; that is, it must be *modulated*. If you got the recording from another program which explicitly says it produces IQ output, then that's fine.

If you have audio data, and the signal is intended to be fed to a single-sideband (SSB) transmitter, such as most HF digital modes, then you can use it anyway, but you will get double-sideband (DSB) transmission — two copies of the signal, one with the spectrum inverted. This may be adequate for testing purposes, but don't make a habit of it as you're wasting bandwidth.

If you have audio data which is intended to be modulated as FM (such as an AFSK APRS packet, for example), then you will need to modulate it. This can be done fairly easily given the right tools, as I will describe below.

### Conversion

I recommend that you install **GNU Radio**. While it is primarily intended for real-time processing, and can in fact talk directly to the HackRF One, it can also be used to convert files.

In GNU Radio's graphical tool, **GNU Radio Companion**, you can design a "flow graph" to read a file, write a file, and do any particular conversions along the way, such as for your case:

Here we take the two “stereo” channels of the WAV file (which GNU Radio automatically converts to floats in the −1 to +1 range), put them in alternating left-right-left-right sequence, resample it from an assumed rate of 44.1 kHz to 2 MHz (that being the minimum supported by the HackRF One), rescale to −127 to +127, and write to the raw output file (which will have the same sample rate as the input file).

If you needed to perform modulation (as I described above) as well, that would be just another block or two in this chain.

Unfortunately, GRC does have some limitations — for example, this has the filenames hardcoded into it. But GRC generates (overly verbose) Python programs which you can then clean up into something reasonable, or write from scratch once you're familiar with the vocabulary.

There is a lot to learn to use GNU Radio effectively, but it is a very useful tool for SDR experimentation, if with some rough edges, and I recommend it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5450/hackrf-one-expected-hackrf-transfer-t-file-format-and-its-creation, by M6JNY, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
