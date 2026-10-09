# What does ALC do on a transceiver?

*Tags: transceiver, ssb, agc · score 6*

## Question

What is ALC on an HF transceiver?  
What are the disadvantages (if any) of operating using a rig without ALC? What might be the difference between a good and bad implementation of ALC?

## Answer (score 5, by jstarek)

ALC, in general, stands as an abbreviation for Automatic Level Control, which is a class of circuits designed to back-feed information about the output signal to an amplifier. The goal is to change the parameters of the amplifier so that a clean output that remains within certain parameters is attained.

In normal HF transceivers, such a circuit will most likely be used to control the final amplifier's output. The goal here is to enable use of the final amplifier to precisely it's specified capabilities, but not beyond. This is important since otherwise, simply feeding a signal with too high power into the transceiver (by speaking too loudly into the microphone or connecting a digital modem with too high an output voltage) would overdrive the amplifier stages, adding distortion to the output signal.

Similarly, most transceivers offer an ALC OUT connector that allows an analogous control loop for external, higher power amplifiers.

In both cases, the ALC circuit creates a negative DC voltage that is proportional to the output level and is used to change the gain of the preamplifier stage in the transceiver (which, in turn, will result in more or less input to the final amplifier stage and perhaps the external high power amplifier).

When you are operating a transceiver without ALC, you lose the feedback described above, which will result in (possibly severe) distortion of your output signal if you overdrive the amplifiers with a too loud signal.

With regard to the implementation, ALC circuits, like all control loops, have an "attack" and "decay" time constant which need to be tweaked for the use case (most likely voice transmission, in this case). They need to "attack" quickly, i.e. dampen the total amplification quickly in case a sudden loud noise comes in, and then "decay" a bit slower, allowing again more amplification. If this is not tuned well, voice will sound strange due to the alternating amplification factors over time.

And finally, there is an enlightening rant at http://www.sm5bsz.com/dynrange/alc.htm in which the author describes the potential of ALC circuits creating splatter-type interference if they are, as is done often in practice, (mis-)used as a cheap voice limiter.

## Answer (score 2, by Phil Frost - W8II)

ALC limits the the input power to the power amplifier (PA). Overdriving the PA would be bad: it might overheat, or exceed the voltage or current ratings of the components, eventually, or sometimes immediately, damaging the PA. Or it might just cause a lot of distortion and spurious emissions.

If the radio has adjustable output power, often this controls the point at which ALC will begin to reduce the PA drive.

Operating without ALC simply means controlling the PA drive by some other means, manually. With this comes the risk of inadvertently overdriving the PA, leading to damage or spurious emissions.

There seems to be folklore around that claims "bad ALC" is responsible for "splatter" or transmitter power outside the intended channel. For example, Transceiver Performance 10 Years of Change gives this example on page 27:

The claim seems to be that as the ALC responds to peaks and dips in the input power, it modulates the output power, effectively becoming an amplitude modulator. This modulation broadens the spectrum and is responsible for the out-of-band emissions.

However, the data here do not prove that point. Notice the "ALC Half Scale" has about 7 dB more power in the intended channel. For every 1 dB increase in output power, third order intermodulation products will increase by 3 dB. Now observe the spectral power at the point labeled "1.8 kHz away": if these skirts are caused by intermodulation we'd expect a 21 dB difference (because that's 3 * 7 dB), and indeed that looks about right.

All real amplifiers have some amount of intermodulation distortion, so this behavior is exactly what we'd expect of any real amplifier which is asked to produce 7 dB more output power. ALC has nothing to do with it: more output power means more distortion for any real amplifier.

Here's an experiment to try: instead of increasing ALC by increasing the input power until the ALC meter reads half scale, *decrease* the output power setting on the radio. This will cause ALC to reduce the PA drive, so there will be less output power, and thus less IMD. I think you'll see that when the test is performed this way, more ALC leads to less distortion, so it can't be true that ALC is causing the distortion.

It's technically true that ALC could broaden the spectrum though amplitude modulation, it can't be broadened more than the bandwidth of the ALC control signal, which is typically quite low. Making it very high would distort the signal, not just broadening the spectrum but also rendering it unintelligible. While I'm sure somewhere, someone has managed to implement a really bad ALC which causes significant distortion, and it's also true splatter can be an observed problem with some stations, I haven't seen any evidence that it's specifically ALC causing splatter in practice.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17889/what-does-alc-do-on-a-transceiver, by hotpaw2, jstarek, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
