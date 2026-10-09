# What is the purpose of having multiple bays for a bowtie antenna?

*Tags: antenna, antenna-theory, bowtie · score 3*

## Question

What would be the difference between a two-bay antenna designed like this:

and a four-bay antenna designed like this:

Assuming that everything about these two antennas are identical aside from the number of bays, what exactly does "adding more bays" do for a bowtie antenna?

## Accepted answer (score 2, by Phil Frost - W8II)

It increases the directionality and gain of the antenna. This helps it reject noise coming from directions other than towards the transmitter. The higher signal to noise ratio leads to better reception.

For this antenna as drawn, the directions of maximum gain are two: one coming out of the page, and one in the opposite direction. Sometimes these antennas will have a reflector behind them to reduce that to just one direction.

For a wave arriving from the maximum gain direction, the wavefront hits all the bowties at the same time. The individual signals received from each bowtie then add constructively.

It's not immediately obvious why there's the crossover in the antenna. That is, why not are all the blue halves on one side, and the reds on the other? The reason is the two outer bowties are farther away from the feedpoint than the inner bowties. If the incoming wave hits all the bowties at the same time, but then the bowties are at different lengths from the feedpoint, by the time the signals have traveled from the bowtie to the feedpoint they will no longer be in phase, and no longer add constructively.

The crossover compensates for this delay. The wave is oscillating with some period; if we wait half this period the polarity at that instant will be reversed. The crossover accomplishes the same thing, not by waiting but by crossing the wires. Meanwhile, the extra distance that must be travelled from the farther bowties introduces another half-period of delay. That half-period, plus the additional half-period of the crossover, means that we are effectively delaying the signal by a full period, which is the same as not delaying it at all.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7531/what-is-the-purpose-of-having-multiple-bays-for-a-bowtie-antenna, by user420777, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
