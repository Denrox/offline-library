# What causes the light and dark bands (of background noise) in an HF waterfall display?

*Tags: propagation, frequency, noise, panadapter-and-waterfall · score 4*

## Question

While monitoring the 40-meter band (among others) throughout a typical day/night as propagation changes I have noticed there are often bands of very low noise (black area) and others with much higher noise (some color) in the waterfall display. These are much too consistent, persistent, and wide bandwidth to be intentional signals of any type.

My two-part question is:

1.

What causes those light and dark bands in the waterfall? (More specifically, what causes there to be background noise patterns like that. They are just easier to see on the waterfall obviously.)

2.

If I was looking for a clear frequency transmit on and there was a spot in a dark band and one in a light band would one expect a better signal propagation in one over the other?

Hypothesis: My best guess is that this is something do with signals being absorbed, reflected, transmitted or not transmitted from a distance by or through one of the ionosphere layers. Still, I'm wondering if there is something more specific and how the phenomenon relates to the second part of this question.

**Requested example screenshots:** I know the WSJT-x "waterfall" is not technically the same as the waterfall display of an SDR but I don't have that hooked up right now. However, the visual effect is similar.

Example running FT8 on 40M

Example running WSPR on 20M

## Accepted answer (score 2, by Scott Earle)

What you are seeing there is the frequency response of your receiver's audio stage (or possibly even the input of your computer's sound card). It is amplifying frequencies around 300Hz and 2500Hz much more strongly than it is amplifying frequencies less than 100Hz, and those between 800Hz and 1700Hz. It's clear on both those screenshots, even though you are (presumably - you don't do FT8 on the same frequencies as WSPR) tuned to different RF frequencies.

It's not something you need to worry about, as the digital modes in question don't depend on absolute signal strength at a specific frequency as much as they rely on signal-to-noise ratios.

## Answer (score 2, by hotpaw2)

Often, the source of bands of noise in an SDR spectrum is locally generated RFI or EMI. During a neighborhood power outage, one might notice a large number of these bands disappear. Sharper bands in the waterfall can sometimes be mitigated by reducing or choking EMI sources in your "shack".

Other possible sources for these bands can be ripple in passband of the various digital filters in the DSP signal chain (for anti-aliasing, decimation, FFT windowing, audio, etc.)

Yet another possible source might be antenna gain and pattern, which can vary with frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15701/what-causes-the-light-and-dark-bands-of-background-noise-in-an-hf-waterfall-di, by Josh, Scott Earle, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
