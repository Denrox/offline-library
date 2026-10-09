# Ferrite rod or core permeability determination

*Tags: measurement, ferrite · score 7*

## Question

Is there a simple empiric way of determining the permeability (mhu) of a ferrite object (be it a ring, rod or any form)?

I've been thinking this for a rod: if I wind coils with different number of turns (same wire, just wind or unwind it) and measure the inductance, then given the number of turns, diameter of the rod and "height" of the coil I would be able to determine the permeability. I tried a couple of times but I'm getting inconsistent results. My LCR meter can measure only upwards of 0,01mH (or 10uH). Is the meter the culprit or is my method flawed?

## Accepted answer (score 5, by dfannin)

you're on the right track to measure/calculate effective permeability.

However, you need to use an inductance meter that can measure up to 1 nH accurately or so. If you're trying to use one of those $25 LCR meters , it won't have the accuracy or precision you require, plus you won't be able to zero it. Another issue is that you'll have a wide variance in results due to the wire, winding, lengths, etc - see Silvio's comments at http://www.sklaic.info/forum/index.php?topic=175.0 .

The other method is to measure frequency resonance, by using the loop as the inductor in an LC circuit. Put a known capacitor in series with the loop, and then use a frequency generator and frequency counter to measure the resonance (peak) frequency of the LC circuit.

## Answer (score 6, by Marcus Müller)

Following up on @dfannin's excellent answer:

The most intuitive way of dealing with this would be:

1. wrap your ferrite rod in halfway stable paper or so, something that certainly doesn't have high $\mu_r$ (gut feeling: baking paper is nice as it is very "slippery" on flat surfaces)
2. make as many turns as you want around that; you're building a coil now, with the ferrite core.
3. Measure ferrite core coil's inductance by one way or another
4. carefully slip the core out of the paper. Now you have exactly the same coil, but with an air core
5. repeat measurement
6. since air has $\mu_r\approx1$, the ratio between the ferrite core inductivity value and the air core inductivity value is the $\mu_r$ of the core.

Downsides:

- Since ferrite's $\mu_r$ is going to be *impressively high*, you'll need a measurement method that can span easily 3 orders of magnitude
- high-inductivity coil (which would allow measurements with your >1 mH LCR meter) might mean that even at relatively benign currents, you might be saturating the core and get it to nonlinearity (that's not all that likely, but don't rule it out before knowing how much power your meter uses)
- might waste a lot of copper :)

Things that can generally go wrong:

- core saturates
- core too small for coil, not (nearly enough) all field gets concentrated into core, so that measurement isn't proportional to core's $\mu$
- ohmic losses make measurement hard

## Answer (score 3, by Mike Waters)

Because ferrites aren’t marked, it is difficult to know what frequencies they work on. However, now we can use the popular NanoVNA along with free software (and Excel) to graph the unknown ferrite’s impedance over frequency.

**YouTube video by Fair-Rite Corporation**, using a Nano VNA and software: https://youtu.be/KmKQibSDzqM

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/8984/ferrite-rod-or-core-permeability-determination, by Luca, dfannin, Marcus Müller, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
