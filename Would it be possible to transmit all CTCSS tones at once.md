# Would it be possible to transmit all CTCSS tones at once?

*Tags: tone-squelch · score 5*

## Question

What happens if all CTCSS tones are transmitted at once? Would it trip all radios listening on that frequency?

## Accepted answer (score 8, by Kevin Reid AG6YO)

You could get several different results, depending on exactly how the receiver recognizes the expected tone.

From a small amount of web research, it sounds like the usual methods are either a filter passing only the expected tone, or a frequency counter which determines the frequency of the tone in the signal which is then compared with the expected tone frequency.


If the receiver uses a filter to detect the tone, then its squelch will open, because it doesn't care about any other part of the frequency content of the signal.


If the receiver uses a frequency counter to detect the tone, then if all the tones are close enough to equal strength, the counter will not have a valid output, just as if there was no tone at all (only noise) in the relevant frequency range.

However, there is likely to be some non-flat frequency response somewhere along the way, so one particular tone will win and the squelch will open only if that tone is the one the receiver is expecting.

You will also run into issues transmitting all the tones at once — your audio signal will have high peaks as the tones beat against each other, and you will have to keep the total amplitude low to avoid over-deviating/distorting — quite likely low enough that the individual tones aren't strong enough to be recognized as CTCSS tones.

I thought I'd see what the actual result is, so I wrote a program with GNU Radio to synthesize the combination of all tones listed on Wikipedia's page. In order to prevent the output from clipping (analogous to overdeviating in an analog FM signal), I had to set the amplitude of the individual tones to 0.05 (-26 dB), which is significantly below the 0.15 (-16 dB) level that Phil Frost's answer said is normal for CTCSS.

```
#!/usr/bin/env python

from gnuradio import gr, blocks, analog

sample_rate = 44100
tones = [67.0, 69.3, 71.9, 74.4, 77.0, 79.7, 82.5, 85.4, 88.5, 91.5, 94.8, 97.4, 100.0, 103.5, 107.2, 110.9, 114.8, 118.8, 123.0, 127.3, 131.8, 136.5, 141.3, 146.2, 150.0, 151.4, 156.7, 162.2, 167.9, 173.8, 179.9, 186.2, 192.8, 199.5, 206.5, 213.8, 221.3, 229.1, 237.1, 245.5, 254.1, 159.8, 165.5, 171.3, 177.3, 183.5, 189.9, 196.6, 203.5, 210.7, 218.1, 225.7, 233.6, 241.8, 250.3]
duration = 10
gain = 0.05

t = gr.top_block()
sum = blocks.add_ff()
out = blocks.wavfile_sink("out.wav", 1, sample_rate, 16)
t.connect(
sum,
blocks.head(gr.sizeof_float, int(sample_rate * duration)),
out)
for i, tone in enumerate(tones):
t.connect(
analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, tone, gain),
(sum, i))

t.run()

```

## Answer (score 2, by Phil Frost - W8II)

No, you can't. Based on the particular method the receiver uses to decode CTCSS, multiple tones may or may not be recognized. But that's moot, because you can't transmit all the tones anyway.

CTCSS adds a low frequency tone to the baseband input to the FM modulator. Standards vary, but the amplitude of this tone is around 15% of the deviation. The amplitude needs to be high enough to allow for reliable detection above the noise floor, while low enough to allow the intended transmission (your voice, etc) to also be modulated without overdeviating.

Let's just use round numbers to make the math easy and say the deviation is 10 kHz. That means the CTCSS tone will be responsible for deviation of 1.5kHz, leaving the other 8.5 kHz of deviation available for the intended transmission.

If you transmit two tones, you've doubled the power of the CTCSS tones. The deviation also increases, leaving less headroom for the intended transmission. Still workable, I suppose. Presuming of course that the decoder will recognize this as valid.

But if you transmit *all* the tones, there just isn't enough deviation left to transmit all the tones at the specified power. When you add the power of all the tones together, you won't even be able to transmit them without overdeviating. You could reduce the power of the tones to avoid overdeviating, but then whatever tone happens to be the right one at the decoder will no longer be strong enough to be detected.

So, you can transmit a horribly distorted signal, or a tone too weak to be detected.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2336/would-it-be-possible-to-transmit-all-ctcss-tones-at-once, by Richard Hum, Kevin Reid AG6YO, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
