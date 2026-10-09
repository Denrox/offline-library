# Cause of harmonic spurs?

*Tags: software-defined-radio, testing · score 6*

## Question

Harmonic spurs (harmonics of the transmitter frequency, as seen by a wide-band receiver or SDR) in the RF spectrum might be caused by an imperfectly sinusoidal or badly filtered transmitter carrier frequency oscillator, non-linearities in the transmitter amplifier, or non-linearities somewhere in the receiver before or inside the 1st mixer.

What might be some tests or other means for helping determine where (most of) this harmonic spur problem might be located? Are there any ways to test this without needing to acquire extremely expensive lab equipment? Basically, are the spurs a transmitter or receiver problem? (assuming neither comes with manufacturer specs, e.g. home-built or kit, etc.)

## Answer (score 7, by Marcus Müller)

You've nailed this!

So, I'm sometimes involved in these kinds of investigations. It all gets easier when you have control over the transmitter – when some spurs disappear as soon as you turn it off, but others remain, you've ruled out the transmitter as the source of these.

Then, digital receivers typically, as you notice, have different sources of spurs. As I'm usually not at the receiver that is being "debugged", the only way to work with this is really an elimination approach; in no particular order, Problems, the way I'd approach detecting them and some mitigation hints:

## Problem sources

### Harmonics all over the place: clipping?

Reduce receiver gain. Add attenuator. Can usually (often, depending on the receiver DSP chain) be seen by looking at the numerical values of samples coming from device; it should be $|z| < 1$. If not: Looks like $(1)$

### Spurs due to intermodulation of receive signals due to receive (typically: LN) amplifier saturation

Add attenuation in-line to receive antenna. If spurs significantly reduce, we've got this.

### LO leakage & DC offset

Typical artifact of all direct conversion receivers. Can (on some SDR peripherals) completely be mitigated by letting the built-in DSP functionality digitally shift the receive signal in frequency prior to decimation, see $(2)$. For a "relatively good" mitigation: a notch HPF directly after the ADC is often part of SDR receivers, too.

### Sampling clock spurs

Mixing products of receiver LO and ADC clock. Tune the LO a few Hertz to either side. Do they move, but keep the same distance from LO leakage?

### Unwanted LO synth side products

Oscillator synthesizers are impressive devices, which are able to produce a huge number of tones from a single reference oscillator (example: MAX2871). They do that by elegantly multiplying frequencies, and having non-integer multiples through cleverly "jumping" PLLs (keyword: fractional-N PLL). That inherently, however, might produce some frequencies that are not even multiples or integer divisions of the target clock. If you can, try a configuration where you use integer-N tuning only. If that helps, there's your problem. Often, when using a wideband receiver especially if it supports $(2)$, you can choose from a whole range of physical LO frequencies without affecting what part of the spectrum you see. Experiment!

### Digital Operating Clocks

SDR devices are digital devices, thus have a lot of square wave clocks... If you see something that happens to be relatively strong, and research shows it's one of $1\cdot f_{clock},\, 3\cdot f_{clock},\, 5\cdot f_{clock},\ldots$, there you go. You'll have an easier time figuring out $f_{clock}$s that appear in your device if you have a schematic, and knowledge of Firmware/FPGA images used.

### Supply Noise

A classic. If the SDR has an external power supply, try a different one, ask the manufacturer about known spurs, and use ferrites where applicable.

### Digital Interface Noise

Your SDR device is a USB1/2 device and you see a $N\cdot11$ MHz signal, spread around with some rather "sinc"-y shape: USB's to blame, typically. Applies to other buses with other baud rates, too. Hard to mitigate if hardware's fixed.

### Phase noise of LO

The aforementioned synthesizers are typically pretty good; this often stems from phase noise of the reference oscillator. If possible with yout device: try a "less accurate" (read: you got lying around) one, and compare.

### Reference oscillator overtones, noise through ref oscillator input

Yeah, not all things that seem to be a good idea actually are. I've seen it more than once that people, thinking their external high-accuracy, long-time stable oscillator would significantly improve operation, only to find out later, that the reference signal not only contains the wanted (e.g. 10 MHz) tone, but also other components, partly from supplies etc. Make sure your reference is clean! If in doubt, try the internal one, too!

## Illustrations

### (1)

By twitter user "da Swede", https://twitter.com/uber_security/status/844116167870627841

### (2)

*Offset tuning with the DSP chain of an Ettus USRP". By myself, copyright Marcus Müller/Ettus Research.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7416/cause-of-harmonic-spurs, by hotpaw2, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
