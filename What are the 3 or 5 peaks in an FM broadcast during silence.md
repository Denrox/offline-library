# What are the 3 or 5 peaks in an FM broadcast during silence?

*Tags: software-defined-radio, frequency, fm · score 3*

## Question

Looking at the waterfall spectrum of any ordinary FM public broadcast station (88-108 MHz), during the silence, there are 3 or 5 visible peaks.

**What are they?**

It's possible this has a trivial answer, but I have not found a very satisfying answer. So please explain in a bit more than one sentence. Here's a picture of what I mean.

## Accepted answer (score 4, by Scott Earle)

The way that stereo sound is broadcast using a single 'channel' is to broadcast the L+R (the sum of the left channel and the right channel) signal on the centre frequency, and include the L-R (difference between the left and right channels) signal modulated on a frequency at a known difference from the main carrier.

What you are seeing is the main (L+R) carrier, the two sidebands of the 'pilot' 19kHz frequencies, and the two sidebands of the 38kHz (L-R) sub-carrier, of a stereo broadcast.

See this Wikipedia entry for more details, as well as information about the original amateur radio origin of this system.

## Answer (score 5, by Kevin Reid AG6YO)

This grouping is what frequency modulation looks like whenever the *input* to the modulator is a constant single tone of a fairly high frequency.

(If the tone were of a much lower frequency, then you would instead see a single peak moving in a sinusoidal fashion as a straightforward understanding of frequency modulation would suggest. This can be observed on repeater transmissions that use CTCSS tones, with a fast waterfall.)

The single tone that is present but that you are not hearing is the 19 kHz (higher than audible, and usually filtered out by a receiver) “pilot” tone for FM stereo encoding.

FM broadcast stereo works by taking the two stereo audio channels and rearranging them into a single channel where everything but the combined mono signal is of a higher-than-audible frequency. Wikipedia has a nice chart (including some additional features beyond stereo):

This is **not** a plot of RF frequencies. This is the signal which is *sent into the FM modulator* in place of the audio signal which a mono transmitter would use — note that the 0 to 15 kHz audible range is just audio. (This is for compatibility with mono receivers.)

When the stereo audio is silent, the L+R and L−R outputs are both silent, so the only thing in the signal (assuming none of the additional digital features charted above are present) is the 19 kHz tone.

The purpose of that “pilot tone” is to allow the FM stereo decoder in the receiver to precisely locate the frequency-shifted stereo difference audio (at twice the pilot tone frequency; can be seen as DSB-SC modulation) and shift it back, despite any drift in the relevant oscillators.

Again, the pilot tone is at a *single* frequency; it is just the case that when that single tone goes through a FM modulator, a theoretically infinite (and in practice bandlimited) collection of sidebands is produced, which is the way FM always works.

## Answer (score 2, by Marcus Müller)

There's the stereo sum channel (Left + right), a 19 kHz pilot tone, the stereo difference channel (L-R), and the RDS carrier. Depending in where you are, the station might have further digital channels for additional systems.

Also, if your reception is very strong (which it seems to be), you might be saturating your RX amplifier and see "phantom" intermodulation products that aren't actually on the air. Reduce your RX gain. If some peaks go away faster then your main peak, than you've found those.

If you massively overpower your RX, your ADC will clip, and things will look horrible:

From here

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7517/what-are-the-3-or-5-peaks-in-an-fm-broadcast-during-silence, by not2qubit, Scott Earle, Kevin Reid AG6YO, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
