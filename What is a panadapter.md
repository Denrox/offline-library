# What is a panadapter?

*Tags: software-defined-radio, jargon, history, panadapter-and-waterfall · score 8*

## Question

To what does the term "panadapter" refer? (Physical hardware or software?) How did the term "panadapter" originate as related to radios or electronics?

How is the term "panadapter" different from the spectrum and/or spectrum waterfall display on an expensive receiver/transceiver or an SDR software application? Or is the term a superset of subset of those?

## Answer (score 5, by Phil Frost - W8II)

A panadapter is a device that adapts the narrow (typically 4kHz) bandwidth of a traditional receiver into a much wider bandwidth, perhaps the entire band. The *pan-* prefix means *all*, as in *panoramic*, *pandemic*, or *Pangaea*.

A waterfall display isn't a panadapter, though a panadapter may have a waterfall display built in. A spectrum analyzer can also make a waterfall, but the waterfall isn't the spectrum analyzer.

Since most SDRs have relatively wide bandwidths, they can be used as panadapters. Many panadapters today are based on the RTL SDR design, tuned to the receiver's IF and inserted just prior to the filter.

An SDR used as a standalone receiver would not be a panadapter: there's nothing to *adapt*.

## Answer (score 2, by user10489)

Is a panadapter hardware or software?

If you use a hardware spectrum analyzer and a scope, it's hardware.

If the panadapter is based on an SDR, then it requires both the SDR hardware and software.

The difference between a waterfall and a panadapter is that the waterfall shows the spectrum analysis of a range of frequencies over time, which may include just the 3-4KHz audio pass band of the receiver, where the panadapter usually shows at least 12KHz, and more likely at least 1-5MHz (all of one or more bands). Also, the panadapter might only show the instantaneous spectrum analysis, or it could show a wide band waterfall.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7183/what-is-a-panadapter, by hotpaw2, Phil Frost - W8II, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
