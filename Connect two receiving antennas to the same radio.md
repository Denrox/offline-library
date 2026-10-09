# Connect two receiving antennas to the same radio

*Tags: antenna, receiver, antenna-system · score 10*

## Question

I have built a 1090 MHz ADS-B antenna roughly following some video instructions. It appears to work reasonably.

However, because of how it is placed, it captures signals for more or less a half of the sky. So I would like to build another and put it on the other side of the house to receive from the other half. Is there some proper way to attach the two antennas to the same receiver (possibly connecting them via some impedance matcher or whatever is needed)? Or do I really need to put two receivers in operation?

(beside the practical answer itself, I am also curious of the explanations)

## Accepted answer (score 9, by Kevin Reid AG6YO)

Yes, you can do this. There are two issues: connecting it to the radio, and the effect on reception. The latter might be problematic enough that using two receivers is actually a better option.

#### Connecting two antennas to the radio

If you simply connect two antennas in parallel, the math is just like connecting two resistors in parallel: the impedance is halved. This is in principle a problem, because there will be losses due to the mismatch reflecting some received power.

The “correct” thing to do is use a *power combiner* (a.k.a. power divider (when used in the other direction) or “splitter” in TV-cable-land). This device has three ports with equal impedances, one of which goes to your receiver and the others go to the two antennas. Since you're using 75 Ω TV coax for your antenna, you might as well get one sold for TV/cable/satellite use.

However, not using one might not matter much, or might even improve things, because there's a very good chance that your antenna is not actually well matched to your receiver already (because your antenna's resonant frequency is not 1090 MHz, or the antenna has a resistive impedance not equal to the receiver's or coax's impedance). I recommend trying things and seeing what happens. Or if you have access to an antenna analyzer, start measuring.

#### Effect on reception (radiation pattern)

What you're doing is building an *array antenna*. When the signals from the two antennas meet, the waves are summed, and this means there can be either constructive or destructive interference (stronger or weaker resulting signal). Which one you get depends on the *phase* of the signals.

If your antennas literally saw exactly half the sky, then there would be no problem. But in practice, they will overlap in coverage — a transmitter (aircraft) can be in the view of both antennas at once. In this case, if the signals from both antennas are *in phase*, you will receive a good signal; if they are *out of phase* (more or less), you will receive a weaker signal than if you had only one of the two antennas.

In order to make sure the signals are in phase in this case, the coax from the two antennas to the combiner must be of equal length, plus or minus complete wavelengths. A wavelength at 1090 MHz is 27.5 cm; but this must be adjusted for the velocity factor of the coax, so the easiest thing is to use identical lengths.

If you were building a array antenna in free space, then the antenna will have a highly uneven pattern with many nulls (directions of almost no reception), as the varying distance to the two antennas from the transmitter changes the phase, but insofar as your house blocks the signal from arriving at more than one antenna at a time it will cause a more uniform pattern.

You can in principle use antenna modeling software to determine the pattern to expect and adjust it to be omnidirectional, but it would be very, very hard to create a sufficiently accurate model of your house.

#### Using two receivers

If you're using RTL-SDR dongles or similarly cheap receivers, using two receivers is **highly likely to be a better option**. Using two receivers:

- avoids the possibility of the two antennas canceling each other out.
- avoids signal loss from the length of coax needed to cross your house (coax which has low loss at 1 GHz is expensive and bulky).

The disadvantage of separate receivers (besides needing software to combine the data streams in this particular application) is that if the transmitter *is* in sight of both antennas, you don't get the SNR benefit from receiving a stronger combined signal.

## Answer (score 5, by Pete S)

Rather than two receivers, maybe a switch that selects between antennas could be a cheaper option?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4905/connect-two-receiving-antennas-to-the-same-radio, by Giovanni Mascellani, Kevin Reid AG6YO, Pete S. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
