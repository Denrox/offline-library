# Why are radio frequency ranges aligned on multiples of 3?

*Tags: frequency, jargon, bandwidth · score 9*

## Question

Why are the radio bands organized by multiples of three?

For example the HF band is from 3–30MHz and UHF is from 300–3000MHz. Why not multiples of 2? Or plain powers of ten?

## Answer (score 15, by natevw - AF7TB)

The ITU bands **are** actually delineated along plain powers of ten! They're just hiding a bit.

From the description above a table of all the bands on Wikipedia:

As a matter of convention, the ITU divides the radio spectrum into 12 bands, each beginning at a wavelength which is a power of ten ($10^n$) metres…

So the HF band is from 100–10m, or the UHF band is from 1–0.1m. Neat!

The "3" comes up only when the bands are given in **frequency** instead of **wavelength**. The usual conversion between those is given for example as:

**3**00 divided by wavelength in meters equals frequency in MHz.

[emphasis mine]

That formula is in turn just the general frequency vs. wavelength relationship with the ideal 299,792,458 m/s propagation velocity (i.e. the speed of light in a vacuum) rounded to 300 Mm/s.

So the "3" in all our bands is simply because the ITU defined them as simple magnitudes of ten along one unit (wavelength in meters), which happens to be related to another unit (frequency in hertz) by way of factors/definitions that round to three [with its own zeros after it].

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11811/why-are-radio-frequency-ranges-aligned-on-multiples-of-3, by natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
