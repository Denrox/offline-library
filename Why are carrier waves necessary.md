# Why are carrier waves necessary?

*Tags: modes · score 4*

## Question

I am studying for the technician exam and I have come across the section on carrier waves, basebands, and various kinds of modulation.

It makes sense to me that you create a signal by combining the baseband, which carries data, with the carrier signal (a sine wave of some kind) before transmitting.

My question is - why? What would stop us from just transmitting the raw data (voice or whatever) as it is? My guess is that "voice" frequencies for example are in the range of 300hz - 3000hz and we need to "boost" them up to the frequency we are on (for example 167.000 MHz). However this is just a guess.

## Accepted answer (score 5, by Glenn W9IQ)

The simplest answer is that the modulating signal, while it could be electromagnetic, will not have the desired propagation characteristics to carry out effective communications. By mixing the modulating signal with the carrier, the resulting signal has a much higher frequency that results in the desired propagation effects.

Hams often find that they cannot make their desired contacts on a given band (short frequency range) so they switch bands in the hope of making a contact. The modulating signal stays the same but the carrier frequency is dramatically changed as they switch bands.

Having the ability to change the carrier frequency also helps to avoid interfering signals or talk with another ham by tuning to their transmitting frequency.

## Answer (score 3, by Phil Frost - W8II)

This really depends on what you consider to be a "carrier wave".

If you consider it a sine wave at RF, then it may or may not be present. For example, an analog AM or FM station transmitting silence is just a pure tone: the carrier.

But silence in single-sideband (SSB) doesn't have a transmitted carrier: in fact if there's no audio doing into the microphone, the transmitter doesn't transmit anything. This is because is simply the baseband signal (voice into the microphone, for example) shifted up in frequency. If the transmitter is tuned to 10,000,000 Hz, and you whistle in the microphone a 500 Hz tone, the transmitter shifts that up by 10,000,000 Hz and transmits a tone at 10,000,500 Hz. In a sense, this is "transmitting the raw data".

However, 10,000,000 Hz is still the *carrier frequency*. Although it's not part of the transmission, the transmitter somehow needs to convert the baseband frequencies (your voice) up to RF. It does this by multiplying the baseband signal with a 10,000,000 Hz oscillator in a mixer. This alone is effectively an AM transmitter, so to make an SSB transmitter requires additional complexity to remove the second sideband from the transmission.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9761/why-are-carrier-waves-necessary, by Glenn W9IQ, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
