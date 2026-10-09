# Can this 960 MHz CelWave fiberglass antenna be retuned for the 70cm band?

*Tags: antenna · score 5*

## Question

I recently inherited a CelWave fiberglass antenna pictured below.

It is marked that it's for 959.9875 MHz.

The model number appears to be either 339 or 359. It is 96 1/2 inches from base to tip.

I checked it on my MFJ Antenna Analyzer and found it start to get a decent SWR over 460 MHz. I expected as much since half of 960 is 480.

Is there any way this antenna can be disassembled and retuned for use in the 70cm ham band?

I don't mind even if there is risk involved. It didn't cost me anything and I have no use for it as it is.

## Accepted answer (score 5, by Phil Frost - W8II)

The wavelength at 959.9875 MHz is approximately one foot. So this antenna is approximately eight wavelengths long. That means it is not a simple monopole or dipole. Based on the dimensions I would guess it is a co-linear array of dipoles with the objective of increasing gain towards the horizon by suppressing radiation at less useful high angles, while maintaining an omnidirectional pattern.

That the antenna has a decent SWR does not necessarily mean it's any good on 480 MHz. For a co-linear array to work as intended, each element must be in phase so they interfere constructively at the horizon. The phase of each element is controlled by transmission lines or reactive elements within the antenna, all of which have frequency-dependent behavior. It is unlikely the phasing components continue to perform their function at any frequency but the one for which it was designed.

Consequently, the antenna elements will most likely be out of phase, resulting in a radiation pattern which is worse than something much simpler.

A simple A/B test using a simple 1/4 wave monopole (or whatever else you have lying around, or can quickly improvise) as a reference should be sufficient to make a determination. If the mystery antenna isn't significantly better than the reference antenna, you can reasonably infer the phasing is all messed up and this antenna isn't going to be useful, even if it is a good match.

You certainly could disassemble it and modify it to work better, however that will be a more advanced effort. Even that may not work so well: halving the frequency requires doubling the size for an equivalent design. Generally it's easier to make things shorter, while making them longer is...harder.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12000/can-this-960-mhz-celwave-fiberglass-antenna-be-retuned-for-the-70cm-band, by Lance, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
