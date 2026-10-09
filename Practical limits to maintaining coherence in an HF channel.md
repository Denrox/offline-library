# Practical limits to maintaining coherence in an HF channel

*Tags: hf, propagation, modes, qrp · score 11*

## Question

Lately I've been thinking about weak signal communication on HF. *Very* weak, like weaker than even WSPR could achieve.

It would be nice if one could simply take any existing modulation and slow it down to achieve an arbitrarily high Eb/N0 and thus, given sufficient time, communicate with arbitrarily low power. However I understand ionospheric conditions introduce distortions which make this not really work in practice.

For example, there exists a WSPR-15 mode, which is like WSPR-2 but uses 15-minute instead of 2-minute intervals. This should mean WSPR-15 is about 9 dB more sensitive, but the documentation states:

WSPR-15 is not recommended for use at HF: the tone spacing is only 0.183 Hz, less than the Doppler spreading typical of many HF paths

So, what is "Doppler spreading", and how much of it is there on HF paths, and what can be done to overcome this challenge? More broadly, are there other properties of HF channels that limit the attainable sensitivity?

## Answer (score 6, by pidloop)

Doppler spreading is the change in received frequency from a distance transmitter due to the rise and fall of the ionosphere along the signal path. When the effective height of the ionosphere rises, this lengthens the path and causes the received frequency to drop; when it falls the path decreases and the frequency rises.

You can measure this frequency change yourself in real time using simple equipment and, making some simple assumptions, compute the change in ionospheric height. The equipment and technique are both described in my Sept 2018 QEX article available here. The idea is to use a digital frequency synthesizer synchronized to GPS, then record the difference between the locally generated signal and a signal with a well-known frequency such as WWV. Then assuming the path is a simple triangular up-reflect-down profile, the change in frequency can be used to compute the change in path length and thence the change in ionospheric effective height.

My measurements suggest a 5 MHz frequency measured over a 1000 km path changes a few tenths of Hz during stable day and night periods, but can change up to half a Hz or more during twilight when ionospheric recombination (dusk) or excitation (dawn) is changing rapidly as the sun sets and rises over the path. These correspond to changes in the effective ionospheric height of a few tens of km.

## Answer (score 3, by hotpaw2)

If a transmitter is moving toward or away from you, the received frequency will get shifted up or down, depending on direction and rate of movement. Even if the transmitter and receiver are not moving relative to each other, but a reflector, reflecting the signal between them, is moving, the you can get the same Doppler effect.

It's well known (at minimum, from the license exam question pool) that non-line-of-sight HF propagation is made possible by refraction and reflection off of the ionosphere. But the ionosphere changes in many aspects, including height, not only with time-of-day, but with high altitude weather, solar radiation, and etc., lots of things. As the ionosphere altitude changes, you get a moving mirror, thus a bit of doppler shift of your HF signal frequency.

But that's not all. The ionospheric reflector is nowhere near flat. Thus you get multiple reflections (or refractive “bounces”), much like a fun house mirror. As the shape and layering changes, the directions and amplitudes of the different multi-path paths move around; and different combinations of paths constructively and destructively interfere in a (unpredictably?) changing pattern. Since each path has a different distance, its reflection likely has a different phase from other paths. Thus, depending on how the combinations of multiple reflection paths changes, you get phase modulation on top of frequency modulation of your signal. And fading with increasing phase cancellations.

If your demodulation scheme is using a DFT or FFT (or similar filter) on a strong signal, but half of the FFT window sees one phase and the other half sees the opposite phase, that signal will be invisible to the FFT result bin where you might expect to find your signal.

The statistics are such that the likelihood of a phase and frequency change of dF over time T increases with T. (I don't know where to find those statistics. Anybody?) There appear to be papers from the 70's and 80's on research in this area. Maybe earlier research papers as well.

So, any narrowband communication scheme should either:

1) track the doppler with a PLL or other adaptation, or

