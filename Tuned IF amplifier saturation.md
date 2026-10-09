# Tuned IF amplifier saturation

*Tags: electronics, amplifier, fm · score 3*

## Question

I was designing a tuned IF amplifier. I went with a staged Amplifier design with freqeuncy of 10Mhz. While reading through different sources, i found out that we get about max 5mV amplitude from an antenna, and we would need about 50-300mV RMS, for our FM demodulator stage. I designed a amplifier which gives about 7-10dB gain, about (15mV amplitude only). If i make my gain go higher, my output is getting saturated, im thinking, im not able to bias it properly. Is there any source like a textbook/video which explains about staged tuned alpifiers, which work.

## Accepted answer (score 4, by Ryuji AB1WX)

I assume this is a continuation of your previous question in designing a VHF FM broadcast receiver.

It would be helpful to know whether you plan to use a quadrature, ratio, or Foster-Seeley detector. Each design has pros and cons, and they differ in the input signal level/impedance.

In short, your amplifier's insufficient gain is in part due to the very small VCE (see the next paragraph) and local feedback from the Cob of the transistors. For higher gain and stability, I recommend adopting a different topology. The bias points (24.5mA and 31mA) are about right for that transistor; changing them cannot greatly improve the amplifier.

The clipping amplitude can be increased by designing the loadline so that the VCE is about half of the Vcc. Currently, the emitter resistor takes up about 3V, and the 250 in the collector takes up 6 to 7.5V, so those leave tiny room for the VCE swing. That is not good for dynamic range and the gain. I would reduce or eliminate those 250 ohms, perhaps reduce the two 100's in the emitter, and adjust the base current bleeder resistors to keep the collector current around 10-25mA range where both hFE and fT are near maxima simultaneously.

The IF amplifier for the FM receiver should have an IF filter (typically a ceramic filter or doubly-tuned LC filter, perhaps two of them) and an ample 50-80dB gain total. This is because you'll want an amplitude limiter (i.e., saturation) after the filter to maximize the noise immunity advantage of FM modulation. Typically, a 4-stage differential amplifier coupled with a tuned transformer is considered a classic design—study the spec sheet of TA7060AP (Toshiba) and CA3053 (Harris).

A good example to study is Revox B760 (I recently worked on it), whose IF amplifier block is:

where each CA3053 is a single-stage differential amplifier. Revox B760 does a lot of intricate tricks in other areas, partly because the components back then were not as good as today but tried to their best. But the IF amp is very straightforward. (The filter is perhaps somewhat overkill but that's Revox. The actual boards are also beautifully built, just like broadcast-grade equipment from that era.)

As a sidenote, AM/FM radios are difficult to use for this illustration because those radios typically used 455kHz/10.7MHz double-decker construction for AM and FM. But it looks like this:

which is Becker Mexico Cassette 375, which was factory standard with Mercedes, Ferrari and others. TR203-205, 207 are the IF amp. TR203 and 207 are for FM only, but 204-205 are shared with AM. TR206 is for signal detection to drive the mechanical station-seeking function (You should see how the mechanism is implemented! It reminds me of the very first lock-needle automatic exposure function in Konica 35mm SLRs in the 1960s. That mechanism requires good cleaning and lubrication to revive.) I've worked on a few of those, and those old RF/IF transistors are holding up surprisingly well.

Of the two types, I recommend the Revox design as the starting point for your project. It is much better design for FM IF amplifier. The Becker car stereo design (ignoring/bypassing the AM IFTs) would work but not note how diodes are used to implement the amplitude limiter.

Also, study TA7302P + TA7303P (Toshiba) or CA3089, CA3189 (Harris) for the IF chain and FM detector. Those Toshiba chips were typical FM radio ICs from the late 1970s to the early 1980s. I think the Harris ones were for more performance-oriented applications. (Don't buy those chips, but study them.) Philips must have similar products for the same market, but I don't know, top of my head.

The advantage of using a differential amplifier in the unbalanced mode in the above example ICs is to minimize the effect of feedback capacitors (Cob) in the amplifier stages, which kills the high-frequency gains. In your circuits, the Ic are set at 24.5mA in the first stage and 31mA in the second stage, where fT is around 300MHz. Theoretically, if you can eliminate the feedback from the Cob's, you would be getting well in excess of 40dB gain, but you are only getting 7dB due to the local feedbacks. A differential amplifier with an unbalanced load works just like a cascode amplifier with a built-in amplitude limiter, which is ideal for FM IF amplifiers.

The tube-generation people would mention a technique called feedback neutralization or simply neutralization. That technique can certainly be used, but it complicates the design and tuning/alignment process. It is not worthwhile doing at 10MHz with today's transistors because better RF transistors and better circuit topology lead to better overall engineering tradeoffs. (Neutralization was commonly used in FM transistor radios until the early or mid-1970s. In the Becker Mexico above, C209, C223, C232, C247, C254 are neutralization capacitors. BF451 they used have better RF properties than BC547C but still needed neutralization.)

You could also use a transistor of higher RF gain (such as 2SC3355; the original was NEC but the Chinese copies are available. Some have wrong pin assignments so be careful).

Another factor is impedance matching (loadline design). The collector output impedance should be taken at a higher impedance than assumed in that circuit design. I would use a transformer or a T-network at the end. (although I would really use a different topology to begin with)

Regarding textbooks, few people prefer to design an FM IF amplifier using discrete transistors because ICs are available and are easier/cheaper overall. Those mentioned above are classic ICs whose data sheets give a little insight into how the internal circuits work. Modern ICs are much more integrated and black-box. Also, FM IF amplifiers have somewhat distinct design requirements compared to IF amps for AM/SSB/CW/other modes, video amplifiers, line drivers, etc. since those all have to be linear. Finally, RF amplifiers typically built with discrete transistors have very different requirements than FM IF amps. So, a lot of available materials would not apply to your problem at hand. I think high-bandwidth analog electronics textbooks are of interest to you, especially those for integrated circuit designers. These were typically used in 3rd or 4th year of electrical engineering majors in decent universities, but I think most schools got rid of those subjects, so you may have to look for classic textbooks (as is often the case with analog/RF anything). The electrical engineering college curriculum today is more like a generic quantitative engineering.

I don't know if anyone is really interested in what I mean by the classics, but these are my coffeetable reading:

and this is on my lunch table:

Gray and Meyer is a true classic. Anyone who does analog must have studied it at some point. It does not discuss RF/IF amps, but it does discuss the high-frequency analysis of single-stage diff amps and multi-stage amps. I'm not sure how well-known Soclof is, but it is a good catalog of standard techniques as of the 1980s. It discusses video amplifiers, for example. Both of these books are recommended only to those who have solid theoretical foundations and are determined to go super deep dive.

Bowick is more like a collection of really good cheat sheets on today's RF engineering. It's handy but does not necessarily give you the foundation. It certainly does not get into discrete component IF amplifier design. The photo is of the 2nd edition (2008), but the original is kinda classic among practicing engineers. What was added in the 2008 edition is already old. But what was in the 1st edition is still current.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23276/tuned-if-amplifier-saturation, by Chiranka K, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
