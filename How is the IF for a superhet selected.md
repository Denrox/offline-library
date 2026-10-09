# How is the IF for a superhet selected?

*Tags: superheterodyne, equipment-design · score 12*

## Question

There seem to be almost as many choices for the intermediate frequency (IF) as there are superheterodyne receivers and transceivers out there. The ones I have come across are 455 kHz, 452 kHz, 1.6 MHz and 6 MHz.

What would be the rationale for choosing a particular IF for a superhet?

## Accepted answer (score 12, by WPrecht)

The short answer is that these are "standard" frequencies set aside for IF use and are reasonable free from interference.

The longer answer follows if you are interested in the why.

The choice of an IF frequency is one of those design tradeoffs.

The lower the IF frequency used, the easier it is to achieve a narrow bandwidth to obtain good selectivity in the receiver and the greater the IF stage gain. On the other hand, the higher the IF, the further removed the image frequency is from the signal frequency and hence the better the image rejection.

One problem of the problems of a superheterodyne receiver, is its ability to pick up a second or image frequency that is twice the intermediate frequency away from the signal frequency.

For example, if we have a signal frequency of 1 MHz which is mixed with an IF of 455kHz. A second or image signal, with a frequency equal to 1 MHz plus (2 x 455) kHz or 1.910 MHz, can also mix with the 1.455 MHz to produce the 455 kHz.

The choice of IF is also affected by the selectivity of the RF end of the receiver. If the receiver has a number of RF stages, it is better able to reject an image signal close to the signal frequency and hence a lower IF channel can be tolerated. This is why modern rigs have 2 or even 3 IF stages.

The chosen IF frequency should be free from radio interference. Standard intermediate frequencies have been established and these are kept dear of signal channel allocation.

As you have noted, 455KHz is a common IF. This is because broadcasters settled on this as a standard frequency during the broadcast AM days.

From a design point of view 455KHz it leads to poor image response when used above 10 MHz. One commonly used IF for shortwave receivers is 1.600 MHz and this gives a much improved image response for the HF spectrum. Ham band SSB HF transceivers have commonly used 9 MHz as a receiver intermediate frequency

This frequency is a little high for ordinary tuned circuits to achieve the narrow bandwidth needed in speech communication, however, when used with ceramic crystal filter networks it leads to good results.

Some recent amateur transceivers use intermediate frequencies slightly below 9 MHz. A frequency of 8.830 MHz can be found in various Kenwood transceivers and a frequency of 8.987.5 MHz in some Yaesu transceivers. This change could possibly be to avoid the second harmonic of the IF falling too near the edge of the 17m WARC band.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/850/how-is-the-if-for-a-superhet-selected, by VU2NHW, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
