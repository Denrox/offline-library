# decibels as ratio and dBm as absolute values

*Tags: rf-power · score 9*

## Question

I am just trying to understand the nitty gritty of using decibels and absolute measurements in dBm. I see them referred to routinely in RF, and using reference sheets I can understand enough to make sense of gains and losses, but I would like instead to acquire a much better understanding for myself, being able to convert and calculate freely (without the need for reference sheets) between any power or dB value.

I think I understand that dB is merely a ratio of measurement. But if, for example, a component under test had 20W at its input and 15W at its output and there is an overall loss of 5W, how would that be worked out and expressed in a ratio of dB?

Trying to work it out I did:

```
20W (in) = 10log10(20W/1W) = 13dB(W)
15W (out) = 10log10(15W/1W) = 11.76dB(W)
so, component power loss = 13dB(W) – 11.76dB(W) = 1.24dB(W)

```

However, I can see that I am merely subtracting absolute measurements still and not determining the dB ratio of power transfer efficiency or loss. If so, then what would be the equivalent dB ratio for this example?

In addition, I am able to convert 13dB(W) back to watts with:

```
10 to the power of (13/10) or 10^1.3 = 19.95W

```

and so too for 11.76dB(W):

```
10^1.176 = 14.997W

```

but for 1.24dB(W):

```
10^0.124 = 1.33W

```

which does not appear correct, as I expected instead a value of ~ 5W, for which 1.24dB(W) represents between 13dB(W) and 11.76dB(W), so I unsure where I am going wrong. If someone could let me now I would sure appreciate the insight.

Finally, what would it mean to say a receiver has a receive level of -45dBm?

Is it right to conclude that such a receiver is capable of extracting information from signals received at -45dBm less power than what they (signals) were originally transmitted at? Or actually it just occurred to me that since 45dBm is an absolute value that it perhaps means that the receiver could receive signals as low as -45dBm or:

```
10^(-45/10) = 0.0000316mW

```

and still be able to extract the information transmitted so long as the S/N ratio is adequate? Which if that was the case then, if one transmits a signal with 20W or 43dBm of power, then the signal could be attenuated by up to 88dBm:

```
43dBm - -45dBm = 88dBm

```

and still be detected adequately enough by the receiver in question so that the original information sent is received?

I hope I have explained my questions well enough to be easily understood.

## Accepted answer (score 12, by Kevin Reid AG6YO)

Trying to work it out I did:

```
20W (in) = 10log10(20W/1W) = 13dB(W)
15W (out) = 10log10(15W/1W) = 11.76dB(W)
so, component power loss = 13dB(W) – 11.76dB(W) = 1.24dB(W)

```

Your error is merely in the units, not in the calculation. Taking the difference of two dBW (or any two absolute dB values *using the same reference level*) gets you dB.

If you want to think of this algebraically, you could use the definition

$$x\,\mathrm{dBW} \equiv x\,\mathrm{dB} + (0\,\mathrm{dBW})$$

where $(1\,\mathrm{dBW})$ can be treated as a funny-named constant we don't need to assign any numerical value to, much like *any other unit symbol* — except that we're adding, not multiplying, it, because logarithms transform multiplications to additions (basic property: $\log(a\cdot b) = \log a + \log b$). If we transform the above to non-logarithmic form, we get the trivial and obvious equation

$$y\,\mathrm{W} = y \cdot (1\,\mathrm{W})$$

Using the above definition for dBW, your calculation becomes:

