# Theoretical Wifi antenna not working for the expected range

*Tags: antenna, wire-antenna, wifi · score 5*

## Question

### You buy a "20dBi omni" Wifi antenna, operating in the 2.4-2.5GHz band. You note that the expected range is not achieved from this 300mm long antenna. What could be wrong?

**Can someone please tell me whether may approach is correct**

λ(min) = 300/2500 = 0.12m = 120mm

Dipole length is therefore = 300mm/120mm = 2.5λ => 0.5λ (neglect '2' since its just a full revolution on smith chart??)

driven element have length of = 0.5λ/2 = 0.25λ

Actual gain of the antenna = 300mm/(0.25λ) = 10dB, therefore antenna in question is not 20dB and therefore thats why doesnt meet expected range. - is this the right way to calculate gain?

-Thanks.

## Accepted answer (score 1, by tomnexus)

Nice try but that's definitely not how you calculate gain!

Gain depends on many things, but first is the number of dipole elements in the stack. You could estimate the gain by guessing the number of half-wave dipoles that fit in the antenna. I suppose in your case a 300 mm antenna would fit four dipoles, to leave space for the top cap, connector and matching at the bottom.

Then the maximum theoretical gain will be:

2 dBi for the first dipole, + 3 dB for each further doubling, so 8 dBi.

In practice, each additional antenna also brings some further losses. So it is probably closer to: 1 dBi for one dipole, 3 dBi for two, 5 dBi for 4, 7 dBi for 8.

I've never heard of 20 dBi in an omni before. That would require a minimum length of 32 wavelengths, 3 m, and more in practice. It would have an elevation beamwidth of around 1 degree. Not much use having such a flat beam anyway. I think you have a 5 or 6 dBi omni, which should give you about double the range of the little dipole that comes with the router.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4970/theoretical-wifi-antenna-not-working-for-the-expected-range, by HappyFeet, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
