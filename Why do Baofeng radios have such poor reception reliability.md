# Why do Baofeng radios have such poor reception reliability?

*Tags: receiver, baofeng, equipment-design · score 5*

## Question

What is the nature of Baofeng radios' poor receiver performance?

This brand of handhelds has somewhat notoriously poor receivers. I hadn't noticed this much when using them for short distance simplex work on hikes and whatnot, but during recent foxhunts and even with a local repeater this has become apparent. It's especially pronounced compared to a higher end Yaesu HT as well as a Uniden scanner — the Baofeng handhelds we have are incredibly deaf to signals the other receivers can pull in quite clearly in the same location.

What I've noticed is that:

- holding the monitor button doesn't help — where I would expect to hear at least a faint scratchy signal below squelch, there is just total noise without a trace of the expected signal
- sometimes the effect is temporary, e.g. on the local repeater it might miss the first five or ten seconds of a known transmission until finally the squelch opens up and the signal then comes in loud and clear! (The timing is unrelated to antenna position and again — total static when/if I hold down MONI during the missed parts until it randomly/suddenly "locks on".)
- a better antenna doesn't help — we've tried everything from an up-high discone, longer dual/tri-band whips, a roll up dual band "Slim Jim", a monoband (tape measure) Yagi and still just total static where there should be a clean signal. In fact, the stock rubber duck seems the best of the lot as far as slightly more reliable *reception* goes.

None of these clues quite add up for me. For instance, if the problem were one of sheer overload due to strong FM broadcast on the discone, I would expect the 2m Yagi would help. But the problem can be just about as bad with both. If the problem were just signal/noise ratio I would expect both the up-high discone or the pointed-towards-repeater Yagi to help, but the rubber duck somehow beats them both?!

I've read some blaming of this on "direct conversion receiver" rather than I guess a [multi-stage??] "superheterodyne" architecture. But again this doesn't explain why the signal seems to be either all the way there (opening squelch automatically) or completely absent (not a trace heard when squelch manually opened).

One thing I haven't tried is a bandpass filter to see what difference that makes. But before I would invest in one of those (so far the only off-the-shelf ones I've found cost more than the transceivers themselves) I'd like a better technical understanding of what's making the receive ability of these radios be so inferior. Has anyone come to any real conclusions whether these radios have a specific problem of e.g. "sensitivity" or "selectivity" or "intermodulation" or even just "poorly-tuned AGC" or "bad DSP implementation"? What further experiments should I try?

## Answer (score 8, by user10489)

You get what you pay for. The Baofeng radios take a number of shortcuts in their design to make them cheaper, including leaving out front end filters. The result is that the radio is marginal on suppressing spurious emissions on transmit and has poor sensitivity on receive.

Basically, because of the poor filtering, strong adjacent signals will cause the AGC to turn down the gain making the radio insensitive to the signal you are trying to get.

Ironically, a better antenna makes this problem worse, as it will bring in more noise. A worse or more narrow band antenna may actually help.

## Answer (score 5, by hotpaw2)

A big clue is that the short ducky antenna seems to allow better reception than the higher gain Yagi. So it could be that the receiver input is overloaded, possibly by signals outside the band of interest.

For a cheap experiment, try using the Yagi, not only aimed away from possibly interfering broadcast stations, but with a high value attenuator in series.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20840/why-do-baofeng-radios-have-such-poor-reception-reliability, by natevw - AF7TB, user10489, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
