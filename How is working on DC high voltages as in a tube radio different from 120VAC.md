# How is working on DC high voltages as in a tube radio different from 120VAC?

*Tags: electronics, transmitter, safety, voltage, vacuum-tubes · score 3*

## Question

Suppose that I am familiar with the safety procedures for working on 20 A 120 VAC 60 Hz household lines.

What should I be prepared for before working on high voltage DC circuits (say, 800 volts) as is commonly found on the anodes in tube transmitters?

## Answer (score 3, by Mike Waters)

**800 volts is far more likely to burn you**. Just doubling the voltage from 120 to 240 will *quadruple* the power heating your flesh.

This is just basic Ohm's Law: [P=E*I]

DC is one nasty customer:

It is easy to get complacent after spending a youth and a career working with docile, harmless 5-24 volts DC, or well-behaved 100 - 240 V AC voltages because of its frequent zero crossings.

DC in that same range is a mean drunk. You may have been in very old houses and felt switches that had a definitive SNAP when switched on or off. Those are throwbacks to when house power was DC, and they snap the contacts quite wide, to assure an arc is snuffed. Above that, you need magnetic or pneumatic "blowouts" designed to pull the arc up into an arc chute to blow it out. ,

... Look at the DC ratings for contactors and relays. You will see very different voltage ratings for DC than AC.

As a result, the various regulations treat higher voltage DC differently from low voltage, and allowable maximums are typically in the 30-50 volt range

And if RF is present, the burn will be even worse.

A friend of mine was severely burned by 240V when his hand was momentarily inside a breaker panel, and *it took several months to heal and for the redness to go away*.

Also, I watched an old electrician show off by testing for the presence of 120 volts at the ends of two wires using his old and dry thumb and forefinger. He would have been burned if he was touching 800 volts, either AC or DC.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14976/how-is-working-on-dc-high-voltages-as-in-a-tube-radio-different-from-120vac, by Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
