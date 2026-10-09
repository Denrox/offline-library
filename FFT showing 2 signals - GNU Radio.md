# FFT showing 2 signals - GNU Radio

*Tags: gnuradio · score 6*

## Question

I receive OOK signals from a remote control in 433MHz. I'm using a dongle RTL-SDR on GNU Radio. The FFT output signal from the RTL-SDR Source block is represented on the picture:

My question is, why i have two signals with similar amplitude? Shouldn't it be only one?

The signal in the time domain:

The output in time domain after demodulate:

## Accepted answer (score 10, by Kevin Reid AG6YO)

#### What's going on

Most software-defined radios use **quadrature** in their signal processing architecture. This means there are two copies of the signal processing chain, with local oscillators that are 90° apart in phase while being otherwise identical. Once they reach software, they can be processed using complex number arithmetic (hence the "real" and "imaginary" labels on GNU Radio's time domain graph) which makes various signal processing operations much more straightforward.

However, if there is a problem with *one* of the two signals paths, such that there is significantly different gain between them (there will always be *some* mismatch since real components aren't perfect and even DSP has finite precision), then you will see what you see here — the signal appearing mirrored, having similar peaks on the positive and negative-frequency sides. (You can experiment with this in GNU Radio — take a signal, convert complex to pair of floats, multiply one by a constant, then convert back to complex, and watch the mirror image appear.)

Specifically in your images, notice that the copy is **at the same frequency with opposite sign** (−0.23 and +0.23) and also that it is **very strong** — in the time domain plot the line is nearly ±1.0, which is the absolute maximum representable value in the hardware. All RF hardware will deal worse with strong signals, but digital clipping like you seem to have here will abruptly produce spurious signals of many kinds.

#### What to do

What you can do is turn off the AGC on your RTL-SDR — it is not good at this task because it does not leave any headroom for suddenly appearing signals — and then set the manual gain setting until the spurious peak appears less but you still have enough signal to process. If that doesn't suffice, then install an attenuator in the antenna line, or relocate the antenna farther away. (Or try unplugging the antenna entirely; strong signals may be picked up anyway.)

Or, if you are solely trying to pick up that OOK signal and don't care about selecting it out of other nearby signals (filtering) or the cleanliness of the pre-demodulation signal, then you could just leave things the way they are and not try to tweak it. (The *general* risk here is that the receiver might be damaged by a too-strong signal, which you can't tell from the current situation once it's gotten strong enough to clip, but that seems unlikely from a simple battery-powered remote control.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12434/fft-showing-2-signals-gnu-radio, by Marcos Pinho, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
