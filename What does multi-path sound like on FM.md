# What does multi-path sound like on FM?

*Tags: propagation, fm · score 4*

## Question

I know I have probably experienced multi-path propagation on FM modes when I was working a repeater in the grand canyon and in the mountains. How can I identify when I am getting multi-path, and what does it sound like while using frequency modulation?

## Answer (score 6, by Phil Frost - W8II)

Multipath distortion can be problematic on fast digital modulations since the receiver sees multiple copies of the transmitted signal, each delayed by some appreciable fraction of a symbol. For example, digital TV uses a symbol rate of something like 4 million symbols per second. That means each symbol is about 250 nanoseconds long, which corresponds to a distance of about 75 meters at the speed of light. Thus, if one path is 75 meters longer than another, the receiver will actually be receiving the previous symbol at the same time as the current signal. This introduces obvious complications in decoding the digital signal.

FM voice, however, is relatively slow. It's not digital so we don't have a symbol rate, however we can say that the highest frequency components in the baseband signal (your voice) are somewhere around 4kHz. 1/4000 seconds corresponds to about 75,000 meters at the speed of light. Any path that's 75,000 meters longer will be significantly attenuated from the direct path, so any audible distortion due to multipath propagation on FM voice is insignificant.

However, still significant for FM voice is the effect multipath has on the effective antenna pattern. Consider a simple case where the receiver sees the direct path, and also a reflection off a building near the transmitter. We could consider the building as a second transmitting antenna, transmitting the same signal with some delay and attenuation.

Depending on the position of the receiver, and the resulting path length to the two transmitting sources, the source phases might be equal, resulting in constructive interference and a stronger received signal, or the phases might be opposite, resulting in destructive interference and a weaker received signal. As the receiver moves in a circle around the two sources, the path lengths and thus the phase delay to each source change, and thus the receiver will encounter alternating regions of constructive and destructive interference.

Effectively, the transmitter's antenna pattern has been modified to have a large number of narrow lobes. These are called "grating lobes" in the context of phased arrays:

*"Typical antenna pattern with grating lobes" by Mr. PIM at the English language Wikipedia. Licensed under CC BY-SA 3.0 via Wikimedia Commons*

Notice how between the 5 large peaks, there are very many smaller peaks. Depending on the multipath geometry, there might be very many such peaks, and the receiver might not need to move very far from being in one of the peaks to one of the nulls.

And this is what most amateurs mean when they talk about "multipath" on FM. It's especially noticeable when operating from a moving vehicle where the mobile station might go through many of these peaks per second. When conditions conspire to make the nulls very deep, and the mobile station is at the edge of the repeater's coverage, the station can alternate between hitting the repeater and not. The resulting sound is sometimes called "picket-fencing", because it sounds like a station is moving past a picket fence where the individual pickets intermittently occlude the station.

## Answer (score 2, by tomnexus)

Multi-path doesn't make any sound itself, and if the environment is constant, you'll never notice it.

What you will notice is the *fading* caused by multi-path, if you move (or the reflector moves) which causes a regular drop in the RF signal strength. When FM is demodulated, this drop results in an increase in the background noise heard, so it sounds like a rising hiss, or a repeating shhp sound.

It generally repeats as you move, every half-wavelength or so. Walking around, it's an irritating fading on the signal. Driving, it's a fluctuation that even becomes a fast flutter or buzz as you move.

In the mountains, you are more likely to be shielded from the direct path to the repeater, so your propagation depends more on the reflected paths.

How to tell? Unless you're talking to a satellite or aeroplane, the signal you hear always contains some reflected components. The question is whether they're strong enough to cause significant cancellation of each other. They can only cancel completely if they're the same strength. So if you move your receive antenna by a few wavelengths, and you can detect a significant change in audio quality, then you have significant multi-path propagation.

FM receivers produce clean audio as soon as the RF SNR is over (say) 10 dB, and there's no change as it rises after that. So if you have a strong signal (60 dB above noise) and good cancellation (99%) then you could still be 20 dB above noise, which won't cause any change in the audio quality. So you can only tell multipath by listening, if the signal is weak to begin with.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3782/what-does-multi-path-sound-like-on-fm, by Skyler 440, Phil Frost - W8II, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
