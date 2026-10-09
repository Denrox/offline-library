# Substitute for 455 kHz Ceramic filters in new designs

*Tags: receiver, equipment-design · score 5*

## Question

I am looking to design a dual conversion FM receiver/power meter for t-hunting similar to the MK4 sniffer using 10.5 MHz and 455 kHz IF. In my research it appears that manufactures have stopped making 455 kHz ceramic filters. I am in the U.S.A. and the only thing I can find still in production is in England.

My question is what can/is used for a very high Q if filter (Q of about 45 = 455 kHz / 10 kHz) at 455 kHz in the absence of ceramic filter/discriminators.

## Answer (score 6, by Marcus Müller)

Since this platform considers questions asking for products as off-topic, I'll interpret your question as:

I have an IF receiver, but there's no good filters for the rather low IF it uses (455 kHz). What to do?

If you're doing a new design, simply pick an IF that works with the filters you can get.

That, and pretty much nothing else, is what defines what IF is chosen in commercial detectors. Your high-sensitivity Spectrum Analyzer does that. Your cheap FM Radio receiver IC does that.

On the other hand: If you're just reworking a superhet where the final receiver stage failed, then consider why you need the IF filter:

Its purpose is to isolate the wanted spectrum from all the unwanted stuff, so that noise and interference has lesser influence on the receiver. That's why you want that IF filter to be sharp; and that's why you'd use an IF to fit your filter (and not the other way around). Adjusting an oscillator to a different LO frequency is easy, building a good filter for an arbitrary frequency band is not.

Now, what if I tell you that 455 kHz is "practically baseband" in 2019. If you, say, build a very relaxed low-pass filter that lets through 0 to 550 kHz and a very relaxed high pass that lets through 400 to $\infty$ kHz, and then digitized at more than 300 kS/s, then you could do the IF processing with digital filters (in software!), and these can be pretty much arbitrarily steep. You can modify them to your hearts delight (for example, to account for actual signal spectrum shape or LO inaccuracies), and that doesn't cost anything and has no risk of not working.

People's classical argument is that a good IF filter is paramount to receiving weak signals between and especially near to strong ones – but that's no problem for a digital receiver, that is, as long as the dynamic range of the ADC can still "see" the weaker signal without clipping the stronger one.

So, say you want to be able to, without even using oversampling¹, detect a signal that is say 80 dB weaker than its neighbor. Your Superhet receiver with nice IF filter would require an IF filter with a suppression of at least 83 dB if you want your SNR to be still 3 dB, i.e. crosstalk to only be half as powerful as the signal of interest. In reality, you'd probably need more filter attenuation.

I doubt the MK4 achieves that selectivity (I've not found two-tone test charts for it), but let's assume it did and you'd want to achieve the same.

Your ADC would thus need to be able to not overflow on the 80 dB stronger signal, and still have at 3dB dynamic range to spare on resolving the weaker one; a 18 bit ADC gladly does that (and far more) and comes at less than 10 USD.

If you can accept only a DR of a little more than 60 dB (which will, for fox hunting and the like, more than suffice), a < 20 USD Microcontroller eval board's on-chip ADC will simply do. That microcontroller itself is so plenty fast enough at doing math that applying even a mean filter on a couple kHz of signal is no big deal.

Notice that I'm an SDR guy – I really know that the time for narrowband filters under benign circumstances implemented as analog hardware components is over. You still need to do your anti-aliasing filtering, but seriously, instead of hoping you can calibrate your analog filtering to be acceptably steep and stable, digitally filter. Microcontrollers are plenty fast enough for the bandwidths you use.

¹ You can increase the SNR of signals by sampling faster than you need to. And this will have happened dramatically after your digital filter.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13036/substitute-for-455-khz-ceramic-filters-in-new-designs, by Jason R. Moore, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
