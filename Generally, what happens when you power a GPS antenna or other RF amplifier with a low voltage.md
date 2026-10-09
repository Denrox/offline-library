# Generally, what happens when you power a GPS antenna or other RF amplifier with a low voltage?

*Tags: lna, gnss · score 3*

## Question

I have a 5V active GPS antenna, and want to try using it on a device with a 3.3V bias provided. Obviously, operating at an over-voltage can damage or destroy the LNA. But what happens when the voltage is too low? Will it work with reduced gain, or will it cause some weird state and distort the signal? Is there a risk of damage of components?

I do not know the specifications of my antenna nor my device that provides the 3.3V bias voltage.

## Accepted answer (score 2, by rclocher3)

It's hard to say whether your active antenna would work properly if provided with 3.3 VDC instead of 5 VDC. I doubt that any damage would be done, but I'm not the engineer that designed the antenna. You might consider adding a boost regulator (and the other parts it requires) to your circuit, which could convert 3.3 VDC to 5 VDC. Here's such a part, selected more-or-less at random from the astonishing variety of boost regulators on offer.

Your LNA may work fine with 3.3 VDC, so you might as well just try it as-is first. A boost regulator has an inherently-noisy switching power supply inside, which might raise the noise level at the frequencies used by the GPS satellites, as @AndrejaKo points out, so there is some risk that a boost regulator would impair your circuit. However, the switching power supply internal to the boost regulator uses many of the external parts that the boost regulator requires; this gives the engineer an opportunity to reduce the noise level on the band of interest by tweaking the component values, if the noise proves to be a problem.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6843/generally-what-happens-when-you-power-a-gps-antenna-or-other-rf-amplifier-with, by Paul, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
