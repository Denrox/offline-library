# Excessive frequency deviation for DMR handsets?

*Tags: software-defined-radio, dmr · score 3*

## Question

A Hytera DMR handset that I am working with has a frequency deviation of 2300-2700 Hz. This is higher than the expected 1944.0 Hz frequency deviation specified in the DMR specification (ETSI TS 102 361-1). Is it expected that low cost handsets have excessive frequency deviation? I'm wondering how the receiver performs synchronization when the frequency deviation can be so far out of range?

More info:

- I/Q samples are collected with an SDR
- This question is *not* about carrier frequency offset but rather the FSK frequency deviation
- To determine the deviation, I used an FM demodulator then measured the distance between minimum and maximum deviation.

**Update 1:**

- the frequency deviation is closer to 2100-2400 Hz after further measurement.

## Accepted answer (score 1, by BigBrownBear00)

Verification through simulation of a DMR burst shows that the excessive frequency deviation is caused by the overshoot from the pulse shape filter ($\alpha$=0.20). The DMR modulator uses a RRC at the transmitter and receiver which can cause the deviation to go beyond 1944 Hz.

Here are the ideal simulated frequency deviations after the RRC filter:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22139/excessive-frequency-deviation-for-dmr-handsets, by BigBrownBear00. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
