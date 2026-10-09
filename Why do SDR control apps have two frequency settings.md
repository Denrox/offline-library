# Why do SDR control apps have two frequency settings?

*Tags: software-defined-radio, rtl-sdr · score 10*

## Question

Why do many SDR control apps have two frequency settings, even when the app is designed or set up only for listening to or decoding one signal? Should the two SDR frequency controls be set differently or the same? If different, how much for which modulation schemes (CW, USB, LSB, AM, etc.), in which direction, and why?

## Accepted answer (score 12, by Kevin Reid AG6YO)

One controls the hardware, and the other controls the software.

1.

The *hardware* selects some section of the entire RF spectrum (by a local oscillator and mixer), and down-converts it into a frequency an analog-to-digital converter can handle, filters it (to discard out-of-band signals), samples it, and delivers that data to the computer.

This data determines what you can *see* in the so-called “waterfall” or “panadapter” displays. It also sets the limit for the widest-bandwidth signal you can possibly demodulate.

2.

Then the *software* does a similar process in order to select a *single signal* to demodulate; it shifts it to baseband (a “0 Hz” signal which only varies according to the modulation), applies a low-pass filter, and demodulates appropriately.

Both stages have their own controllable local oscillator, and those two controls are what you are seeing.

Here are some reasons for there to be these two separate stages:


Analog hardware is imperfect; there are various sorts of garbage you can get in the digital signal (DC offset, IQ imbalance, insufficiently filtered out-of-band signals). You can change the hardware center frequency to shift the garbage *away* from the signal of interest.

For example, if there is a DC offset (RTL-SDRs with E4000 tuners do) then you have garbage at the center frequency, so you would set it to be slightly different from the signal of interest so that the following digital filter removes that part. **This is one of the main reasons to specifically set the two frequencies differently,** if your receiver has this problem. It doesn't matter which direction you offset, as long as the offset is enough that the bandwidth of the desired signal doesn't overlap the unwanted signal.

On the other hand, filtering is imperfect and the way this shows up in the signal from the hardware is that signals which are *out* of the tuned band, but strong, will be seen to “wrap around” and appear at an in-band frequency modulo the hardware bandwidth (sample rate). This is a reason to receive *close* to the center; the hardware filtering is at its best at that point.

I highly recommend playing with changing the (hardware) center frequency slowly and watching and listening to how the displayed signals change or don't. You will learn what to do.


If you are interested in monitoring a whole band rather than a single station (e.g. a single amateur HF band) then keeping the hardware settings fixed leaves your waterfall display undisturbed to watch activity over the whole band while you are free to select which stations you are currently demodulating (listening to).


Digital filters can be optimized for the particular mode in use, and, if you don't care about power consumption, be extremely sharp (good at selecting exactly what is wanted) compared to analog filters. They can also be adjusted in bandwidth or shape to trade off filtering out nearby unwanted signals vs. better intelligibility in the absence of nearby signals. (Note that this is a reason for the two-stage architecture, but it isn't directly a reason to have independent tuning controls as you've asked.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1407/why-do-sdr-control-apps-have-two-frequency-settings, by hotpaw2, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
