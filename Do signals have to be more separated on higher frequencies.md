# Do signals have to be more separated on higher frequencies?

*Tags: bandwidth · score 5*

## Question

Someone told me that 10 meters was the biggest band because you can fit the most channels in it.

He said that in higher frequencies like 2 meter etc, you have to separate the signals more apart for them to work.

Is this true? Can HF frequencies have more signals clustered together, or is he just getting confused because FM takes up more bandwidth?

## Answer (score 7, by Phil Frost - W8II)

Someone was wrong. The 300 GHz band is the biggest, because it has no upper bound. You can fit an unlimited number of channels in it. See [Which band will I be authorized the most bandwidth?](Which%20band%20will%20I%20be%20authorized%20the%20most%20bandwidth.md)

There is no theoretical requirement that signals be more "spread out" at higher frequencies. However, as VHF and up tend to be larger bands, the band plans tend to include wider modulations. FM is much wider (25 kHz) than SSB (4 kHz). Consequently, if the band is primarily FM (such as 2 meters), then signals must be spread further apart to avoid interfering with each other. Nothing to do with the frequency: just the modulation in use.

## Answer (score 2, by user)

In principle? No.

Now, on the wider bands, *wider transmission modes* are often used as well. 28 MHz, for example, is the only HF band that has allocations in the band plan for FM.

Early on, a common trick for going higher in frequency was to employ a frequency multiplier. That works well with FM, but of course also widens the signal. So if you had 25 kHz FM on 144 MHz and frequency-multiplied it by three, you'd end up at 432 MHz but also with a 75 kHz bandwidth. The naïve approach doesn't work nearly as well with amplitude-modulated modes such as AM or SSB though because you'd change the actual modulation as well, so whoever was listening would have to have a receiver built to the same standard that you are using in transmission. (For example, a first intermediate frequency at 144 MHz, obtained by frequency division from the received frequency.) I can't cite sources, but I expect the relative ease of doing frequency multiplication is a major reason why many amateur bands are on harmonically related frequencies.

Consider the SSB portion of 2 meters during an active contest; there's more room to spread out and there are fewer stations within range of any one given station than on HF, but you can easily find stations as cramped together as on HF if it's an active contest, and it's no more or less difficult to work any particular one than under similar conditions on HF.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1194/do-signals-have-to-be-more-separated-on-higher-frequencies, by Skyler 440, Phil Frost - W8II, user. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