2) finish before the doppler shift and phase shifts are likely to be greater than the demodulation filter width and carrier lock delta-F.

wspr-2 likely finishes fast enough often enough. wspr-15 possibly might not over typical HF ionospheric paths. Neither wspr seems to have an internal PLL.

The equivalent of a PLL might be a signal re-acquisition. So perhaps repeating something the same length as a wspr-2 data transmission 7 or 8 times (or more) might provide more reliable coding gain than wspr-15, since each repeat would require a new fresh frequency and phase acquisition by the receiver, similar to a slow-motion step-function PLL.

Added: Here’s an ITU document recommending an HF channel simulation model that includes Doppler shift/spreading :

https://www.itu.int/rec/R-REC-F.1487/en

## Answer (score 2, by Phil Frost - W8II)

ITU Recommendation F.1487-0 defines methods for testing HF ionospheric paths for bandwidths up to 12 kHz. While ionospheric propagation can be complex, this document provides a starting point for the widely applicable basics.

It characterizes an HF channel with two parameters:

- multipath differential time delay, and
- Doppler spread.

The multipath differential time delay is the maximum difference in time of arrival between multipath components. Put another way, it's the length of the channel impulse response. When the length of a symbol is very long compared to this value, differential time delay has negligible effect on demodulation performance. The ITU document states that the differential time delay exceeds 5 ms 5% of the time. Given that most very weak signal communication modes will have symbols much longer than this, differential time delay is not likely a major detriment to performance in this case.

The other parameter, Doppler spread, quantifies how "spread out" the power spectra of the signal will become due to each path having a randomly changing Doppler shift. The worst environment described is "disturbed conditions at high latitudes", with a Doppler shift of 30 Hz.

If the objective is coherently detecting a very long symbol, Doppler spread may better be understood by its dual, *coherence time*. Coherence time $T_C$ can be defined as:

$$ T_c = {9 \over 16 \pi f_m} $$

where $f_m$ is the Doppler spread. This definition of coherence time gives the time where the correlation of the channel impulse response will be above 0.5. In other words, if one were to receive a signal at some time, and then an identical signal $T_c$ later, the correlation of those received signals will be on average 0.5.

For the worst case of 30 Hz, this works out to a coherence time of:

$$ {9 \over 16 \pi\ 30\:\mathrm{Hz}} = 5.97\:\mathrm{ms} $$

In other words, detecting a 6 ms symbol might work OK, but doubling the symbol length to 12 ms doesn't make the symbol twice as easy to detect since the second half of the symbol doesn't correlate perfectly with the first.

This is why polar paths are so challenging: Doppler spread can be extremely high.

WSPR-15 has a symbol rate of 0.1831 baud, whereas the ITU document gives a differential time delay of 0.5 Hz for "quiet conditions" at mid and low latitudes. From this we can already see the challenge: considered in the time domain, we can't count on an individual tone to maintain the same phase long enough that it won't start to cancel itself out. Or considered in the frequency domain, it's a challenge for WSPR-15 to resolve individual tones since the Doppler spread smears them together.

What can be done about it? I'm not entirely sure: I am after all answering my own question. But if the challenge is to establish communication even when slowing the symbol rate enough to approach the coherence time is insufficient, and transmitter power can't be increased, I'd guess the approach must be to take many shorter samples and add them noncoherently over a long time.

Consider the bad polar case where the coherence time is 6 ms: one could calculate an FFT every 6 ms and accumulate the magnitudes of each bin over a longer time. The Doppler spread means the received phase will be effectively random but a constant carrier, given enough time, will accumulate enough bias in the magnitude to become detectable above the noise. The short FFT duration will also mean the bins will be wider than necessary, which will introduce additional noise and require a wider tone spacing, but then if it was easy everyone would do it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15335/practical-limits-to-maintaining-coherence-in-an-hf-channel, by Phil Frost - W8II, pidloop, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
