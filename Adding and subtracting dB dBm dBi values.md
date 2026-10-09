# Adding and subtracting dB/dBm/dBi values

*Tags: antenna, math · score 4*

## Question

I've got a question and any clarification on that would be greatly appreciated. For calculating the pathloss in wireless communication we usually use the following formula: PL = pathloss (in dB) + shadow fading (in dB) + antenna gain (in dBi) + noise floor (in dBm) + penetration loss(in dB)

My question is: do I need to convert dBm to dB and then add all of these value together to calculate PL. Would be the PL in dB?

For example if I have a scenario in which path loss modeled as

$$ \text{Pathloss(dB)}=148.1+37.6\ \log_{10}(d) $$

shadowing is equal to 8dB, antenna gain is 10dBi, penetration loss is 5 dB and noise floor is 54 dBm, what would be the PL and what is its unit?

## Accepted answer (score 9, by hobbs - KC2G)

A value given in "dB" is a dimensionless ratio. 10dB is a ratio of 10:1, -10dB is a ratio of 1:10, 3dB is a ratio of approximately 2:1, etc.

dBi is dimensionless; it represents decibels relative to an isotropic radiator.

Values given in "dBm", "dBW", "dBV", etc. are dimensioned values, given as decibels *relative to some specific unit*. 0 dBm = 1 milliwatt, 0 dBW = 1 watt, 0 dBV = 1 volt, etc.; and e.g. 20dBm = 100 mW.

Keeping this in mind, it should be clear how you can and can't mix these units. If you add dB and dB, the result is dB. If you add dB and a dimensioned value, the result has the same unit. If you subtract two dB values with the same unit, the result is plain dB.

"13dBm + 3dB = 16dBm" is okay; this is the same statement as "20mW * 2 = 40mW".

"16dBm - 10dBm = 6dB" is okay; this is the same statement as "40mW / 10mW = 4".

"10dBm + 3dBm = ???" isn't okay; this is equivalent to "10mW * 2mW = ???" (okay, it's 20 mW^2, but what's the physical significance of a square milliwatt?)

And since "dBi" is dimensionless, you can use it the same as you would "dB", but remember that adding a dBi figure is "taking into account antenna gain" (e.g. 50dBm input power + 15dBi gain = 65dBm EIRP) and subtracting a dBi figure is the inverse operation.

## Answer (score 3, by Phil Frost - W8II)

A decibel (dB) expresses a ratio. So:

$$ -35\:\mathrm{dB} = 10^{-35/10} = 0.0003162 $$

This is a dimensionless number. Maybe it's the ratio of input power to output power, or something like that.

A dBm expresses a ratio relative to 1 milliwat. So:

$$ 20\:\mathrm{dBm} = 10^{20/10} \times 1\:\mathrm{mW} = 100\:\mathrm{mW} $$

When you do:

$$ 20\:\mathrm{dBm} - 35\:\mathrm{dB} $$

this is equivalent to:

$$ 10^{20/10} \times 1\:\mathrm{mW} \times 10^{-35/10} $$

Which is:

$$ 100\:\mathrm{mW} \times 0.0003162 = 0.03162\:\mathrm{mW} $$

dBm can't be converted to dB any more than 100 mW can be converted to 100 (no unit); doing so would be dimensionally inconsistent.

Adding (or subtracting) decibels is equivalent to multiplying (or dividing) ratios because:

$$ b^c \times b^d = b^{c+d} $$

and,

$$ \log(xy) = \log(x) + \log(y) $$

Multiplying a number in watts by a dimensionless number yields a number in watts. Likewise, adding or subtracting dB to dBm yields a number in dBm.

dBi is a bit unusual because you might think the "i" at the end implies some dimension, but dBi expresses a ratio of antenna gain relative to an isotropic radiator. And the gain of an isotropic radiator is just 1 (dimensionless) by definition, so dBi are also dimensionless.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17591/adding-and-subtracting-db-dbm-dbi-values, by susan, hobbs - KC2G, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
