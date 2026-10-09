# rtlsdr - hearing an FM broadcast on different frequencies

*Tags: rtl-sdr · score 4*

## Question

There is an FM station in my city which transmits at 105 MHz.

Today I discovered that I can also hear it quite well if I set the LO to 32.6 MHz and then shift the signal a bit. I'm using an rtlsdr with RT820T2 and gqrx.

Some of the combinations that work are:

```
LO: 32.6 MHz Broadcast: 32.4 MHz
LO: 32.7 MHz Broadcast: 32.8 MHz
LO: 32.8 MHz Broadcast: 33.2 MHz

```

So, an LO increase by 100kHz shifts the signal by 400kHz. How is this effect called and what is the formula to compute the frequencies?

**Edit 28.12.2020**  
I was able to research this a bit more today.

First, I found a lot of other posts describing the same effect, for example:

- FM broadcast mirrored to different bands - fault?
- Picking up FM Radio in the 20-30MHz range
- Hearing FM Broadcast radio at around 30mhz
- Why do I see commercial FM in the ~20 MHz range?
- Radio stations at 24-30 MHz band in Montreal, QC, Canada

The problem is that none of the answers in those threads satisfies me. They usually throw around terms like "overloading" and "intermodulation" without further explanation. I want to know exactly why, for example, 103.0MHz mirrors at 32.0MHz, and 106.0MHz mirrors at 33.0MHz - these are nice, exact integers, so I suppose that some rather simple formula which explains them should exist.

Second, I created a more detailed table of some of those frequencies in the range 32.0MHz - 33.0MHz (The range where this happens is much larger however, for me it's 26.6MHz - 33.7MHz):

- LO  Freq  Shift  Real Freq
- 32.0  31.4  -0.6  103.6
- 32.0  32.0  +0.0  103.0
- 32.0  32.8  +0.8  104.0
- 32.1  31.4  -0.7  104.0
- 32.1  31.8  -0.3  103.6
- 32.1  32.4  +0.3  103.0
- 32.2  31.8  -0.4  104.0
- 32.2  32.2  +0.0  103.6
- 32.2  32.8  +0.6  103.0
- 32.3  31.4  -0.9  103.0
- 32.3  32.2  -0.1  104.0
- 32.3  32.6  +0.3  103.6
- 32.3  33.2  +0.9  103.0
- 32.4  31.6  -0.8  105.0
- 32.4  32.6  +0.2  104.0
- 32.4  33.0  +0.6  103.6
- 32.5  31.6  -0.9  103.6
- 32.5  32.0  -0.5  105.0
- 32.5  33.0  +0.5  104.0
- 32.5  33.4  +0.9  103.6
- 32.6  31.8  -0.8  105.6
- 32.6  32.4  -0.2  105.0
- 32.6  33.4  +0.8  104.0
- 32.7  31.8  -0.9  106.0
- 32.7  32.2  -0.5  105.6
- 32.7  32.8  +0.1  105.0
- 32.7  33.6  +0.9  106.0
- 32.8  32.2  -0.6  106.0
- 32.8  32.6  -0.2  105.6
- 32.8  33.2  +0.4  105.0
- 32.9  32.6  -0.3  106.0
- 32.9  33.0  +0.1  105.6
- 32.9  33.6  +0.7  105.0
- 33.0  33.0  +0.0  106.0
- 33.0  33.4  +0.4  105.6

Third, this is a screenshot as I move from 32.5 to 32.6MHz.  Things that I want to note:

1. The strange way the frequencies move - they move up in frequency as the LO moves up - which is the opposite of what usually happens. You can see other weaker signals moving the usual way to the left.
2. These signals are really strong - the audio quality is actually great.
3. The amplifier gain is set to auto here, but I can hear audio if I set it as low as 20dB, and on some frequencies I can go down to 2.8dB and still hear the station.

## Answer (score 2, by hotpaw2)

Likely 5th order IMD (inter-modulation distortion), caused by a strong signal mixing with the 4th harmonic of another frequency (internal digitally synthesized signal or oscillator) related to the “LO” setting.

RTL2832 USB SDRs use an offset LO in the R820T mixer to produce an IF signal. A superhet, of sorts, followed by an IQ sampler at the IF.

Try an FM band blocking filter to reduce the level of the strong FM signal, and thus reduce non-linear mixing (clipping or overload) byproducts.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17650/rtlsdr-hearing-an-fm-broadcast-on-different-frequencies, by Ardavast Dayleryan, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
