# Where to find HF channel models or statistics?

*Tags: hf, doppler · score 6*

## Question

When designing a waveform for packet radio usage, it'd be helpful to know a few things, mainly

- distribution of coherency bandwidths
- distribution of coherency times

Whilst such statistics are reasonably possible to generate for higher frequencies based on own measurements, for terrestrial HF propagation, due to the large distances involved and the low useable bandwidths, a sufficient measurement campaign would be infeasible.

HF propagation models are very light on details or vary wildly when it comes to the relevant aspects that would allow for simulation of the same (that being delay spread and doppler spread). Mostly, they're early cold war studies that care only about amplitude attenuation.

1. Are there more modern channel models for HF propagation?
2. Alternatively, statistics over the coherency properties?

## Accepted answer (score 1, by Phil Frost - W8II)

ITU-R F.1487-0 (*Testing of HF modems with bandwidths of up to about 12 kHz using ionospheric channel simulators*) seems like what you're looking for. It discusses briefly how an HF channel can be modeled, and provides 9 sets of parameters, every combination of (low, mid, high) latitudes and (quiet, moderate, disturbed) conditions, as well as statistics on how frequently those conditions can be expected.

For completeness, other resources which are useful for a complete model:

- VOACAP, for path loss and channel reliability estimation
- ITU-R P.372-14 for data on ambient radio noise

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15970/where-to-find-hf-channel-models-or-statistics, by Marcus Müller, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
