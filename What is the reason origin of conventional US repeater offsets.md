# What is the reason/origin of conventional US repeater offsets?

*Tags: united-states, repeater · score 6*

## Question

In the US, the common (though not universal) repeater offsets are ±600 kHz in the 2m band and ±5 MHz in the 70cm band. **How and why did these offsets come to be standard for amateur repeaters?** The minimum simplex channel spacing is much less than the repeater offset convention.

As an example, spacing between FRS channels and GMRS channels, both near the 70cm band, is 25 kHz. Is there a reason why a smaller interval is undesirable, or a larger interval is advantageous?

## Answer (score 6, by tomnexus)

Repeaters need to receive and transmit at the same time. The offset needs to be large enough to make it possible for the filters to separate the transmit and receive frequencies.

In my opinion 600 kHz is a very narrow spacing, it results in filters that are enormous, usually six cavities each 150 x 500 mm. Even so, they have several dB of loss in both bands.

5 MHz is much more reasonable, the filters can be made much smaller by helical loading of the coaxial elements inside. This lowers the Q somewhat, but with the larger spacing, it's much easier. A filter for a 5 MHz spacing might be 1/2 the length and diameter, and probably with less loss.

Reducing the offset below 600 kHz would be very difficult, the filters would be unstable over temperature changes, and the losses would be enormous.

Now the reason - I suspect - 600 kHz was chosen is because the amateur band is only 2 MHz wide in many countries. 600 allows some repeaters and some simplex traffic, space, etc. Possibly the lower parts of the band (144.0 - 144.5) were already allocated for CW, SSB and so on, so when FM came along, the repeaters needed to squeeze into the top 1.2 MHz.

## Answer (score 3, by Charles Boling)

Was going to comment, but don't have enough rep on the ham site yet. This discussion offers a few tidbits regarding history/reasoning behind the 600kHz split and other oddities of the 2m band: https://forums.qrz.com/index.php?threads/history-of-vhf-repeater-splits.26321/

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5181/what-is-the-reason-origin-of-conventional-us-repeater-offsets, by ESV, tomnexus, Charles Boling. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
