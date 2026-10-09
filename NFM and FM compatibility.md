# NFM and FM compatibility

*Tags: modes, bandwidth, frs · score 3*

## Question

I read that using narrow band (NFM) when you should be using normal(FM)/wide-band(WFM) can result in the a reduced volume at the receiver.

What happens in the opposite situation? (What if you are transmitting with FM and the receiver is expecting NFM? Is the received audio extra loud, clipped/distorted, or perhaps quieter (because the information outside of the narrow band is being discarded?)

Example: FRS and GMRS have some overlapping channel frequencies. All FRS channels are NFM, and GMRS channel 1 uses FM. So if both an FRS and GMRS transceiver are set to channel 1, what is the result?

## Answer (score 4, by Phil Frost - W8II)

A wide FM transmission in a narrow FM receiver is effectively overmodulation: the excessive deviation of the transmitter results in the instantaneous frequency of the transmission deviating outside the bounds of what the receiver is designed for.

A practical FM receiver will pass the signal through a channel filter before demodulation. The objective of this filtering is to remove adjacent signals and noise, while passing the desired signal with minimal distortion. Theoretically FM results in an infinitely wide spectrum, but Carson's rule can be used to estimate the channel bandwidth where most of the signal energy exists:

$$ \text{channel bandwidth} = 2(\Delta f + f_m) $$

$\Delta f$ is the peak frequency deviation, and $f_m$ is the highest frequency component in the baseband input. For narrow FM, $\Delta f$ will typically be 5 kHz or less, and for voice communications $f_m$ will be 4 kHz or less. The choice of these parameters will dictate the design of the receiver's channel filter and minimum channel spacing.

If the deviation is excessive, as would be the case with a wide FM transmitter and a narrow receiver, the receiver's filter will truncate the FM sidebands. Because FM is a nonlinear operation this distorts the demodulated baseband audio in a nonlinear way, and the result is some pretty nasty sounding distortion at the receiver.

## Answer (score 2, by Kevin Reid AG6YO)

As Phil Frost's answer already said, if the audio is at full amplitude the modulated signal will exceed the channel filter's bandwidth and the resulting audio will be distorted.

From a time-domain audio processing perspective, we could describe the effect approximately as if the signal *fades out* whenever the modulation exceeds the passband of the channel filter. Thus, the (audio) peaks are replaced with (RF and also audio) noise; the strength of this effect will depend on how sharp the channel filter is.

This is similar to an FM receiver tuned off the correct frequency, except that the off-center receiver will replace only *half* the audio waveform peaks (those of one polarity, depending on which way it is detuned) with noise; whereas a too-narrow but centered filter will replace all peaks.

An extreme case of this is attempting to receive a broadcast FM (wideband FM, 75 kHz deviation) signal with a communications receiver — you will hear almost entirely noise, because unless the program is very quiet, all but the zero-crossings of the original audio signal will be lost.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16394/nfm-and-fm-compatibility, by Bort, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
