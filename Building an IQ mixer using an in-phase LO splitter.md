# Building an IQ mixer using an in-phase LO splitter

*Tags: electronics, mixer · score 3*

## Question

There are many examples of IQ mixers on the internet; all use 90 degree hybrids to split the LO to the mixers with the outputs being combined in-phase. I'm curious, could both mixers be fed an *in-phase* LO and a 90 degree hybrid used to combine the signals from the two mixers instead, in a sort of reversed IQ mixer?

Is such a thing even possible? And if not, why?

## Answer (score 2, by Marcus Müller)

Yes, this will work.

In fact, that is nothing but emulating an ADC with twice the sampling rate by using two synchronous ADC of the original rate, delaying one branch of the signal by half a sample clock.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6494/building-an-iq-mixer-using-an-in-phase-lo-splitter, by Sam, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
