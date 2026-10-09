# What's wrong with 220MHz?

*Tags: ht, mobile, vhf · score 17*

## Question

It seems like 220MHz is the bastard step-child of the amateur world. Every HT is either 2m or 2m/70cm. Some companies offer tri-banders, but they almost always add 6m (?!), not 220MHz.

The only way to get this band easily is the Chinese radios. I have a BAOFENG UV-5RC which is 2m/220MHz, and I have seen for sale single band 220 MHz mobile unit from TYT.

In an otherwise competitive market, it seems odd to me that none of the major makers have 220 in their lineup. Why?

## Accepted answer (score 16, by user)

While for an authoritative answer to this I believe you'd have to ask the manufacturers directly (unless we happen to have someone here on the site who works for one of them), there is a pretty big *plausible* reason why so few multiband radios include 220 MHz capability.

**The band is allocated to amateur radio mostly in the United States and Canada.** (Source: Wikipedia.) Outside of ITU Region 2, the *only* country listed as having an allocation there is Somalia. On the other hand, with minor differences in frequency ranges for which it is trivial to implement restrictions in software only, two meters and 70 cm are both allocated to amateur radio practically worldwide.

Since 220 MHz also is not harmonically related to the band pair two meters and 70 cm, adding it to an existing design would probably require a fairly significant outlay in new electronics, filters etc. You would, at the very least, need to fix up the receiver so it performs well on the band, add the ability to tune the VFO to the band (assuming you don't already have a wide coverage VFO) and add a proper band pass filter to filter the transmitted signal. Other steps might be needed as well depending on the particular transceiver design. There is also the related problem that a 2m/70cm antenna is not resonant at 1.25 meters, which increases the risk of damage due to mistakenly transmitting into an unmatched load.

It would seem that manufacturers don't consider the demand for 220 MHz capability to outweigh the cost of such design changes for a relatively limited market. The conclusion we can draw from this line of reasoning is that the reason why none of the major manufacturers include a multiband HT with 220 MHz capability in their lineup is precisely *because* it is a competitive market.

## Answer (score 13, by Adam Davis)

220MHz has a long and storied history which leads to the lack of available equipment, and thus low adoption rates in the Amateur Radio community.

The short version is that two things contributed to its lack of usage:


Few commercial bands are near enough that existing equipment can be simply modified to serve this band. There are numerous commercial bands near 2M and 70CM, thus many, many commercial products can be modified, or simply used without modification, to serve those bands. However there are few products ready-made that can easily be modified to run in the 220MHz amateur radio allocation, and it's been this way for decades.


The band has been, at various times, allocated and reallocated, divided, and placed on secondary use for some portions over the last several decades. Some are hesitant to invest in a band with such a variable history, which suggests that it may not be available in the long term.

We do have a handful of products now, and enterprising amateurs are setting up repeaters and encouraging use so that, unlike in the 90's, a commercial service can't easily show that it's not well used by the amateur community.

But due to its history, and the lack of nearby commercial bands and equipment, it simply isn't as popular as 2M and 70CM.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/986/what-s-wrong-with-220mhz, by WPrecht, user, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
