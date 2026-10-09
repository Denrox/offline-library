# DStar audio distortion, sounds like a kazoo

*Tags: d-star, digital-voice · score 3*

## Question

I am new to DStar, and I have been listening to a local DStar repeater. Most of the time the DStar audio is very clear. However, sometimes I hear audio that has a peculiar and distinctive distortion. It sounds like a nasal whine, or someone trying to talk through a kazoo. Sometimes this distortion is mild, other times it is severe, to the point of making the voice signal unintelligible. From past experience with other types of digital communication, it seems like usually it either works, or it doesn't. In trying to learn about this particular type of distortion in radio, a see some differences of opinion regarding range and sensitivity of digital versus analog signals, but I have not found anything that seems to relate to this peculiar type of distortion at all.

## Answer (score 3, by Marcus Müller)

Figure up front: This is your receiver from 11km height

```
[wave]-> Antenna [current]
 -> amplifiers/mixers/filters [electrical signal]
 -> analog-to-digital-converter [digital RF-equiv. samples]
 -> bit decision [coded data bitstream]
 -> error correction [data bits]
 -> audio decoder [audio samples]
 -> audio digital-to-analog converter [current] -> filters, amplifier
 -> speaker [pressure waves]
 -> ear [neuron activity]
 -> brain [speech understanding]

```

From past experience with other types of digital communication, it seems like usually it either works, or it doesn't.

That would indicate a lack of *graceful degradation* in the presence of errors. Modern audio-carrying digital systems are better than that – they encode voice digitally such that loss of bits or even complete frames has as little perceptible effect as possible.

In the case of D-Star, there's a rather inefficient rate 1/2 convolutional code; that, in the end, means that your radio transmits two bits for every bit of audio data, and the other end can make sense of most cases where a couple bits flip during transmission. The errors that make it through will typically not be "catastrophic" (that's an actual channel coder term) in the sense that you don't corrupt all following bits if you have one uncorrectable error, just a few. (at most two out of four following bits, actually); in most cases, you're quite likely to not even notice that!

But with a bit of bad luck, you do. And depending on what parameters of the voice reproduced by your handset that affects, you might get different audible effects. Like the kazoo. A receiver might decide to drop a frame if it notices it couldn't correct all errors, or it might hand the "damaged" frame to the audio decoder, in hopes it makes the best of it. And this is where different D-Star receivers might simply differ.

The moment that so many bits flip during reception that nothing works anymore and errors can no longer be correct is "quite far down the SNR slope". Thing is this: the error correction can reduce the number of transmission bit errors that reach your handset's audio codec quite successfully for a large range of SNRs, but at some point the energy to get the right bits out of the noise is simply not in the signal anymore, and then you get the "it gets really bad, quite rapidly", and thus the "it works pretty perfectly, and then doesn't at all" behaviour.

It's possible your handset is constantly operating in that "waterfall region" of the error correction. But it's unlikely. It's more likely that your specific device is erring on the "well, let the audio codec deal with the bit errors" side, and thus you get the "funny" sounds.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23586/dstar-audio-distortion-sounds-like-a-kazoo, by Wayne_H, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
