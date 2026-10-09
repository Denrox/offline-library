# How can you calculate the frequencies for each band?

*Tags: frequency, band-plan · score 9*

## Question

I've just started studying for my HAM license a couple of weeks ago, so please excuse me if this is a remedial question...

I have the *Canadian Amateur Radio Basic Qualification Study Guide* (which I'm finding is terribly hard to understand). Their explanations of just about everything appear to be missing pertinent information that allow the reader to connect the dots and consequently I'm struggling to understand what they're explaining... anyway, the book discusses a formula which supposedly allows you to determine the bond between frequencies and their band - i.e. the calculation in the book tells me that 300 / Wavelength = Frequency... where one is to assume that 300 is a rough simile of the speed of light in millions of meters per second. The book suggests the resultant frequency is approximately (within some unexplained tolerance) the middle of the bandwidth for that band plan.

I'm noticing that using this formula for many bands the resulting frequency doesn't fall within the suggested frequency range for that plan and where they do, many don't fall within any discernible tolerance of the middle.

For example:

- 20m band = 300 / 20 = 15.000 MHz, whereas the book suggests the frequency band falls between 14.000 - 14.350 MHz. (Clearly 15.000 MHz falls outside that range)
- 2m band = 300 / 2 = 150.000 MHz, whereas the book suggests the frequency band falls between 144.000 - 148.000 MHz.
- 33cm band = 300 / 0.33m = 909.091 MHz, a long way from the middle of the suggested frequency band of 902.000 - 928.000 MHz

Even if I substitute the more accurate (according to Google) measurement of c being 299,792,458 m/s, I arrive at 14.990 MHz for 20m, still not within the frequency band.

Clearly I'm missing something, can someone explain what I'm not understanding?

## Accepted answer (score 12, by Kevin Reid AG6YO)

$$ \frac{c}{ \text{frequency}} = \text{wavelength}$$ $$ \frac{c}{ \text{wavelength}} = \text{frequency}$$

The above relation is a fact of physics. It's true unconditionally (provided you are using consistent units, e.g. wavelength in meters and $c$ in meters per second); it's how you convert between two different ways of measuring a wave.

The frequency limits, and names, of the bands are not physics; they were invented by humans. The frequency limits are a matter of the regulations that divide up the radio spectrum among many users. The limits of the amateur bands are semi-arbitrary.

The common names for the bands ("20 m", "2 m", and so on) are simply **the closest round number to the actual wavelengths**. (In your example of 33 cm, note that 32 and 34 cm would be outside the band entirely. 33 is the best two-digit approximation.)

What your book *should* have told you is not that you can use the above relation to find the limits of the band, but that **given that you already know the bands and frequencies, you can use it to find *which* band a frequency belongs to, or vice versa**, because while the band names do not always fall in the frequency limits, the correct band/frequency will always be the *closest* match.

For example, $300/143 ≈ 2.098$, so we can conclude that 143 MHz is in the 2 m band *if it is in an amateur band at all*, which it *isn't* (but e.g. 145 MHz is).

If you wish to know the limits of bands, you must memorize them; there are no shortcuts. The relationship between wavelength and frequency can, however, be used to match up those limits to the wavelength-names of the bands.

## Answer (score 5, by Phil Frost - W8II)

The names make a kind of sense if you take into account the history behind them. Look at this pattern of names and lower end of the allocation:

- 80m: 3.5MHz
- 40m: 7.0MHz
- 20m: 14MHz
- 10m: 28MHz

Note how the frequencies and canonical names are related by multiples of two. 80m is almost perfectly named: the allocation goes from 75.0m to 85.7m. Sure, as you go up in frequency it gets less perfect: 20m is closer to 21 meters. But these are nice, round numbers. There being no other bands allocated at the time, there wasn't any particular reason to be more specific.

Of note, those bands have been allocated for a very long time, internationally allocated by the ITU in 1927.

15m was allocated in 1947. Clearly that can't be rounded to 10m or 20m because those names are already taken. 14m would be a more accurate name, but 15 is a "rounder" number, being a multiple of 5.

30m, 17m, and 12m are the WARC bands, allocated more recently in 1979. 12m couldn't be 10m because that name was taken. 30m is a round number that's close enough that wasn't already used. 17m is actually closer to 15m, but that name was also already taken. I suppose it could have been 16m. Maybe you can dig up the notes from 1979 to figure out why it wasn't. My guess: someone wanted some free space between 15m. You will notice that 12m is right on the money: the actual allocation is from 12.00m to 12.05m.

60m is relatively new, being allocated in the US in 2002. I don't think the ITU allocates it internationally. Though it's actually around 55m, 60 is a nice round number and there wasn't already a band called that.

And that's all the HF bands.

The VHF bands are pretty accurate:

- 300/50MHz = 6.00m
- 300/144MHz = 2.08m
- 300/225MHz = 1.333m

I'll forgive you for questioning the last one, because you are Canadian and you use the metric system. Had Canadians named it, they would have called it 133cm. But this band first encountered amateur use in the US, where fractions with powers of two are preferred. So this is the "1¼-meter band". Of course at the time the band was named, Canada wasn't using the metric system either. So maybe not.

As you go up the spectrum, the names continue to be pretty accurate. Eventually, people tend to stop calling them by wavelength. "Four-forty" is a colloquial name for "70 centimeters" in some places. No one has a "13 centimeter" Wi-Fi access point. They have a 2.4GHz access point.

## Answer (score 4, by Mike Waters)

```
"I'm noticing that using this formula for many bands
the resulting frequency doesn't fall within the
suggested frequency range for that plan and where
they do, many don't fall within any discernible
tolerance of the middle."

```

Here's why this is the case today.

In the early days of radio (that is, the late 19th and early 20th centuries) **everyone referred to the approximate wavelength in meters, rather than the actual frequency in MHz.** *That's simply the way it was!* Other than Lecher wires (mostly for VHF), there was almost no way of accurately measuring the actual transmit or receive frequency with any degree of accuracy. Back in those days, there were no frequency counters or accurately calibrated VFOs.

In those days --before the days of vacuum tubes, which were a HUGE technical advancement-- all that anyone had were noisy, raucous spark transmitters, which occupied a ridiculously wide bandwidth above and below the center frequency.

(Better yet were crystal-controlled triode oscillators, even if they did have key clicks and chirps.)

Later, when broadband spark transmitters gave way to narrower and much cleaner tube oscillators like this, tuning became more accurate, and it was more prudent to refer to the frequency.

And that's why we still have the word "wavelength" in our list of amateur radio terms. Like it or not, we're just stuck with the term, and all the confusion that came with it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3575/how-can-you-calculate-the-frequencies-for-each-band, by BenAlabaster, Kevin Reid AG6YO, Phil Frost - W8II, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
