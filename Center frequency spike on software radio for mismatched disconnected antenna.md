# Center frequency spike on software radio for mismatched/disconnected antenna

*Tags: antenna, receiver, software-defined-radio · score 7*

## Question

A while ago I was using a software radio receiver to perform some antenna analysis. I left the spectrum display on while disconnecting the cable and noticed that when the cable was disconnected I could see a very large spike in the frequency component at the center frequency of the display (where the receiver was tuned). I changed the center frequency several times and noticed the same spike appeared regardless of where I tuned.

Some time later I reconnected a cable and accidentally tuned to a frequency that was completely "out of spec" for the antenna I was using. The same spike appeared at the center of the display; I tuned around to several nearby frequencies and found that the spike stayed put. It disappeared when I moved back to a frequency at which the antenna was designed for operation.

**What is the nature of that spike** and why does it appear when tuned to a frequency at which the antenna is not resonant, as well as when the antenna is disconnected?

EDIT: Here are some screenshots of the spike I'm referring to:

This is an FFT of the received spectrum through an antenna tuned for the 2M band. Everything is nice and flat.

This is an FFT of the spectrum through the same antenna but at a completely unworkable operating frequency. The middle is a bit noisy but still shows the spike at the center frequency well.

Here's the FFT at the same frequency, but with no antenna connected. The spike is clearly visible here, and this is what I'm interesting in learning about.

## Accepted answer (score 1, by Phil Frost - W8II)

That is probably 1/f noise. This is noise where each octave has equal power. At lower frequencies, each octave is narrow, and thus has more power per unit frequency. It is ubiquitous in every electrical circuit, and in fact a great many physical processes.

This will always appear at the center of your FFT, regardless of where the radio is tuned, as the center of the FFT always corresponds to the frequency of your receiver's VFO input to the mixer. For example, if the VFO is tuned to 900 MHz, then a 900.01 MHz signal will appear at 900.01 - 900 MHz = 10 kHz, after mixing. 900 MHz appears at 0 Hz after mixing, the lowest frequency possible.

1/f noise is present in all electronics, and this is why you observe it even with no antenna connected. It can originate in the components that comprise the gain stages of the receiver like resistors and transistors, and noise so generated then goes on to be amplified and made visible in the FFT.

Better, and usually more expensive engineering can reduce noise like this, but in your particular case it would have negligible benefit. If you compare the scale on the left, this noise is significantly below the RF noise floor when you have an antenna connected. Consequently, [you will realize very little benefit from reducing the noise](Can%20I%20improve%20reception%20with%20a%20more%20sensitive%20antenna%20preamplifier%20better%20feedline.md).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2248/center-frequency-spike-on-software-radio-for-mismatched-disconnected-antenna, by mtrberzi, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
