# Are there any modes that use pseudo-random noise codes to "amplify" signals?

*Tags: digital-modes, noise · score 3*

## Question

GPS for example uses them to allow receivers to decode extremely weak signals far below the noise floor.

From https://blank005.tripod.com/gps/psedo_random.html :

If we tuned our receivers to the GPS frequency and graphed what we picked up, we'd just see a randomly varying line (the earth's background noise). The GPS signal would be buried in that noise. The pseudo random code looks a lot like the background noise but with one important difference: we know the pattern of its fluctuations. What if we compare a section of our PRC with the background noise and look for areas where they're both doing the same thing? We can divide the signal up into time periods (called "chipping the signal") and then mark all the periods where they match (i.e. where the background is high when the PRC is high). Since both signals are basically random patterns, probability says that about half the time they'll match and half the time they won't. If we set up a scoring system and give ourselves a point when they match and take away a point when they don't, over the long run we'll end up with a score of zero because the -1's will cancel out the 1's. But now if a GPS satellite starts transmitting pulses in the same pattern as our pseudo random code, those signals, even though they're weak, will tend to boost the random background noise in the same pattern we're using for our comparison. Background signals that were right on the border of being a "1" will get boosted over the border and we'll start to see more matches. And our "score" will start to go up. Even if that tiny boost only puts one in a hundred background pulses over the line, we can make our score as high as we want by comparing over a longer time. If we use the 1 in 100 figure, we could run our score up to ten by comparing over a thousand time periods. If we compared the PRC to pure random noise over a thousand time periods our score would still be zero, so this represents a ten times amplification.

Are there any amateur radio modes/software that use this method?

## Accepted answer (score 2, by tomnexus)

There has been some experimenting with DSSS on HF - I recall (but can't find online) some discussion of trans-atlantic below-the-noise communication.

A quick search though finds a mode called Chip64 which is a Direct Sequence Spread Spectrum mode. It takes a data stream (the operator typing) of 37.5 bits per second, and multiplies it by a 64-bit long gold code. The final modulated signal is 580 Hz wide.

The HF channel (RF path) is quite complex and fast-changing; effectively the signal you hear is made up of many copies of the transmitted signal, arriving not just microseconds apart (like multipath in an urban environment) but milliseconds apart. This means that high symbol-rate modes like DSSS can be significantly distorted. I believe this channel favours modes like WSPR which use narrow tones present for quite long times, hundreds of milliseconds. The ionosphere will be less kind to spread spectrum modes, which although "below the noise", fundamentally depend on the channel being stable. So WSPR is probably better than any wide band spread-spectrum mode in the HF band. Of course WSPR also transmits a substantial random code for synchronisation purposes (162 bits sync code, 162 bits message), but this code has the same bit rate as the original signal so the effective "spreading" is small.

In general, in a band without significant narrowband or wideband interference, there is no magic processing gain benefit to using DSSS instead of basic modulation. For example, if you wanted to send just the 50 bps NAV messages that GPS transmits under the code, you could do just as well with 50 baud BPSK. Heresy! GPS of course needs the 1.023 Mbps code as a time synchronisation mechanism, not just to spread the data.

## Answer (score 5, by natevw - AF7TB)

If you're asking if Amateur Radio licensees use modes based on PRC, it may depend on how those are defined exactly. There are some relatively common ham radio modes that allow decoding near or below noise levels, many of the most well-known being developed by K1JT within his Weak Signal Communication Software programs, and they do typically rely (in part) on correlation to some sort of pre-arranged numeric sequence.

For example, part of the FT8 protocol implemented in his WSJT-X software relies on:

Tone patterns known as Costas arrays are embedded in FT8 and FT4 waveforms to allow the receiving software to synchronize properly with received signals in both time and frequency.

(source: https://www.physics.princeton.edu/pulsar/k1jt/FT4_FT8_QEX.pdf — I've added the Wikipedia link here.)

I'm not qualified to judge whether a Costas array is a "Pseudo-random noise code" but to my eye it does seem to have similarities, i.e. a pre-knowable sequence of numbers that hop around.

Similarly his WSPR protocol uses both a Convolutional code and again a pre-arranged pseudorandom sequence:

This information is compressed into 50 binary digits and then encoded using a convolutional code with constraint length K = 32 and rate r = 1/2. Each of the resulting 162 bits is used as the most significant bit of a two-bit "channel symbol" to be transmitted using 4-tone frequency-shift keying at 1.46 baud. The least significant bit is defined by a pseudorandom sequence known to the software at both transmitter and receiver and used to establish accurate synchronization of time and frequency.

(source: https://physics.princeton.edu//pulsar/K1JT/WSPR_QST_Nov_2010.pdf)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21389/are-there-any-modes-that-use-pseudo-random-noise-codes-to-amplify-signals, by 2080, tomnexus, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
