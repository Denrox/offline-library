# How does FM encode BOTH amplitude and frequencies of full audio signal spectrum?

*Tags: fm, math · score 7*

## Question

How does frequency modulation encode both amplitude and frequency of the modulating audio signal only by varying frequency? How do both components get spread across and encoded in the side bands? I generally understand that AM side bands occupy sufficiently wide band width to recreate the spectrum of the modulating audio signal (while varying amplitude at each frequency in the spectrum of the sound wave)--so the spectrum of a side band should look basically like the spectrum of the underlying modulating audio wave. Is this understanding wrong?

My understanding is that FM modulates the instantaneous frequency of the carrier signal according to the amplitude of the modulating signal, but the modulating audio signal should be made up of a wide spectrum of frequencies at various amplitudes that make up the underlying sound. So the carrier can only be modulated with a single frequency of varying amplitude. What about the other frequencies in the audio signal spectrum? Is this information spread out across the side bands somehow? If so, how?

(I am studying for my technician license; I don't know Fourier math.)

## Accepted answer (score 11, by Phil Frost - W8II)

Whatever modulation we use, there's a baseband signal we wish to transmit (music, voice recording, whatever), which somehow modulates a carrier to produce the output signal.

Your question suggests you are primarily concerned about how the frequency domain representation of the baseband translates to the frequency domain of the output. This is a valid thing to wonder, and it has particular relevance to determining how much bandwidth will be occupied by the transmission for a given input, for example. But it's not always the best way to understand a modulation scheme. That's better done in the time domain.

For AM, we modulate the amplitude of that signal. Let's say the baseband signal is a square wave. Here's an example of a "loud" square wave and AM, with the baseband in red, and the output in blue.

With a quieter baseband input, the variation in amplitude of the output is less.

For FM, we modify the frequency instead of the amplitude. Here again is a loud square wave. Note the large variation in frequency between the periods where the square wave is a large value, versus where it's a low value:

With a quieter baseband input, the variation in frequency is less:

Of course in practice the baseband signal will be something more interesting than a square wave. Here's an AM example with a more complex input:

Note the baseband waveform can be anything at all: it can have any number of frequency components, at any number of amplitudes. But that's not necessarily relevant: all we need to know at any instant is the value of the baseband signal, and that's what the amplitude of the carrier is.

And now with FM:

What does FM look like in the frequency domain? Let's generate some waterfall plots with a sine wave baseband which changes only in frequency or amplitude.

Altering the baseband amplitude increases the amplitude of the FM sidebands. Here's a sine wave baseband, increasing in amplitude.

Increasing the baseband amplitude is equivalent to increasing the modulation index or deviation. You can see that even with just a sine wave baseband, there are several sidebands generated. Mathematically, these repeat out to infinity, but in practice they can be ignored at some point. A typical modulation index will be such that there are at least a few sidebands, otherwise most of the power would be in the carrier, making inefficient use of transmitter power.

Altering the baseband frequency changes the spacing between the sidebands. Here's a sine wave input of constant amplitude, increasing in frequency:

Of course in practice baseband will contain many frequency components, varying in amplitude. Because even a single baseband frequency generates several sidebands, the individual frequencies in baseband create overlapping output frequencies and the result is a jumbled mess, visually.

## Answer (score 5, by Kevin Reid AG6YO)

I generally understand that AM side bands occupy sufficiently wide band width to recreate the spectrum of the modulating audio signal (while varying amplitude at each frequency in the spectrum of the sound wave)--so the spectrum of a side band should look basically like the spectrum of the underlying modulating audio wave. Is this understanding wrong?

This is correct, but it is useful to understand that the *process* of amplitude modulation does not treat frequencies individually. The structure of the sidebands is a *mathematical consequence of* the modulation process, not the process itself, which doesn't involve any frequencies explicitly at all.

My understanding is that FM modulates the instantaneous frequency of the carrier signal according to the amplitude of the modulating signal

This statement is not correct, and could be the root of your confusion. The frequency is modulated according to the instantaneous *value* of the signal, not the amplitude.

To illustrate the difference between value and amplitude, in the simple sinusoidal signal

$$ y = A \sin(t),$$

$y$ is the value and $A$ is the amplitude. Defining amplitude gets more subtle with more complex signals, but this is sufficient to understand the distinction. Here, $A$ is (may be) constant but $y$ is not.

Any signal (of the kind we are concerned with when talking about AM and FM), no matter how complex, is still a single value, a single number, varying over time. If you transform that value in some way (in FM, to frequency), and then reverse the transformation correctly (a FM demodulator), then you have the original signal.

In practice there are deliberate limitations to these processes — deviations from the mathematical ideal — which mean that the higher frequencies of the modulating signal are attenuated (bandwidth is not infinite). But those can be understood independently of the modulation techniques themselves.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7440/how-does-fm-encode-both-amplitude-and-frequencies-of-full-audio-signal-spectru, by Tom Zahner, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
