# Yaesu exceeding power limit under certain conditions

*Tags: rf-power, yaesu · score 6*

## Question

I noticed something fairly interesting today, under certain operating conditions my FT857D will exceed the power limit, the highest I saw it go was around 150W! This happened when the power was set to 8W or below on 20m 17m 15m 10m etc (but not VHF/UHF). Strangely, 80m and 40m works as expected. I was working PSK31 and adjusting the Digi Gain when I noticed this first. With the output set to 8W or lower increasing the Digi Gain kept increasing the output power. At first I wrote this off to my tuner giving me a wrong value but then I noticed the current draw from my power supply.

This was not only when doing digital, I saw the same behavior on AM. When set to 5W the output could be as high as 40W. I'm really glad I saw this in the shack and didn't take this radio for QRP operation as I was planning. Has anyone seen something like this before?

These results were confirmed when operating into a dummy load. It seems to be an ALC problem. On 40m the ALC works as expected, on 20m the ALC level is noticeably lower and the power a bit over what I set it. On 10m the ALC doesn't seem to kick in at all and the power output is 130W+.

## Answer (score 6, by Phil Frost - W8II)

Think of the "power" setting on the radio as more of a guideline than a rule. It should be more or less accurate, given reasonable inputs.

Few radios actually measure the output power and adjust gain to achieve the desired power. More likely, the power setting simply adjusts the gain of the radio's power amplifier with no feedback whatsoever.

Ideally, ALC keeps the input power to the power amplifier at the appropriate level. However, the ALC is probably just measuring peak voltage of the input signal and adjusting gain based on that. It's simpler to implement a peak detector than it is to measure true RMS voltage, and usually this works fine enough.

What's probably happening is this: when you turn the digital gain up, you are clipping at some stage. Once you start clipping, increasing the gain adds more power in harmonics, but does not increase the peak voltage of the signal. Because the ALC circuitry is looking at the peak voltage, it doesn't decrease the gain to compensate for this additional power.

For digital modes, you really don't want this to happen. That power in the harmonics means you are occupying more bandwidth than intended: it wastes your transmitter's power and interferes with nearby stations. Here are some waterfall examples of PSK31 from an eham.net.

Here's a good signal, with no visible distortion:

And here's one with extreme distortion:

See how the signal has "echos" above and below the center frequency? That's harmonic distortion caused by clipping.

To properly set your levels for digital operation, you want to adjust your digital gain and/or computer's audio output level so that the ALC just barely kicks in, then back it off a tad. You don't want ALC working at all, since the variable attenuation provided by ALC is equivalent to multiplying your signal with some other function, and this can introduce additional distortion which degrades your signal quality.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3478/yaesu-exceeding-power-limit-under-certain-conditions, by s3c, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
