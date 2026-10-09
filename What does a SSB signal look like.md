# What does a SSB signal look like?

*Tags: ssb · score 9*

## Question

I don't really get it. How is it possible to just send upper or lower side of a band (SSB USB/LSB):

And how is it possible to send anything without the carrier wave!

If I have misunderstood anything I am sorry because I am new to this and would like a answer.

## Accepted answer (score 5, by Phil Frost - W8II)

It looks like you are confused about what these graphs represent. Here's the diagram you used in the question:

Probably, this diagram is intended to be interpreted with the horizontal axis being time, and the vertical axis representing voltage or current.

Using that same representation, then SSB looks like this:

For comparison, AM looks like this:

and FM looks like this:

In fact, they all mostly look the same. Why? In these images, we can only see about 5 cycles of the carrier. While the carrier is modulated somehow, the highest frequencies in the baseband signal (your voice) are usually much lower than the carrier frequency. So although the amplitude or frequency may be changing, we can't see any significant changes over such a short span of time.

These images, because the X axis represents time, are said to be *time domain* representations.

However, one thing we know from Fourier analysis is that we can also represent any periodic signal in the *frequency* domain. We can represent that graphically by making the Y axis frequency instead of time.

To illustrate, we can look at a square wave in the time domain ($f$), and see how it can be represented in the frequency domain ($\hat f$):  
"Fourier transform time and frequency domains (small)" by Lucas V. Barbosa - Own work. Licensed under Public Domain via Wikimedia Commons.

We don't usually use square waves in radio communications because they have power spread over a wide range of frequencies. A square wave at 1 MHz also has energy at all the odd harmonics, 3 MHz, 5 MHz, 7 MHz, and so on. This would cause a lot of interference, since each station is typically allocated just a small channel in which to transmit. Broadcast FM, for example, is allocated a channel 200 kHz wide, and all their transmitted power has to fit in that. For example, from 89.7 MHz to 89.9 MHz.

Consequently, most transmissions look more or less like sine waves, since a sine wave has all its power at exactly one frequency. Then we vary the amplitude or frequency of this wave to carry information, but at a relatively slow rate compared to the frequency of the carrier.

Once you understand the concept of looking at signals not as a function of time, but as a function of frequency, then it is easy to say what SSB looks like: it looks just like the baseband signal (your voice), but shifted up in frequency to wherever the transmitter is tuned.

As an example, a whistle is approximately a pure sine wave. So if you whistle at 1kHz into the microphone, and the transmitter is tuned to 1MHz, then what you will see transmitted is a pure sine wave at 1.001 MHz (1 MHz + 1 kHz). If you make no sound at all, then nothing is transmitted.

If you get two people whistling at different frequencies, say 1 kHz and 2 kHz, then what you will see is the sum of two sine waves, one at 1.001 MHz and another at 1.002 MHz. Because these two frequencies are so close together, if we view it on any timescale where we can see the individual oscillations of the transmitter, it will just look like a sine wave.

So it doesn't really make much sense to think about what SSB looks like in the time domain, and consequently, most of the graphics you see represent the signal in the frequency domain.

## Answer (score 4, by PearsonArtPhoto)

Let's start with voice, just to show what it looks like. Voice doesn't have a "carrier wave". It simply contains the up and down level of the voice. Where the sound wave is 0 is effectively the carrier.

Typical AM signals take this signal, and modulate it with the carrier wave. Thus, the signal has a large peak at the peak of the carrier wave, and a relatively small part of the signal is everything else.

Okay, so how does SSB actually work then? Imagine that the signal contains signals that go both above and below the base value. Let's say you are broadcasting a tone, with amplitude X. The tone will have some signals with value X, and some with value -X, with a sinusoidal wave between the two.

With the figure you showed isn't really what is transmitted in SSB. Rather, it is a rectified sin wave, such that half of it is shown at 0, and the other half shown above. As sound doesn't really change that much over the frequency of sound waves, this is an acceptable way to show the signal. The carrier wave is then the part of the signal at 0. As that isn't really important, just not sending the 0 part of the signal removes a significant part of power that doesn't add much to the signal.

Bottom line, this chart from Wikipedia shows how the various modes work.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5101/what-does-a-ssb-signal-look-like, by Axel, Phil Frost - W8II, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
