# Tweak antenna resonant frequency higher

*Tags: antenna, hf, wire-antenna, impedance-matching · score 3*

## Question

This is a very simple question and I'm sure if I had a bit more background knowledge, I could figure it out myself.

Let's say I have a 1/4 wave vertical antenna that is slightly too long, but it is impractical to cut shorter or fold back on itself. What do I need to add to raise the resonant frequency slightly higher (10 - 100kHz) without using a full-fledged tuner? To put it simply, I can't use a tuner. Can I do it with one or two components?

With electrically short antennas, I know I can add an inductor in series with the antenna to lower the resonant frequency, but how do I do the opposite?

## Answer (score 5, by Brian K1LI)

An antenna which is electrically long at the desired frequency usually presents inductive series reactance at the feedpoint. This inductive reactance can be compensated by adding series capacitive reactance - a single capacitor - between the feedline and the antenna at the feedpoint. This will probably be a relatively narrow-band solution.

Be sure to use a capacitor which can withstand the RF current flowing through it and the RF voltage that will appear across it. You must use a capacitor that presents high Q (low loss) at the operating frequency. I know from sad experience that using a "transmitting" or "doorknob" capacitor is no guarantee of success. To avoid converting your capacitor into smoke, start by applying very low power and, at the very least, measuring the capacitor's temperature before increasing the power. Duty factor will also affect heating; extended application of a steady carrier - for example, tuning, AM, FT8, etc. - will produce more heating than CW or SSB.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15540/tweak-antenna-resonant-frequency-higher, by Synaps3, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
