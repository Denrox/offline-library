# Fourier transform of air breakdown impulse waveform

*Tags: antenna-theory, frequency, signal-identification · score 3*

## Question

i am a beginner on signal processing.

I learned from some papers, site online, including this forum that lightning discharge or any electrical arc emits wideband radio frequency. because the odd integer harmonic of a square wave. and electrical arc is similar to a square wave (Correct me if i am wrong, please)

So today i try to generate impulse voltage with multistage impulse generator, and here is the picture of the waveform from the oscilloscope

White : impulse voltage without air breakdown.

yellow: impulse voltage with air breakdown (electrical arc occurred on the sphere gap)

So when i generate the impulse voltage with air breakdown, its create an arc on the sphere gap. my question is can i get the frequency domain from this yellow wave with fourier transform? i am not really understand it yet, but since this is a non-periodic wave, can i get the frequency spectrum?

i want to know what exactly the **electrical arc create electromagnetic wave on a very wide frequency** really mean, and how.

Thankyou!

## Answer (score 3, by Phil Frost - W8II)

If you approximate the yellow trace as a rectangular function:

$$ \text{rect}(ax) $$

then the Fourier transform of this is:

$$ {1 \over |a|} \cdot \text{sinc}\left(\xi \over a\right )$$

Of course, a lightning impulse isn't exactly a rectangular pulse, but I suspect that does not substantially change the character of the frequency response: infinite, with periodic peaks that decay with increasing frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17731/fourier-transform-of-air-breakdown-impulse-waveform, by Ramanda Nvl, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
