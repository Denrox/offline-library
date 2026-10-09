# What is radio pollution?

*Tags: jargon · score 3*

## Question

In a slide on calculating link budget, detrimental effects to a link included “Radio pollution (selectivity, blocking, IP3)”.

- What is radio pollution?
- Specifically, what are selectivity, blocking, and IP3 in connection with radio pollution?
- Do all major forms of radio pollution fall into one of those three, or are there other forms of radio pollution one should be aware of?

## Answer (score 5, by Kevin Reid AG6YO)

“Selectivity, blocking, and IP3” are three properties of a receiver's ability to receive the desired signal in the presence of other signals at *different* frequencies. Thus it would seem this document is referring to all such signals as “pollution”, presumably on the grounds that they are manmade signals as opposed to “natural” noise.

(I am not aware of a matching accepted definition of “radio pollution”; insofar as the term is defined it seems to refer to signals occurring outside of appropriate spectrum allocations, which is largely not relevant to this.)


*Selectivity* refers to the receiver's ability to “select” the desired signal by filtering out others not at the intended frequency; insufficient selectivity means receiving the adjacent signals as well as the desired signal.


*Blocking* is a phenomenon where strong nearby signals cause an apparent reduction in the strength of the desired signal. The (lack of) susceptibility of a receiver to this effect is quantified as *blocking dynamic range*.


*$IP_3$*, or *third-order intercept point*, is a measure of the strength of *third-order intermodulation products*. Intermodulation products appear as unwanted signals at frequencies with a specific relationship to actual signals; third-order products are particularly of interest because their frequency is close to the original signals; for input signals at frequencies $f_1$ and $f_2$, third-order products occur at $2f_1 - f_2$ and $2f_2 - f_1$.

So, what they said very elliptically was that you should consider, in your link budget calculation, the effects of the other signals in the environment on the imperfections of your receiver.

Do all major forms of radio pollution fall into one of those three, or are there other forms of radio pollution one should be aware of?

Going by this apparently idiosyncratic definition, the other case you would be concerned with is where the unwanted signal is *at* your chosen frequency, in which case none of the above receiver properties are relevant since as far as it's concerned it is the wanted signal.

This is a completely different problem, which is mostly independent of a link budget (unless you, say, use your budget calculation to determine that your signals will be much stronger than the unwanted signal, e.g. by using high-gain (directional) antennas between your link endpoints).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1613/what-is-radio-pollution, by Adam Davis, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
