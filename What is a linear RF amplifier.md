# What is a linear RF amplifier?

*Tags: amplifier · score 15*

## Question

Most of the RF amplifiers advertised, and most of the questions about amplifiers, are "linear" amplifiers.

What is a linear amplifier, and what other common amplifier type(s) exist that requires people to say "linear" every time they talk about RF amplifiers?

## Accepted answer (score 15, by Phil Frost - W8II)

Google defines "linear" as "arranged in or extending along a straight or nearly straight line." Wikipedia tells me that "linearity refers to a function or relationship which can be graphically represented as a straight line". Such systems can be described by an equation of the form $y=mx+b$.

In the case of RF amplifiers, the relationship is the input voltage vs. the output voltage. The output is identical to the input, only "louder". Mathematically, $V_{out} = A \cdot V_{in} + 0$, where $A$ is the voltage gain of the amplifier.

Linearity is a generally desirable property but it comes at the cost of reduced efficiency. At any instant, the amplifier's output is probably something somewhere between its power supply rails, and consequently, the output transistors will have some voltage $E$ across them and some current $I$ through them. The rate of electrical energy consumption is the product of these two: $P=IE$. That consumed energy can't vanish: it's converted into heat. This requires big heatsinks, and it drains your batteries faster or runs up your electric bill.

Here's a solution to the heat problem: we amplify the input signal so much that the output is always greater than the supply rails. Now we are effectively connecting the load directly to one supply rail or the other. Now the output transistors either have 0V across it, or are passing no current. Thus, the power ($P=IE$) in the transistors is low because always either current or voltage is nearly 0. The energy is going to the antenna, not to heating the transistors.

The problem is now that the output is horribly distorted. If the input was a nice clean sine wave, the output will be a square wave, full of odd harmonics. We can remove the harmonics with a filter, and because the filter is made of reactive components like inductors and capacitors which alternately store and release electrical energy, rather than converting it to heat, they don't get so hot, and the amplifier is more efficient.

This mostly solves the distortion problem, but something is lost: the amplitude of the input signal. Fortunately, the frequency is preserved.

So now we know when non-linear amplifiers are acceptable: when the amplitude of the signal is insignificant, such as FM, or frequency modulated digital modulations like FSK, some PSK flavors, or GMSK. Modes where amplitude is significant like AM, SSB, or digital modulations like QAM require a linear amplifier.

## Answer (score 3, by Communicationantennas.com)

Actually, any amplifier is non-linear but has a linear region. The linear region is a region of power input to the amplifier. If you use the amplifier at an appropriately low power level, it works as linear in this region. You can find the linear region in the datasheet for the amplifier.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1319/what-is-a-linear-rf-amplifier, by Adam Davis, Phil Frost - W8II, Communicationantennas.com. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
