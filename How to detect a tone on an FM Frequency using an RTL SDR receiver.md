# How to detect a tone on an FM Frequency using an RTL SDR receiver?

*Tags: software-defined-radio, rtl-sdr, linux · score 6*

## Question

I'm transmitting a simple tone which lasts 50 ms using an FM transmitter. I can see clearly this tone being received on my RTL-SDR device when I look at a spectrum graph (using GQRX).

I need to call a linux kernel function a soon as the tone is received, so I want a real-time solution which processes the signal. I'm thinking the best way would be to have the output stream piped into a shell program of mine via terminal, but I would need this stream to simply be a demodulated amplitude of the signal. I would then call my function when the amplitude has increased by enough of a factor.

Is there any way to achieve this?

## Answer (score 4, by Kevin Reid AG6YO)

If the tone is, or can be made to be, a DTMF tone or one of several other simple tone code protocols, then you could use multimon-ng to detect it. multimon-ng will output text corresponding to the detected tones. This also means you don't need to program the amplitude criterion. Something like this:

```
rtl_fm -f <freq> -s 22050 -M wbfm | multimon-ng -a DTMF -t raw - | <your program>

```

where “<your program>” is a program that waits for some input on stdin and calls the function you need. Explanation of the options:

- rtl_fm ... -s 22050 sets the audio rate appropriately for multimon-ng which requires an input sample rate of 22050 Hz.
- rtl_fm ... -M wbfm is because you say you're using a "FM car radio” to transmit, by which I assume you mean those low-power transmitters intended for use with a car stereo. Broadcast FM is wideband FM, not the narrowband FM used by amateur / two-way radios. If you were using one of those, it would be -M fm (or left out as that's the default).
- multimon-ng ... -a DTMF tells multimon-ng to decode DTMF only and not try anything else.
- multimon-ng ... -t raw - tells multimon-ng to read from stdin rather than opening an audio device.

You may also wish to use the frequency correction PPM, gain, filtering, etc. options to rtl_fm; that would be a whole other article, and so I just want to point out they exist.

The output of multimon-ng will be one line per detected code with the prefix DTMF:, like this:

```
DTMF: 1
DTMF: 2
DTMF: 3

```

There are several other codes multimon-ng supports that you could use — I suggest researching the codes mentioned in multimon-ng's readme. You could even use MORSE_CW (Morse code), which doesn't have a specific pitch but does have specific durations of the tones (a lone 50 ms tone would always decode as “E”).

It would also be reasonable to build this within GNU Radio, which would allow integrating all of the signal processing in one program and more choices of RF hardware. However, it would require considerably more code to set everything up.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5020/how-to-detect-a-tone-on-an-fm-frequency-using-an-rtl-sdr-receiver, by Ash, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
