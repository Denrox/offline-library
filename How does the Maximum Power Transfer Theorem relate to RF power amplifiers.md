# How does the Maximum Power Transfer Theorem relate to RF power amplifiers?

*Tags: rf-power, antenna-system, electronics, impedance-matching, amplifier · score 4*

## Question

The Maximum Power Transfer Theorem says that maximum power transfer occurs when the source impedance equals the load impedance, when the power transferred to the load is 50%, the other 50% being converted to heat inside the source.

The output impedance of a transistor in an RF power amp is very low before it's converted to 50 ohms by the various matching networks in a transmitter, so how does that work?

## Answer (score 6, by Kevin Reid AG6YO)

The maximum power transfer theorem tells you **how to design a load to extract the maximum possible power from a given source.** It does *not* tell you that the source will survive this treatment, and it does not tell you **how to best design a source given a load.** If you apply the maximum power transfer theorem to a typical solid-state RF transmitter, it will overheat (or reduce output to protect itself).

In a radio transmitter or amplifier, we design the output to operate *efficiently*, sending RF to the antenna and not heating itself up unnecessarily. A low impedance works fine for this purpose.

The maximum *practical* power is achieved at the point where the transmitter has reached its heat-dissipation limit (would overheat) or its circuits can no longer deliver more current to the output (would distort).

You may wonder: but don't we always make sure the antenna system is 50 Ω (or whatever impedance) everywhere? Aren't impedance mismatches really bad?

This is true — everywhere but at the transmitter/amplifier output! What we want to avoid is *reflections that cause phase shifts*. At the transmitter, there is not yet any length for the reflection to travel over, so there cannot be any phase shift. The output device is interacting instantaneously with (the matching network connected to) the 50 Ω line, and so the output can be designed as a lumped circuit driving a 50 Ω resistive load without transmission-line effects.

Another point is that this reasoning does not apply to receivers. In receivers, the incoming signal has already been traveling when it gets to the antenna and there is no active device driving it. An impedance mismatch at any point in the entire free space→antenna→feed line→receiver system will reflect some of the signal back out, making the received signal that much weaker.

Or, to say the same thing differently: **the maximum power transfer theorem *does* apply to receivers**, because your source (radio waves in free space) is unchangeable and so you match its impedance to extract as much signal power as possible.

(Unless, I suppose, you're operating in an environment of *too much* RF power, like some kind of RF-heating system or physics experiment. Then a deliberate mismatch could allow you to sample a calibrated fraction of the signal without overloading the receiver and without dissipating the RF in an attenuator.)

Of course, the receiver does not specifically need *power* in the sense of energy transferred over time (unless it is an RF-energy-harvesting device) — it needs a detectable signal. But that signal must be stronger than the noise inherent to the receiver circuit; and whether the receiver input is sensitive to voltage, current, or power, it will always see a better signal-to-noise ratio if less of the incoming signal is reflected.

## Answer (score 4, by Phil Frost - W8II)

The objective of specifying a 50 ohm load isn't to generate maximum power per se. The transmitter is subject to damage from excessive current or voltage. The currents and voltages will depend on the attached load.

If the load is specified as 50 ohms then it's possible to calculate what will happen in the transmitter and design it such that the specified device can operate to its maximum potential while staying within it's ratings (thermal, voltage, and current). If the load isn't 50 ohms then the transmitter may have protection circuitry to reduce power, or it may simply self-destruct.

If the load could be anything, the design will have to be more conservative to accommodate the worst case without damage. This means either a more expensive and robust transistors, or reduced performance.

## Answer (score 2, by MagnusO_O)

It's true that at maximum power transfer 50% of the power are lost to heat inside the source.

However often maximum power **efficiency** is intended instead of maximum power transfer to prevent overheating of the source.

And maximum power efficiency is achieved by a low source resistance.  
Some links concerning max power transfer / effiency:

Wikipedia - Maximizing power transfer versus power efficiency

allaboutcircuits - Maximum Power Doesn’t Mean Maximum Efficiency

electronics.stackexchange - answer from mkeith

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15158/how-does-the-maximum-power-transfer-theorem-relate-to-rf-power-amplifiers, by Andrew, Kevin Reid AG6YO, Phil Frost - W8II, MagnusO_O. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
