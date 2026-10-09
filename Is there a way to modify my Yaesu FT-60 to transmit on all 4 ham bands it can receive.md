# Is there a way to modify my Yaesu FT-60 to transmit on all 4 ham bands it can receive?

*Tags: ht, modification, yaesu · score 3*

## Question

I have a Yaesu FT-60, and it can transmit on 2m, 70cm, and receive 1.25m and 33cm bands. I would really like to find a way to get it to transmit on 1.25 and 33cm. Is there a way to make this happen?

## Accepted answer (score 2, by Dan KD2EE)

No. You likely would need to build two new transmit stages and rewrite the firmware. Each transmit stage uses a precise final oscillator and mixer which is specific to the frequency band as well as a filter to suppress harmonics, use of the hardware for 70cm at a 33cm frequency would result in most of your transmit signal being filtered out - if it was even possible.

There are quad-band transmitters - yaesu makes a few - I am not aware of any with 33cm coverage, however. This would likely be a simple mod in a desk unit, but any modification of this sort of a handheld or even mobile radio is extremely difficult due to the fact that so many functions are concealed inside multi-purpose chips, many signals are inaccessible due to multi-layer PCBs and components without exposed leads, and there is simply no room inside the case for any add-on boards that we could manufacture.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/175/is-there-a-way-to-modify-my-yaesu-ft-60-to-transmit-on-all-4-ham-bands-it-can-, by PearsonArtPhoto, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