$$ \begin{align} &\phantom{{}={}} 13\,\mathrm{dBW} - 11.76\,\mathrm{dBW} \\ &= (13\,\mathrm{dB} + (0\,\mathrm{dBW}) - (11.76\,\mathrm{dB} + (0\,\mathrm{dBW})) \tag{change notation}\\ &= 13\,\mathrm{dB} - 11.76\,\mathrm{dB} + (0\,\mathrm{dBW}) - (0\,\mathrm{dBW}) \tag{reorder terms}\\ &= 13\,\mathrm{dB} - 11.76\,\mathrm{dB} \tag{$x - x = 0$} \\ &= 1.24\,\mathrm{dB} \tag{compute} \end{align} $$

However, I can see that I am merely subtracting absolute measurements still and not determining the dB ratio of power transfer efficiency or loss. If so, then what would be the equivalent dB ratio for this example?

The result of the subtraction *is* a ratio expressed in dB; you've just mislabeled it as being absolute.

In addition, I am able to convert 13dB(W) back to watts … but for 1.24dB(W):

```
 10^0.124 = 1.33W

```

which does not appear correct, as I expected instead a value of ~ 5W

The 1.24 value is dB, not dBW, so treating it as an absolute value does not get you the answer relative to the original power level you measured. (However, there is a meaning to the figure 1.33 W: it's the amount of power in that would be required to get 1 W of power out. You can check this against simply computing ratios with no logarithms.)

Remember, logarithms are simply a computational convenience. If you have a calculation starting in watts and ending in watts, then you can do the intermediate work in dBW and dB (adding and subtracting) or in power and ratios-of-power (multiplying and dividing) and get the same answer. If you don't get the same answer, you made an error in setting up the formulas.

Finally, what would it mean to say a receiver has a receive level of -45dBm? … Or actually it just occurred to me that since 45dBm is an absolute value that it perhaps means that the receiver could receive signals as low as -45dBm … then, if one transmits a signal with 20W or 43dBm of power, then the signal could be attenuated by up to 88dBm:

Yes, you have this right, except that it's “attenuated by up to 88 dB”, not dBm.

## Answer (score 5, by Phil Frost - W8II)

Trying to work it out I did:

```
20W (in) = 10log10(20W/1W) = 13dB(W)
15W (out) = 10log10(15W/1W) = 11.76dB(W)
so, component power loss = 13dB(W) – 11.76dB(W) = 1.24dB(W)

```

Here's your problem: the answer is 1.24 dB, not 1.24 dB(W).

Why? Subtraction of logarithms corresponds to division. You end up with watts in the numerator and denominator which cancel, leaving you with a unitless ratio.

Formally:

$$ \log(a) - \log(b) = \log\left({ a \over b }\right) $$

When you do $ 13\:\mathrm{dB(W)} - 11.76\:\mathrm{dB(W)} $, you are actually doing:

$$ \require{cancel} { \left(10^{13\over 10}\right)\cancel{\mathrm W} \over \left(10^{11.76 \over 10}\right)\cancel{\mathrm W} } = {19.95 \over 14.10 } = 1.33 $$

We can convert 1.33 to decibels:

$$ 10 \cdot \log(1.33) = 1.24\:\mathrm{dB} $$

This also raises a point of common practice: since you are calculating a *loss*, it's conventional to arrange the calculation so that the result expressed in decibels is *negative*. A negative number in decibels corresponds to a fraction less than 1. Example:

$$ 11.76\:\mathrm{dB(W)} - 13\:\mathrm{dB(W)} = -1.24\:\mathrm{dB} $$

More generally:

$$ \text{power out} \ -\ \text{power in} = \text{loss or gain in decibels} $$

Which, if you think about the identity above, is equivalent to

$$ {\text{power out} \over \text{power in}} = \text{loss or gain as a ratio} $$

This makes the ratio not 1.33 as calculated above, but 1/1.33 or 0.752. This allows us to calculate losses in watts by multiplication. If we were to put 100W into this system, for example...

$$ 100\:\mathrm W \cdot 0.752 = 75.2 \:\mathrm W $$

...we'd get 75.2W out.

## Answer (score 2, by Steve Noskowicz)

When you use this stuff on the job, it becomes second nature...

I hope these other ways to look at in general help.

The thing to remember is that dB is only used to represent a *ratio of two powers*. That is the definition. A **bel** is a ratio of power of 10 to 1; after Alexender Graham Bell. That is why the B is capital and the d is not. (see note below) A decibel is one tenth of a bel.

A ratio means that you divide one by the other (when expressing power in watts). The reference is on the bottom (denominator) of the ratio.

That 5 W difference between input and output is not a ratio of 5 W to anything, so converting it to dB makes no sense, it is a **difference**, not a ratio. I can't think of a time when the actual amount lost is expressed that way. We usually use -1.25 dB or express it as an efficiency of 75%.

We only say that there is 1.24dB of loss (actually 1.2499, or 1.25), we (engineers) also can say that it has a "gain" of -1.25 dB. These represent **ratios** of 1.33 and 0.75 respectively.

You subtracted in the reverse order you should have. When calculating the difference of two things you subtract the reference from your number. Since we usually reference the output to the input, the difference is *minus 5* watts.

Please note the following:


20 to 15 watts is a loss of 5 W, but a ratio of 0.75 and -1.25 dB.


1 W to 0.75 W is a loss of 0.25 W, but a ratio of 0.75 and -1.25 dB.

Going to dB allows you to add or subtract numbers when looking at gains and losses..

The "absolute" versions are still ratios referenced to a known power that is shown by the last letter:


dBm references a mW


dBW reference is a watt

TV engineers use dBk = reference to a kW.

*Note:* For the pedants, we do use dB to represent voltages (and sometimes currents) in places like OP-Amp designs, where the powers are not being calculated. The powers and impedances are totally ignored in many cases.

However, this *is improper* use of dB .

Double however, those of us who do that know what we mean and that makes it OK. This is because there are places where only the voltages matter and powers are unimportant, and using dB is still useful in the grand scheme.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3500/decibels-as-ratio-and-dbm-as-absolute-values, by nanker, Kevin Reid AG6YO, Phil Frost - W8II, Steve Noskowicz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
