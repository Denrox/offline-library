# What does a receiver's noise reduction function do?

*Tags: equipment-operation, noise, dsp · score 5*

## Question

Some receivers contain a noise reduction button or function.

- What does this noise reduction do?
- Is there more than one type of noise reduction?
- How does the circuit or software know what part of the signal to reduce as noise and what part to not attenuate? (e.g. the stuff the operator wants to hear)

## Answer (score 4, by Marcus Müller)

What does this noise reduction do?

That should depend on the device.

Generally, it's to be assumed that it applies (analog and/or digital) signal processing to improve the *perceived Signal-to-Noise ratio*.

In simple cases, this might simply mean reducing the bandwidth of an analog receiver. Sure, voice will not sound as crisp, but if that buys one a reduction in 75% of noise, that might be worth it.

How does the circuit or software know what part of the signal to reduce as noise and what part to not attenuate? (e.g. the stuff the operator wants to hear)

In more complex cases, DSP will be used to find and isolate the components in the signal that match a mathematical model of what constitutes intelligible speech. This is not unlike the vocoder problem, where you'd want to condense the wholeness of audio data to only the parts that define the contained speech just well enough to reproduce it reliably.

So, this becomes an estimation problem: What's the speech content that led to the observed, noise signal?

An intuitive approach is: If you had all possible speech signals to choose from, which one has the least quadratic difference to the noisy signal you're observing? Pick that.

Of course, since you can't wait forever, this is not viable. What indeed is viable is trying to estimate a very limited set of speech model parameters, and then continuously updating that, predicting what would happen next, comparing that to the next freshly received bit of noisy signal, and so on.

Think of that as a speech synthesizer (that for example mimics the human mechanics of producing sound, by having different coefficients for different things your mouth and vocal chords could do), continuously just being fed the coefficients that someone estimated based on the noisy reception.

That brings me to

Is there more than one type of noise reduction?

Yes! not only are there many ways the above can be implemented, you also have different kinds of noises you might want to reduce:

While the bandwidth reduction most certainly pays for e.g. low-SNR FM and AM subject to stationary wideband noise, it won't do much against impulse noise (e.g. from spark plugs), since that just means a potentially huge spike with a lot of energy all over the spectrum.

It's easy to zero out that impulse. That would already improve the situation, but: you'd really want the uttering in progress when the impulse noise started to be continued, extrapolated for the duration of the impulse. Then, it becomes incredibly helpful if you're already using a predictive model coder, because you can just let it run freely without continously adjusting it.

Let me add one last question you didn't ask but that I'd like to answer:

What would be the best noise cancelling system, including a transmitter that cooperates?

Well, if the transmitter knows about the characteristics of the noise you're expecting, it could spend its transmit power on transmitting only what you really use to reconstruct, and not on the rest of what you spoke into your mic.

In the simple narrower-filter case above, that would simply mean it'd use a filter that is matched to what you use in the receiver on the transmit side. (And, yes, that is actually the same thing as *matched filtering* known from comms theory.)

In the voice-model case, it's not hard to see that it'd be way cleverer to just use the transmit power to transmit the coefficients needed to reconstruct voice and nothing else. Make sure the whole bandwidth you get is filled as much power put into these. Furthermore, the more important a specific coefficient is for intelligible reconstruction, the more power should be spent on encoding it.

That's exactly what vocoders due. It's intuitively not hard to see, thus, that digital voice comms with receiver RF SNR knowledge at the transmitter will be better than analog comms (especially AM). The often stressed argument of "digital doesn't do gradual degradation, it just fails" really isn't true for modern vocoders; there's a lot of channel coding going on that distributes errors as well as possible, and joint source/channel coding that makes sure that the remaining bit errors would have least possible effect on intelligibility.

You can actually make use of that with an SSB radio: just use the SSB audio in/output as bandwidth carrying digital signals. FreeDV does exactly that!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15104/what-does-a-receiver-s-noise-reduction-function-do, by hotpaw2, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
