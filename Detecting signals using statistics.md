# Detecting signals using statistics

*Tags: signal-identification, dsp · score 5*

## Question

I have sampled a section of spectrum every few Hz. I have mean, standard deviation, and range data for every frequency sampled (and I can gather more statistics if necessary). I've sampled for several seconds before storing the spectrum statistics.

I would like to be able to guess where man-made signals (i.e. channels) exist in this spectrum (as opposed to noise floor). This is proving to be a difficult task, especially since the noise-floor power sometimes changes (different antenna inputs for different bands, for example.)

I doubt anyone has a ready solution for this, but what are some starting points, or tips, to help me begin to identify channels?

In the below image 'normal' is really autocorrelation from Pandas

## Accepted answer (score 1, by hotpaw2)

You might try taking a image capture of the spectrum waterfall for some duration, and feeding that image to a machine learning inference engine, perhaps a DNN.

The inference engine could be trained on a large image database with lots of waterfalls of lots of known or suspected signal types, similar to these signal ID databases:

https://www.sigidwiki.com/wiki/Signal_Identification_Guide

http://qrznow.com/signal-identification-guide/

## Answer (score 7, by Rodney Price)

There is a range of possibilities, depending on what kind of signal you want to find. I'll start from easy and move up to hard. I'm assuming that you are using an FFT to get your spectra.

1. RFI. An earlier poster referenced some papers on finding RFI. I don't know precisely how that is defined, but lets assume that it is unintentional RF from things like switching power supplies (line spectra) and poorly wired auto engines (impulsive noise). Impulsive noise is narrow in time and wide in frequency, which suggests that you simply have a look at your receiver output. There is probably some statistical test you could apply (say, the null hypothesis is white Gaussian noise). For line spectra, do the same in the frequency domain. Perhaps those who know more about RFI than I do would say otherwise. I would suggest, however, that rather than process your signal as you're doing, that you use the initial processing that I discuss next.
2. Conventional analog signals. By this I mean the AM, FM, SSB, etc. transmissions that you run across all the time. These live in an intermediate region between impulses and line spectra, which makes things a bit harder. I would suggest that you compute a power spectrum, and from that, the autocorrelation. This is easy if you are already using an FFT: compute the FFT, then multiply each element by its complex conjugate. Now you have the power spectrum. Next do the inverse FFT to get the autocorrelation. If there's a signal there, you'll see a smeared out peak near $\tau=0$, where $\tau$ is the delay. If it's relatively wideband, the peak will be narrower; if it's narrowband (compared to your FFT) the peak will be wider. Look for peaks in both the power spectrum and the autocorrelation. This works better than statistics-gathering the way you describe because it takes advantage of the coherence of the signal. If you use a large FFT, you'll be averaging over a lot of signal, which will suppress the noise and better show you what's there. If it's just noise, you'll see a very narrow peak right at $\tau=0$ and a flat power spectrum.
3. Conventional digital signals. I mean conventional from a ham radio perspective; modes like PSK31, etc. An autocorrelation/power spectrum approach can work well here, too. The same physical principles apply: noise averages incoherently, while signal averages coherently. There is a caveat, however. As signals get more bandwidth-efficient, they start to look more like white noise. An AFSK signal like those often used in packet radio, for example, is terribly (forgive me, packet radio enthusiasts) inefficient. It takes a lot of bandwidth to get a few bits through. PSK31 is much better. Some of the more modern modes, such as WSPR and relatives, are really good. You'll see a flat spectrum across the entire signal bandwidth. They're not trying to be sneaky. That's just the physics of the situation.
4. Wideband digital signals. This is a broad category, but includes spread-spectrum signals as well as very highly optimized signals like the ones your cell phone uses. There has been a remarkable amount of R&D put into these signals to make them efficient, and because they have to push a lot of bits across, they are wideband, and so the signal-to-noise ratio in any given frequency bin a few Hz across is going to be poor. They're just plain hard to see, and there are a surprising number of them out there. This is where cyclostationary processing, a form of higher-order statistics, comes into its own. Cyclostationary processing is used to extract the bit rate from an unknown signal. Even if you can't see the signal through second-order statistics (like the autocorrelation) the bit rate of the signal will often pop right out of a cyclostationary approach. The math can be intimidating, but if you're really interested, stick with it and you'll find that it's really not that hard.

Here are a few examples to illustrate the autocorrelation/power spectrum approach. In the images, I plot the signal first, then the power spectrum, then the autocorrelation. These are simulated signals with sampling interval $\Delta t = 1$.

#### White Gaussian noise

Flat power spectrum, autocorrelation has a peak at zero lag, flat everywhere else.

#### Barker-coded pulse

Radars use these to reduce their peak power requirements while maintaining range resolution. $\sin^2 \omega/\omega^2$ structure due to the pulse shape. Autocorrelation shows a narrow peak at zero lag. In the wild, these pulses are much shorter than I show here, leading to flatter, wider spectra. They can be difficult to distinguish from noise unless you have some independent way to calculate the SNR in the channel (which is difficult if you don't actually know that there *is* a signal in the channel). Best to just look directly in the time domain.

#### FM with sinusoidal modulation

Easy to see in both the power spectrum and autocorrelation.

#### Sum of all three

Here I've set the noise $\sigma = 1/4$, the peak amplitude of the pulse to $2$, and the peak amplitude of the FM signal to $1/4$. The fourth plot is a close-up of the autocorrelation near zero lag.

## Answer (score 4, by Raul O.)

Well, this is a well-studied field (Radio Frequency Interference detection and mitigation). There are tons of literature about it.

The noise you receive is theoretically Additive White Gaussian Noise (AWGN). That means that its Probability Density Function (PDF) is Gaussian, and the pdf of its samples' power is exponential. By setting a false alarm probability according to the power of the signal, you can easily detect samples that potentially are not noise. Check the point 2.2 of this paper, for example. This threshold method is applied in the frequency domain in Frequency Blanking and Spectrogram Blanking techniques.

Normality Test are used as well to evaluate if a signal is AWGN. I have read a lot of mentions to Anderson-Darling test, but I never worked with it.

You can use Kurtosis to see if a signal is Gaussian or not (but be careful because Kurtosis is weak against certain sinusoidal signals). If it is not Gaussian, it is likely to be man-made (however, some frequency Jammers could emit Gaussian signals). Kurtosis has been also used to detect RFI in the frequency domain, not only in the time domain (look for spectral kurtosis).

Here you have an other interesting (and open!) paper about RFI detection.

I am not sure if there are AWGN-like signals made by humans different that noise for jamming. The spectrum of signals encrypted with codes (such as GPS signals, which use Pseudo-Random-Noise codes) are sincs, and they are only flat in a small fraction of its bandwidth. Even if you are sampling this small fraction, I am not sure if the signal in time will seem Gaussian.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/8919/detecting-signals-using-statistics, by Ken - Enough about Monica, hotpaw2, Rodney Price, Raul O.. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
