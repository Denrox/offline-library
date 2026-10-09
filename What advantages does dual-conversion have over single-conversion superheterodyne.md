# What advantages does dual-conversion have over single-conversion superheterodyne?

*Tags: receiver, equipment-design, superheterodyne, mixer · score 4*

## Question

I've seen a variety of radio block diagrams, and some have two mixers inline with the signal.

If the signal is already in a frequency range suitable to work with, what does the second conversion/mixer offer that the single-mixer design does not?

## Accepted answer (score 4, by WPrecht)

The reason that this is done is the difficulty of obtaining sufficient adjacent channel selectivity in the front-end tuning while still achieving high levels of image rejection across a range of frequencies as wide as the HF bands.

The first intermediate frequency is higher, often in the range of 10MHz. This is used for adequate image rejection, while the lower second intermediate frequency, usually the common 455KHz, provides high selectivity and gain.

High-end HF transceivers have usually **3 IF stages**, for even higher selectivity.

You can also review this [question](How%20is%20the%20IF%20for%20a%20superhet%20selected.md) and it's answers for more insight into IF selection.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1015/what-advantages-does-dual-conversion-have-over-single-conversion-superheterody, by Adam Davis, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
