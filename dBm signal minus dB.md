# dBm signal minus dB

*Tags: rf-power, measurement, math · score 8*

## Question

I've got a 27dBm signal that I'm going to put through a 6dB attenuator. How do I work out the resultant signal in dBm?

I've tried Googling that without any luck.

## Accepted answer (score 8, by natevw - AF7TB)

Decibels are all "ratios" at their core. A unitless dB is a simply a ratio of one number to another, perhaps input power relative to output power. We can also use decibels for absolute values, by fixing the denominator to a standard reference — e.g. one milliwatt in dBm. But the most convenient thing about decibels is that, although they are ratios, because they have been "logarithm"-ed, we can add and subtract them instead of having to multiply and divide.

So if you have a 27 dBm signal attenuated by 6 dB, the result will be a 21 dBm signal, since 27 minus 6 is 21.

We could have looked at this by saying "I've got a 500 mW signal which I'm going to put through an attenuator which divides signals by 3.98" and gotten a result of 125.6 mW. That's not so bad with a calculator, but a bit harder to do precisely in our head especially after we add in more links (amplifiers, antenna gain, coax/path losses, etc.) to a communications system.

I found a page dB: What is a decibel? that goes more in depth if you're interested in the underlying math. That page is in the context of audio, but the concepts are generalizeable. In fact, going beyond decibels entirely, a slide rule uses the same underlying principle to make general multiplication/division easier without an electronic calculator.

## Answer (score 7, by mike65535)

Think about it this way.

27 dBm means 27dB above a milliwatt.

Take 6dB away.

Now you have something that's 21 dB above a milliwatt.

Or, 21 dBm.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12454/dbm-signal-minus-db, by Chris Pavey, natevw - AF7TB, mike65535. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
