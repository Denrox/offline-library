# Failing to detect Hydrogen line with 105cm dish

*Tags: antenna-theory, software-defined-radio, uhf, rtl-sdr, microwave · score 5*

## Question

I've seen many examples of roughly 1 metre sized dishes being used w H+ sawbird and an SDR to detect and analyze Hydrogen line signal, and have been trying myself but can't seem to get anything beyond maybe a small whiff. I'm using a 105cm satellite tv dish with a paint can roughly 13 cm in diameter as my feed, going into the H+ sawbird and then into my laptop, but not getting any signal when pointed in the Cygnus region (although pointing an offset dish isn't particularly nice either, maybe I'm screwing that up). If anyone can think of something I might be missing, that'd be great. Maybe my paint can is too garbage a feed - what are the best designs for this purpose?

Photo of dish and feed:

## Answer (score 5, by tomnexus)

The sawbird H+ looks like a nice LNA, do you have the H+ H1 version?

The plan version seems to be for 1542 MHz, "center frequency of the module is 1.542GHz with approximately 80MHz of bandwidth (-6dB rolloff). As such, it should be used for reception of frequencies between 1.50GHz-1.58GHz" but the H+ H1 has "65MHz bandpass region, centered near 1.42GHz" which is perfect.

Try measuring the Sun Noise of your dish at 1420 MHz - how many dB does the noise floor rise when pointed at the sun, compared to pointing 45 degrees away from the sun but still high in the sky? Make sure all AGC is off. This is the first test of the sensitivity of your system. You can also try cold sky vs warm ground.

Try also the feed alone - straight up (Tsky = a few K) vs straight down (300 K) vs on dish. Try to estimate the system temperature from this.

Feeding an offset dish generally requires a much smaller feed angle - higher gain - than a centre-fed dish. It's possible your can feed is much too broad, resulting in a lot of ground noise pick-up. Your can does look too close to the dish, but you can determine that by experiment.

Aiming is usually along the arm that holds the feed, or sight along (bottom-of-dish) to (top of where the Ku-band feed would have been) as that's how the offset is designed.

Take a look at the classic microwave book by W1GHz Chapter 6 is all about dish feeding, including detailed notes about "coffee can feeds".  
Figure 6.3-2 (from 1988) is for a $0.6\lambda$ coffee can and includes a graph of dish efficiency considering spillover. Your dish F/D will be about 0.65, so the illumination efficiency might be below 30%, and with 70% spillover the antenna temperature will be very high.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18198/failing-to-detect-hydrogen-line-with-105cm-dish, by Jack_SH, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
