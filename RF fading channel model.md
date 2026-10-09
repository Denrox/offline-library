# RF fading channel model?

*Tags: hf, software-defined-radio, testing · score 3*

## Question

What statistical or other descriptions exist regarding modeling of an HF-band RF fading channel?

This is allow making (as in code my own software) lots of simulated test input signals for an SDR demodulator to allow testing different software demodulation algorithms under different and varying signal and noise levels (etc.), even when not around an HF antenna.

There seem to be channel modeling standards for commercial cellular bands, but I am interested in typical fading in amateur radio HF bands.

## Answer (score 2, by tomnexus)

Here's a paper from the IEEE antennas and propagation society, describing a channel model and the experimental verification thereof. Noise will be another whole subject on its own, but the IEEE APS will be a good place to start.

Experimental Confirmation of an HF Channel Model

The abstract describes the model quite well. Unfortunately to read the whole article and find the coefficients, you need to subscribe, or find it elsewhere.

Specially designed HF ionospheric propagation measurements were made and analyzed to confirm the validity and bandwidth limitations of a proposed stationary HF ionospheric channel model. In the model, the input (transmitted) signal feeds an ideal delay line and is delivered at several taps with adjustable delays, one for each resolvable ionospheric modal component. Each delayed signal is modulated in amplitude and phase by a baseband tap-gain function, and the delayed and modulated signals are summed (with additive noise) to form the output (received) signal. Statistical specifications for the tap-gain functions involved three hypotheses: 1) that each tap-gain function is a complexGaussian process that produces Rayleigh fading, 2) that the tapgain functions are independent, and 3) that each tap-gain function has a spectrum that in general is the sum of two Gaussian functions of frequency, one for each magnetoionic component. Statistical tests were performed on daytime and nighttime measurements confirming the validity of the three hypotheses, and thereby the validity of the model. For practical applications, the model can be considered valid over a bandwidth equal to about one fourth of the reciprocal of the effective (weighted) time spreads on the ionospheric modal components. The model should be useful both in theoretical analyses of communication system performance and for channel simulator designs.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6076/rf-fading-channel-model, by hotpaw2, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
