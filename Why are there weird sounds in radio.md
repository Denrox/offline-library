# Why are there weird sounds in radio?

*Tags: hf, noise, theory, qrn · score 3*

## Question

When I'm tuning through the radio on HF, suddenly, I hear a tone. So, I tune back, and the more I tune back, the more the tone changes pitch. For example, if I tune back 1 kHz, the sound rises by 1 Hz. Every time I tune through the radio, this happens. Also, sometimes I hear one of these tones over someone talking. Is it because that person wants privacy? Or is it because of my equipment?

## Accepted answer (score 6, by user10489)

What you describe is at least in part a feature of single side band demodulation. The radio is taking a range ("window" of bandwidth) of RF spectrum and shifting it to the audio spectrum. SSB doesn't know what the original audio frequency was, so it changes as you shift your RF receive frequency window. (Contrast this with FM which locks onto the signal even when you shift the frequency by a small amount. FM can still demodulate the signal correctly even when off frequency, as long as the signal is still in the receive filter bandwidth.)

The sources of these tones could be people adjusting their antenna tuner, naturally generated noises, noises from near by power supplies, carrier signals from AM transmitters, or even artifacts from your own radio's own internal oscillators and electronics ("birdies").

Most amateur HF radios have numerous filters and adjustments for those filters to try to combat these noise issues. Some have a "notch" filter that can recognize solid tones and try to mask them out. (But turn this off for CW and digital modes or you might filter out the target signal!)

You may also have a skirt filter, or high/low pass filters, or bandwidth adjustments. If there is a noise signal near the signal you want to hear, you can adjust these filters to try to cut off the low end or high end of your receive window to try to remove the noise. Between the bandwidth filters and the notch filter, you should be able to (mostly?) remove solid tones and maybe other neighboring signals.

Also, the radio typically has separate adjustment for audio amplification ("AF") and radio frequency amplification ("RF"). When you start, you want to turn up the RF amplification to max and adjust AF to something comfortable to listen to. But this brings a steady hiss into your received signal ("noise floor"). You can use RF to try to lower that noise floor below audible levels, and then readjust the actual audio with AF to bring the volume back up and again make it comfortable. (Until there's a weak signal close to the noise floor and then you need to mess with these adjustments all over.)

Modern radios also have DSP filters that try to remove predictable noise. For best results, try turning off DSP, adjusting the bandwidth filters and nose floor, and then turn the DSP back on. Prefiltering the noise like this helps the DSP work better.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22266/why-are-there-weird-sounds-in-radio, by John Doe, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
