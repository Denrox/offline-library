# How to estimate ladder line loss?

*Tags: feed-line · score 5*

## Question

There have been a number of questions regarding the issue of feed line loss and ladder line eventually gets discussed. So I am curious, how does one begin to estimate the loss in ladder line?

So, for the case of 2 bare wires "somehow" spaced an appropriate distance apart acting as a feedline with SWR=1.000, what loss could be expected? (Loss due to SWR was very well covered here: [What is the actual loss in a feed line with high SWR?](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md) )

I would think that spacing the wires farther apart would increase the impedance, lowering the current and thus the loss/100m (at a cost, perhaps, of more complicated and lossy impedance transformers at each end which I am ignoring). I would think that adding an insulator would (1) lower the velocity factor --somewhat increasing the loss by somewhat increasing the number of wavelengths at a given frequency-- and (2) add some sort of additional loss mechanism in addition to that which could be attributed directly to the velocity factor.

Is there a way to quantify any of this?

## Accepted answer (score 5, by Phil Frost - W8II)

For most feedlines, dielectric loss is very low, and at HF where ladder line is practical, negligible. So significant losses are due to resistance and associated Joule heating of the copper conductors.

The characteristic impedance $Z_0$ gives the ratio of voltage to current in a matched line, so we can always find voltage if the current is known:

$$ E = Z_0 I \tag 1 $$

and the power $P$ transmitted by the line is the product of current and voltage between the conductors:

$$ P_\text{tx} = IE $$

substituting equation 1 for $E$, we get

$$ P_\text{tx} = I^2 Z_0 $$

and solving for $I$ we can determine the current in a matched line as a function of power and characteristic impedance:

$$ I = \sqrt{P_\text{tx} \over Z_0} \tag 2$$

Now, Joule heating which is most of the loss is the product of resistance $R$ and current squared:

$$ P_J = I^2 R $$

substituting equation 2 for $I$ yields

$$ P_J = {P_\text{tx} \over Z_0} R \tag 3 $$

therefore as a first order approximation, we can say losses are inversely proportional to characteristic impedance:

$$ P_J \propto {1 \over Z_0} $$

In other words, doubling the impedance halves the power lost.

Keep in mind "loss" in transmission lines is actually the ratio of power in to power out: it's power *not* lost. So don't make the mistake of thinking a feedline with 1dB of loss, if the impedance is doubled, becomes 3dB better with a result of 2dB of gain!

Rather, a loss of 1dB means $ 1 - 10^{-1/10} = 20.6\% $ of the power is lost. Doubling the impedance would change that loss to $ -10 \log_{10} (1- .103) = 0.47\:\mathrm{dB} $.

Equation 3 provides a start for calculating the loss, but the devil is in the details, especially in calculating $R$. Both the skin effect and proximity effect must be taken into account, and the math is not nearly so simple.

For practical purposes I suspect the approximation is good enough to appreciate the potential benefits of a feedline change. If more precise loss numbers are required then perhaps an empirical method is easiest.

## Answer (score 4, by Cecil - W5DXP)

There is a program called TLDetails, available from https://ac6la.com/tldetails1.html, that will calculate the loss for many standard transmission lines. One enters the frequency, the type and length of transmission line, and the load impedance and TLDetails will calculate the line loss, SWR, and impedance seen at the source plus other parameters. More information on k0, k1, and k2 is covered under https://ac6la.com/zplots1.html.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14441/how-to-estimate-ladder-line-loss, by Chris K8NVH, Phil Frost - W8II, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
