# How does signal strength relate to bandwidth?

*Tags: digital-modes, ssb, theory, bandwidth, psk31 · score 9*

## Question

Let's say I have a 25 W transmitter. First I transmit some SSB signal with 2500 Hz bandwidth (no audio compressor is used, etc...). Then I transmit a BPSK31 signal with at most 100 Hz bandwidth using the same power.

Is it accurate to say that BPSK31 signal is at least 2500/100 = 25 times stronger, e.g. it will be received as if an SSB signal was transmitted using 625 W? Or, in other words, if someone somewhere receives my SSB signal with some level, he or she will receive a BPSK31 signal transmitted using 1 W with the same level?

If this is false, what is the actual relation between the signal strength and its bandwidth, if there is any?

## Accepted answer (score 13, by Kevin Reid AG6YO)

It depends on what you mean by "stronger".

Ignoring actual limitations of your hardware and just considering the theory of communications, if you have 25 W of transmit power, then you can spread that over as much bandwidth as you want, and **you're always transmitting 25 W of power.**

The quantity which is 25 times higher in the 100 Hz case than the 2500 Hz case is called *power spectral density* (PSD), which we can get by dividing the power by the bandwidth and measure in watts per hertz. **In your two cases you're transmitting 0.25 W/Hz and 0.01 W/Hz;** that's how they are different.

The place that PSD starts being interesting to calculate with is when you want to consider *noise* — by which I mean here “all RF that is not your transmitter”. We can roughly approximate noise as having a constant PSD (this is true when it is primarily wideband natural or manmade noise as opposed to strong transmissions specifically on the same or a nearby frequency). From this we can conclude that if your receiver's filter is wider, it receives proportionally more noise power along with the desired transmission — making the signal-to-noise ratio (SNR) worse.

This is why — to compare two modes that are alike in that they are both decoded by ear — CW can get through where SSB cannot, because the signal-to-noise ratio is much higher in the narrow bandwidth of CW. (It also helps that the ear has to distinguish only the beginning and end of the tone rather than phonemes; in digital terminology, there are fewer *symbols* the receiver must discriminate between. Of course, that means that information is being transmitted at a slower rate.)

However, you should not conclude that using the same power in less bandwidth *always* improves SNR *after demodulation.* For example, spread-spectrum transmissions use a very wide bandwidth without correspondingly worse performance. To see why this can be true, consider a simple frequency-hopping spread spectrum system: the receiver and the transmitter agree on a sequence of frequencies to rapidly jump between in sync with each other. Therefore, at any moment the receiver only uses the signal in that narrow bandwidth, with correspondingly low noise, even though overall the system occupies a wide bandwidth. This effect is called process gain.

## Answer (score 3, by Phil Frost - W8II)

If by "strength" you mean "subjective volume as determined by a human operator", then reducing the bandwidth of the transmission while keeping the transmitter power constant does indeed produce a "stronger" signal.

This is because noise is typically assumed to have a constant power spectral density over some range of frequencies of interest. Meaning, every hertz of bandwidth has some amount of power in it. Double the bandwidth, and the noise power is doubled. However the signal has the same power regardless of bandwidth. Thus, narrowing the bandwidth reduces the noise power, and increases the signal to noise ratio.

We could write this mathematically as:

$$ \text{subjective strength} \approx {S \over N_0 B} $$

where:

- $S$ is the received signal power in watts
- $N_0$ is the noise spectral power density in watts per hertz
- $B$ is the channel bandwidth in hertz

If the transmitter power is fixed, and we can't increase the received power by upgrading the antennas, reducing the transmission distance, etc., and the noise power is fixed by the conditions at the time, then the only thing we can really change is $B$ by choosing to transmit a wider or narrower modulation. We can then adjust the receiver filter bandwidth to remove noise outside the bandwidth also occupied by the signal, or even if we don't adjust the receiver filter the human auditory system is pretty good at doing this kind of filtering without any additional help.

But if your definition of a "strong signal" is "could theoretically send more information per unit time", a narrow modulation is actually worse. You need the Shannon-Hartley theorem:

$$ \text{channel capacity in bits/sec} = B \log_2\left( 1 + {S \over N_0 B} \right) $$

The Shannon-Hartley theorem provides an upper theoretical limit on the rate at which information can be communicated in an additive white Gaussian noise (AWGN) channel. Actual communication may occur at below this rate of course, but not above.

As an example, say the signal power ($S$) is 1 (the particular unit doesn't matter, as long as we use the same one for noise) and the noise density ($N_0$) is 0.000004. This gives a SNR of:

$$ {1 \over 0.000004 \cdot 2500} = 100 = 10\:\mathrm{dB} $$

This is a reasonable SNR for an intelligible SSB contact. The theoretical maximum channel capacity is:

$$ 2500 \log_2\left( 1 + {1 \over 0.000004 \cdot 2500} \right) = 16646\:\text{bits/sec} $$

It's a bit odd to think of spoken words in terms of bits per second, yet within information theory this is a valid thing to do. We could just as easily consider this example as any digital modulation that occupies 2500 Hz.

Now reducing the bandwidth to 100 Hz yields a channel capacity of:

$$ 100 \log_2\left( 1 + {1 \over 0.000004 \cdot 100} \right) = 1129\:\text{bits/sec} $$

This is actually an order of magnitude *decrease* in channel capacity. So in this sense, a narrower bandwidth is actually *weaker*! Although the narrower channel may be easier to hear, its theoretical capacity to communicate information is less.

How can this be? Say the modulation is something really simple, like the transmitter is either on for 1 seconds transmitting a steady carrier, or it's off. The receiver has to decide for each 1 second interval if the transmitter is on or off. This can occupy a very small bandwidth, 0.5 Hz at a minimum. And let's further assume the transmitter power is high enough that the chance of an error is negligible.

In this 0.5 Hz, one bit is communicated per second.

Now say we have four receivers each tuned to a slightly different frequency, and in each interval, the transmitter will transmit on one of the 4 frequencies.

- If the first receiver detects the tone, we say this means 00.
- If the second receiver detects the tone, this means 01.
- The third receiver, 10, and...
- the fourth receiver, 11.

Adding more receivers doesn't make any one of them less reliable, so simply increasing the channel bandwidth also increases the channel capacity.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12960/how-does-signal-strength-relate-to-bandwidth, by Aleksander Alekseev - R2AUK, Kevin Reid AG6YO, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
