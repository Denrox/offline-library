# Testing old coax cable

*Tags: coaxial-cable, testing · score 3*

## Question

I have a situation similar to this: [Testing for 'Bad' Coax](Testing%20for%20%27Bad%27%20Coax.md) . In addition to checking for DC continuity or shorts, here was my test method:

My 50Ω dummy load (Elecraft DL1) has a diode and capacitor test point so that you can use a volt meter to measure power at the dummy load.

I connected the dummy load to the rig (transmitting a carrier at 144 MHz) and measured the voltage (using a Fluke 75III DVM), then connected the cable under test between the rig and the dummy load and measured the voltage again. With just the dummy load, I measured 6.2V at the test point (which calculates to the expected 1.6W).

The first cable was short (<5m) and it measured 5.4V (i.e., a significant loss); other cables (all of them RG-8 type, and all <20m long) measured under 1V.

- Was that a valid test?
- Am I correct that these cables were junk?

## Accepted answer (score 2, by Marcus Müller)

Belden, which typically produce the upper middle-class non-measurement-grade cables, would spec something like 5 dB/100m, or 1 dB for 20m at 150 MHz, for their RG-8/U. Whatever you're seeing significantly exceeds that.

Note that the diode used in your dummy load will not work well for low voltages (as you can see in the figure on the second page of the instructions to your dummy load); as an engineer, I'll allow myself that this is not a great way to measure powers over a large range. However, for your kind of tests it suffices; you don't care how much lower exactly the power is, just that it's more than, say, 2 dB.

So, if you're confident in your connectors, I'd say damaged cabling is the best explanation. Hard to tell with your setup whether it's *leaky*, i.e., has some kink/cut somewhere that makes it emit more than it carries, or whether it's lossy (i.e., converts RF power to ohmic heat in oxidized conductor or dielectric heat in the insulation), but a) doesn't really matter much b) would notice if turning on a receiver tuned to the same frequency in the vicinity.

So:

- Yes, I'd call this a valid test, and
- I'd agree with that assessment.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21185/testing-old-coax-cable, by Duston, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
