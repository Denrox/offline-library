# How can I tell the frequency without an oscilloscope, or frequency counter?

*Tags: frequency, oscillator · score 3*

## Question

Just going through the RF oscillator listed on SM0VPO's web-site. I replaced C1 by a reverse biased 6A8, and used an E-core transformer pulled out of a Compact Fluorescent Lamp instead of an inductor for the 40m bad. In all probability, she wont' swing.

But if she does, is there a hack to find out the frequency without using an oscilloscope, or digital frequency counter?

## Answer (score 3, by Kevin Reid AG6YO)

You *can* use a radio receiver that has appropriate coverage, but the catch is that you have to sweep across the entire frequency range the oscillator might be oscillating at — you're limited to the bandwidth of the radio's filters, so you can't get an immediate answer like a frequency counter would give you.

First, you need to make sure the signal is getting to your radio. Since you don't know anything about the signal characteristics, not having a scope (and I wouldn't trust an AC voltmeter to read properly at RF), you don't want to plug it into the antenna port. Instead, just place [a small, insulated antenna](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md) near the oscillator.


The best type of radio for this purpose is one with some kind of spectrum display ("panadapter", SDR, whatever) — the wider the better. Tune it to where you hope the oscillator is oscillating, then look for peaks on the spectrum. Turn the oscillator off and check that the peak disappears, to confirm that it isn't some other signal. If you don't see anything, change the tuning step by step (by just less than the bandwidth of the display) so you get a look at the entire plausible band.


If you have a CW or SSB receiver, use its “scan” feature and listen for a continuous tone with no modulation, confirming it as above. Once you've found a tone, here's how to get the exact frequency if you need it:


If you have a CW receiver with a tuning indicator or "spot tone", use it to find the frequency exactly.


If you have only a SSB receiver, tune until the tone goes inaudibly low-frequency.


If you're stuck with an AM or FM receiver, listen for silence instead of static. (Don't forget to open the squelch so you can hear the static!) You won't be able to make a precise measurement this way.

Once you have determined a frequency using this procedure, you have the additional problem that you may have found a harmonic of the original signal. Therefore, check frequencies which are 1⁄2, 1⁄3, 1⁄4, 1⁄5, etc. of the one you found.

Of course, this procedure is immensely tedious (depending on how fast you can scan the spectrum), and won't help if the oscillator's frequency is outside of your receiver's coverage. Depending on your personal value of time vs. money it may well be a better idea to buy or build a frequency counter (or oscilloscope).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2346/how-can-i-tell-the-frequency-without-an-oscilloscope-or-frequency-counter, by VU2NHW, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
