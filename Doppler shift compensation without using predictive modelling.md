# Doppler shift compensation without using predictive modelling

*Tags: software-defined-radio, satellites, doppler · score 5*

## Question

Doppler shift mitigation has been studied extensively in the literature. In my implementations of satellite receivers (using GNU Radio), I use predicted Doppler shift from a software (GPredict) to compensate for Doppler shift. After that, I use a Frequency-Locked Loop (FLL) for course carrier synchronization. This approach works very well. However, I have been trying to implement new carrier frequency synchronizers that will enable operations without the help of an external software. When I looked at the literature again (Umberto Mengali book, chapter 3), carrier frequency recovery is divided into two cases:

1. When the frequency offset is much lower than the symbol rate (< 10%?)
2. When the frequency offset is in the order or the symbol rate

The two cases listed above are pretty straightforward to implement (I'm in the process of doing so). However, there are other cases, such as those at S-band which use "low rate telemetry" in the order of a few 10s of kilobytes. The Doppler shift is many orders of magnitude higher than the symbol rate. Can anyone suggest any algorithm that can work in this case? All I want to avoid is the use of an external software.

Thanks.

## Accepted answer (score 2, by Marcus Müller)

You can actually implement something like that as a rake-style receiver: Simply put up an array of (partially overlapping) more narrowband receivers and let them run in parallel until one "locks" onto a signal, and then follow that (typically: higher-order costas loop; and: I can heartily recommend fred harris' slides and recording from GRCon'17 on *band-edge filtering*; also, I recommend watching Andy Wall's Talk on *Symbol Clock Recovery and Improved Symbol Synchronization Blocks*, slides).

Now, assume you get an initial lock, what to do now?

Obviously, your control loop needs not only correct stationary phase (first-order costas loop would do that), but also frequency offset (which is nothing but a linear phase shift over time; second order costas), and, to make matters worse, possibly even a shift in frequency over time (that's why I said "higher-order costas" above).

You can of course go ahead and just do a "blind" high-order phase control loop; but that would never be as good as something as something able to predict the frequency development over time. Basically, what you'd want to do is to find the signal, observe how its phase develops on short term, and infer the "Doppler trajectory", which is the result of the satellite/receiver geometry. Then, you'd base your corrections on that prediction, and only use the control loops to get rid of residual error.

That can get very interesting in effect – what you'll basically be doing is building kind of the frequency-over-time-equivalent to a matched filter.

Another observation: If you've got a beamforming receiver setup, that geometrical prediction would directly allow for adjusting the relative phase shifts of the individual receive chains – which would both have an effect on the beam pattern and the described frequency / phase correction. The same idea applies if you have a directive antenna – say a dish – that mechanically follows the path of the satellite!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10184/doppler-shift-compensation-without-using-predictive-modelling, by Moses Browne Mwakyanjala, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
