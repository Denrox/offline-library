# Can I use an RG-8X crimper/stripper on LMR-240?

*Tags: coaxial-cable, connectors · score 3*

## Question

From all my reading online it seems LMR-240 and RG-8X are only about .002 inches apart in diameter and most connectors/tools that support one support the other. I'm looking for a crimper and stripper for some LMR-240 I plan on buying and have found a lot that say they will do RG-8X, but fewer that mention LMR-240 specifically.

Will RG-8X tools work on LMR-240?

For example, I am considering this crimper (as well as this other one) and this stripper.

## Accepted answer (score 3, by Phil Frost - W8II)

RG-8X is very close to LMR-240, and the two are usually compatible. But the crimpers you list are for RG-*8*, not RG-*8X*. The two are not the same, not even close. RG-8 is roughly twice the diameter of RG-8X.

To determine the crimper you need, you'll want to find the datasheet for the connectors you will be using. For example, look at Amphenol Connex 172135. This is described as an "N crimp plug for LMR-240 / RG-8/X cable". It specifies crimp sizes of 0.255" and 0.100".

Strippers are usually adjustable, so a 0.002" difference will not be a problem. But again, you want tools for RG-*8X*, not RG-*8*.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4964/can-i-use-an-rg-8x-crimper-stripper-on-lmr-240, by Seth, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
