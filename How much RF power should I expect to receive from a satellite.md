# How much RF power should I expect to receive from a satellite?

*Tags: satellites · score 3*

## Question

I am trying to receive beacon from the analog satellites and observe its power on signal analyzer.I am using a 15dB gain and LNA with a 40dB gain. I am trying satellites like Ho-68(-81.64 dB at 56 deg elevation), JUGNU(-95 at 50 deg elevation), CO-57 etc. What should be the value of received power? Does anyone have any reference values?

## Answer (score 4, by Phil Frost - W8II)

You can calculate the answer with the [Friis transmission equation](What%20does%20the%20Friis%20transmission%20equation%20represent%20and%20how%20is%20it%20derived.md). The great thing about space communications is that the path is very close to free space, so even highly idealized calculations are pretty accurate.

According to some information on HO-68, its CW beacon transmits with a power of 200 mW (or 23 dBm). I don't see any information on its antenna gain, but it's probably not much, so we can just assume a gain of 1. It might be more: a free space dipole has a gain of 1.5. But it could also be less: it's unlikely its antenna is aligned precisely to your station.

From that same information it looks like HO-68's altitude is in the neighborhood ot 1200 km. Of course the distance is greater for anything but an overhead pass, so you can use some tracking software to calculate a more accurate number.

Using those numbers as examples, we can calculate the transmitted power, less free space path loss as:

$$ 23\:\mathrm{dBm} + 147.6 - 20\log_{10}(1200\:\mathrm{km} \cdot 435.79\:\mathrm{MHz}) \approx -124 \:\mathrm{dBm} $$

Adding your receive antenna gain (15 dB) brings this up to -109 dBm. You will want to make sure this is above the noise floor of your test equipment, otherwise you will measure nothing but noise.

Adding the LNA gain of 40 dB then brings it up to -69 dBm, which is approximately the power you'd expect to measure. It's probably safe to bet that's within 10 dB of reality, which must also take into account the alignment and gain of the satellite's antenna, cable losses, etc.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3754/how-much-rf-power-should-i-expect-to-receive-from-a-satellite, by Girish, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
