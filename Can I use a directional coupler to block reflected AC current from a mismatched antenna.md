# Can I use a directional coupler to block reflected AC current from a mismatched antenna?

*Tags: antenna-theory, impedance-matching, directional-coupler · score 3*

## Question

Is there any kind of directional coupler device such as you find in a SWR meter that only allows traveling AC waves of one direction to pass which i could use to block the reflected wave from my badly matched antenna and therefore save the output devices in my transmitter from failing ? I would then short the coupler out when receiving ...

## Accepted answer (score 7, by Phil Frost - W8II)

There is a device that does this, but it's not a directional coupler. Rather, it's a circulator.

A directional coupler isn't suitable since the forward and reflected ports merely "sample" the power in each direction. Most of the power just passes through the coupler, so at best you'd only reduce the reflected power reaching your transmitter by some insignificant amount.

For example, a typical directional coupler might have a *coupling factor* of -20 dB, meaning if there are 100 watts reverse then -20 dB of that (1 watt) makes it to the reverse coupled port. The remaining 99 watts just pass through the coupler (or are lost to heat).

This is good for driving an SWR meter with negligible impact to the signal but not so much if your objective is to absorb the reflected power in a dummy load.

Attempting to solve this by increasing the coupling factor means increasing the forward power lost. A directional coupler is inherently a 4-port device, and the coupling factor is the same in forward and reverse directions. So if the coupling factor is increased to 0 dB the coupler would indeed be able to absorb all reflected power, however it would also absorb all forward power. Not a very useful device.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15754/can-i-use-a-directional-coupler-to-block-reflected-ac-current-from-a-mismatche, by Andrew, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
