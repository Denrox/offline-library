# How does a Dual Band Handheld Antenna work?

*Tags: antenna · score 10*

## Question

Looking to get a (highly recommended) NAGOYA NA-771 37cm "Dual band (2M/70cm) handheld antenna" for my Baofeng UV-5R.

If my math is correct - this is about a half-wavelength antenna for 70cm, but doesn't seem to correlate to anything for 2m.

What does this mean? Is it really good for 70cm but no so much for 2m, or am I misunderstanding the principals/construction of this antenna. (Also, it's just a handheld antenna, so it's not a "dipole" nor does it have an evident "ground" - so I might not just understand what it "is").

## Accepted answer (score 12, by Phil Frost - W8II)

A half-wave dipole, or a quarter-wave monopole, are resonant on their fundamental frequencies and all odd harmonics thereof. 2m and 70cm have that harmonic relationship, 70cm being approximately the first odd harmonic of 2m:

$$ 144 \mathrm{MHz} \cdot 3 = 432 \mathrm{MHz} $$

So, an antenna that looks like a half wavelength on 2m will look like 1.5 wavelengths on 70cm. Although the radiation pattern is different, the antenna impedance is the same, and so will provide a good match to the radio in either case.

Keep in mind that handheld antennas are usually monopole antennas, like a vertical. They are approximately equivalent to a dipole of twice the length. There is no obvious ground plane as there is with a vertical because mobile antennas usually sacrifice performance for size. See [How do Handheld antennas work without ground?](How%20do%20Handheld%20antennas%20work%20without%20ground.md)

For further reading, I suggest antenna-theory.com, which expands on some math and shows diagrams of radiation patterns under various conditions.

## Answer (score 3, by WPrecht)

I don't have one, but I have similar antennas. What "it" is is slightly more metal than the stock antenna. Reviews on this antenna are mixed and some comments state there are counterfeit Nagoya antennas out there. Why someone would want to counterfeit something with a margin this low is beyond me. Never the less many folks feel this improves performance over the stock unit.

My guess would be that it uses coil in the base to get 1/4 wave on 2m and bypasses it for 1/2 wave on 70cm.

What this means for you is impossible to predict. VHF/UHF being largely line of sight, things like terrain, power, repeater siting and power all factor into the kind of reception you will get. I wouldn't trust the dB rating on anything like this. For one thing, at least my UV-5R didn't state the gain of it's stock antenna, so it's hard to know if this is an improvement. It probably is, but at $14, you may as well get one and do a test in your environment. If it sucks, return it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1918/how-does-a-dual-band-handheld-antenna-work, by Brad, Phil Frost - W8II, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
