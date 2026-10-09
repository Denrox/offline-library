# How to derive antenna gain from radiation pattern

*Tags: antenna, radiation-pattern, path-loss, gain · score 8*

## Question

I need to calculate the antenna gain in both dimensions: azimuth and elevation. The datasheet of the antennas I am using has two different radiation patterns, one for the elevation and one for the azimuth.

Given the two angles I can derive 2 different values of gain, but then I don't know how to compose these values to obtain the overall gain. Should I sum them? Should I interpolate them?

## Accepted answer (score 4, by Glenn W9IQ)

First a bit of context regarding terminology.

In antenna engineering, we use the term "loss" to refer to RF energy that is lost as heat. This is typically an undesirable loss that creates inefficiency in the antenna system. This is the loss that Phil addressed in his (now deleted) answer.

When we speak about the directionality of an antenna, we use the term "gain". Gain is typically expressed in decibel form and in comparison to a reference antenna such as an isotropic antenna (dBi) or a free space dipole (dBd). Even when the gain is negative, it is still referred to as gain.

I edited your question as I believe you are actually asking about the *gain* of the antenna, not loss, and how to interpolate between the azimuth and elevation *gain* plots (thanks for confirming this in your later comments).

**Plot Styles**

Some gain plots will have 0 dB as the outer circle of the plot. This is an indication that 0 dB refers to the maximum possible gain of the antenna. The actual dBi or dBd value of this gain can be determined by looking at the antenna specification sheet.

Another style of plot, favored by the ARRL for example, shows the actual maximum possible gain on the outer circle of the plot. In this case the outer circle units should be shown as dBi or dBd.

**Interpreting Plots**

By convention, unless stated otherwise, the azimuth plot shows the maximum possible gain for each direction (regardless of elevation). The elevation plot will show the maximum possible gain for a given elevation but only in the direction of the maximum azimuthal gain. To then collectively interpret these plots, you would typically start with the azimuth plot to determine the direction with the maximum gain and then look at the elevation plot to determine at what elevation angle this maximum gain occurs. These two points from the two graphs will show the same gain. No further interpretation is needed. You may also examine the elevation gain in that direction for any other elevation angle of interest.

**Other Azimuthal Directions**

If you are considering an azimuthal direction that does not show the maximum possible gain, you should not refer to the elevation plot as the elevation pattern at that direction may be quite different from what is shown. You should instead obtain or generate a 3D model of the antenna pattern which you can examine or slice for the direction and elevation of interest.

**Oblique Angle Gain**

[Edit: Added based on further details from the OP in comments]

The azimuth and elevation plots are of little use when the direction of interest is not within the primary lobe of the antenna. In this case, I recommend using AutoEZ along with EZNEC to develop a model of the antennas involved. This will be an initial investment in effort that can then be quickly re-used to calculate the gain of the antenna pair at any oblique angle.

The AutoEZ tool is Excel based. It drives the EZNEC engine and allows a wide variety of "what if" type calculations from which you can derive tabular gain numbers for a wide range of azimuth/elevation angle pairs. You could also build in your Friis calculations into AutoEZ to give you a direct go/no-go analysis for any subscriber situation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12252/how-to-derive-antenna-gain-from-radiation-pattern, by gabriel-shatana, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
