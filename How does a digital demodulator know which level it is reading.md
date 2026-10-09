# How does a digital demodulator know which level it is reading?

*Tags: digital-modes, rfi · score 6*

## Question

I have recently started getting into wireless digital communications and I read about QAM modulation.

But I am a little confused as to how the receiving demodulator would know which symbol it is reading.

For example with 64-QAM there would be 8 amplitude levels transmitted over the air. I understand these levels are modulated as voltage in the baseband quadrature modulator. But when the receiver receives the signal and demodulates, the voltage has been significantly attenuated.

So how does the reciver know if it is receiving "level 4" or "level 7" in the amplitude carrier if the voltage has attenuated?

Eg. The transmitter sends voltages between 2-10 volts (1 volt difference per level for 64 QAM). But the receiver can read any voltage depending on its distance from the transmitter e.g 0.1-0.5 V or even 0.002-0.01V. How would the receiver know which symbol it is reading?

## Accepted answer (score 5, by Kevin Reid AG6YO)

This same problem of discriminating symbols can appear in as simple a system as transmitting an "unmodulated" binary code (2 symbols) over an AC-coupled cable (such as is used in Ethernet). If your message has a long string of 1s or 0s, how does the receiver tell them apart?

The solution in either case is to use a coding which ensures that **all symbols occur in the message**.

In the binary case, this is known as bit stuffing; and it can be done by a rule as simple as, for example, "if you would transmit 000000, transmit 0000001 instead; if you would transmit 111111, transmit 1111110". The receiver knows the rule in use and can therefore remove the extra symbols, and the rule ensures that every message longer than six bits contains a transition.

And every message will be at least that long, because (especially in QAM) you also want to use a preamble to ensure that every message is not just long enough to have a symbol transition, but long enough for the receiver's synchronization to lock onto the timing, amplitude, and phase of the signal — it should contain *many* symbol transitions.

I don't know what methods are used in practice for QAM.

## Answer (score 6, by Marcus Müller)

You're asking exactly the right question – *my receiver can't know this property of the transmission, how do I figure it out reliably* – and that way of thinking makes for good receiver designs :)

There's two classes of methods to solve this:

1. statistics-based methods
2. transmitter data assisted methods

What is very common in receiver design is that you have an automatic gain control (AGC) that amplifies your receive signal to a fixed *average* power. That makes a lot of sense from the analog hardware point of view, because no amplifier is *really* linear over its full range, and thus, if possible, you'd always want to work your amplifiers in roughly the same power region.

Finding the average power and scaling so that the result is always the same power works, because you can be pretty sure that all symbols in your transmission are equally likely; if that's not the case, you could have compressed your source data (using source coding, i.e. lossless entropy coding) better. Furthermore, as Kevin illustrated for binary wired systems, you employ techniques to avoid the signal having a distinct pattern (e.g. constant, or only alternating between the corner points of a QAM, or..:).

In wireless systems, bit stuffing isn't common, because the problem that solves ("consecutive runs of the same symbol") is just a subclass of the problem that you need to solve in wireless comms, namely that you need your data symbols to look uncorrelated, so that their spectrum is white. That is important so you can make the most use of the bandwidth you're given¹ but also because of statistical methods in the receiver².

Instead, *scramblers* are used. Often, that's nothing but a simple pseudo-random bit generator that is XORed both on the transmitter side and the receiver side bits after channel coding or before channel decoding, respectively.

Armed with that, it's very unlikely that the average power of your signal (say, averaged over a hundred symbols) varies a lot. Thus, you can scale your signal's amplitude with the inverse of the square root of the received power.

This is often not sufficient for QAM, since small fluctuations are very likely, and because QAM is indeed pretty sensitive to amplitude variations.

So, alternatively, but more often, in combination with that, the transmitter is designed to include pilot symbols or sequences, which can be easily detected: either on frame start something like a fixed preamble that can be found using correlation, or simply at known positions in the frame.

These aren't data, but fixed values that some standard defines. The receiver observes them, says, "ah, they should be this, but they are that, so we need to scale accordingly". *Data-aided recovery* of amplitdue would be how this is called.

Some channels can be assumed to stay constant for the duration of one frame³. Then, a single pilot sequence or symbol might suffice. If the channel changes, you'll need a new pilot occassionally, to keep track of things. Of course, if you have a sufficiently fine resolving receiver, and enough error correction, you could also keep track of how the amplitudes change in your symbols by reconstructing what you should have received under your current channel state information, and continuously compare that to what you've actually receive and notice a drift early on. Then you're even *decision-feedback recovering* amplitude of your signal.

In practice, you use QAM when you need a high data rate, which most often⁴ means it uses a large bandwidth, and the channel is hence a wideband channel and needs an equalizer to look flat. In this common case, the data-aided or decision-feedback amplitude recovery doesn't happen as its own step, but as part of the equalizer.

¹ if you have 20 MHz of bandwidth and a peak power over any 1 kHz swath in that that you can legally use, you'll make damn sure your data spectrum is flat and doesn't have spikes at any frequency, because that would mean you need to reduce your transmit power overall.

² not only for amplitude recovery, but also for phase and frequency recovery. The same problem you noticed about levels also applies to rotations!

³ that's actually an inversion of reality: I should have said "some systems were designed so that frames are short enough, so that the ever-changing channel can be considered to not change within the duration of a frame. But putting it like that gives you all the headaches of the designer of the whole system when you should just be developing a receiver.

⁴ not always; some channels, for example satellite communications, typically form an exception to that. For the satcom channel, you often prefer to use high-number-of-points PSK over QAM, because you have good phase recovery, but don't need an equalizer to combat multipath, and thus, you want to avoid going through the extra effort of having amplitude recovery, especially because neither atmosphere nor the very high-gain LNAs will make that any easier for you.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17208/how-does-a-digital-demodulator-know-which-level-it-is-reading, by YellowBadger, Kevin Reid AG6YO, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
