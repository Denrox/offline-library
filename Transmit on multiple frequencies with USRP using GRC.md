# Transmit on multiple frequencies with USRP using GRC

*Tags: software-defined-radio, frequency, transmission, gnuradio · score 3*

## Question

I am using an Ettus Research B200 with GNU Radio Companion (GRC) and I would like to transmit two signals at two different frequencies simultaneously.

As a simple example, I would like to transmit a sine wave at 915 mhz and another at 916 mhz, both at the same time.

The frequencies are within 2 mhz of each other, so I would imagine that this is possible. Not having any luck messing with GRC to make this work; I'm a total noob to SDR! Which blocks do I need to use in GRC?

## Accepted answer (score 5, by Kevin Reid AG6YO)

To transmit two signals at once, just generate the two signals with the appropriate frequency spacing between them, and add them together.

With your mentioned frequencies, you might generate the signals at −0.5 MHz and +0.5 MHz, add them together, and transmit with the hardware center frequency set to 915.5 MHz. (You don't have to use the exact midpoint, but doing so allows you to use the lowest sample rate and filter bandwidth.)

Specifically to transmit two unmodulated sine waves, in GRC:

- Create two Signal Source blocks, complex sine, with their carrier frequencies set to -0.5e6 and 0.5e6.
- Connect them to two inputs of an Add block.
- Connect the output of the Add block to your (USRP) sink block with center frequency 915.5e6.

If you want to use a modulator that produces a baseband signal, you will have to take that baseband signal and frequency-shift it to the desired offset, in place of the signal source which creates the signal at any frequency.

Unfortunately, there's no block that is actually convenient for this purpose; the easiest is the "Frequency Xlating FIR Filter", which does decimation as well as shifting. Just enter 1 for the decimation, [1] for the filter taps, and it'll do the job.

The “Rotator” block does pure frequency shifting, but it needs the shift specified as a complex vector (amount of rotation per sample) so it's not convenient to use.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6128/transmit-on-multiple-frequencies-with-usrp-using-grc, by Shrout1, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
