# Can I improve reception with a more sensitive antenna / preamplifier / better feedline?

*Tags: receiver, noise · score 5*

## Question

I am trying to receive a station, but I can only barely hear it through the noise. Will doing anything that increases the signal from my antenna help, such as:

- using a more sensitive antenna
- adding a preamplifier
- installing a shorter or higher quality feedline
- improving SWR, thus reducing losses

## Accepted answer (score 8, by Phil Frost - W8II)

These things will significantly help under one condition: the RF noise floor is below the receiver's noise floor. This is almost never the case on HF, where low-noise amplifiers are easy and atmospheric noise is high. On VHF and UHF the natural noise floor is lower, and low-noise receivers are more expensive, so it is possible but not guaranteed. It will depend on the quality of your receiver, and noise in that particular location and frequency. The 2.4 GHz ISM band, for example, is *full* of man-made noise.

Here's a simple test: compare the noise floor with a dummy load versus an antenna connected. If the noise floor is higher with the antenna connected, then the RF noise floor is higher than the receiver noise floor, and a more sensitive antenna will not significantly help. In this case you need to investigate ways of increasing the signal to noise ratio in other ways, such as by increasing transmitter power or installing directional antennas.

If we think of the radio's output as the combination of three components:

1. The desired signal, free of any noise
2. RF noise received by the antenna. This could be atmospheric noise, interfering stations, or noise from electronics, powerlines, etc.
3. Noise generated internally by the receiver. That is, thermal noise in its resistors, its amplifiers, etc.

We might think that the radio is contributing noise in all circumstances, and if we can boost the noise and signal from the antenna, then the radio's noise becomes relatively less significant, and SNR is improved. However, when the RF noise floor is above the receiver's noise floor, that improvement will be negligible.

The reason is that RF noise and the receiver's noise are uncorrelated, like random white noise. As I will demonstrate, even if the RF noise is just a little above the receiver noise, because of the way uncorrelated noise adds, the receiver's noise will make very little contribution to the total noise. As such, there is very little to be gained by reducing the receiver's noise, or equivalently, making the antenna "louder".

### Orly? Show Me The Math.

Uncorrelated noise powers simply add:

$$ P_1 + P_2 = P_\text{total} $$

But in this context our noise power is probably specified in dBm. To add these, we must first convert them to plain milliwatts (without the decibel), add, then convert back to dBm:

$$ 10 \log_{10}\left( 10^{P_\text{1(dBm)}/10} + 10^{P_\text{2(dBm)}/10} \right) = P_\text{total(dBm)} $$

So for example, if the receiver noise floor is -96 dBm and the RF noise floor is 6 dB above that (-90 dBm), then the total noise floor is effectively:

$$ 10 \log_{10}\left( 10^{-90\:\mathrm{dBm}/10} + 10^{-96\:\mathrm{dBm}/10} \right) = -89.03\:\mathrm{dBm} $$

So, the receiver's noise, which was only 6 dB below the RF noise, increased the total noise floor from -90 to -89.03, or by 0.97 dB. Not a terribly big deal.

An equivalent, and perhaps more intuitive way to think about it is this: uncorrelated noise amplitudes (that is, RMS voltage or current) add like orthogonal vectors:

Geometrically, we can see that as the RF noise becomes greater than the receiver noise, the triangle gets increasingly thin, and the total noise isn't much longer than the RF noise.

Mathematically, that's:

$$ E_\text{total} = \sqrt{E_1^2 + E_2^2} $$

And we can convert between dBm ($P_\text{dBm}$) and RMS volts ($E_\text{RMS}$), assuming a 50Ω impedance, with:

$$\begin{align} E_\text{RMS} &= \sqrt{ 0.001\:\mathrm{W} \cdot 50 \:\Omega \cdot 10^{P_\text{dBm}/10} }\\ &= \sqrt{0.05\:\mathrm V^2} \cdot 10^{P_\text{dBm}/20} \\ &\approx 0.2236\:\mathrm V \cdot 10^{P_\text{dBm}/20} \end{align} $$

and:

$$ \begin{align} P_\text{dBm} &= 10 \log_{10}\left( E_\text{RMS}^2 / (0.001\:\mathrm W \cdot 50 \:\Omega) \right)\\ &= 20 \log_{10}(E_\text{RMS}) - 10 \log_{10}(0.05\:\mathrm V^2) \\ &\approx 20 \log_{10}(E_\text{RMS}) + 13.01 \end{align}$$

One might still say that even this small improvement is an improvement, and is worth doing. However, there are two circumstances where that would be a bad idea:

Firstly, if you are increasing your antenna sensitivity by adding a preamplifier, this preamplifier will introduce noise of its own. Unless the preamplifier's noise figure is lower than that of your receiver, or your receiver lacks sufficient gain to bring the RF noise floor above the receiver noise floor, then you are making things worse.

Secondly, increasing the signal+noise from the antenna by any means in many situations *decreases* dynamic range. This is especially a concern with SDRs that are recently popular, because they have such a wide receive bandwidth. Consider that at some point, this signal in an SDR ends up at an analog to digital converter. Say it's a 16 bit converter. If the noise floor is high (because the antenna is so sensitive), then the least significant of these bits contain nothing but noise, and are essentially wasted. Furthermore, you approach overloading the converter and running into clipping.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2213/can-i-improve-reception-with-a-more-sensitive-antenna-preamplifier-better-feed, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
