# How does lowering the RF Gain help with SNR?

*Tags: noise, equipment-operation, gain · score 5*

## Question

Let's say for sake of example we are in the 40m band.

I've read articles and posts about riding the RF gain (or even just simply lowering it). And I can see how it is useful in overload situations.

What I don't quite get is how lowering the RF gain can help dig a weak signal out of the noise. A "weak signal" just means that it's not much stronger than the noise floor. Lowering the RF gain will lower the noise floor. But it will also lower the signal as well.

How is it possible that lowering the RF gain will attenuate the background noise faster than the desired signal. If you lower the gain by 3dB. Everything goes down by 3dB, right? The SNR doesn't improve.

I've also heard of "riding the RF gain" where you crank up the AF and use the RF as your volume control. How does this help? You are lowering the noise floor and the desired signal by the same amount with the RF gain. And then making it loud again with the AF gain.

There must be something happening when going from the IF to audio then benefits from having an overall quieter signal I guess. I just don't see how any of this can somehow know to attenuate static and amplify desired signal more.

Is dynamic range an issue with weak signals? I can see it being a problem with strong signals (hence the overload and need to attenuate). But with a weak signal, unless your noise floor is S9, you have enough dynamic range right?

Articles (i.e. forum posts)

https://www.eham.net/reviews/review/148466

Next, with the RF Gain still all of the way Counter-clockwise, so that the radio is nearly silent (don't move the RF Gain yet), we bring the AF Gain (volume) up to a quieted -- not quite normal listening level, where we cut hiss, but still just hear the signal clearly.

Once that AF Gain volume is set (about half for Icom 7300), you just leave it where it is, roughly, but you will twiddle it a bit up or down, to keep HISS down to lowest possible levels, as your slowly raise your RF Gain. You are now using your RF Gain as your volume control, by turning it clockwise to raise the volume, or counter-clockwise to lower the volume. While you are adjusting your RF Gain, you are looking for a happy medium between where signals are loudest, but the noise around them is quietest.

… I also twiddle with the AF Gain a little bit, if that helps the signal -- it really depends. Experiment!

https://forums.qrz.com/index.php?threads/rf-gain-more-powerful-than-nr.554997/

With AF gain on full, while using the RF gain to control volume, and aggressive EQ settings on upper-middle frequencies, signals barely readable often rise to an easy 56 to 57.

https://forums.qrz.com/index.php?threads/help-me-like-my-new-ic-7300-more.551169/

My KX2's RF Gain, when used with either ATT or Pre-amp, and EQ, will dramatically cut hiss noise while digging out signals.

## Accepted answer (score 13, by Phil Frost - W8II)

For an ideal, linear receiver, reducing the RF gain by 1 dB lowers signal and noise by 1 dB, so there would be no change in SNR.

However, receivers are not perfectly linear. This means that besides just amplifying inputs, they also *mix* them to some extent. So any input to the receiver which contains more than just a single frequency will generate some intermodulation products, that is, new frequency components at frequencies based on the sums and differences of the input components, and harmonics thereof.

The reason for this argument to reduce RF gain is that these intermodulation products aren't linear. For a 1 dB increase in gain, the 3rd order intermodulation products increase by 3 dB. Thus if intermodulation is contributing significantly to noise, decreasing gain improves SNR.

You can see an example in the animation below. The two central markers M1 and M2 are the "signal" inputs, two tones from signal generators. D3 and D4 are the third-order distortion products, and outside of those we also see the fifth, seventh, and ninth order products rise above the noise floor. The animation shows in each frame a gain increase of 1 dB: note how the gain of the intermodulation products increases faster than 1 dB per frame. This is because as gain is increased, the amplifier becomes less linear, and thus generates disproportionately more distortion.  
By Ice Ardor - I measured the intermodulation characteristics of an amplifier myself on a spectrum analyzer, CC BY-SA 4.0, Link

Of course in practice the input to the receiver isn't just two tones in an otherwise quiet spectrum, but rather a cacophony of many signals and external noise. As a result, the intermodulation distortion isn't tidy, regular spurs such as this, but rather a raising of the noise floor. The distortion can be generated in the receiver front-end, and also in mixer stages when very strong signals can have an effect even through the filter's stop-band attenuation. Digital modes like PSK31 present a particular challenge since many signals all fall in the receiver passband, and thus can intermodulate quite strongly.

The extent to which this effect is significant depends significantly on the quality and design of the radio. In recent years, many radios have adopted direct-sampling or direct-conversion SDR architectures, and this has the effect of greatly reducing intermodulation distortion since there are very few analog stages to introduce such distortion.

In contrast, superheterodyne receivers have several intermediate mixer stages, and each one can add some distortion. A very high quality design might have very effective filtering and very linear stages, approaching the performance of a direct-conversion SDR. But a cheaper design can be quite terrible.

As an example, I have a Softrock RXTX, and a Yaesu FT-897. The former is a direct-conversion SDR which costs under \$100, and the latter is a superheterodyne receiver that cost over \$900 when it was new. Decoding FT8 with WSJT-X on the Softrock I get easily twice the decodes compared to the FT-897. The FT-897 simply generates too much intermodulation distortion.

Reducing the RF gain on the FT-897 does help, though it's never as good as the Softrock. On the other hand, the Softrock is so linear, adjusting gain makes no relevant difference because the intermodulation products are always well below the noise floor.

## Answer (score 3, by hobbs - KC2G)

I've seen this argument before and never been entirely convinced by it either, but I *think* the theory is that it comes down to nonlinearity. The silicon in the amplification and detection stages of your rig is never perfectly linear. Nonlinearity at the high end is what causes overload issues, but there's also nonlinearity at the low end, where a signal that is too small is greatly attenuated or causes no reaction at all. So if you can push the noise down far enough by reducing the input gain, the noise level in the output will suddenly fall off of a cliff, "revealing" your weak signal, or so the theory goes.

However, since the signal is (in this scenario) very close to the noise, we must be adding quite a bit of nonlinear distortion to it as well, and indeed the nonlinearity must be *multiplying* the signal with the noise (since the gain in the nonlinear region is dependent on the sum of signal and noise), so it's not clear that the result is any better than what we started with. Perhaps, since the mixing means that even most of the distortion products we hear are somehow *correlated* with the signal, copyability should improve even though the absolute fidelity doesn't?

## Answer (score 2, by user19290)

All answers above somewhat miss the point of the original question. Lowering the RF Gain does not magically improve the SNR of all signals, but it surely does for the medium and strong ones on SSB. Since a voice in SSB varies its instantaneous power a lot during transmission, if you set you RFG to max and put your AGC to fast, you'll notice strong noise in between words as the AGC is always trying to follow the voice peaks. This is the worst you can do in most situations. To improve this, if you lower the RFG to raise the S-meter exactly as the signal you're receiving, your receiver gain will be almost constant (as it should be) and the background noise will be greatly reduced. Of course you won't obtain such a great effect if your signal is of the same magnitude as the noise: lowering the RFG will just lower your global audio volume since the AGC is already working at nearly constant gain.

So, basically, the answer is this: lowering the RF Gain improves the resulting SNR since the noise between words doesn't get amplified as much as the useful signal during the peaks. The answer citing non linearities within the RX are totally missing the point, but they're correct in saying that the lower the RFG, the lower the distortions, but then it's a matter of finding a compromise between sensitivity and distortion... and this could be summed up into: the lower the band, the lower your RFG should be set. Finally, your preamp should be used just above 21MHz.

73

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13074/how-does-lowering-the-rf-gain-help-with-snr, by Paul, Phil Frost - W8II, hobbs - KC2G, user19290. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
