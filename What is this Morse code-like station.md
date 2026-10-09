# What is this Morse code-like station?

*Tags: software-defined-radio, uhf, rtl-sdr, signal-identification · score 3*

## Question

I’m trying to identify this signal at 928.807 MHz. A sample of the raw I/Q from gqrx is here (9.2 MB, .wav, 48000 Hz) and this is the waterfall:

I’ve tried decoding some common digital modes (including CW) with fldigi but have not had success.

I’m using an RTL-SDR with a telescopic antenna, and I’m in Stillwater, OK.

## Accepted answer (score 2, by Marcus Müller)

Been probing around in your signal.

The longer "blips" definitely start with a tone (... with a region where phase is a linear function of time), but then it looks rather random.

So, likely, a PSK system with some constant tone preamble?

My quick & dirty analysis tool here is Miek's inspectrum

You'll need to convert your wav back to 32bit float complex first (audacity can do that. I don't know whether GQRX has a direct export functionality for that).

Three representations of the signal in the picture:

1. topmost, a (horizontal) waterfall of your signal (I just realized I didn't properly set the sampling rate, so ignore the time axis labels). If I hadn't put the red line across it, you'd clearly see the aforementioned tone as horizontal line at the beginning of the "white selection" (and at the end, too. If I'm doing the math right, the temporal length between these two is about 60ms)
2. below that, a derived phase plot. Note the "more or less clean" linear phase ramps. (frequency is the derivative of phase, and if phase is linear, than frequency is a constant)
3. below that, simply the I and Q (real and imaginary) part of the signal filtered to the (vertically white limited9 bandwidth).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7419/what-is-this-morse-code-like-station, by Henry Elliott, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
