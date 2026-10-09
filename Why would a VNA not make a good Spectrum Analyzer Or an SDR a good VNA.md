# Why would a VNA not make a good Spectrum Analyzer? Or an SDR a good VNA?

*Tags: software-defined-radio, equipment-design, spectrum-analyzer, nanovna · score 7*

## Question

Happy to be corrected where I'm wrong in any of this but in broad strokes my understanding is:

### Spectrum Analyzer

- measures input signal strength while sweeping across frequencies, measuring RF emissions
- often includes "tracking generator" to output a sweeping sine wave too, so as to measure a filter's frequency response
- can easily be used with an SWR bridge, so as to measure reflected power
- is "scalar" in that it does not measure phase differences and/or complex impedances

### Vector Network Analyzer

- essentially always a 2-port device, with a built-in reflectance bridge
- also sweeps across frequencies generating / detecting signals
- is "vector" because it pays attention to the phase of signals and thus can measure complex impedances

So it seems like a VNA is a really full-featured (or "superset of" a) spectrum analyzer: all the "sold separately" tracking and reflectance stuff built in, plus the phase detection instead of just magnitude.

Yet I see that instead of, for instance, having a spectrum analyzer features in the NanoVNA firmware there is a separate tinySA spectrum analyzer device — why? Is there something about a VNA's architecture that makes it less optimal for spectrum analysis than a dedicated design?

For that matter, what about:

### Software Defined Radio

- a flexible VCO, mixer, and ADC/DAC components — some support full-duplex operation
- can sweep across a wide range of frequencies, sampling a significant bandwidth (around a particular frequency) of what is still just a slice of spectrum (relative to overall VCO range)
- software can control the sweep and do any analysis it wants on the data

Are there parameters/constraints that make a dedicated spectrum analyzer better than a full-duplex SDR? (Not in the sense of "a PlutoSDR doesn't have its own screen or nice knobs and buttons like an Agilent does" but in the architecture of the underlying RF circuitry itself.)

Or if one were to set up a pair of full duplex SDRs with reflectance bridges, would that make a perfectly good VNA or would it also lack something compared to a specifically tailored design?

## Accepted answer (score 8, by erik)

A VNA generally does not have to worry about a multitude of input signals as it controls its own test signal generation. A SA has to be able to show small signals even in the presence of large other signals but it does not have to worry about the phase of the signal.

Another difference between a VNA and an SA that is often overlooked is the way they do scan a certain frequency range. A VNA often only measures at the frequencies on the grid defined by the span and the number of display points and can do this measurement with a narrow resolution bandwidth. An SA has to ensure EVERY frequency within the set span is covered by stepping its resolution filter through the complete stepped sweep span and the number of steps will depend on the width of the resolution filter, or, with a continuous sweep, the sweep speed is determined by the speed of the log power detector.

You can use a VNA as an SA but it may be a very limited SA as there could be problems with mirrors and slow scanning speed. Scanning speed over large bandwidth can be optimised in an SA using a log power detector and a wide resolution filter.

Realizing high dynamic range in the presence of possibly blocking signals often requires a preselector such as an up-conversion and band-pass filter or YIG filter as the dynamic range of the ADC is often insufficient to cover the full dynamic range.

An SDR without a preselector will often show false signals on (sub)harmonics of an actual input signal.

From a HW perspective a dedicated VNA or SA can be build more cost effective than a combined SA/VNA, but the cost of such a combined device will be lower than the cost of separate SA & VNA.

Examples of combined VNA/SA devices are the LibraVNA (optimized for its VNA function) and the SVA series of Siglent (optimized for the SA function). The tinySA and NanoVNA are so cheap because they leave out everything not needed for their pure SA or VNA function.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20699/why-would-a-vna-not-make-a-good-spectrum-analyzer-or-an-sdr-a-good-vna, by natevw - AF7TB, erik. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
