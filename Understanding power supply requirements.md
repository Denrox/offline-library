# Understanding power supply requirements

*Tags: dc-power · score 10*

## Question

I have a basic question about power supply requirements for typical transceivers. I'm looking at the specs for a Kenwood TM-V71A, which is a 50W mobile transceiver.

I figured that a 50W transceiver running on a 12V(-ish) power supply would pull around 4A max, but the specs for this radio show a "maximum current drain" of around 13A. How does that work?

## Accepted answer (score 11, by Phil Frost - W8II)

A 50W transmitter is one that can create 50 watts of RF output. The RF amplifier is never 100% efficient, so the input power requirements will always be higher than the output power.

Furthermore, the maximum current drain accounts for startup transients and other peaks in excess of the average current drain.

## Answer (score 3, by hotpaw2)

Note that even when not transmitting, a transceiver will draw power for the receiver, audio amplifier, control panel processor and display, etc. That idle power adds on top of the power sent thru the antenna output connector divided by the amplifier efficiency (the rest of that power/energy heating up the shack).

## Answer (score 3, by Scott Earle)

The circuitry in a standard radio transceiver will probably draw around an amp while it is powered on - this includes the CPU, display and other such things that are always running. Handheld radios obviously try to keep this current as a minimum, because they run on batteries.

While receiving, there is also the power used by the receiving circuitry, and the audio amplifier, while there is audio being sent to the speakers. This can use an additional amp or so.

However, the real current draw is when transmitting, where most of the current is used by the PA (power amplifier) final stages. These usually operate in class A, AB or B, which are not very efficient - but offer good linearity, and thus low distortion. See the Wikipedia entry on Power Amplifier Classes. These amplifiers require large heatsinks to dissipate the 'waste' energy as heat.

Note that mobile and handheld radios that only transmit FM can use class C amplifiers, which are non-linear, since they always transmit at a constant power. These are much more efficient than class A, AB or B amplifiers, and mean that mobile or handheld FM-only radios use less power when transmitting, and require smaller heatsinks.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11922/understanding-power-supply-requirements, by larsks, Phil Frost - W8II, hotpaw2, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
