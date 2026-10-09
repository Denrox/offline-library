# Why is the solar-flux index measured at 10.7 cm?

*Tags: sunspots, space-weather · score 17*

## Question

Why is the solar-flux index measured at 10.7 cm? What makes that such a special frequency?

## Accepted answer (score 11, by Amber)

So as it turns out, the reason behind this is fairly simple: the first receiver that was used to take recordings which wound up being linked with solar flux operated at 2800MHz (and thus a 10.7cm wavelength). In order to allow historical comparison of readings, that wavelength has been preserved ever since.

Here's an article with the full origin story.

## Answer (score 6, by Bogdanovist)

The component of the solar flux that actually impacts the ionospheric strength is the Extreme Ultra Violet (EUV) part of the spectrum. This is what causes the ionosation that produces the ionosphere. However, because the EUV is being absorbed by the upper atmosphere, it (fortunately!) doesn't make it to ground (at least the flux is much much lower at ground level). This means ground based receivers can't get a good handle on the actual solar EUV flux. In modern times we have access to satellites that measure the EUV flux outside the atmosphere.

Historically, there are two main proxy measurements of the EUV flux. The oldest is sunspots. Since the EUV is emitted from sunspot regions, the more sunspots the higher the EUV flux and hence the stronger the ionosphere.

The 10.7cm radio flux was serendipitously found to also correlate with the sunspot number in the years after WWII. The physics behind this is complex, and not fully understood. Empirically though, there is a non-linear relationship between sunspot number and 10.7cm flux that has held for several decades. The 10.7cm flux is a simpler measure than subjectively counting sunspots and can be performed during cloudy weather. Interestingly, during the last 5-10 years, the relationship between sunspot number and 10.7cm solar flux has been changing, most probably due to an overall weakening of the solar coronal magnetic field as the Sun moves into a quieter phase after the space age 'grand maximum' that has been experienced over the last 50 years or so.

Going forward, direct EUV measurements from satellites are becoming a more predominant method of measuring solar flux as relevant to the ionosphere although 10.7cm radio noise will still remain an important ground based back-up for many years.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/273/why-is-the-solar-flux-index-measured-at-10-7-cm, by Dan, Amber, Bogdanovist. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
