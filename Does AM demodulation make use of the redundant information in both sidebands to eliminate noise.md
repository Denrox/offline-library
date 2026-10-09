# Does AM demodulation make use of the redundant information in both sidebands to eliminate noise?

*Tags: modes · score 7*

## Question

XLR microphone cables, for example, make use of the dual channels out of phase to cancel noise by injecting the inverted and non-inverted signal into one end of the cable. Then any noise injected along the way will presumably be equal, and re-inverting the signal at the other end negates the noise. Since the AM sidebands are opposite, does a similar principle come into play?

## Answer (score 5, by Phil Frost - W8II)

No, not really. By essentially transmitting the same information twice (two sidebands), you'd think there would be more information there about the signal. But, the transmitter's power is divided between these two sidebands, so each has less transmitter power behind it. Also, in this additional bandwidth, there is more noise. Since the noise spectral density is roughly the same everywhere, more receive bandwidth necessarily means more noise received.

Further, not a small part of the power transmitted in AM is in the carrier, which has no information about the signal at all in it. This is a poor use of available transmitter power.

These are the reasons behind the development of SSB. SSB beats AM in almost every respect. It requires less spectrum for the same information, and makes better use of transmitter power. Because more of the transmitter's power can go into useful signal, this increases the signal to noise ratio. The disadvantage is in the more complex electronics required of the receiver and transmitter. The lack of a carrier also makes tuning more difficult: if the receiver and transmitter are not tuned to the same frequency, the sound of the received voice is shifted up or down in pitch, making a weird, inhuman sound.

Interestingly, although more difficult to implement electronically, SSB is simpler conceptually. USB is simply all the frequency components of your voice, shifted up to the desired frequency. LSB is the same thing, with the whole thing flipped left-for-right, if you were to view it on a spectrograph. To "demodulate" it, just shift them back down. Though this is difficult to realize with discrete electronics, it's actually trivial in an SDR.

## Answer (score 2, by WPrecht)

No, they don't. The key is that while the sidebands are opposites, they are symetrical about the carrier frequency.

The popularity of DSB-AM (broadcast AM) has to do with the capabilities of the receiver. The simple, early mass-market receivers needed the carrier in order to reproduce undistorted audio on recieve. More sophisticated receivers can generate the carrier locally and feed that into the mixer.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/789/does-am-demodulation-make-use-of-the-redundant-information-in-both-sidebands-t, by Bill - K5WL, Phil Frost - W8II, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
