# Can an ultra-wideband system transfer data at high speed without precise clock synchronization?

*Tags: rfi, modes, dsp · score 6*

## Question

Recently, ultra-wideband technology has been in the news again. From the Wikipedia article:

UWB transmissions transmit information by generating radio energy at specific time intervals and occupying a large bandwidth, thus enabling pulse-position or time modulation.

From other reading I've done, I've gotten the impression that UWB signals can be used in a way quite similar to radar which makes sense. (In that it seems relatively plausible that one could send out a *known* broad-spectrum signal and look for reflected returns that correlate well to what was sent.)

But how would UWB work for transmitting data between two transceivers? My impression is that the transmit power is weak enough and spread out enough that these devices are allowed by the FCC as ± a Part 15 **un**intentional radiator. Without sharing an exact timebase [at least, not initially?] how would a receiver discern signal pulses it should be interested in, versus other random broad-spectrum noise? And how many devices could be communicating simultaneously in a given area before the strategy falls apart?

## Answer (score 3, by Marcus Müller)

As hotpaw2 said, the thing is that while it looks like random noise, the actual UWB signal *is* correlated, in *some specific way* known to the receiver.

I'll explain this using an example (keeping it short, I'm at GRCon):

Imagine your UWB transmitter using a scheme where it generates a wideband noise signal. The way it encodes a "0" bit is that it turns on the noise for exactly 1 ms, and then off for exactly 1 ms. To encode a "1", it turns off the noise first, then on, same 1ms+1ms timing.

Your receiver would now always aggregate the noise power it sees for 1 ms, and for the following 1 ms; it would then compare these two, e.g. by dividing the first by the second energy value. If their difference is significant enough, it would be fairly sure that a) there is a transmitter operating, and b) what the transmitted bit was.

If it was just noise, it would be unlikely that it'd be on only in the first millisecond, but not in the second.

In reality, you probably wouldn't do a 1 ms on, 1 ms off scheme (that only gives you 500 symbols per seconds, and each symbol only carries one bit. Not a lot of data speed!). Instead, for UWB, the typical times would more be in the nanosecond scale. Then, you wouldn't do a simple on-off or off-on method, but more likely a more complex sequence, dividing the symbol time in way more *chips*, allowing for way more orthogonal sequences ("orthogonal" means that if you add two sequences, you can still detect the presence of both sequences from the sum). That would allow for more bits per symbol, or for multiple simultaneously operating transmitting devices.

I didn't address clock synchronization here so far:

Especially for power-detection-only systems like UWB, symbol timing recovery is necessary; you'd often counter that by using short packets to avoid that clocks run out of sync, and start these short packets with a specially crafted sequence that has an autocorrelation that allows you to estimate the chip rate easily.

## Answer (score 3, by hotpaw2)

Even if all the transmitted UWB pulses are identical, and initially start at an unknown time, the pattern variations in the delta time between pulses could be used to code information.

As with any spread (spectrum or otherwise) system, a longer sequence with more coding might allow more (orthogonality coded?) signals to occupy a channel at some given reliability probability level.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15347/can-an-ultra-wideband-system-transfer-data-at-high-speed-without-precise-clock, by natevw - AF7TB, Marcus Müller, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
