# How can I use the 455kHz IF signal?

*Tags: equipment-design · score 3*

## Question

As I own a PL-660, I saw a post that 455kHz IF signal can be obtained by connecting a wire to the board.

I wonder, if I can tune to any signal by using this IF signal by SDR? And what are some common usage of this signal?

## Accepted answer (score 5, by Phil Frost - W8II)

Your radio, as most modern radios, is a superheterodyne receiver. These receivers work by first converting the intended signal to a fixed intermediate frequency (IF, 445kHz in your case) then demodulating that. This is in contrast to a direct conversion receiver, which demodulates the signal directly, without first converting it to an IF.

The superheterodyne design has a number of advantages, mostly due to the fact that much of the filtering and demodulation is done at a single frequency and so does not need to be tunable. For example, this allows crystal filters to be used, which can be very stable but can't be tuned.

Since whatever frequency to which you tune your receive is first converted to the IF, which is always the same frequency, if you can feed the IF to as SDR, then the SDR can see anything you can tune on the receiver. Essentially, you are replacing the demodulator of your receiver with an SDR.

The advantage here is that many cheaply available SDRs lack all the filters or the tuning range necessary to get the band coverage available in many receivers. Using an SDR at the IF allows one to use the radio for tuning, but use the SDR for demodulation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1727/how-can-i-use-the-455khz-if-signal, by Harold Chan, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
