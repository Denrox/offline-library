# Confusion about SDR

*Tags: software-defined-radio, rtl-sdr · score 12*

## Question

I've just written code for the RTL2832 to receive and decode ADS-B packets (very cool!). I had some confusion about what is actually happening:

- Is the raw data coming from the USB dongle literally samples of the ~1090 MHz wave? Or is the carrier frequency first demodulated (in that case, what actually am I receiving?)
- What is the relationship between sampling rate and bandwidth? (I've read that it's equal; e.g. 1 MSPS = 1 MHz, but reading about higher end SDR setups doesn't confirm this)
- Isn't the ADS-B encoding scheme particularly sensitive to phase and sampling frequency differences (like if my receiver is slightly out of calibration)? It seems that if I were sampling just a little faster or slower, that I would have received a much different signal than the one below:

Thanks!

## Accepted answer (score 15, by Kevin Reid AG6YO)

Is the raw data coming from the USB dongle literally samples of the ~1090 MHz wave? Or is the carrier frequency first demodulated (in that case, what actually am I receiving?)

It's downconverted, not demodulated, using a local oscillator, mixer, and filters. That is, the signal you obtain is the same as if the transmitter had its carrier frequency set to 0 MHz instead of 1090 MHz (ignoring for the moment the fact that negative frequencies don't exist as propagating waves).

What is the relationship between sampling rate and bandwidth? (I've read that it's equal; e.g. 1 MSPS = 1 MHz, but reading about higher end SDR setups doesn't confirm this)

If your receiver has perfect antialias filtering, you can have bandwidth equal to sample rate (in a quadrature (IQ) system). In practice, your filter lets some out-of-band signals through, so whatever sample rate you pick, you get less usable bandwidth than that.

To demonstrate that the filtering is not perfect, find a continuous narrowband signal (e.g. weather radio), then change the hardware frequency gradually. As the signal gets closer to the edge of the receive bandwidth, it will decrease in amplitude — but when it gets to the edge it will *wrap around to the other side*, weaker! This is aliasing.

However, if you have a situation where *you do not need to reject nearby signals or noise* (that is, the signal you want to receive is stronger than everything else nearby in frequency), then you could use all of your sampling rate. But that is an unusual situation, and not robust against interference.

Isn't the ADS-B encoding scheme particularly sensitive to phase and sampling frequency differences (like if my receiver is slightly out of calibration)?

In this type of receiver, the phase and exact sample rate of your *analog-to-digital converter* is **not** the same as the phase and *symbol rate* of the signal you're receiving. Instead, the software has a a control loop which looks at the incoming signal (knowing its expected properties) and adjusts to match its phase and symbol rate.

The other way (phase-locking the ADC to the digital signal) is possible, but that requires additional hardware to precisely control the local oscillator, and makes the receiver hardware more specific to the characteristics of the particular modulation being received (rather than a general-purpose software-defined radio).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5830/confusion-about-sdr, by Nathan Wong, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
