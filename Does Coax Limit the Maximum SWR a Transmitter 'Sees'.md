# Does Coax Limit the Maximum SWR a Transmitter 'Sees'?

*Tags: coaxial-cable, antenna-system, transmission-line, impedance-matching · score 10*

## Question

A recent discussion about SWR led to the assertion that a length of coax cable will ultimately limit the SWR to which the transmitter will be exposed.

By experimenting with an SWR calculation tool like *TLDetails*, there appears to be a basis for this assertion. For example, with a 100 foot length of RG-8X coax on 15 meters, the SWR at the transmitter end never goes above 5.8:1. Even an open or shorted cable at the far end does not raise the SWR above this limit. Experimenting with different lengths and types of coax changes the limit but there always seems to be a limit of some kind.

What is causing this and what it the math behind it? Can this be used to 'fix' a high SWR at the antenna?

## Accepted answer (score 7, by Glenn W9IQ)

The source of the SWR limit on the transmitter end is the losses in the feedline. In general, the higher the matched line loss, the lower the maximum SWR that will be present at the transmitter end. Since the SWR limit is the result of losses in the feedline, the efficacy of the 'high SWR fix' must be considered.

The mechanism has to do with the trips that the transmitter power must make along the length of the feedline. A simple example will help to describe the effect:

First consider a feedline that has a 3 dB matched loss connected to a 100 watt transmitter. We can convert dB loss to a percent loss:

$$\text{Percent Loss} = \frac {1} {10^{(L_{dB}/10)}}*100 \tag 1$$

where LdB is the loss in dB form.

This means that when the 3 dB matched line is terminated in its characteristic impedance, only 50% of the transmitted power (50 watts) will arrive at the antenna end of the line and be aborbed/radiated by the load. The other 50% has gone up as heat in the coax.

Now instead of a matched load, let's consider a most extreme case of leaving the far end of the coax cable open. In this condition, 100% of the power arriving at the open end is reflected back towards the transmitter. As before, only 50% of the transmitted power (50 watts) arrives at this open connection. This is now fully reflected back toward the transmitter. But just as the forward power was attenuated, so is the reflected power by the same percent. So only 25 watts arrives back at the transmitter.

We can now calculate the SWR at the transmitter:

$$\text{SWR}=\frac{1+\sqrt {P_r/P_f}}{1-\sqrt {P_r/P_f}} \tag 2$$

where Pr is the reflected power, Pf is the forward power.

The SWR at the transmitter is 3:1 in this example. Quite an amazing transformation of an infinite SWR at the far end of the feedline but it comes about as power dissipated in the coax.

Now let's generalize the example by creating an equation that allows us to calculate the maximum SWR at the transmitter end based on the matched line loss. Note that in the open end example, the power arriving back at the transmitter was attenuated twice. We can represent this as the square of the loss (i.e. loss times loss). Then if we use equation 2 but normalize the transmit power at 1 watt, the lower Pf factor goes away. This leaves us with the following:

$$\text{SWR}_\text{max}=\frac {1+\sqrt{\text{Percent Loss}^2}} {1-\sqrt{\text{Percent Loss}^2}}=\frac {1+\text{Percent Loss}}{1-\text{Percent Loss}} \tag 3$$

If we now make a plot of formula 3, we get the following view of matched loss vs. maximum SWR:

Formula 3 can be converted to a version that directly uses dB matched loss:

$$\text{SWR}_\text{max}=\frac {1}{\tanh \left({\frac{L_{dB}}{8.686}}\right)} \tag 4$$

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9722/does-coax-limit-the-maximum-swr-a-transmitter-sees, by Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
