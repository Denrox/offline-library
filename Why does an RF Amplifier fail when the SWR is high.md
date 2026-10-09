# Why does an RF Amplifier fail when the SWR is high?

*Tags: antenna-theory, electronics, amplifier, transmission-line · score 4*

## Question

Exactly why does an RF output transistor fail if the SWR is bad ?

Is it A because the impedance mismatch between the transmission line and the antenna results in maximum power not being transferred to the antenna but rather being converted to heat inside the transistor ?

Or is it B because the reflected AC current caused by the impedance mismatch from the antenna goes back into the transistor output somehow ?

If the answer is B, then what stops the output signal produced by the RF output transistor from going back into the transistor in the same way as the reflected signal caused by a bad SWR ?

## Accepted answer (score 4, by Phil Frost - W8II)

A high SWR implies the load impedance is significantly different from 50 ohms, violating the design specifications of the amplifier.

Yes, there is power reflected in a feedline. But it's not this power per se that causes problems, it's simply that the impedance seen by the transmitter isn't the 50 ohms it was designed for. In other words, the transmitter can't tell the difference between reflected power and simply the wrong impedance connected directly at the antenna connector with no feedline.

With the design assumptions violated, all the design specifications (like not catching fire) are off the table. Excessive current may lead to overheating. Or there may be too much voltage across them leading to avalanche breakdown. These are just examples: other failure modes are possible depending on the design of the amplifier.

## Answer (score 2, by hotpaw2)

I like to turn the question around.

Why does a transmitter amplifier not burn up or fail? There's power coming into the transmitter from the power supply. Why doesn't it melt the transmitter?

Well, some of that energy (power over some period of time) goes into warming up heat sinks and eventually the air around your locale. But a transmitter isn't (designed as) a toaster or room heater. It's designed as part of a system to radiate RF energy. So a transmitter is designed for (a large fraction of) the energy to exit your locale as electromagnetic radiation.

But a high SWR means a large portion of the power being sent up the feedline isn't being electromagnetically radiated. Thus, energy has to be dissipated somewhere. So, if the transmitter doesn't fold back the power level to below what the feedline and the heatsinks can radiate away, something will melt or otherwise stop functioning due to overheating.

Added: Alternatively the power reflected back by a high SWR can be reflected back up the transmission line by yet another impedance mismatch at the transmitter. But that reflection will either increase the voltage or current at the reflection point, depending on the impedance mismatch. So again, you either dissipate, arc, or melt something.

Also, a non-resonant antenna system is a reactive load. One thing about reactive systems is that they store energy. If you pump more power into a reactive system than it dissipates, the system will store energy in the form of increasing voltages and/or currents across or within components. If you keep on increasing voltages or currents without bound, eventually something will melt or arc over. An antenna system with a nice low SWR and moderate resistance will radiate most of that energy away (as RF or heat), rather than turning the transmitter into a blown fuse.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15157/why-does-an-rf-amplifier-fail-when-the-swr-is-high, by Andrew, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
