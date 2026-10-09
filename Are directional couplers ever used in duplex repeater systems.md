# Are directional couplers ever used in duplex repeater systems?

*Tags: repeater, filter, directional-coupler · score 4*

## Question

I understand that most single-band repeaters will use a tuned cavity duplexer to isolate the received signal from the transmitted signal, since the frequencies are very close and extremely sharp filtering is needed to separate them.

But while the frequencies are close, another difference between the incoming and outgoing signals is just that: they are traveling in opposite directions! Could a repeater use a directional coupler to separate the two signals?

## Accepted answer (score 5, by Phil Frost - W8II)

Are you thinking something like this?

Let's say you have a really good directional coupler with a directivity of 55dB. And the antenna is a good match with a VSWR of 1.1, or equivalently a return loss of 26 dB. And the transmitter power is 10 W, or 30 dBm. And we'll say we select a directional coupler with a coupling factor of 10 dB (though as you'll see, the coupling factor doesn't really matter).

30 dBm, after the 55 dB directivity of the coupler, and the 10 dB coupling factor, means the receiver will see 30-55-10 = -35 dBm at its input from the transmitter.

Let's say we want to hear a 1 W (20 dBm) station that's 1 km from the repeater. At 144 MHz that's a free space path loss of 76 dB, so the power received at the antenna will be in the neighborhood of 20-76 = -56 dBm. Maybe a little more after adding antenna gain.

That -56 dBm is then subject to the 10 dB coupling factor, so at the receiver it becomes -66 dBm.

Signal power: -66 dBm  
Noise power (from the transmitter): -35 dBm  
SNR: -12 dB

Obviously this is not going to work. And it's actually worse than this, because any reflected power from the antenna will also show up at the receiver. The 30 dBm of transmitter power, after the 26 dB return loss, is 4 dBm. Then subject to the 10 dB coupling factor is another -6 dBm of transmitter power finding its way into the receiver.

## Answer (score 3, by Kevin Reid AG6YO)

Among the problems is that a directional coupler *only* discriminates based on direction, and in a real system there will be reflections from many elements of the system beyond the coupler:

- Imperfect transmission line
- Imperfect antenna
- Birds sitting on the antenna, or other environmental effects detuning it
- Reflective objects in sight of the antenna

Any such reflection would end up in the receiver. A duplexer will instead discriminate based on frequency, so the reflection is re-reflected back out the antenna (very similarly to the function of an antenna tuner).

Directional couplers *can* be used when the reflections from any of these sources are actually what is of interest, usually in RF test equipment or some types of radar.

## Answer (score 3, by Marcus Müller)

In addition to what Kevin said, if you can, you'd usually use frequency duplex.

That has technological reasons:

- It's nearly impossible to build a broadband (i.e. $\frac{f_\text{max}}{f_\text{min}} < 0.75$) directional coupler – most designs depend on the wavelength being within close limits. Filter design is a lot more flexible.
- for isolation purposes, and within reasonable size constraints, practically only *circulator* are viable; those are finely tuned, very expensive devices, compared to filters
- the isolation of directional couplers that aren't extremely narrowband is usually much worse than what's realizable with filters. For example, you can reasonably buy 20dB-isolating circulators. Good ones sometimes reach ~43 dB. Compare that to the out-of-band suppression of your cavity filter

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7319/are-directional-couplers-ever-used-in-duplex-repeater-systems, by natevw - AF7TB, Phil Frost - W8II, Kevin Reid AG6YO, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
