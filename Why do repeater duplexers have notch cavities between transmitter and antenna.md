# Why do repeater duplexers have notch cavities between transmitter and antenna?

*Tags: repeater, transmitter, duplexer · score 3*

## Question

Why are notch filters used on the transmit side of a repeater duplexer?

The primary purpose of a duplexer is to keep the transmitter output out of the receiver input, since they both operate at the same time from a common antenna on frequencies which are closely spaced. Secondarily, (say, at a hilltop radio site where a bunch of transmitters are clustered) it keeps strong signals from neighboring transmitters out of both the receiver and transmitter, so the receiver doesn't desense and the transmitter doesn't suffer/produce IMD.

The secondary purpose is obviously accomplished with bandpass cavities in line with both the transmitter and the receiver, and the primary purpose is accomplished by also adding notch filter cavities. My question is: Why are there always notch filters (on the receiver frequency) shown in line with the transmitter output?

Obviously, you want notch filters (on the transmitter frequency) in line with the receiver to keep the transmitter output out of the receiver input. But you don't want notches (on the transmit frequency!) in line with the transmitter output, because that would block the transmitter from the antenna. And if they're tuned to the receiver frequency, what exactly are they accomplishing in the transmit circuit? The transmitter doesn't need protection from the receiver, because the receiver doesn't transmit any signal.

It seems like it would be better served by placing those notch filters on the receive side to further attenuate the transmit energy, or else spend the money on bandpass cavities instead of notch cavities to better isolate the repeater from everyone else on the hilltop.

And yet, every duplexer diagram or setup I've seen seems to have notches between the transmitter and the antenna (usually the same number as on the receive side). Am I missing something here?

## Answer (score 2, by Graham G8URP)

The transmitter doesn't need protection from the receiver, because the receiver doesn't transmit any signal.

Indeed. The notch filter in the transmit side is instead to protect the receiver from the transmitter.

As well as the familiar harmonics and spur signals generated on specific frequencies by the transmitter it also produces broadband noise centred on the transmit frequency and extending out far enough to cover the receive frequency.

If the broadband noise on the receive frequency was allowed to enter the receiver it would desense (i.e. desensitise) it; incoming receive signals would need to be strong enough to exceed the transmitter broadband noise level.

We get rid of this noise (or at least reduce it below the receiver's own noise floor) by putting a notch filter tuned to the receive frequency in the transmit path. Note we can't put this filter in the receive path as it would filter out the desired incoming receive signals.

Some more reading:

Transmitter noise/receiver desense primer

Transmitter Broadband Noise (shows calculations)

Or try your preferred search engine.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17515/why-do-repeater-duplexers-have-notch-cavities-between-transmitter-and-antenna, by AC0CW, Graham G8URP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
