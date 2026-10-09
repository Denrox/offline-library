# What frequency ranges are most common for Amateur radio astronomy and why are most parabolic antennas tuned to such high frequencies?

*Tags: antenna, antenna-theory, frequency, space-weather · score 4*

## Question

What frequency ranges are most common for amateur radio astronomy?

I am mostly interested in radios for the purpose of astronomy. In general I was expecting that the lower frequencies would be more useful, since hams usually can receive and transmit longer distance signals with lower frequencies.

However since parabolic antennas seem to be most frequently (although not exclusively) preferred for astronomy, I was surprised to see that most models I can find for sale (at a price point in the hundreds of dollars USD, or low thousands) are tuned for incredibly high frequencies, e.g. 1.7 GHz - 6.4 GHz and sometimes higher. Why is that?

According to the tables featured by this source, it looks like the professional radio astronomers are using up to the hundreds of GHz(?).

## Accepted answer (score 6, by natevw - AF7TB)

In general I was expecting that the lower frequencies would be more useful, since hams usually can receive and transmit longer distance signals with lower frequencies.

This is because a certain range of lower frequencies tends to interact with the ionosphere in a useful way for **terrestrial** communication. There's sort of a sweet spot in the HF bands for long-distance signals propagation between stations on earth. This is in contrast to both:

1. upper VHF and especially the UHF/SHF signals, which tend only work at approximately line-of-sight distances
2. low frequency long-wave signals which *can* reach reasonable distances over the horizon via ground wave, but still only *hundreds* of miles

This "sky wave" aka "skip" propagation on HF is great for talking *thousands* of miles **around** the world — but the signals radio astronomy cares about are **line of sight**, which you can receive straight from the sky from *bazillions* of miles away!

However since parabolic antennas seem to be most frequently (although not exclusively) preferred for astronomy, I was surprised to see that most models I can find for sale (at a price point in the hundreds of dollars USD, or low thousands) are tuned for incredibly high frequencies, e.g. 1.7 GHz - 6.4 GHz and sometimes higher. Why is that?

Any given size of parabolic dish will give better and better gain the higher the frequency. That is, super high frequencies can be collected and "focused" much more effectively than VHF and lower frequencies. A small 60cm diameter modern satellite TV dish isn't particularly effective until the frequencies get into the 12–18 GHz range. A 100 meter diameter radio telescope would have quite good gain on much lower VHF/UHF frequencies — but it will have *incredible* gain on super high GHz frequencies.

So by moving up the frequency, you get away from lots of earth noise sources (HF bands tend to generally be a lot noisier on earth, both atmospheric/storms and man-made interference) and don't need such a big antenna to begin with. And if you have a big antenna anyway, you get "stellar" performance at microwave frequencies!

And remember, these astronomical signals are line-of-sight but also coming from very very very far away! So being able to focus a high-gain antenna towards a distant galaxy (and away from terrestrial noise) is a big advantage.

## Answer (score 3)

Wavelengths above 10 meters tend to be blocked by the ionosphere. Wavelengths below 10 centimeters tend to be absorbed by the atmosphere. There are other windows that allow narrow frequency bands to reach the Earths surface.

In many cases they are looking for the RF from atoms as the electrons go from a high energy orbit to a low energy orbit. Hydrogen for example will radiate at 1420 Mhz or 21 centimeters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21321/what-frequency-ranges-are-most-common-for-amateur-radio-astronomy-and-why-are-, by Hack-R, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
