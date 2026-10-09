# Do External Signals Affect Antenna S11/SWR Measurement?

*Tags: antenna, measurement, swr-meter · score 5*

## Question

Do external signals affect the S11/SWR measurement of an antenna?

For example, if I try measuring the S11/SWR of an HF antenna with a SWR meter or a Vector Network Analyzer in the middle of a field day with many transmitters near the antenna, or try measuring a 2.4 GHz dipole at a lab with many wireless access points, is it possible that the instrument sees a higher reflected power, thus giving me invalid S11/SWR results?

If it's a possibility, what can I do to reduce the measurement error? Shielding is often impractical for a large HF antenna. Is a SWR meter less vulnerable to this problem than a VNA due to its higher output power?

## Accepted answer (score 4, by tomnexus)

Yes, in my experience antenna measurements on a VNA are affected by external transmissions. They look like "noise" on the graph.

Usually you can exclude them by eye - they're narrow and sharp while the antenna response is smooth.

To make them smaller it helps to:

- increase the output power of the VNA
- reduce the measurement bandwidth
- turn on averaging. VNAs average coherently - i.e. the real and imaginary parts of the response are averaged separately. Because the interfering signal is almost certainly not coherent with the VNA, it averages to zero over some time.

A scalar measurement like an SWR meter will be worse affected, and there's no way to average it down, the effect will always be to increase the SWR. Worse, an SWR meter may have no preselector, so it might consider *all* power coming in to be a reflection of its transmitted signal. In this case, for example, a single strong transmitter at 143.500 MHz could spoil the measurement of the whole 2 m band. A band-specific filter would help a lot in this case.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16029/do-external-signals-affect-antenna-s11-swr-measurement, by 比尔盖子, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
