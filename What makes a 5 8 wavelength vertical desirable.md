# What makes a 5/8 wavelength vertical desirable?

*Tags: antenna, vertical-antenna · score 25*

## Question

An ordinary 1/4 wavelength vertical is smaller and resonant without any loading coil or matching network. What's the advantage to a 5/8 wavelength vertical? Why 5/8 in particular, and not something longer or shorter?

## Accepted answer (score 29, by WPrecht)

Indeed, why? A 5/8λ isn't resonant where a 1/4λ or 1/2λ would be.

The reason is the radiation pattern. The pattern for a 1/4λ monopole is essentially a doughnut, tasty and a pretty good pattern especially for a VHF antenna. Extending the antenna changes the current distribution. This flattens out the pattern removing power from the useless (for VHF purposes) vertical dimension and giving more horizontal gain and at a lower angle. See the following illustration from the late great L. Cebik:

Depending on the source, they will quote anywhere from 1.2dB to 3.5dB gain over the 1/2λ design. There has also been some discussion that in some areas (urban and mountainous terrain) the lower angle of radiation is a detriment and a standard 1/4λ or 1/2λ antenna is to be favored. I don't know. I guess they are pretty cheap, if this is a concern you can buy one mount and two and antenna, compare them for a bit and return the loser.

So, why 5/8λ? Why not long longer? After all more gain is better right? Well, inspecting the figure above you will notice the appearance of high angle lobes. As you lengthen the antenna past 5/8λ these lobes become more pronounced and break up the pattern in undesirable ways. Making it shorter maintains a good pattern, but the gain is less. So, 5/8λ is about optimal for this style of antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1142/what-makes-a-5-8-wavelength-vertical-desirable, by Phil Frost - W8II, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
