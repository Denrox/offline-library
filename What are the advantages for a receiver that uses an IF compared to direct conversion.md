# What are the advantages for a receiver that uses an IF compared to direct conversion?

*Tags: electronics · score 4*

## Question

What are the advantages for a receiver that uses an IF compared to direct conversion ?

## Accepted answer (score 7, by Phil Frost - W8II)

A superhet has two distinct *properties*, which may or may not be advantages:

1. The image frequency is far away, and
2. The IF is not DC

In a typical superhet design, the LO and signal frequencies will be quite far apart, making the image frequency in an entirely different band. Thus it's not difficult to exclude the image frequency with a simple analog filter.

In a direct conversion receiver, the LO is at or very near the signal frequency, and thus the image frequency is immediately adjacent. Obtaining a sufficiently selective filter at the signal frequency is often impractical: it would require a very small fractional bandwidth, and would need to be tunable over the operating band of the receiver. Contrast with a superhet design which allows the channel filter to be tuned at just one frequency: the IF.

Thus, a direct conversion receiver must typically perform channel selection *after* the mixer, typically with a quadrature mixer. Dealing with quadrature signals in the analog domain requires more circuitry since there are twice as many signals to process, which must each be treated carefully to maintain coherence. Furthermore, it is difficult to minimize DC offset and 60 or 50 Hz hum.

These issues are largely mitigated in modern times by digital electronics. Many (perhaps most?) modern HF amateur rigs now utilize either direct sampling (example: Icom IC-7300, FlexRadio, Hermes), running an ADC fast enough to sample RF with no mixing at all, or direct conversion with a quadrature mixer (example: Softrock, QRP Labs QCX, everything from Elecraft).

Modern VHF+ applications tend to use direct conversion and digital demodulation as well. For examples, consider the ubiquitous, cheap RTL-SDR receivers, and BaoFeng handhelds.

Often, the digital solution not only performs better but is cheaper too, especially when the modulation in question is a digital one that already requires digital hardware. So arguably, there is not much modern advantage to a superhet design, except possibly cost when a very simple analog demodulation circuit is possible, for example AM.

## Answer (score 4, by Scott Earle)

There are several advantages to converting to an IF. These include:

- It is easier to make a multi-band receiver, as you just need to change the RF stage for each band, and everything after the IF is the same. It is cheaper to have one set of expensive filters in the IF path with a high-quality audio path, and then use it for every band.
- If the IF is a lower frequency than the RF stage, then filters can be much cheaper. Also, the tuning circuitry can be made much simpler. Imagine trying to tune accurately a microwave receiver to separate two signals 500Hz apart.
- Some receivers use multiple (two or three, sometimes four) intermediate frequencies, in an attempt to get around the disadvantages of a superhet design (image rejection is the big one).
- As mentioned in another answer, there can be issues with 50Hz/60Hz hum from mains electricity in a direct-conversion receiver. This is a complete non-issue in a superhet receiver, assuming that the final conversion to baseband and the audio path are designed properly to avoid it.

Of course there are also disadvantages - the big one is of course image rejection, but careful selection of an IF and some basic filtering can make that go away. Another one is the display of the frequency being tuned.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15288/what-are-the-advantages-for-a-receiver-that-uses-an-if-compared-to-direct-conv, by Andrew, Phil Frost - W8II, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
